# Harness Mentor — Product Plan

## Funktionsabgleich und Änderungsplan

**Bestätigte Zielvorstellung:** persönlicher Onboarding- und Begleit-Skill für die Arbeit mit
KI-Agenten; bestehende Umgebung verstehen, gemeinsam verbessern, persönlichen Kontext pflegen
und die Person zur eigenständigen Nutzung befähigen. Begleitung nimmt mit Erfahrung ab.
**Name:** Harness Mentor (`harness-mentor`). Der zwischenzeitlich gewünschte Name Set Me Up ist
durch Manuels Korrektur ersetzt. **Umfang dieser Änderung:** Namensangleichung und Analyse;
keine funktionale Erweiterung. Quelle: Manuels Auftrag und anschließende Namenskorrektur im Chat,
Stand 2026-10-25.

### Befund am aktuellen Bestand

„Implementiert“ bedeutet hier als ausführbare Skill-Anweisung vorhanden, nicht als deterministische
Softwarefunktion garantiert. Bewertet wurde der aktuelle lokale Bestand einschließlich schon vor
diesem Auftrag vorhandener Änderungen. Die Architektur bleibt Skill als Programm plus
`project`-Memory-Eintrag als Zustand. Quelle: `.qoder/skills/harness-mentor/SKILL.md`,
`references/begleiten-disziplin.md` im selben Skill, Stand 2026-10-25.

| Ziel | Status | Beleg und verbleibende Lücke |
|---|---|---|
| Bestehenden Harness analysieren und Verbesserungen finden | **Teilweise** | `references/einrichten-leitfaden.md`, Block 0, fragt nach Harness und vorhandenen Regeln und verlangt deren Erhalt. Es fehlt ein systematischer Abgleich von aktiven Konfigurationsorten, Ladereihenfolge, verfügbaren Funktionen und Konflikten. Ohne Begleitnotiz führt die Moduswahl immer in Einrichten, auch bei einer bereits erfahrenen Person. |
| Im Dialog passende Arbeitsweisen entwickeln | **Implementiert** | Einrichten-Leitfaden: Zweck jeder Frage, Verhaltens-Prüfstein, vorhandene Antworten wiederverwenden, Vorschläge zur Korrektur, Sprache und Beispiele anpassen. Einschränkung: „eng führen“ wird einheitlich voreingestellt; bereits gültige Freigaben und Erfahrung sind nicht ausdrücklich von dieser Vorgabe ausgenommen. |
| USER-, Regel-, Vision- und Memory-Dateien aufbauen | **Implementiert** | Leitfaden und `assets/vorlagen/` liefern Dateien, Strukturen und Memory-Schreibregeln; vorhandener Kontext soll erhalten bleiben. Der tatsächliche Ladeeffekt ist gesondert zu prüfen. |
| Die tatsächlichen Dateikonventionen des Harness beachten | **Teilweise** | `references/anhaenge/qoder.md` ist der einzige Anhang und enthält feste Pfade eines Referenzrechners. Der Kern setzt vielfach `AGENTS.md`, `USER.md` und ein bestimmtes Memory-Schema voraus. Verifizierte Anpassungen für andere Harnesses fehlen. |
| Fehlende Funktionen und Strukturen erkennen und anbieten | **Teilweise** | Begleiten-Disziplin benennt wiederholte Reibung, fehlenden Kontext und Werkzeuge aus der tatsächlichen Werkzeugliste. Ein initialer bedarfsbezogener Funktionsabgleich und die Unterscheidung verfügbar/deaktiviert/nicht geprüft fehlen als expliziter Ablauf. |
| Kontext kontinuierlich verbessern | **Teilweise** | Memory-Hygiene, Umkehrbedingungen, Quellenpflicht und Pflege bei Fehlern/Richtungsänderung sind vorhanden. Widerspruch: Zustand soll aktualisiert werden, die Begleitnotiz dagegen nur angehängt und zugleich klein gehalten werden. Eine eindeutige Regel zur aktuellen Zustandsansicht fehlt. |
| In den ersten Tagen und Wochen begleiten | **Teilweise** | Begleitnotiz, vereinbarter Pflegeanlass, Fortsetzung und Retention-Gegenprobe sind beschrieben. Ein optionaler Qoder-Hook wird erwähnt, aber nicht eingerichtet oder als wirksamer Wiederaufnahmeweg nachgewiesen. Ein Skill allein wacht nicht zu einem Termin auf. |
| Nur hilfreich und mit Rückzugsmöglichkeit eingreifen | **Implementiert** | Begleiten-Disziplin fordert beobachtbare Signale, Kosten des Schweigens, begrenzte Interventionen und akzeptierte Ablehnung. Pausen-/Snooze-Semantik und ein protokollarmer Umgang mit Schweigen sind noch nicht eindeutig beschrieben. |
| Befähigung statt Abhängigkeit | **Implementiert; Wirkung ungeprüft** | Didaktik verlangt eigenes Anwenden und Korrigieren; Begleitung bietet bei belegter Selbstständigkeit ihr Ende an und akzeptiert „aus“. Ein längerfristiger unabhängiger Nutzerbefund liegt nicht vor. |

Quelle für die gesamte Tabelle: `.qoder/skills/harness-mentor/SKILL.md`, dessen
`references/einrichten-leitfaden.md`, `references/begleiten-disziplin.md`,
`references/didaktik.md`, `references/anhaenge/qoder.md` und `assets/vorlagen/`, Stand 2026-10-25.

### Was tatsächlich getestet ist

