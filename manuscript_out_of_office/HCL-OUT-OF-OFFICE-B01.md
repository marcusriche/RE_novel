# Human Contribution Log — HCL-OUT-OF-OFFICE-B01

Per-title IP log referenced by the seed row's `Human_Contribution_Log_Ref`
(§13.5, R22). Records operator decisions and the editorial provenance of
this title's production run.

Seed: `01KYFVZ2V7QFV4DN2XRAAPHTQ3` — row 3 of
`Romance_Engine_Unified_Seed_Matrix.xlsx` (*Out of Office*, Kelvin Row Book 1).

| # | Date | Actor | Contribution |
|---|------|-------|--------------|
| 1 | 2026-07-26 | Operator (Claude agent session, on user instruction) | Selected Seed-Matrix row 3 (`01KYFVZ2V7QFV4DN2XRAAPHTQ3`, *Out of Office*) for production from the re-uploaded matrix. Extraction via `tools/seed_from_xlsx.py <matrix> 3` → `seed/seed_row_kelvin.json`. |
| 2 | 2026-07-26 | Operator | Scene-count decision: 45 scenes against the Rom-Com/Workplace arc profile `E = [10,12,12,8,10,10,10,8,10]` (sum 90), halved to `[5,6,6,4,5,5,5,4,5]` (sum 45) since every entry is even — same halving discipline used for Books 1 and 2, so all three titles are directly comparable at the same scene count. |
| 3 | 2026-07-26 | Operator | Ran the existing generic pipeline (`main.py` unmodified, `binding/offline_client.py`'s schedule-selectable `OfflineBindingClient`, `run_book.py --seed --schedule --out --scenes --path`) unchanged from Books 1–2. No engine or binding-layer code modified for this title. |
| 4 | 2026-07-26 | Editorial (offline binding schedule) | Authored the 45-scene editorial schedule (`binding/schedule_out_of_office.py`): cast realization (A→Robyn Fyfe, B→Nadia Quinn, C→Priya Shah, E→Kirsty Lennox, antagonist node → "the funding review"), six-broadcast structure, set-piece placement (panel promise, stunt kiss, listener call-in midpoint, C2/C3 consent negotiation, off-script finale), CE lifecycle (Promise/Revelation/Absence/Obligation — no Secret/Threat, unlike Books 1–2), fracture-initiator overrides at scenes 36 and 40 for the structurally unreachable Phase 6 ceiling. |
| 5 | 2026-07-26 | Operator | Five scheduling repairs made during dry runs, each recorded rather than papered over — see "Engine-level repairs" below. |
| 6 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Rendered all 45 scene briefs into prose under kernel VK-EN-RC-01 (24 chapters, no epilogue — `Epilogue_Included = false`). |
| 7 | 2026-07-26 | Operator | Word-count decision: seed target `Word_Count_Target = 62000`. Final `Word_Count_Actual` = 62,271 (per `tools/build_manuscript.py out_of_office`, assembled manuscript incl. front matter), within 0.5% of target. |
| 8 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Enrichment pass across all 24 chapters, run in several rounds. No scene added, removed, reordered, or reassigned relative to `artifacts_out_of_office/scene_ledger.json`. New material is scene-interior and inter-scene texture — dialogue, interiority, secondary-character beats (Priya, Kirsty, Malcolm, Fiona, Sandra, Grant, Dev), and a recurring sister-phone-call throughline — not new plot or new CEs. |
| 9 | 2026-07-26 | Editor pass 1 of 1 (R22 gate: `Editor_Pass_Count` = 1) | Full-manuscript QC. See "Editor pass findings" below. |

## Engine-level repairs (item 5, itemized)

These are recorded because each one is a place where the schedule, not the
engine, was wrong — and the engine's refusal to advance (or its delta-cap
rejection) is the evidence.

