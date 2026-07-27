# RE_novel — Romance Engine v5.0, implemented, with three produced novels

This repository implements the **Romance Engine** (Consolidated Operating
Document v5.0, with Addendum M and the Calibration Corpus v0.1 in force) and
uses it to produce complete novels from rows of the Unified Seed Matrix.
Three titles have been produced, all through the same orchestrator and the
same binding:

> **Book 1 — Seed `01KYDG7NWVMNN9C7DTKZ76F54Q`, *Clean Exit*** (Sable Voss,
> Moretti Family #1) — Mafia/Dark, enemies-to-lovers, Heat 4, HEA, Chicago,
> late winter, 31-day story clock. **80,185 words.**
>
> **Book 2 — Seed `01KYF6MB0CBHSYJG5CC2TKW0WD`, *Safe Passage*** (row 3 of
> the matrix) — Mafia/Dark, forced-proximity / reluctant-allies-to-lovers,
> HEA, the Great Lakes freight corridor Chicago→Port Huron, May, 19-day
> story clock. **71,217 words.**
>
> **Book 3 — Seed `01KYFVZ2V7QFV4DN2XRAAPHTQ3`, *Out of Office*** (Wren
> Halliday, Kelvin Row #1) — Rom-Com/Workplace, sapphic fake-dating,
> Heat 2, HFN, community radio in Glasgow, autumn, 46-day story clock.
> **62,271 words.**

## Layout

| Path | What it is |
|---|---|
| `main.py` | The reference orchestrator (deterministic core §15.8, canonical scene loop §11.1, executable §15 fixture). Used verbatim as supplied, for both books. |
| `seed/` | The Unified Seed Matrix workbooks and the extracted seed rows (`seed_row.json`, `seed_row_safe_passage.json`, `seed_row_kelvin.json`) — §16 Unified_Seed_Row. |
| `tools/seed_from_xlsx.py` | Stdlib-only xlsx → seed-row extractor. Takes `<matrix.xlsx> [row_index]`. |
| `tools/build_manuscript.py` | Assembles a book's chapter files into the single deliverable and reports word counts. |
| `binding/` | The **offline-agent-v1 binding configuration** (Addendum M): `offline_client.py` (the `ModelClient` adapter, schedule-selectable) + one authored editorial schedule per title (`schedule.py`, `schedule_safe_passage.py`, `schedule_out_of_office.py`). |
| `run_book.py` | Driver: runs the §11.1 loop over a seed row. `--seed / --schedule / --out / --scenes / --path`. |
| `artifacts/`, `artifacts_safe_passage/`, `artifacts_out_of_office/` | Per book: `scene_ledger.json` (per-scene structural ledger), `scene_briefs.md` (PRIMARY-PROSE work orders), `run_summary.md`. |
| `manuscript/` | *Clean Exit* — 16 chapters + epilogue, plus the per-title IP log. `CLEAN_EXIT.md` is the assembled deliverable. |
| `manuscript_safe_passage/` | *Safe Passage* — 17 chapters + epilogue, plus the per-title IP log. `SAFE_PASSAGE.md` is the assembled deliverable. |
| `manuscript_out_of_office/` | *Out of Office* — 24 chapters, no epilogue (`Epilogue_Included = false`), plus the per-title IP log, blurb, and cover. `OUT_OF_OFFICE.md` is the assembled deliverable. |

## How to verify

```bash
python3 main.py --fixture                      # reproduces every §15 ledger value exactly

# Book 1
python3 run_book.py

# Book 2
python3 run_book.py \
  --seed seed/seed_row_safe_passage.json \
  --schedule binding.schedule_safe_passage \
  --out artifacts_safe_passage

# Book 3
python3 run_book.py \
  --seed seed/seed_row_kelvin.json \
  --schedule binding.schedule_out_of_office \
  --out artifacts_out_of_office \
  --scenes 45

python3 tools/build_manuscript.py              # rebuild all three assembled manuscripts
python3 tools/seed_from_xlsx.py seed/Romance_Engine_Unified_Seed_Matrix.xlsx 2
```

The fixture requires no binding (Addendum M's proof instrument); `run_book.py`
re-runs all 45 scenes of any title deterministically — same ledger, same
briefs, byte for byte.

## The binding configuration (Addendum M compliance)

Per §1.2 the model's entire role is elicitation; every blend, threshold,
gate, transform, fit and simulation is orchestrator arithmetic in `main.py`.
This repo binds the elicitation surface to **`offline-agent-v1`**, a
deterministic configuration that runs with no network access:

- **PRIMARY-STRUCT / JUDGE** — answered from an authored editorial schedule:
  the proposer emits the authored move plus procedurally generated admissible
  alternates; the pairwise judge encodes the editorial preference order (both
  within-pair orders, per R12); pair-tension bands are solved numerically so
  the elicited values reproduce the scheduled `T_scene` trajectory exactly
  under the §15.8 arithmetic. The BT fits, Stage-1/Stage-2 blends, shortlist,
  lookahead, utility selection, anchored confirmation and the ED floor all
  run in `main.py`, unmodified.
- **PRIMARY-PROSE** — the loop emits scene briefs; the finished prose was
  authored from those briefs by the bound agent (Claude, acting as the
  PRIMARY-PROSE lane) and shipped as the manuscript directories.
- **Reconciliation** — `main.py` pins §7.2 reconciliation to the orchestrator
  but does not implement grant/CE lifecycle application; the binding performs
  those side effects at extraction time (consent grants, withdrawals, CE
  close/misfire), exactly as §7.2 assigns them.
- **Caller-side initiator wiring** — `main.py`'s `evaluate_phase` computes the
  §6.3 initiator from `T_scene` only and notes the fracture/inversion
  initiators are "tracked by caller in full wiring"; `run_book.py` supplies
  that wiring for each title's scheduled fracture scenes. Gates G1–G6 are
  still evaluated unmodified.

The adapter surface really is one `ModelClient` subclass, as Addendum M
claims: adding Book 2 and Book 3 each required only a new schedule module
and a seed row, and no change whatsoever to `main.py`.

No calibration card exists for this configuration, so all floors and ρ
readings are **provisional**, exactly as R11 requires; the ED floor (0.45,
provisional) was evaluated on every shipped winner in both books and never
failed.

## Book 1 — *Clean Exit*

- **Scene count**: 45 scenes (operator override of the 90-scene reference
  allocation; phase blocks scaled proportionally, `3·4·5·5·5·6·6·5·6`).
  All six §6.3 gates passed at every phase boundary; zero regressions;
  zero review flags; zero unrealized deltas.
- **Set pieces** land in their seeded phases: the on-the-record interview
  (Ph0), the staged threat against the brother (Ph2), the consent negotiation
  before first C3 contact (Ph5), the family-dinner confrontation over the
  ledger (Ph5), and the ledger's disposition resolving on the page (Ph7).
- **CE lifecycle**: CE-02 (Threat) closes at the Ph5 dinner; CE-03
  (Obligation) closes on the confidant's confession; CE-01 (Secret) misfires
  at the warrant execution (weight 0.9 → 1.0, stays open) and closes at the
  Ph7 proffer; CE-04 (Promise) pays verbatim (L7 discipline) and closes at
  the release door.
- **Word count**: rendered at the seed's `Word_Count_Target`.
  `Word_Count_Actual` = **80,185** (16 chapters + epilogue; mean ≈ 1,780
  words per engine scene). R22 editor pass and full constraint verification
  logged in `manuscript/HCL-CLEAN-EXIT-B01.md`.

## Book 2 — *Safe Passage*

- **Scene count**: 45 scenes against the same Mafia/Dark arc profile and the
  same phase blocks, for direct comparability. Final run: 45 scenes,
  0 flags.
- **Set pieces** land in their seeded phases: the passage debt called in at
  the yard (Ph0), the first deviation onto an unlisted crossing (Ph2), the
  freighter-layover truth trade (Ph4), the consent negotiation before first
  C3 contact (Ph5), and the handover at the border yard resolving on the
  page (Ph7).
- **Consent architecture (§4.5)** is the spine of this title rather than a
  compliance layer. The custody imbalance is named on the page and converted
  into a standing boundary (sc. 19); a real, funded exit is offered and
  refused (sc. 21) *before* any grant exists; first kiss is her move with
  that exit still standing open (sc. 22); withdrawal is performed by the
  party who was in custody, for the clause that was actually broken (sc. 39);
  and the re-grant is his initiative, from outside the gate, with widened
  scope (sc. 43). `First_Kiss_Phase = 4` and `First_Intimacy_Phase = 5` are
  honored as scheduling priors subordinate to the grants, per §16.3.
- **CE lifecycle**: CE-03 (the passage secret) closes on the Alpena
  breakwater; CE-02 (the licence threat) closes when the road boss walks out
  onto gravel; CE-01 (the debt) is discharged by being *voided* rather than
  paid; CE-04 (Promise) pays verbatim at the witness box.
- **Four scheduling repairs** were required during dry runs — an inadmissible
  contact, a missing band crossing at G4, a premature Phase-4 advance that
  would have broken `First_Kiss_Phase`, and a register that ended warm but
  not safe. Each is itemized in the IP log; in every case the schedule was
  wrong and the engine's refusal to advance was the evidence.
- **Word count**: the seed's band is 70,000–90,000. `Word_Count_Actual` =
  **71,217** (17 chapters + epilogue). R22 editor pass and full constraint
  verification logged in `manuscript_safe_passage/HCL-SAFE-PASSAGE-B02.md`.

## Book 3 — *Out of Office*

- **Scene count**: 45 scenes against the Rom-Com/Workplace arc profile
  `E = [10,12,12,8,10,10,10,8,10]`, halved to `[5,6,6,4,5,5,5,4,5]` since
  every entry is even — same halving discipline as Books 1–2, so all three
  titles are directly comparable at the same scene count. Final run: 45
  scenes, final phase 8, **0 review flags**, 0 unrealized deltas.
- **Set pieces** land in their seeded phases: the panel promise made with
  nothing to back it (Ph0), the on-air stunt kiss at the end of broadcast
  one (Ph2), the listener call-in neither presenter can answer in character
  (Ph4), the consent negotiation before first C3 contact (Ph6), and the
  final broadcast running off script and onto the record (Ph7).
- **Consent architecture (§4.5)**: initial terms (no unplanned physical
  contact, the overnight desk stays off the record, a stop-word ends any
  segment immediately) are negotiated on the record, in writing, witnessed
  by a third party (ch. 3); the scripted stunt kiss is separately asked and
  granted off mic the night before broadcast one (ch. 6); the first
  *unscripted* kiss is asked and granted on Nadia's own terms (ch. 15);
  first intimacy (`First_Intimacy_Phase = 6`) is granted on the page inside
  the negotiated Phase 6 window, with the standing request to be asked
  again, repeatedly, honoured explicitly (ch. 18).
- **CE lifecycle**: CE-04 (Obligation) closes first; CE-03 (Absence, the
  mother's voicemail tape) closes with company present rather than alone;
  CE-02 (Revelation, Nadia's anonymous segment) closes privately between the
  leads before it is ever disclosed to the show's audience; CE-01 (Promise)
  misfires when the hot-mic accident breaks it and pays verbatim (L7
  discipline) at the origin scene and again at the final broadcast.
- **Five scheduling repairs** were required during dry runs — a scene-
  authoring `TypeError`, a phase-advance drift across all eight transitions
  traced to a one-scene-early delta placement, six delta-cap violations
  fixed at the source rather than relying on inferred repair behaviour, a
  regression this introduced into the Phase 7→8 crossing, and three missing
  CE `close=[...]` calls. Each is itemized in the IP log; in every case the
  schedule was wrong and the engine's rejection or refusal to advance was
  the evidence.
- **Word count**: seed target `Word_Count_Target = 62000`. `Word_Count_Actual`
  = **62,271** (24 chapters, no epilogue per `Epilogue_Included = false`).
  R22 editor pass and full constraint verification logged in
  `manuscript_out_of_office/HCL-OUT-OF-OFFICE-B01.md`.
- **Blurb and cover**: `manuscript_out_of_office/BLURB.md` and
  `manuscript_out_of_office/cover/` (source HTML/SVG plus the rendered
  cover image, at the seed's `Cover_Dimensions`).