Die vorhandene Qoder-Baseline meldet 34 von 35 korrekten Trigger-Entscheidungen; ein positiver
AGENTS-Fall wurde verfehlt. Fortsetzungsfälle verwenden vorbereitete Begleitnotizen und simulieren
Zeitabstände; sie belegen keine tatsächlich über Wochen laufende Begleitung. Manuelle
Qualitätschecklisten sind im Bericht noch offen. Quelle: `../evals/results/2026-10-24-baseline.md`
und `../evals/cases.json`, Stand 2026-10-24.

Der Varianzlauf ergänzt erfolgreiche Wiederholungen, ersetzt aber keinen Nutzerbefund.
Die Ablation ist als kontaminiert dokumentiert, weil Dateien des Skills aus dem Test-Workspace
weiter erreichbar waren. Der Unterschied zwischen „mit Skill“ und „ohne Skill“ ist deshalb
nicht sauber nachgewiesen. Quelle: `../evals/results/2026-10-24-variance.md`,
`../evals/results/2026-10-24-ablation.md` und `../evals/README.md`, Stand 2026-10-24.

### Priorisierter Vorschlag — noch nicht implementieren

| Priorität | Betroffene Dateien | Konkrete Anpassung | Abnahme |
|---|---|---|---|
| Hoch: Bestandsanalyse vor Einrichtung | `SKILL.md`, `references/einrichten-leitfaden.md`, `evals/cases.json` im aktuellen Skill bzw. Repo | Vorhandene Umgebung und konkreten Bedarf erfassen; ohne Begleitnotiz nicht automatisch ein Erst-Setup unterstellen. Vorhandene gültige Regeln, Freigaben und Dateien erhalten; nur die nötige Ergänzung anbieten. Kein neuer Modus nötig. | Ein bereits eingerichteter Workspace erhält eine begründete Diagnose ohne erneutes Interview und ohne überschriebenen Kontext. |
| Hoch: Dateikonventionen und Ladebelege | `references/anhaenge/qoder.md`, `references/einrichten-leitfaden.md`, `assets/vorlagen/AGENTS.md`, `assets/vorlagen/MEMORY.md`; bei belegtem Bedarf weitere Anhänge | Pfade aus der aktuellen Installation ermitteln statt einen Benutzernamen vorauszusetzen. Native Regeldatei, Geltungsbereich, automatische Ladung und bloße Referenzen getrennt beschreiben. Unbekannte Harnesses ausdrücklich ungeprüft lassen. Neue-Sitzung-Test mit Dateiquelle/Ladebeleg ergänzen; eine passende Antwort allein beweist keinen automatischen Ladevorgang. | Kontext landet am tatsächlichen Ladeort; ein nicht ladender Marker wird erkannt; bestehende native Konventionen bleiben erhalten. |
| Hoch: Sicherheitsgrenze richtig formulieren | `SKILL.md`, `references/anhaenge/qoder.md` | Aussagen, Hooks seien die Stelle für Garantien, korrigieren: Rechte und externe Durchsetzung an konkrete Aktion/Nutzlast binden; ein Hook allein ist keine Sicherheitsgrenze. | Keine Vorlage oder Erklärung verspricht Schutz durch Markdown oder allein durch Hook-Registrierung. |
| Hoch: Fortsetzung ehrlich und nutzergesteuert | `references/einrichten-leitfaden.md`, `references/begleiten-disziplin.md`, jeweiliger Harness-Anhang | Wiederaufnahme nur über einen tatsächlich verfügbaren und geprüften Mechanismus vereinbaren. Ohne diesen: Wiedereinstieg durch die Person. Einverständnis, Pause, Ende und gegebenenfalls vorhandene Erinnerungsfunktion festhalten; keine erfundene Hintergrundbeobachtung. | Mit und ohne Wiederaufnahmemöglichkeit bleibt die Zusage korrekt; Ablehnung und „aus“ beenden die Begleitung sofort. |
| Mittel: Zustand konsistent halten | `references/begleiten-disziplin.md`, `references/einrichten-leitfaden.md`, `assets/vorlagen/memory-eintrag.md` | Aktuellen Grad und offene Punkte aktualisieren, wichtige historische Begründungen kompakt erhalten. Routine-Schweigen nicht unbegrenzt protokollieren. „Begleitgrad“ und externe Handlungsfreigabe klar unterscheiden. | Wiederaufnahme mit alten oder widersprüchlichen Einträgen nutzt den aktuellen Zustand und erfindet keine Erlebnisse. |
| Mittel: Funktionslücken bedarfsbezogen anbieten | `references/einrichten-leitfaden.md`, `references/begleiten-disziplin.md` | Gewünschten Arbeitsablauf gegen reale Werkzeuge/Rechte prüfen; verfügbar, nicht verbunden und ungeprüft unterscheiden. Nötige Einrichtung anbieten, fehlende Credentials nur als Nutzeraufgabe notieren. | Eine konkrete Reibung führt zu einem begründeten Angebot; ohne Reibung entsteht kein Tool-Installationsprogramm. |
| Mittel: Wirksamkeit und Selbstständigkeit belegen | `evals/cases.json`, `evals/run.py`, `evals/README.md`, `references/didaktik.md` | Fälle für bestehenden Workspace, alternative Dateikonvention, fehlenden Trigger, Pause und Kontextkonflikt ergänzen. Ablation wirklich isolieren. Retention mit realer Nutzung prüfen; eigenes Korrigieren und Weiterarbeiten höher gewichten als das Wiedergeben von Begriffen. | Reproduzierbare technische Befunde und getrennt dokumentierter Nutzerbefund; keine Qualitätsbehauptung allein aus Trigger-Raten. |

Alle Skill-Pfade in dieser Tabelle sind relativ zu `.qoder/skills/harness-mentor/`, Eval-Pfade
relativ zum Repository. Reihenfolge ist eine Agentenempfehlung, keine Freigabe. Quelle: Abgleich
des oben genannten Bestands mit Manuels Zielvorstellung, Stand 2026-10-25.

