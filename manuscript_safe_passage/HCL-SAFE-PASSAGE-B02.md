# Human Contribution Log — HCL-SAFE-PASSAGE-B02

Per-title IP log referenced by the seed row's `Human_Contribution_Log_Ref`
(§13.5, R22). Records operator decisions and the editorial provenance of
this title's production run.

Seed: `01KYF6MB0CBHSYJG5CC2TKW0WD` — row 3 of
`Romance_Engine_Unified_Seed_Matrix.xlsx`.

| # | Date | Actor | Contribution |
|---|------|-------|--------------|
| 1 | 2026-07-26 | Operator (Claude agent session, on user instruction) | Selected Seed-Matrix row 3 (`01KYF6MB0CBHSYJG5CC2TKW0WD`, *Safe Passage*) for production from the re-uploaded matrix. Extraction via `tools/seed_from_xlsx.py <matrix> 2` → `seed/seed_row_safe_passage.json`. |
| 2 | 2026-07-26 | Operator | Scene-count override: 45 scenes against the Mafia/Dark arc profile `E = [6,8,10,10,10,12,12,10,12]`, scaled proportionally to phase blocks `3/4/5/5/5/6/6/5/6`. Same `--scenes` discipline used for Book 1, so the two titles are directly comparable. |
| 3 | 2026-07-26 | Operator | Generalized `binding/offline_client.py` to take a `schedule` module argument, and `run_book.py` to take `--seed/--schedule/--out/--scenes/--path`, so both titles run through one orchestrator and one binding. Book 1 re-verified byte-identical after the refactor. |
| 4 | 2026-07-26 | Editorial (offline binding schedule) | Authored the 45-scene editorial schedule (`binding/schedule_safe_passage.py`): cast realization (A→Mira Dalca, B→Adam Marek, C→Benny Osei, D→Gino Traversa), set-piece placement, CE lifecycle, consent-grant timeline, tension trajectory, phase-advance and fracture points. |
| 5 | 2026-07-26 | Operator | Four scheduling repairs made during dry runs, each recorded rather than papered over — see "Engine-level repairs" below. |
| 6 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Rendered all 45 scene briefs into prose under kernel VK-EN-MD-01 (17 chapters + epilogue). |
| 7 | 2026-07-26 | Operator | Word-count decision: the seed's band is 70,000–90,000. Target set at ~75,000; `Word_Count_Actual` = 71,217 (assembled manuscript incl. front matter), inside band. |
| 8 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Enrichment pass across chapters 1–17 and epilogue. No scene added, removed, reordered, or reassigned relative to `artifacts_safe_passage/scene_ledger.json`. New material is scene interior — dialogue, blocking, interiority, subsidiary beats inside the scheduled move — not new plot. |
| 9 | 2026-07-26 | Editor pass 1 of 1 (R22 gate: `Editor_Pass_Count` = 1) | Full-manuscript QC. See "Editor pass findings" below. |

## Engine-level repairs (item 5, itemized)

These are recorded because each one is a place where the schedule, not the
engine, was wrong — and the engine's refusal to advance is the evidence.

1. **Inadmissible contact.** The first C2 kiss was scheduled at scene 22 with
   the covering grant at scene 25; `main.py` correctly raised
   `plan verification: inadmissible contact (no covering grant)`, because
   grants only realize at extraction after a scene ships. Fixed by moving the
   C2 ask and the mutual grants into scene 21 — which is also where the
   drama wants them, since scene 21 is where the funded exit is offered and
   refused, and that refusal is what makes contact admissible at all.
2. **Scene 3 failed G4.** No band crossing had accumulated by the time the
   gate was evaluated. Fixed by moving the crossing delta (B→A fear +0.15,
   0.45 → 0.60, crossing B2→B3) from scene 3 into scene 2, since the gate at
   step 5 sees only cumulative deltas through scene N−1.
3. **Phase 4 advanced one scene early**, which would have pushed the first
   kiss into Phase 5 and violated `First_Kiss_Phase = 4`. Cause: Ph4's
   ceiling is the deliberate false-resolution dip (0.50) and the layover
   scenes were running above it. Fixed by lowering scenes 18–21 to
   0.42/0.44/0.46/0.48 — plot pressure stays in the CER and `T_causal`, the
   *pair* charge dips, which is what Phase 4 means.
4. **B→A register ended "yearning"** — warm but not safe, because his fear
   never decayed. Added fear/resentment decay at scenes 38/40/43/44. Both
   directions now end "tender."

Final run: 45 scenes, 0 flags.

## Editor pass findings (item 9, itemized)

- **Brand-lexicon ban sweep** (`orbs`, `smirked`, `chuckled darkly`,
  `little one`, `suddenly`): 0 hits.
- **Preferred lexicon** (`manifest`, `diesel`, `water`, `iron`, `cold`):
  present throughout; `manifest` ×42 carries the title's central pun (the
  document, and what a life amounts to).
- **Dialogue punctuation**: no semicolons inside quoted dialogue. Narrative
  semicolons in action beats retained per kernel SYN.
- **Duplicate-paragraph scan**: 1 hit (a doubled exchange in ch. 16 left by
  an insertion), removed.
