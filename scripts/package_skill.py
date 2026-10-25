"""Export the installable skill using an explicit file allowlist; no Git mutation."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('.qoder/skills/harness-mentor')
RUNTIME_FILES = (
    'SKILL.md', 'README.md', 'references/bestandsaufnahme.md',
    'references/einrichten-leitfaden.md', 'references/begleiten-disziplin.md',
    'references/didaktik.md', 'references/anhaenge/qoder.md',
    'assets/vorlagen/USER.md', 'assets/vorlagen/AGENTS.md',
    'assets/vorlagen/VISION.md', 'assets/vorlagen/MEMORY.md',
    'assets/vorlagen/memory-eintrag.md',
)
PUBLIC_FILES = (Path('README.md'), *(SKILL / p for p in RUNTIME_FILES))


def export(source: Path, destination: Path) -> list[Path]:
    source = source.resolve()
    destination = destination.resolve()
    if destination.exists():
        raise ValueError('Output must be a new directory; existing contents are never overwritten.')
    if source == destination or source.is_relative_to(destination):
        raise ValueError('Output may not contain the source workspace.')
    for relative in PUBLIC_FILES:
        candidate = source / relative
        if not candidate.is_file() or candidate.is_symlink() or not candidate.resolve().is_relative_to(source):
            raise ValueError(f'Missing or unsafe release source: {relative}')
    destination.mkdir(parents=True)
    for relative in PUBLIC_FILES:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / relative, target)
    return list(PUBLIC_FILES)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    archive = args.output.resolve().with_suffix('.zip')
    if archive.exists():
        raise ValueError('Archive already exists; choose another output name.')
    files = export(ROOT, args.output)
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as bundle:
        for relative in files:
            bundle.write(args.output / relative, relative.as_posix())
    print(f'Installable repository: {args.output.resolve()}')
    print(f'Installation archive: {archive}')


if __name__ == '__main__':
    main()