### Namensmigration und offene Handgriffe

Aktueller öffentlicher Name: **Harness Mentor**; Skill-Slug unverändert `harness-mentor`.
Historische Entscheidungen, ursprüngliche Konzeptquellen und Eval-Rohspuren behalten den Namen,
unter dem sie entstanden sind. Die Vorgängerversion bleibt als solche erkennbar; sie wird nicht
still zum aktuellen Skill erklärt. Quelle: Namenskorrektur im Chat, Stand 2026-10-25.

Die konkrete Ausführung und verbleibende Handgriffe stehen im neuen Namenseintrag der
[`DECISIONS.md`](../DECISIONS.md). Die nachfolgenden Abschnitte sind frühere Planungsstände.

**Status: product idea with sourced market exploration; architecture and development plan proposed, not approved or implemented.**
Working analysis as of 2026-09-19. The title is confirmed by Manuel; technology choices remain provisional.
The follow-up covers process use cases, market entry, replacement versus reuse, and local setup feasibility;
no candidate has been installed or tested as a full substitute.

**Location:** moved here from `D:\OneDrive\Delta Weave\projects\company-harness.md` on 2026-09-19, where
initial implementation starts. The Delta Weave hub keeps a pointer node only. New sessions start in
[`../CONTEXT-SIGNOFF.md`](../CONTEXT-SIGNOFF.md); workspace rules are in [`../AGENTS.md`](../AGENTS.md).