- **Story-clock reconciliation.** The draft had drifted: Adam's testimony
  date was written as the 22nd in chapters 1/9/12 while the ledger fixes it
  at story day 19, and Adam's abduction was dated 9 May against a story day 1
  that had to be 1 May. Reconciled across the whole manuscript to a single
  scheme — story day *N* = *N* May 2026; delivery on the 17th (a Sunday, as
  the text says); testimony and licence hearing both on the 19th. Traversa's
  "seventeenth, eighteenth, nineteenth, all in a row like that" now lands on
  three real dates.
- **The eleven-names ledger reconciled.** Entries were quoted in three
  chapters with dates that did not sort. Rebuilt as one chronological list
  (Aug 2019 → Oct 2025), with #7 kept at position seven so ch. 4's "number
  seven was the one that cost" holds, and #9 kept as the Kharkiv
  mother-and-daughter so the epilogue's photograph is the right person at
  the right age.
- **Adam's age reconciled.** "Eleven years driving" ending Nov 2019, started
  at 23, made him 41 in 2026, not 34 as three chapters had it. Corrected
  everywhere except his own line about who he was *in 2019*, where 34 is
  correct.
- **Wisniewski backstory reconciled.** An enrichment insert had invented a
  Ted Wisniewski who died in 1998; ch. 1 establishes him as the man who sold
  Mira the yard in 2015 and died the following spring. Rewritten so the 1961
  sign belongs to his father Tadeusz — which preserves the intended beat
  (a name over a gate belonging to a man who owed nobody anything) without
  contradicting ch. 1.
- **POV.** Scene 39's ledger POV is B; the breakwater withdrawal was drafted
  in A's interiority and was recast into Adam's.
- **Geography.** One northbound waypoint (Rogers City, which is past Alpena)
  corrected to Harrisville.

## Constraints verified at the editor pass

Automated + read-through verification against `Continuity_Constraints` and
the §4.5 consent architecture:

- **A and D are never in the same room until Phase 6** — held, and load-bearing.
  Traversa speaks to Mira through a lowered car window in ch. 1, by telephone
  in ch. 4 and ch. 11, and through his men in ch. 6. The first room they ever
  share is the scale house at the border yard in ch. 13 (scene 34, Phase 6),
  and the text makes the expiry of the constraint *the tell*: he never comes
  inside, because inside is where you are seen and remembered — so his being
  inside means that after tonight it will not matter who remembers.
- **B's federal testimony date is fixed at story day 19 and never moves** —
  held, after the clock reconciliation above. Every actor who touches the
  date (Adam, Traversa, Raman, the marshals) treats it as immovable, and it
  is the last thing standing when everything else in the plan has failed.
- **The route is physical and continuous; no scene relocates the pair without
  an on-page leg** — held. Chicago → Portage → the dunes → Portage → the
  shore → Muskegon → the sand-and-gravel cut → across the mitten → Bay City
  → Standish → Tawas → Au Gres → Alpena → Lakeport → Port Sanilac →
  Lexington → Port Huron, with the fuel, the mileage and the reason for every
  deviation on the page.
- **The eleven are never named in any document** — held, in the world and in
  the book. Raman asks for them twice and is refused twice, on the record;
  the list is read aloud once, between two people in an empty shed, and
  burned. This is the one place where the growth arc and the plot are the
  same object.
- **Taboo list** — held. No on-page sexual coercion between the leads; all
  coercive pressure runs through D and through the instrument of Benny's
  licence. All intimacy is consent-gated per §4.5:
  - the custody imbalance is **named on the page** (ch. 8, scene 19) and
    converted into a standing boundary in both registers;
  - the exit is made **real, funded and refused** (ch. 9, scene 21) before
    any grant exists — four thousand two hundred dollars, a name that will
    hold three years, an unlisted crossing, and a person at the far end;
  - only then is a mutual C2 grant negotiated, in terms, by the party with
    the power, asking;
  - first kiss (ch. 9, scene 22) is **her move, her timing**, with a real
    exit standing open behind him;
  - C3/C4 grants are negotiated on the page (ch. 11, scene 25) with a stop
    word that either party may use without owing a reason;
  - **withdrawal** (ch. 15, scene 39) voids all standing grants at the moment
    the beat lands, and is performed by the party who was in custody, for the
    clause that was actually broken;
  - intimacy resumes only after an explicit on-page **re-grant at his
    initiative, with widened scope** (ch. 17, scene 43), given from outside
    the gate by a man who arrived on foot.
  `First_Kiss_Phase = 4` and `First_Intimacy_Phase = 5` are honored as
  scheduling priors *subordinate* to the grants, per §16.3.
- **L7 promise discipline** — held. CE-04's wording is quoted verbatim at
  origin (ch. 2, scene 5, the Portage scale house) and at payoff (ch. 16,
  scene 40, the witness box), with no paraphrase drift. Chapter 17 quotes the
  first clause once more, deliberately, as *grammar* rather than as promise —
  the point being that Mira offers a job in the same register she once
  offered a life.

## Provenance

Every number in `artifacts_safe_passage/scene_ledger.json` is orchestrator
arithmetic from the supplied `main.py`, unmodified. `python3 main.py
--fixture` reproduces every §15 ledger value exactly, which is the Addendum M
proof instrument: the model's contribution is elicitation only, and no
arithmetic in this title was performed by a language model.