1. **`TypeError` on scene 5 authoring.** An early draft of the scene-5 `S()`
   call carried a stray extra positional argument before `idelta`, so Python
   raised `got multiple values for argument 'hot'`. Fixed by removing the
   stray token and restoring correct positional alignment; not an engine
   fault, a schedule-authoring bug.
2. **Phase-advance drift across all eight transitions.** The first draft
   schedule advanced every phase later than intended (e.g. Phase 0→1 landing
   at scene 8 instead of the intended scene 5), because crossing/threshold
   deltas were authored on the *last* scene of each phase rather than the
   second-to-last — and the gate at scene *N* only ever sees cumulative
   deltas through scene *N*−1. Diagnosed with a monkeypatched
   `evaluate_phase` trace script. Fixed with one targeted change — adding
   `("A","B","trust",0.08)` to scene 4 — which cascaded to correct all eight
   transitions simultaneously (re-traced and confirmed landing exactly on
   {5, 11, 17, 21, 26, 31, 36, 40}).
3. **Six delta-cap violations** (scenes 32, 36, 40; `|Δ| > K.DELTA_CAP =
   0.15`). `structural_verify()` rejects the whole candidate on a cap
   violation rather than silently clamping it, logging
   `{'rejected': 's{n}-plan', 'why': [...]}` to `state.review_flags`. Fixed
   at the source rather than relying on inferred repair behaviour: each
   offending delta was reduced to exactly 0.15, with the displaced emotional
   magnitude redistributed into an added second channel where the beat
   needed it (e.g. scene 32 gained `emotional_safety +0.06` alongside the
   reduced `vulnerability`; scene 36's fear/emotional_safety pair was
   trimmed from ±0.16 to ±0.15; scene 40's vulnerability/trust pair from
   0.18/0.16 to 0.15 each).
4. **Phase 7→8 regression after the cap fix.** Reducing scenes 32 and 36
   shifted Phase 7's entry snapshot enough that scene 40's G4 crossing
   (previously satisfied) stopped registering. Fixed with a small
   `("B","A","resentment",0.06)` nudge added to scene 39.
5. **Missing CE `close=[...]` calls.** Scene synopses narrated CE-04/03/02
   closing at specific points, but the `close=` kwarg had only been set on
   scene 40 (`CE-01`). Caught via `run_summary.md` showing all three still
   "Open" at story end on a dry run. Fixed by adding `close=["CE-04"]` to
   scene 26, `close=["CE-03"]` to scene 30, and `close=["CE-02"]` to scene 32.

Final run: 45 scenes shipped, final phase 8, **0 review flags**, 0
unrealized deltas, schedule problems: none.
`python3 main.py --fixture` reproduces the §15 fixture exactly, unaffected
by this title's schedule.

## Editor pass findings (item 9, itemized)

- **Brand-lexicon ban sweep** (`orbs`, `smirked`, `chuckled darkly`, `sass`,
  `adorkable`): 0 hits across all 24 chapters and front matter.
- **Preferred lexicon** (`static`, `levels`, `rain`, `tea`, `signal`):
  present throughout — `static` ×21 carries the title's central pun (the
  overnight segment's name, and the space between two people not yet
  saying a true thing); `tea` ×40 and `rain` ×33 run as the book's ambient
  texture per `Locale_Signature`.
- **Dialogue punctuation**: no semicolons inside quoted dialogue anywhere
  in the manuscript.
- **Duplicate-paragraph scan**: automated scan (paragraph-level, >60 chars)
  across and within all 24 chapter files — 0 hits.