Source: Manuel's request, title clarification and follow-up questions in the current conversation, Stand 2026-09-19.
Concept source: Manuel's original synthesis, preserved at
[`sources/konzept-ursprung-2026-09-19.md`](sources/konzept-ursprung-2026-09-19.md), Stand 2026-09-19
(originally a session attachment under `C:\Users\Admin\.qoder\tmp\`, copied here because that path is
temporary). Its product claims are hypotheses, not independently verified findings.
The recommendations below are agent proposals from this analysis, Stand 2026-09-19.
This is internal planning, not a publication approval or a delivery commitment.

## 2026-10-12 — Current direction: harness-mentor (v2)

**Status: direction accepted by Manuel on 2026-10-12; the sections below describe the 2026-09-19
company-work-layer analysis and are kept as background.** The pivot from measurement rig to skill is
recorded in [`../DECISIONS.md`](../DECISIONS.md) (2026-10-11); this section supersedes the product
thesis for the current phase.

**Sources:** five parallel model exploration runs of 2026-10-12 (Qoder sessions in this workspace,
distilled by four parallel agents) plus a live test run of the v1 skill the same day. Two findings
were fixed immediately (flat interview questions; the delegation question — autonomy is now a
prescribed trust ramp, not a preference interview).

**Synthesis — what all five lenses converged on:**

- Trust is operationalisable: predictability, checkability, correctability — with the first working
  correction as the critical trust moment.
- Architecture in two parts: **program** (the skill) and **state** (a `project` memory entry — the
  mentor uses the memory system it sets up; the earlier three-part design with invitation snippet and
  a dedicated `BEGLEITSTAND.md` was cut in the same-day essence pass as unnecessary apparatus).
- The mentor's default is silence: proactivity only on observable friction signals (threshold: two
  occurrences, with source), at most one intervention per session; silence itself is a logged result.
- Experience before artefacts: three mental images (foreign worker with limited memory; context as
  the only lever — say, offer, allow; trust as correctability) come before any template.
- Question discipline: every question states its purpose and must change observable agent behaviour.
- Honesty boundaries: capabilities only from the live tool list; "assumed, not verified" is named;
  a file that is not loaded is not context.
- The mentor has an ending: staged retreat (eng geführt → begleitend → auf Abruf → aus), transitions
  on evidence, acceptance test of three experiences plus a retention check after 2–3 weeks.

**Product:** new skill `.qoder/skills/harness-mentor/` with two modes — *Einrichten* (guided setup,
evolved from v1) and *Begleiten* (quiet companion across sessions). v1 (`company-harness`) remains
as an artefact. Target audience is universal, not chat-world only: audience placement happens in the
intake and selects examples and pace (fit, not pigeonholing); developers and curious owner-led
early adopters alike. Development method: real test runs with personas rather than scripted dialogues;
findings feed the skill, as on 2026-10-12.

**Essence pass (2026-10-12, after build):** Manuel's criterion — nothing that can stand in the way,
no unnecessary workflows, no constraint on the user's creative range; from his own weeks of harness
work: blocking rules are the enemy, guiding rules are the point, and stale documented decisions hold
the agent back. The skill was reduced 16 → 10 files: `BEGLEITSTAND.md` apparatus, invitation snippet,
and the standalone files for retreat, honesty and memory hygiene were cut; their essence folded into
the guide, the discipline and the stance. Rule teaching now distinguishes guiding from blocking rules,
with the TL;DR summary rule (gist first, user to-dos visibly highlighted) as the canonical guiding
example — and as the mentor's own output discipline. better-harness v0.2.21 was read as a source and
stays a separate skill; taken over were only silence-with-tiers, "recorded is not loaded", and the
confirmation that the two-occurrence threshold matches its two-episode discipline.

**Open:** distribution/discoverability (v2 stays manually invoked); whether the explanatory part
permanently belongs to the product (lens fa76's fork — for now yes, as the didactics core).

**Update 2026-10-24:** the synthesis above is kept as written. Direction has since gained a fourth
mental image — *the task is not the intention* — from Manuel's essay *Die Architektur der Intention*;
it is now anchored in the didactics, the intake (Block 2), and the VISION/AGENTS templates. See
[`../DECISIONS.md`](../DECISIONS.md), 2026-10-24.

## Product thesis

**A company-owned AI work layer that carries tasks from relevant company context to reviewed outcomes,
without requiring the owner to reconstruct the business for every conversation.**

The ambition is broader than productivity in an existing role: expand the operational capabilities
available to a small organisation. Research, preparation, coordination and execution share company
context and accountability rather than becoming unrelated specialist chats.

The sellable result is completed, reviewable work with less owner effort. The underlying product is
**context + execution + review + continuity**. A knowledge base answers questions; this system must also
know what is in progress, what changed, what is missing, and who must decide next.

Proposed initial audience: owner-led service businesses with recurring customer-project work and a
reachable decision-maker. This is a testable starting segment, not a permanent industry restriction.
Delta Weave is the first internal proving ground, not evidence of wider market fit.

## Research conclusion: compare replacement, not novelty

Follow-up source research and Manuel's clarification, Stand 2026-09-19, refine the initial proposal:
existing products are not a surprise or a reason to abandon it. The useful distinction is between a
substitute for Manuel's own daily work, a component Delta Weave can reuse, and a substitute for the
commercial offer. A hosted product might replace the internal use case without being available for
white-label redistribution. Conversely, an open-source context engine might remove substantial building
work without delivering the finished customer process.

Current products already combine company knowledge, tool execution and process orchestration. Microsoft
documents event-driven autonomous agents; Glean documents workflow and background-agent execution; Dust
documents webhook-triggered runs. These are not merely hypothetical MCP tool collections.[^microsoft]
[^glean][^dust] Rocketlane explicitly markets shared knowledge, agents performing service-delivery work
and human intervention; Scoro's release notes describe operational-data questions and actual workspace
modifications.[^rocketlane][^scoro] Consequently, neither “context plus agents” nor “processes instead of
personas” is a defensible uniqueness claim on its own.

That does **not** establish complete substitution. The research inspected public documentation and
vendor descriptions, not working customer deployments. It does not prove their reliability, adoption
cost or fit for this offer, and cannot establish that a workflow exists nowhere else. In particular,
missing approval details in a vendor page do not prove missing approvals in the product.

| Candidate | What could replace part of the idea | What remains to be demonstrated |
|---|---|---|
| **Bevel / Hexis** | Git-backed company context, skills, tools, provenance and permissions exposed to agent runtimes; potentially a reusable context/control layer | Qoder integration, actual administration and migration effort, operational case persistence, process execution and licence review; not established as a finished SME workflow product |
| **Lindy** | A hosted daily-work substitute with connected company tools, ongoing work, company context and action approvals | Performance on the same cases, data/export constraints and the applicable product/onboarding variant; no verified Qoder-server or white-label offering |
| **Glean / Microsoft / Dust** | Much of the context-and-execution foundation, configurable rather than invented from scratch | Total configuration/support cost and SME workflow fit; no assumption that a custom platform beats them |
| **Rocketlane / Scoro / Accelo** | An existing operational system may already cover much of customer delivery, scope, capacity and billing | Whether customers already use it, whether external correspondence/exception handling is covered, and whether adoption is easier than adding a separate layer |
| **Fig** | Governed business context and decision/execution infrastructure | The intended company is ambiguous; figlabs.ai is sales-led, not a verified local-install option |

Sources for this comparison: [^bevel][^hexis][^lindy][^glean][^microsoft][^dust][^rocketlane][^scoro][^accelo][^fig].
Relevance AI also advertises context, triggers and human-in-the-loop execution; persona-oriented branding
does not prevent process-oriented use.[^relevance] Relay.app's official site reports closure; it is not
an installation candidate. Its closure alone does not establish why the business ended or invalidate the
workflow-builder category.[^relay]

A credible opportunity is therefore **a repeatable, operated business outcome for a well-defined kind of
company, with less setup and oversight than the alternatives**. That is a hypothesis to prove through
use and buying behaviour, not a market gap established by failing to find an identical landing page.

## Which work actually benefits from a company harness?

The strongest tasks sit where a change in one place creates consequences elsewhere. The system must
connect what was agreed, what is now true, what actions are allowed and what evidence proves resolution.
The value is not another answer to a question: it is bringing those states back into agreement.

A good candidate has a recurring trigger, evidence distributed across sources, genuine judgement about
which action to take, executable next steps, and an observable stopping condition. Company context must
change the action—not merely make the wording more personal. A previous courtesy concession, a delivery
dependency or a customer's acceptance requirement can change what should happen next. Simple invoice
arithmetic, a fixed reminder or copying a field should remain deterministic automation.

“Loop” has two meanings here. Within an active run, the agent gathers evidence, proposes a plan, acts
and checks results under explicit limits. Across business time, a durable case waits for approval, a
customer reply or changed source data, then resumes. Keeping a model thinking continuously is neither
necessary nor desirable. A draft or a sent message is not the same as a resolved case.

### Customer change → agreed and consistent delivery plan

A customer asks for an addition while expecting the original deadline to remain. The harness links that
request to the accepted scope, delivery commitments, current capacity, relevant earlier concessions and
approved commercial rules. It distinguishes a request from an accepted change, identifies the affected
work and develops feasible options: reduce other scope, change timing or quote additional work.

It prepares an evidence-backed decision for the responsible person. After approval, it can prepare or
execute authorised updates to the change document, project plan, internal assignments and customer
message. It waits for the required acceptance, rechecks if capacity or the request changes, and closes
only when the agreed scope and affected operational records match. Pricing and binding commitments
remain approval-gated; a remembered exception is not permission to repeat it.

This is the **strongest initial demonstration of the architecture** because context materially changes
both the reasoning and the actions. It is also a plausible paid entry product where unapproved extra
work is a recurring problem. That demand is still unproven, and PSA products are direct alternatives.
Measure time to an agreed change, review effort and extra work that actually becomes approved and
chargeable—not the nominal value of every issue the agent flags.

### Completed work → invoice-ready evidence

A project milestone is reported as complete, but invoicing depends on accepted deliverables, time records,
a purchase-order reference or customer-specific documentation. The harness compares actual evidence with
the agreement, identifies the precise missing item, prepares a request to the right person and resumes
when the answer arrives. It assembles the billing packet and checks the draft against authoritative rates
and accounting data. Completion means the agreed invoice-readiness criteria are satisfied, not that a
reminder has been sent.

This is a particularly clear **commercial proof candidate** because the buyer can recognise an invoice
blocked by missing paperwork. The agent does not replace accounting rules or decide that delivery is
accepted merely because somebody wrote “done”. Initially it only prepares the packet; posting, tax
classification and sending remain outside autonomous scope. Measure the delay between eligible delivery
and invoice readiness. Do not confuse accelerated billing with additional revenue or promise to eliminate
late payment: customer liquidity and disputed liability may be outside the system's control.[^payments]

### Qualified inquiry → deliverable commitment and clean handoff

An incoming inquiry becomes a small case, not simply a lead to chase. The harness checks the requested
work against service boundaries, relevant previous engagements, delivery capacity, pricing rules and
known constraints. It asks targeted clarification questions, prepares an offer with explicit assumptions
and routes exceptions for approval. Once an agreement exists, it transfers those assumptions and
acceptance criteria into the delivery plan and verifies that an accountable owner can start the work.

This expands the capabilities of a small firm by supporting qualification, planning and commercial
preparation together. The value is an offer the company can actually deliver and a handoff that preserves
its promises—not more personalised outbound email. It is generally applicable within service businesses,
but crowded by CRM, proposal and PSA products. It is an expansion process unless prospect interviews show
that handoff failure is a more painful entry point than changes or billing readiness.

### External requirement → verified evidence package

A customer questionnaire, supplier onboarding request, tender requirement or adviser request asks the
company to prove something. The harness maps each requirement to current authorised evidence, identifies
missing or expired material, asks its owner for a correction and assembles a traceable package for review.
It rechecks the package against the requesting party's criteria before marking it ready.

Here company context prevents invented credentials and inconsistent answers; the loop resolves gaps
rather than simply generating prose. This offers capabilities an owner may otherwise need to buy from
specialists. It is not a claim of legal compliance or a replacement for professional judgement. Begin
with ordinary customer evidence, not a broad tax/legal/compliance product. Specialist evidence platforms
are alternatives that require a separate comparison before selecting this as the entry market.

### Disruption → feasible recovery and confirmed handovers

A supplier delay or capacity change affects an existing commitment. The harness traces dependencies,
checks alternative resources against real constraints and prepares a recovery decision with its effects
on customers, cost and other commitments. Following approval, it coordinates the affected updates and
waits for confirmations rather than stopping at a new schedule.

This is a powerful demonstration of the broader vision: consequences cross departmental boundaries even
though the agent is not impersonating a department. It is a later expansion candidate because feasibility
requires reliable operational data and sector-specific constraints. Restrict access to business-relevant
availability; this is not a justification for employee surveillance or unnecessary personnel-data access.

Across these processes, context repair is a supporting loop: a real case exposes a missing owner,
contradictory rule or undocumented decision; the system requests a targeted clarification and proposes a
reviewed update. Do not turn that into an initial demand to digitise the whole company. Broader knowledge
should grow through useful work, not precede all useful work.

## What to sell, and to whom

“Small and midsize companies” describes a market size category, not a usable first sales segment.
The proposed starting segment is owner-led B2B service firms that repeatedly deliver customer projects,
receive changes through correspondence, and need to reconcile scope, delivery and billing across their
current tools. Engineering services, implementation providers and project-based agencies are examples
to investigate—not confirmed customers or a claim that all have the same process. The buyer is the
person accountable for delivery economics; the daily reviewer may be an operations or project lead.

The front-door offer should describe a result, not the infrastructure: **customer changes made explicit,
decided and reflected in delivery before they become unapproved extra work**. A possible German message
is “Kundenänderungen klären, bevor daraus unbezahlte Arbeit wird.” Demonstrate the request, the original
agreement, the discovered conflict, the approved option and the consistent updated records. The companion
invoice-readiness case shows the same context supporting another outcome. “Company Harness” remains the
platform concept; neither Oracle nor a virtual employee count is the reason to buy.

There is relevant problem evidence, but not yet product demand. KfW identifies tax, record-retention,
documentation and accounting duties as recurring burdens; that is not a measure of time this product can
save.[^kfw] The EU Payment Observatory describes the administrative burden of chasing payment, not proof
that missing documents are the main cause.[^payments] Eurostat reports smaller-firm adoption differences
and expertise/legal/privacy barriers; its enterprise survey excludes the smallest firms, and the barrier
questions concern non-users that considered AI.[^eurostat] Bitkom's survey covers companies with at least
20 employees, not a representative solo-founder sample.[^bitkom] These sources support testing an offer
that reduces implementation work and earns trust, not asserting willingness to pay for a harness.

Start distribution through direct conversations and trusted business introductions, then consider
implementation or business-software partners after the package works. In discovery, reconstruct a recent
actual change or blocked invoice: where was the evidence, who noticed, what happened, how much work was
spent, and why did the current software not resolve it? This is more useful than asking whether an owner
would like an AI assistant. Seek customers who can provide authorised representative cases and an
accountable reviewer; weak access or rare exceptions can make an apparently attractive pilot uneconomic.

The suggested commercial model is a scoped paid setup plus recurring operation of a named process, with
clear source boundaries, review responsibilities and usage limits. Price bands could follow active cases
or project volume rather than invented employee roles, but no price is validated. Track customer review
and maintenance effort as well as Delta Weave's onboarding and support effort. Separate time savings,
verified contribution-margin improvements and cash-flow timing; do not add them together in ways that
count the same benefit twice. A cheap hosted assistant or an existing PSA configuration is a legitimate
baseline, not a competitor to ignore.

## Can we begin in this setup?

**Yes, for a supervised proof of the workflow—not yet for an unattended customer product.** Qoder and the
current structured context repository already provide an operator workbench and an initial knowledge
source. Define a process and preserve each case's evidence, state, proposed actions and approval record
outside the chat. Run it on synthetic or explicitly authorised non-sensitive material first. This can
establish whether company context changes the result before adding a database or another platform.
No software installation is needed for that supervised baseline; reliable event ingestion, multi-user
authorisation and external write execution are still engineering work.

Bevel/Hexis is the most directly relevant **reuse candidate** found for the local-context direction.
Bevel describes versioned context/skills/tools served to agent runtimes over MCP.[^bevel] The README
mirrored by Glama describes Docker Compose, a separate Git repository, PostgreSQL and application secrets;
it also describes HTTP MCP. This is a deployed application, not merely a skill file. Its development path
specifies Node 22, pnpm and Git prerequisites; a container deployment need not change the host's Node
version.[^hexis] Glama lists an Apache 2.0 licence, but the source licence and release still need direct
review before commercial reuse. The GitHub CLI was unavailable during this research, so that source
review was not completed.

Local checks found Node, Python and Git available, but Docker and the GitHub CLI were not available on
this shell's PATH or in the standard installation locations checked. This is not an exhaustive machine
inventory. Source: local version/path checks in this session, Stand 2026-09-19. Therefore an actual Hexis
trial needs an approved local container setup or a separately approved sandbox host, followed by testing
its HTTP MCP authentication and tools with Qoder. Protocol compatibility is plausible, not verified.
Use a new isolated repository; do not let a context server auto-commit into this working hub during a trial.

Lindy offers a different route: use its hosted product instead of extending Qoder. Its reviewed setup
path installs a Slack teammate and links individual accounts; this route requires a paid Slack plan.
That is the documented route reviewed, not a proven requirement for every Lindy product experience.
Its approval settings distinguish “Always allow” from “Ask for approval”, so the latter must be deliberately
selected for a trial. It is not a documented drop-in MCP server for Qoder, and white-label rights were not
established.[^lindy] Do not connect live mail or business accounts merely to inspect a demo.

Fig's reviewed site directs buyers through demos and custom enterprise engagements; it is not the
immediate local starting point.[^fig] Rocketlane, Scoro or Accelo deserve a practical comparison where a
prospect already runs one: extending the existing operational system could be easier than selling a new
layer. No candidate has yet been run against our end-to-end cases, so **full replacement remains an open
empirical question**, not something the research disproved.

## The experiment that decides build versus reuse

Use the same change case and invoice-readiness case in the current Qoder/files baseline and a selected
existing candidate, accounting for its configuration effort. Ask each to find the right evidence,
distinguish request from agreement, develop an allowed next action, wait for a decision, resume after an
interruption and verify the resulting business state. Include changed evidence after approval, a denied
action, a missing document, a revoked source and a retry. A polished draft alone does not pass, and our
own proposed implementation must meet the same standard.

Measure owner effort including context explanation, correction and ongoing curation; elapsed case time;
unsupported claims; wrong or duplicate actions; and total operating cost. Compare with a simple rule or
existing operational tool where appropriate. To isolate the benefit of company context, also compare the
same task and model with only the incoming request versus with authorised company evidence. If context
does not materially improve decisions, it is a poor flagship workflow for this product.

An existing product fully replaces the internal use case if it meets these outcomes acceptably with less
total effort. It replaces the proposed customer offer if target buyers can adopt it, obtain the same
results and operate it more easily at acceptable cost. In either case Delta Weave can choose integration,
configuration or managed delivery instead of recreating infrastructure. Custom development is justified
by an observed missing capability or materially better delivery economics—not by preferring our own stack.

The next commercial gate is an explicitly paid, bounded pilot on a buyer's real process, after data and
approval arrangements are agreed. Combine interviews, a clearly labelled assisted demonstration and a
small reuse test before a larger build. If customers value a different loop, or the current software
already solves the pain, revise the entry offer rather than defending the initial architecture.

## Proposed architecture

These are logical boundaries, not separate services to build immediately.

```text
User / reviewer — initially Qoder, later a branded workspace
                         |
Company application: identity, work items, checkpoints, approvals, audit
                         |
             Agent execution adapter — initially Qoder
                    /                       \
        Context service                 Controlled tool gateway
   evidence, retrieval, policies       scoped reads / approved writes
               |                              |
  Oracle 26ai candidate + originals       Existing business systems
```

**Company application.** Owns durable task state, accountable users, approval records and execution
history. The agent plans how to accomplish a task; application rules control what may advance or execute.
Pausing for a person, restarting a worker and retrying a request must not lose work or duplicate actions.
A small backend and durable job records are a sufficient starting hypothesis; no separate orchestration
platform is justified yet.

**Context service.** Supplies task-relevant, permission-filtered evidence rather than the whole corpus.
Keep original sources, accepted company knowledge, proposed inferences and operational state distinct.
Each accepted fact needs provenance, version, ownership, access scope and an explicit evidence status;
validity and review dates matter where the fact can change. Preserve conflicting claims rather than
letting a summary silently decide which is true. Agent memory must not promote its own guesses to facts.

Start with explicit entities and relationships such as company, contact, project, decision and commitment.
Use exact lookup for identifiers and authoritative values; evaluate semantic retrieval for discovery and
relationship traversal where useful. A graph database is not a prerequisite for a company graph.

**Storage.** Oracle AI Database 26ai is a candidate for consolidated structured context, relationships,
retrieval indexes and work state—not a mechanism that turns arbitrary files into reliable knowledge.
Originals can remain in their source systems or controlled object/file storage, with versioned references
and extraction records. Parsing, access synchronisation, conflict handling and curation remain product work.
Start with a curated subset of authorised material, not an unrestricted company data lake.

**Execution.** Treat “Coda” in the source as provisionally meaning **Qoder**. Use it first as the operator
workbench. A supported machine interface could later make it an execution worker; MCP tool access alone
does not establish an embeddable, durable or commercially redistributable runtime. If that integration is
unsuitable, retain Qoder for development and operations while selecting a supported product runtime.
Do not build the product around UI automation or undocumented session internals.

**Tools and trust.** An execution worker receives limited capabilities, not unrestricted company credentials.
Enforce authorisation outside the model, including at retrieval and immediately before a write. Approvals
bind to the actual action and payload; material changes require renewed review. Use isolated workers and
controlled file/network access so shell tools cannot bypass the gateway. Retrieved documents are evidence,
not instructions allowed to grant permissions. Prompt guardrails and harness hooks are not the security boundary.

Apply access restrictions to derived summaries and indexes as well as originals. Revocation and deletion
must invalidate affected derived content. Decide model-provider data handling and permitted outbound data
before ingestion. For initial customer pilots, prefer dedicated company deployments over shared tenancy;
multiple users within a company still require individual permissions. The hub's `private/` content is
excluded from the prototype and must not be uploaded through this plan.

## Technology validation before commitment

The initial external lookup was blocked; the follow-up market research used available web tools because
the Firecrawl CLI was not installed. Competitor documentation is cited below, but Qoder product-runtime
capabilities, Oracle deployment choices and commercial redistribution rights remain **unverified**.
Do not infer them from the attachment or from the fact that this interactive Qoder session works.

| Candidate | What must be established | Consequence |
|---|---|---|
| Qoder | Supported unattended integration, structured events, cancellation, restart behaviour, tool restrictions, model selection, concurrency, hosted use and white-label rights | Operator tool first; product runtime only after the technical and commercial gates pass |
| Oracle AI Database 26ai | Exact edition/deployment, relevant vector/search/graph features, drivers, permission enforcement, backup/export, region, operating cost and commercial terms | Prototype the actual retrieval workload; do not choose from a feature checklist alone |
| Model providers | Tool reliability, approved data processing, latency and cost on representative tasks | Changes must pass the same evaluation cases; swapping a model can change behaviour |

Keep source documents, canonical records, process definitions and evaluation cases exportable. Isolate
vendor-specific queries at a small service boundary. Database migration can still require query changes,
re-indexing and new embeddings; “replaceable” does not mean cost-free or instant.

## Development plan — evidence gates, not promised dates

| Stage | Deliverable | Gate before expanding |
|---|---|---|
| Validate pain and baseline | Reconstruct actual buyer cases; define change-control and invoice-readiness outcomes; demonstrate with Qoder/files and authorised evidence | The buyer recognises a recurring cost, a reviewer can judge completion, and a simple existing tool is not already sufficient |
| Compare reuse | Test the same cases on a selected existing product/component; Hexis is a context candidate, not a predetermined choice | Know what it replaces, setup/maintenance effort and remaining execution or commercial constraints |
| Internal working loop | Build only the missing pieces for context, durable case state, bounded actions and continuation | Repeated work improves total effort including curation and review; storage beyond files has a demonstrated purpose |
| Customer pilot | Paid, scoped workflow with approved data access and explicit review responsibilities; minimal interface if required | The same core survives company-specific data, roles and vocabulary without a code fork and without the founder interpreting every result |
| Productise | Repeatable onboarding, versioned process packs, provisioning, branding, metering, support and recovery procedures | Reuse and sustainable operating effort are demonstrated across comparable deployments; commercial rights are settled |

Oracle remains a storage candidate, but is not a prerequisite for proving the workflow or the buyer's
interest. If Hexis is selected, its documented PostgreSQL-based application should be evaluated as it is;
do not add Oracle solely to preserve the initial sketch. Revisit consolidation when real data and retrieval
requirements justify it. This refines the earlier technical-spike-first recommendation; it is not a
confirmed vendor choice.

For every stage, include failure cases: absent evidence, stale sources, conflicting figures, revoked access,
untrusted document instructions, denied approval, worker interruption and retries of an external action.
Before enabling external writes, demonstrate that retrying cannot silently repeat a business action and
that a human can see and recover from uncertain outcomes.

The boundary between product and consulting is repeatable configuration rather than bespoke code—not the
presence of a branded chat window. Compare onboarding effort for similar scope; a harder customer is not
by itself evidence against productisation. Prices, budgets and delivery dates are intentionally unset.

## Proposed next decision

Keep the broad company-work-layer ambition. Start here with a supervised **customer-change-to-resolution**
case and use **delivery-to-invoice-readiness** as the companion commercial test. Judge an existing component
or product against those same outcomes before choosing what to build. Hexis warrants an isolated setup
investigation; it is neither a confirmed complete replacement nor a reason to deploy another platform
before the process is clear. The next step is defining the acceptance cases and preparing authorised test
material, not installing software or connecting live business accounts without approval.

## Sources and evidence limits

All external sources below were accessed on **2026-09-19** during the user-requested research. Publication
or update dates are included where the page supplied them. Vendor pages establish documented or advertised
capabilities, not independent proof of reliable execution. Setup has not been tested. Pricing pages showed
variant-dependent information, so no numerical pricing comparison is used. The review is selective, not an
exhaustive market census. Public survey evidence does not establish demand for this particular product.

[^microsoft]: Microsoft Learn, [Design autonomous agent capabilities](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/autonomous-agents), metadata updated 2026-09-12; [Event triggers overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about). Documents autonomous execution and oversight guidance; this is not a deployment test. Stand 2026-09-19.

[^glean]: Glean documentation, [How agents work](https://docs.glean.com/agents/how-agents-work), updated 2026-09-11. Describes Auto/Workflow modes and Independent Agents with system profiles and admin-managed credentials. No inference of missing approvals from this page's silence. Stand 2026-09-19.

[^dust]: Dust Academy, [Webhook triggers](https://dust.tt/academy/agent-automation/chapter/webhook-triggers), dated 2026-05-05. Documents admin-configured built-in/custom event sources and separate conversations for events; does not establish the absence of approval capabilities. Stand 2026-09-19.

[^rocketlane]: Rocketlane, [AI Agents for Service Delivery](https://www.rocketlane.com/agentic-psa), undated product page; [Documentation Agents](https://www.rocketlane.com/blogs/nitro-documentation-agents), published 2026-04-15. Vendor describes shared knowledge, executable delivery tasks, review and source-linked documents updated from correspondence. Stand 2026-09-19.

[^scoro]: Scoro, [April Update: AI-Powered ELI Assistant — Out of Beta](https://www.scoro.com/blog/scoro-version-update-26-4/), article dated 2026-04-09. Release notes describe operational context and workspace actions, including multi-step usage credits. Stand 2026-09-19.

[^accelo]: Accelo, [Professional Services AI Software](https://www.accelo.com/ai), undated product page. Vendor describes project/resource/financial queries, predictive risk, margin warnings and MCP connectivity. Competitor-comparison claims and promotional ROI figures are not treated as verified evidence. Stand 2026-09-19.

[^bevel]: Bevel, [official product site](https://www.bevel.software/), undated. Describes Git-backed context/skills/tools, provenance, permissions, MCP access and open-source Hexis. It does not by itself establish operational maturity or easy installation. Stand 2026-09-19.

[^hexis]: Glama, [Hexis MCP listing and mirrored README](https://glama.ai/mcp/servers/Bevel-Software/Hexis). Third-party metadata lists Apache 2.0; displayed setup describes Docker Compose, Git, PostgreSQL, application secrets and HTTP MCP, with a separate Node/pnpm development path. The original source licence/release was not directly inspected; no install command from this mirror was executed. Stand 2026-09-19.

[^lindy]: Lindy, [product site](https://www.lindy.ai/), [quickstart](https://docs.lindy.ai/start-here/quickstart) and [teammate setup](https://docs.lindy.ai/teammate/setup), undated pages. Product claims and the reviewed Slack onboarding path are distinguished; setup documents configurable write approval. No external Qoder MCP-server or white-label compatibility was established. Stand 2026-09-19.

[^fig]: [Fig Labs](https://figlabs.ai/), undated, advertises governed context/flows/MCP and custom enterprise engagements. [Fig AI](https://hellofig.io/) is another plausible name match from the research; Manuel's intended reference remains unresolved. No identity, availability or traction claim is inferred beyond the pages. Stand 2026-09-19.

[^relevance]: Relevance AI, [product site](https://relevanceai.com/) and [documentation introduction](https://relevanceai.com/docs/get-started/introduction), undated. Describes workforce/agent construction, context, event triggers and human oversight. Marketing personas are not a technical limit on workflows. Stand 2026-09-19.

[^relay]: [Relay.app official site](https://relay.app/), accessed 2026-09-19, states that the service shut down in September 2026. No causal or category-wide business conclusion is drawn from the notice.

[^kfw]: KfW Research, [Mittelstand verwendet sieben Prozent der Arbeitszeit für bürokratische Prozesse](https://www.kfw.de/%C3%9Cber-die-KfW/Newsroom/Aktuelles/Pressemitteilungen-Details_847424.html), published 2025-04-25. German SME panel; measured burden concerns specified compliance processes and is unevenly distributed. It is not an estimate of AI-addressable savings. Stand 2026-09-19.

[^payments]: European Commission, [EU Payment Observatory — analysis](https://single-market-economy.ec.europa.eu/smes/challenges-and-resilience/late-payment/eu-payment-observatory/observatory-analysis_en), Annual Report 2025 summary published 2025-12-15, covering 2024 payment behaviour. Payment terms, actual payment periods, administrative effort and causes are distinct. Unverified secondary statistics are omitted. Stand 2026-09-19.

[^eurostat]: Eurostat, [Use of artificial intelligence in enterprises](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Use_of_artificial_intelligence_in_enterprises), 2025 data, extracted December 2025. Population threshold is at least 10 employed persons in the covered sectors; do not generalise to all microbusinesses. The stated adoption barriers concern enterprises that considered but did not use AI. Stand 2026-09-19.

[^bitkom]: Bitkom, [Digitalisierung der Wirtschaft: Unternehmen beschäftigen sich mit KI](https://www.bitkom.org/Presse/Presseinformation/Digitalisierung-der-Wirtschaft-Unternehmen-beschaeftigen-sich-mit-KI), published 2026-03-11. Survey of 604 German companies with at least 20 employees; evidence about AI/data use and barriers, not a test of this product or all SMEs. Stand 2026-09-19.

Related context in the Delta Weave hub (cross-drive, therefore given as paths and not as links):
`D:\OneDrive\Delta Weave\company\vision.md` — method and positioning, including the open question whether
Delta Weave sells commissioned work or its own product;
`D:\OneDrive\Delta Weave\company\oeffentlichkeit.md` — publication allow-list, required before anything
leaves this workspace;
`D:\OneDrive\Delta Weave\decisions\log.md` — the hub chronicle, which records how this idea was scoped
and moved here.
