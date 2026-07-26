# RE_novel — Romance Engine v5.0, implemented, with one produced novel

This repository implements the **Romance Engine** (Consolidated Operating
Document v5.0, with Addendum M and the Calibration Corpus v0.1 in force) and
uses it to produce one complete novel from the single populated row of the
Unified Seed Matrix:

> **Seed `01KYDG7NWVMNN9C7DTKZ76F54Q` — *Clean Exit*** (Sable Voss, Moretti
> Family #1) — Mafia/Dark, enemies-to-lovers, Heat 4, HEA, Chicago, late
> winter, 31-day story clock.

## Layout

| Path | What it is |
|---|---|
| `main.py` | The reference orchestrator (deterministic core §15.8, canonical scene loop §11.1, executable §15 fixture). Used verbatim as supplied. |
| `seed/` | The Unified Seed Matrix workbook and the extracted `seed_row.json` (§16 Unified_Seed_Row). |
| `tools/seed_from_xlsx.py` | Stdlib-only xlsx → seed-row extractor. |
| `binding/` | The **offline-agent-v1 binding configuration** (Addendum M): `schedule.py` (authored editorial layer) + `offline_client.py` (the `ModelClient` adapter). |
| `run_book.py` | Driver: runs the §11.1 loop over the seed row, 45 scenes, Path B; writes the artifacts. |
| `artifacts/` | `scene_ledger.json` (per-scene structural ledger), `scene_briefs.md` (PRIMARY-PROSE work orders), `run_summary.md`. |
| `manuscript/` | The novel — 16 chapters + epilogue rendered from the scene briefs under kernel VK-EN-MD-01. |

## How to verify

```bash
python3 main.py --fixture          # reproduces every §15 ledger value exactly
python3 run_book.py                # re-runs the scene loop; regenerates artifacts
python3 tools/seed_from_xlsx.py seed/Romance_Engine_Unified_Seed_Matrix.xlsx  # re-extract the seed row
```

The fixture requires no binding (Addendum M's proof instrument); `run_book.py`
re-runs all 45 scenes deterministically — same ledger, same briefs, byte for
byte.

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
- **PRIMARY-PROSE** — the loop emits scene briefs (`artifacts/scene_briefs.md`);
  the finished prose was authored from those briefs by the bound agent
  (Claude, acting as the PRIMARY-PROSE lane) and shipped as `manuscript/`.
- **Reconciliation** — `main.py` pins §7.2 reconciliation to the orchestrator
  but does not implement grant/CE lifecycle application; the binding performs
  those side effects at extraction time (consent grants, withdrawals, CE
  close/misfire), exactly as §7.2 assigns them.
- **Caller-side initiator wiring** — `main.py`'s `evaluate_phase` computes the
  §6.3 initiator from `T_scene` only and notes the fracture/inversion
  initiators are "tracked by caller in full wiring"; `run_book.py` supplies
  that wiring for the two scheduled fracture scenes (34: warrant executed;
  39: reversal complete). Gates G1–G6 are still evaluated unmodified.

No calibration card exists for this configuration, so all floors and ρ
readings are **provisional**, exactly as R11 requires; the ED floor (0.45,
provisional) was evaluated on every shipped winner and never failed.

## Production notes for this title

- **Scene count**: 45 scenes (operator override of the 90-scene reference
  allocation; phase blocks scaled proportionally, `3·4·5·5·5·6·6·5·6`).
  All six §6.3 gates were passed at every phase boundary; zero regressions;
  zero review flags; zero unrealized deltas.
- **Set pieces** land in their seeded phases: the on-the-record interview
  (Ph0), the staged threat against the brother (Ph2), the consent negotiation
  before first C3 contact (Ph5), the family-dinner confrontation over the
  ledger (Ph5), and the ledger's disposition resolving on the page (Ph7).
- **Consent architecture (§4.5)**: every contact above C1 in the book sits
  under an explicit on-page grant negotiated in an earlier shipped scene;
  the post-betrayal withdrawal voids all standing grants the moment the beat
  lands, and intimacy resumes only after an explicit on-page re-grant.
  First_Kiss_Phase 5 and First_Intimacy_Phase 6 are honored as scheduling
  priors *subordinate* to the grants, per §16.3.
- **CE lifecycle**: CE-02 (Threat) closes at the Ph5 dinner; CE-03
  (Obligation) closes on the confidant's confession; CE-01 (Secret) misfires
  at the warrant execution (weight 0.9 → 1.0, stays open) and closes at the
  Ph7 proffer; CE-04 (Promise) pays verbatim (L7 discipline) and closes at
  the release door.
- **Word count**: the manuscript is an abridged-length rendering
  (~30–33k words) of the 80k-word seed target — an operator decision recorded
  in `manuscript/HCL-CLEAN-EXIT-B01.md` with the R22 editor pass
  (`Editor_Pass_Count = 1`).
