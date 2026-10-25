#!/usr/bin/env python3
"""Headless trigger and continuity evals for harness-mentor.

The runner creates a fresh workspace, copies only the skill into it, optionally
seeds a memory entry, runs qodercli in print mode with stream-json output, and
records whether the Skill tool actually loaded harness-mentor.

Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = Path(__file__).resolve().parent
SKILL_DIR = ROOT / ".qoder" / "skills" / "harness-mentor"
CASES_FILE = EVALS / "cases.json"
RESULTS_DIR = EVALS / "results"
RAW_DIR = RESULTS_DIR / "raw"
SANDBOX = ROOT / ".sandbox"

HARNESS_FILES = {"USER.md", "AGENTS.md", "VISION.md", "MEMORY.md"}
HARNESS_DIRS = {"memory", "private"}


def say(message: str = "") -> None:
    print(message, flush=True)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def skill_hash() -> str:
    digest = hashlib.sha256()
    for path in sorted(SKILL_DIR.rglob("*")):
        if path.is_file():
            digest.update(path.relative_to(SKILL_DIR).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def find_cli(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser()
        if path.is_file():
            return path
        raise SystemExit(f"qodercli nicht gefunden: {explicit}")
    which = shutil.which("qodercli")
    if which:
        return Path(which)
    candidates = [
        Path.home() / ".qoder" / "bin" / "qodercli" / "qodercli",
        Path.home() / ".qoder" / "bin" / "qodercli" / "qodercli.exe",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise SystemExit("qodercli nicht gefunden. Pfad mit --cli angeben.")


def load_cases() -> list[dict]:
    data = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    return data["cases"]


def select_cases(cases: list[dict], wanted: str | None) -> list[dict]:
    if not wanted:
        return cases
    ids = {item.strip() for item in wanted.split(",") if item.strip()}
    unknown = ids - {case["id"] for case in cases}
    if unknown:
        raise SystemExit(f"Unbekannte Fall-IDs: {', '.join(sorted(unknown))}")
    return [case for case in cases if case["id"] in ids]


def make_workspace(label: str, case: dict, with_skill: bool = True) -> Path:
    base = SANDBOX / label
    base.mkdir(parents=True, exist_ok=True)
    workspace = base / f"w-{secrets.token_hex(4)}"
    workspace.mkdir()
    if with_skill:
        target = workspace / ".qoder" / "skills" / "harness-mentor"
        shutil.copytree(SKILL_DIR, target)
    seed = case.get("seed") or {}
    for relative, content in (seed.get("files") or {}).items():
        destination = workspace / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
    return workspace


def snapshot(workspace: Path) -> dict[str, str]:
    files: dict[str, str] = {}
    for path in workspace.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(workspace).as_posix()
        if relative.startswith(".qoder/skills/") or relative.startswith(".git/"):
            continue
        files[relative] = sha256_file(path)
    return files


def is_harness_artifact(relative: str) -> bool:
    parts = relative.split("/")
    if parts[-1] in HARNESS_FILES:
        return True
    return parts[0] in HARNESS_DIRS


def diff_snapshots(before: dict[str, str], after: dict[str, str]) -> dict:
    created = sorted(set(after) - set(before))
    deleted = sorted(set(before) - set(after))
    modified = sorted(
        path for path in set(before) & set(after) if before[path] != after[path]
    )
    changed = created + modified + deleted
    return {
        "created": created,
        "modified": modified,
        "deleted": deleted,
        "harness_changes": sorted(path for path in changed if is_harness_artifact(path)),
    }


def read_transcript(path: Path) -> tuple[str, str]:
    """qodercli writes cp1252 on Windows; decode per line and normalize to UTF-8."""
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
    lines = []
    for line in raw.split(b"\n"):
        try:
            lines.append(line.decode("utf-8"))
        except UnicodeDecodeError:
            lines.append(line.decode("cp1252", errors="replace"))
    return "\n".join(lines), "cp1252"


def parse_transcript(path: Path) -> dict:
    events: list[dict] = []
    unparsed: list[str] = []
    text, encoding = read_transcript(path)
    if encoding != "utf-8":
        path.write_text(text, encoding="utf-8")
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            unparsed.append(line)

    init: dict = {}
    result: dict = {}
    tool_sequence: list[str] = []
    skill_calls: list[dict] = []
    texts: list[str] = []
    triggered = False

    for event in events:
        event_type = event.get("type")
        if event_type == "system" and event.get("subtype") == "init":
            init = event
        elif event_type == "assistant":
            for block in event.get("message", {}).get("content", []):
                block_type = block.get("type")
                if block_type == "tool_use":
                    name = block.get("name", "")
                    tool_sequence.append(name)
                    if name == "Skill":
                        payload = block.get("input", {})
                        skill_calls.append(
                            {"skill": payload.get("skill"), "args": payload.get("args", "")}
                        )
                        if payload.get("skill") == "harness-mentor":
                            triggered = True
                elif block_type == "text":
                    texts.append(block.get("text", ""))
        elif event_type == "result":
            result = event

    final_text = result.get("result") or "\n".join(texts)
    return {
        "triggered": triggered,
        "skill_calls": skill_calls,
        "tool_sequence": tool_sequence,
        "final_text": final_text,
        "init_skills": init.get("skills", []),
        "init_model": init.get("model"),
        "init_cwd": init.get("cwd"),
        "result_subtype": result.get("subtype"),
        "result_is_error": result.get("is_error"),
        "num_turns": result.get("num_turns"),
        "duration_ms": result.get("duration_ms"),
        "credits": result.get("total_credits"),
        "unparsed_lines": unparsed[:5],
        "event_count": len(events),
        "transcript_encoding": encoding,
    }


def run_once(
    cli: Path,
    case: dict,
    run_number: int,
    label: str,
    args: argparse.Namespace,
    env: dict[str, str],
    with_skill: bool = True,
) -> dict:
    workspace = make_workspace(label, case, with_skill=with_skill)
    before = snapshot(workspace)
    raw_path = RAW_DIR / label / case["id"] / f"run-{run_number}.ndjson"
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        str(cli),
        "-p",
        case["prompt"],
        "-w",
        str(workspace),
        "--no-session-persistence",
        "--permission-mode",
        args.permission_mode,
        "--max-output-tokens",
        str(args.max_output_tokens),
        "--output-format",
        "stream-json",
    ]
    if args.model:
        command.extend(["-m", args.model])

    started = time.monotonic()
    timed_out = False
    returncode: int | None = None
    error: str | None = None

    try:
        with raw_path.open("w", encoding="utf-8") as raw:
            completed = subprocess.run(
                command,
                cwd=workspace,
                env=env,
                stdout=raw,
                stderr=subprocess.STDOUT,
                timeout=args.timeout,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            returncode = completed.returncode
            if returncode != 0:
                error = f"qodercli exit {returncode}"
    except subprocess.TimeoutExpired:
        timed_out = True
        error = f"timeout after {args.timeout}s"
    except OSError as exc:
        error = str(exc)

    elapsed_ms = int((time.monotonic() - started) * 1000)
    after = snapshot(workspace)
    artifacts = diff_snapshots(before, after)
    parsed = parse_transcript(raw_path) if raw_path.exists() else {}

    memory_text = ""
    for relative in artifacts["created"] + artifacts["modified"]:
        if relative.startswith("memory/"):
            memory_text += (workspace / relative).read_text(
                encoding="utf-8", errors="replace"
            )
    memory_text = memory_text.lower()

    auto = case.get("auto_checks") or {}
    failures: list[str] = []
    notes: list[str] = []

    if error:
        failures.append("run_error")
    if with_skill:
        if not parsed.get("init_skills") or "harness-mentor" not in parsed.get("init_skills", []):
            failures.append("skill_not_available")
        if parsed.get("triggered") != case["should_trigger"]:
            failures.append("trigger")
    elif "harness-mentor" in parsed.get("init_skills", []):
        failures.append("skill_unexpectedly_available")
    if auto.get("expect_no_harness_artifacts") and artifacts["harness_changes"]:
        failures.append("harness_artifacts")
    if auto.get("expect_memory_write") and not any(
        path.startswith("memory/") for path in artifacts["created"] + artifacts["modified"]
    ):
        notes.append("memory nicht geschrieben")
    needle = auto.get("memory_contains")
    if needle and needle.lower() not in memory_text:
        failures.append(f"memory_lacks:{needle}")

    if not args.keep:
        shutil.rmtree(workspace, ignore_errors=True)

    return {
        "case_id": case["id"],
        "run": run_number,
        "should_trigger": case["should_trigger"],
        "mode": case.get("mode"),
        "with_skill": with_skill,
        "prompt": case["prompt"],
        "triggered": parsed.get("triggered"),
        "trigger_pass": (
            parsed.get("triggered") == case["should_trigger"] if with_skill else None
        ),
        "skill_calls": parsed.get("skill_calls", []),
        "tool_sequence": parsed.get("tool_sequence", []),
        "auto_pass": not failures,
        "failures": failures,
        "notes": notes,
        "artifacts": artifacts,
        "final_text": parsed.get("final_text", ""),
        "init_model": parsed.get("init_model"),
        "init_cwd": parsed.get("init_cwd"),
        "result_subtype": parsed.get("result_subtype"),
        "result_is_error": parsed.get("result_is_error"),
        "num_turns": parsed.get("num_turns"),
        "duration_ms": parsed.get("duration_ms"),
        "wall_ms": elapsed_ms,
        "credits": parsed.get("credits"),
        "returncode": returncode,
        "timed_out": timed_out,
        "error": error,
        "unparsed_lines": parsed.get("unparsed_lines", []),
        "transcript_encoding": parsed.get("transcript_encoding"),
        "workspace": None if not args.keep else str(workspace),
        "raw_trace": str(raw_path),
    }


def summarize(results: list[dict]) -> dict:
    total = len(results)
    trigger_results = [result for result in results if result.get("trigger_pass") is not None]
    trigger_pass = sum(1 for result in trigger_results if result["trigger_pass"])
    auto_pass = sum(1 for result in results if result["auto_pass"])
    positives = [result for result in trigger_results if result["should_trigger"]]
    negatives = [result for result in trigger_results if not result["should_trigger"]]
    positive_hits = sum(1 for result in positives if result["trigger_pass"])
    negative_hits = sum(1 for result in negatives if result["trigger_pass"])
    return {
        "runs": total,
        "trigger_runs": len(trigger_results),
        "trigger_pass": trigger_pass,
        "trigger_rate": (
            round(trigger_pass / len(trigger_results), 3) if trigger_results else None
        ),
        "auto_pass": auto_pass,
        "auto_rate": round(auto_pass / total, 3) if total else None,
        "positive_runs": len(positives),
        "positive_hits": positive_hits,
        "positive_rate": round(positive_hits / len(positives), 3) if positives else None,
        "negative_runs": len(negatives),
        "negative_hits": negative_hits,
        "negative_rate": round(negative_hits / len(negatives), 3) if negatives else None,
        "credits": round(sum(result.get("credits") or 0 for result in results), 2),
    }


def write_markdown(report: dict, args: argparse.Namespace) -> Path:
    path = RESULTS_DIR / f"{report['label']}.md"
    without_skill = report.get("without_skill", False)
    lines = [
        f"# {'Ablation ohne Skill' if without_skill else 'Baseline'} — {report['label']}",
        "",
        f"**Stand:** {report['created']}  ",
        f"**Skill-Hash:** `{report['skill_hash'][:16]}…`  ",
        f"**CLI:** `{report['cli']}`  ",
        f"**Rechte:** {report.get('permission_mode', 'n/a')}  ",
        f"**Modell:** {report['models'] or 'n/a'}  ",
        f"**Läufe:** {report['summary']['runs']}  ",
        f"**Kosten:** {report['summary']['credits']} Credits  ",
        "",
        "## Ergebnis",
        "",
    ]
    if without_skill:
        lines += [
            "**Achtung:** Der Workspace liegt im Repo. Der Skill ist nicht geladen, aber seine",
            "Dateien sind per Pfad lesbar; einzelne Läufe haben `SKILL.md` oder Referenzen gelesen.",
            "Das ist keine saubere Ablation, sondern nur ein Indiz. Siehe `evals/README.md`.",
            "",
            "| Kennzahl | Wert |",
            "|---|---|",
            f"| Automatische Checks | {report['summary']['auto_pass']}/{report['summary']['runs']} ({report['summary']['auto_rate']}) |",
            "",
        ]
    else:
        lines += [
            "| Kennzahl | Wert |",
            "|---|---|",
            f"| Trigger korrekt | {report['summary']['trigger_pass']}/{report['summary']['trigger_runs']} ({report['summary']['trigger_rate']}) |",
            f"| Positive erkannt | {report['summary']['positive_hits']}/{report['summary']['positive_runs']} ({report['summary']['positive_rate']}) |",
            f"| Negative sauber | {report['summary']['negative_hits']}/{report['summary']['negative_runs']} ({report['summary']['negative_rate']}) |",
            f"| Automatische Checks | {report['summary']['auto_pass']}/{report['summary']['runs']} ({report['summary']['auto_rate']}) |",
            "",
        ]

    lines += [
        "## Fälle",
        "",
        "| Fall | soll | trigger | Artefakte | Auto | Hinweise |",
        "|---|---|---|---|---|---|",
    ]
    for result in report["results"]:
        trigger = "—" if without_skill else ("ja" if result["triggered"] else "nein")
        artifacts = ", ".join(result["artifacts"]["harness_changes"]) or "—"
        notes = "; ".join(result["failures"] + result["notes"]) or "—"
        lines.append(
            f"| {result['case_id']} | {'ja' if result['should_trigger'] else 'nein'} | "
            f"{trigger} | {artifacts} | {'ok' if result['auto_pass'] else 'prüfen'} | {notes} |"
        )

    lines += [
        "",
        "## Manuelle Prüfung",
        "",
        "Die folgenden Punkte sind bewusst nicht automatisch bewertet. Pro Fall die Rohspur lesen und",
        "die Checks aus `cases.json` mit ja/nein beantworten. Ein grüner Trigger ist kein Nachweis",
        "gelungener Begleitung.",
        "",
    ]
    for case in report["cases"]:
        lines.append(f"### {case['id']} — {case['mode']}")
        lines.append("")
        lines.append(f"> {case['prompt']}")
        lines.append("")
        for check in case.get("checks", []):
            lines.append(f"- [ ] {check}")
        lines.append("")

    lines += [
        "## Grenzen",
        "",
        "- Gemessen wird der Qoder-Harness. Claude Code und Cursor sind ungeprüft.",
        "- Die Läufe teilen sich Maschine, globales Profil und globale Plugins. Der Workspace ist frisch,",
        "  die Umgebung ist es nicht.",
        "- Der Workspace liegt im Repo. Das Modell kann per Pfad die echte `AGENTS.md` des Repos lesen;",
        "  das beeinflusst Antwortinhalte, nicht die Trigger-Entscheidung (siehe `evals/README.md`).",
        "- Kontinuität wird über eine seedbare Begleitnotiz simuliert. Das ersetzt keinen echten",
        "  Retention-Check nach zwei bis drei Wochen.",
        "- Gesprächsqualität, Ton und Didaktik bleiben Sache der Persona-Probeläufe.",
        "- Ein einzelner Lauf ist kein Nachweis. Die Pass-Rate zählt, nicht der grüne Einzelfall.",
        "",
        f"Rohspuren: `{report['raw_dir']}`",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", help="Pfad zu qodercli")
    parser.add_argument("--cases", help="Komma-getrennte Fall-IDs, z. B. P1,P2,N1")
    parser.add_argument("--runs", type=int, help="Läufe pro Fall; überschreibt cases.json")
    parser.add_argument("--model", help="Modell für qodercli -m")
    parser.add_argument("--label", help="Name des Ergebnislaufs")
    parser.add_argument("--timeout", type=int, default=300, help="Sekunden pro Lauf")
    parser.add_argument(
        "--permission-mode",
        default="accept_edits",
        choices=["default", "accept_edits", "bypass_permissions", "dont_ask", "auto"],
        help="Schreibzugriffe müssen erlaubt sein, sonst sind Artefakt-Checks wertlos",
    )
    parser.add_argument("--max-output-tokens", type=int, default=2000)
    parser.add_argument("--keep", action="store_true", help="Workspaces behalten")
    parser.add_argument(
        "--without-skill",
        action="store_true",
        help="Ablation: Workspace ohne harness-mentor, Trigger wird nicht bewertet",
    )
    parser.add_argument("--dry-run", action="store_true", help="Nur Workspaces und Befehle zeigen")
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Markdown aus einem vorhandenen <label>.json neu erzeugen",
    )
    parser.add_argument("--list-cases", action="store_true", help="Fälle auflisten und beenden")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    if args.render_only:
        if not args.label:
            raise SystemExit("--render-only braucht --label")
        source = RESULTS_DIR / f"{args.label}.json"
        if not source.exists():
            raise SystemExit(f"Ergebnis nicht gefunden: {source}")
        report = json.loads(source.read_text(encoding="utf-8"))
        say(f"Markdown: {write_markdown(report, args)}")
        return 0

    cases = load_cases()
    selected = select_cases(cases, args.cases)
    if args.list_cases:
        for case in selected:
            say(f"{case['id']}: {'trigger' if case['should_trigger'] else 'kein Trigger'} — {case['prompt']}")
        return 0

    cli = find_cli(args.cli)
    label = args.label or datetime.now().strftime("%Y-%m-%d-%H%M%S")
    label = re.sub(r"[^A-Za-z0-9_.-]+", "-", label).strip("-") or "run"
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    for key in (
        "QODER_AGENT_SDK_ENTRYPOINT",
        "QODER_AGENT_SDK_VERSION",
        "QODER_SESSION_TYPE",
        "QODER_WORKER_CWD",
    ):
        env.pop(key, None)

    say(f"Skill: {SKILL_DIR}")
    say(f"CLI:   {cli}")
    say(f"Fälle: {len(selected)} · Label: {label}")
    say("")

    if args.dry_run:
        for case in selected:
            workspace = make_workspace(label, case, with_skill=not args.without_skill)
            runs = args.runs or case.get("runs", 1)
            say(f"{case['id']}: {workspace} · {runs} Lauf/Läufe")
            say(f"  {case['prompt']}")
        return 0

    results: list[dict] = []
    for case in selected:
        runs = args.runs or case.get("runs", 1)
        for run_number in range(1, runs + 1):
            say(f"[{case['id']} {run_number}/{runs}] {case['prompt'][:70]}…")
            result = run_once(
                cli,
                case,
                run_number,
                label,
                args,
                env,
                with_skill=not args.without_skill,
            )
            results.append(result)
            state = "ok" if result["auto_pass"] else "PRÜFEN"
            say(
                f"  trigger={'ja' if result['triggered'] else 'nein'} "
                f"auto={state} "
                f"({result['wall_ms']} ms, {result.get('credits') or 0:.2f} Credits)"
            )
            if result["failures"]:
                say(f"  Befunde: {', '.join(result['failures'])}")
            say("")

    summary = summarize(results)
    models = sorted({result["init_model"] for result in results if result.get("init_model")})
    report = {
        "label": label,
        "without_skill": args.without_skill,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "skill_hash": skill_hash(),
        "skill_dir": str(SKILL_DIR),
        "cli": str(cli),
        "permission_mode": args.permission_mode,
        "models": ", ".join(models),
        "raw_dir": str(RAW_DIR / label),
        "summary": summary,
        "cases": selected,
        "results": results,
    }
    json_path = RESULTS_DIR / f"{label}.json"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path = write_markdown(report, args)

    say("Ergebnis")
    if args.without_skill:
        say(f"  Auto-Checks:     {summary['auto_pass']}/{summary['runs']} ({summary['auto_rate']})")
    else:
        say(f"  Trigger korrekt: {summary['trigger_pass']}/{summary['trigger_runs']} ({summary['trigger_rate']})")
        say(f"  Positive:        {summary['positive_hits']}/{summary['positive_runs']} ({summary['positive_rate']})")
        say(f"  Negative:        {summary['negative_hits']}/{summary['negative_runs']} ({summary['negative_rate']})")
        say(f"  Auto-Checks:     {summary['auto_pass']}/{summary['runs']} ({summary['auto_rate']})")
    say(f"  Credits:         {summary['credits']}")
    say(f"  JSON:            {json_path}")
    say(f"  Markdown:        {md_path}")
    say(f"  Rohspuren:       {RAW_DIR / label}")
    if args.without_skill:
        return 0
    return 0 if summary["trigger_pass"] == summary["trigger_runs"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