- **Continuity_Constraints verified**:
  - *"the story is organised around six weekly live broadcasts; every
    phase advance crosses at least one of them"* — held. Broadcasts land in
    ch. 7 (One), ch. 10 (Two), ch. 15/18 region (Three–Five across the
    Phase 3–6 chapters), and ch. 22 (Six, "On the Level, Broadcast Six"),
    with all eight phase advances landing on the scheduled scenes
    {5, 11, 17, 21, 26, 31, 36, 40}.
  - *"the funding decision lands on story day 44 and cannot be brought
    forward"* — held; ch. 23 opens "Day forty-four, exactly where the
    clock always said it would land."
  - *"the station never leaves Glasgow — no travel subplot"* — held. Every
    scene is set in Glasgow (Kelvin Row, Dumbarton Road, Byres Road, the
    Botanics, the Chambers annexe). Fiona's visits are inbound (Aberdeen →
    Glasgow); Robyn never travels.
  - *"B's anonymous segment stays anonymous to the listeners through Phase
    6"* — held. Nadia discloses Static to Robyn privately in ch. 17
    (Phase 6); the segment is only revealed to the listening audience live,
    on air, in ch. 22 (Phase 8, the final broadcast).
  - *"nothing said on air can be unsaid; broadcast is treated as a
    permanent record within the story"* — held, and load-bearing: the
    hot-mic accident in ch. 19 is driven entirely by this constraint (an
    old test recording, never meant for broadcast, aired regardless and
    cannot be recalled), and CE-01's payoff in ch. 22 turns on the same
    fact in the opposite direction — what Nadia says live, she says
    knowing it cannot be unsaid.
- **Taboo list** — held. No on-page sexual coercion; Heat 2 closed-door
  intimacy per `Taboo_List_and_Sensitive_Notes`. The fake relationship is
  never used to obtain anything from the other lead — Nadia's participation
  is fee-negotiated in writing (ch. 3) before any performance begins, and
  every escalation beyond the negotiated segment is separately consented
  off-mic first, per §4.5:
  - initial terms (no unplanned physical contact, the overnight desk stays
    off the record, a stop-word ends any segment immediately) are
    negotiated on the record, in writing, witnessed by Priya (ch. 3);
  - the scripted stunt kiss is separately asked and granted, off mic, the
    night before broadcast one (ch. 6);
  - the first *unscripted* kiss is asked and granted, off mic, on Nadia's
    own terms, in her own flat (ch. 15);
  - first intimacy (`First_Intimacy_Phase = 6`) is asked and granted on the
    page in ch. 18, inside the negotiated Phase 6 window, with Nadia's
    standing request to be asked again, repeatedly, honoured explicitly;
  - the Breakup_Beat (`contract_ends`) and Reunion_Mode (`public_correction`)
    both land as scheduled: the six-week contract's natural end (ch. 18) is
    overtaken by the hot-mic crisis (ch. 19–21), and the reunion is public
    and on the record, live, in ch. 22.
- **L7 promise discipline** — held. CE-01's wording ("What's real off that
  mic stays off the record... I promise you that") is quoted verbatim at
  origin (ch. 6, the fire escape, the night before broadcast one) and at
  payoff (ch. 22, broadcast six, on air), with no paraphrase drift.
- **Backstory consistency pass.** One drafting inconsistency was caught and
  fixed during enrichment (not left for a later reader to find): an early
  pass had Nadia's podcast-related grief framed as loss-by-death rather
  than the seed's specified `handled_off_page` item ("the podcast made
  about B's last relationship"); corrected in ch. 15 to keep the podcast's
  subject a breakup, consistent with ch. 17's established backstory. A
  second continuity check confirmed the sister character (Fiona) is
  distinguished consistently from the same-named broadcast-three caller
  throughout (ch. 9, ch. 12), per the seed's incidental name collision.
- **Foreshadowing check.** An early enrichment draft of a ch. 12 text
  message from Kirsty implied deliberate surveillance of the recording that
  leaks in ch. 19; rewritten before this pass began (see prior session
  notes) to remove any implication contradicting the established accidental
  mechanism (an unarchived test file, misfiled by Priya).

## Provenance

Every number in `artifacts_out_of_office/scene_ledger.json` is orchestrator
arithmetic from the supplied `main.py`, unmodified. `python3 main.py
--fixture` reproduces every §15 ledger value exactly, which is the Addendum M
proof instrument: the model's contribution is elicitation only, and no
arithmetic in this title was performed by a language model.
