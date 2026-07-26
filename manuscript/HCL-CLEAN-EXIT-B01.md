# Human Contribution Log — HCL-CLEAN-EXIT-B01

Per-title IP log referenced by the seed row's `Human_Contribution_Log_Ref`
(§13.5, R22). Records operator decisions and the editorial provenance of
this title's production run.

| # | Date | Actor | Contribution |
|---|------|-------|--------------|
| 1 | 2026-07-26 | Operator (Claude agent session, on user instruction) | Selected the sole populated Seed-Matrix row (`01KYDG7NWVMNN9C7DTKZ76F54Q`) for production. |
| 2 | 2026-07-26 | Operator | Scene-count override: 45 scenes (vs the 90-scene reference allocation), phase blocks scaled proportionally. Recorded as an operator decision under the `--scenes` discipline of `main.py`. |
| 3 | 2026-07-26 | Editorial (offline binding schedule) | Authored the 45-scene editorial schedule (`binding/schedule.py`): cast realization (A→Elena Moretti, B→Cole Brennan, C→Lucia Ferro, D→Nico Gravano), set-piece placement, CE lifecycle, consent-grant timeline, tension trajectory. |
| 4 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Rendered all 45 scene briefs into prose under kernel VK-EN-MD-01 (16 chapters + epilogue). First delivery: 20,344 words (abridged length). |
| 5 | 2026-07-26 | Operator | **Word-count decision revised.** The abridged rendering was expanded to the seed's `Word_Count_Target` of 80,000 at the operator's instruction. `Word_Count_Actual` = 80,185 (assembled manuscript incl. front matter). |
| 6 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Full-length rendering pass. All 45 engine scenes dramatized at scene length (mean ≈ 1,780 words/scene) rather than summarized; no scene added, removed, reordered, or reassigned relative to `artifacts/scene_ledger.json`. New material is scene interior (dialogue, blocking, interiority, subsidiary beats within the scheduled move), not new plot. |
| 7 | 2026-07-26 | Editor pass 1 of 1 (R22 gate: `Editor_Pass_Count` = 1) | Full-manuscript QC on the expanded text: brand-lexicon ban sweep (5 hits fixed across both passes: "suddenly" ×5); dialogue-punctuation rule check (no semicolons inside quoted dialogue — clean; narrative semicolons in action beats retained per kernel SYN); duplicate-line scan (clean); scene-sequence repair in ch. 11; seam repairs at 8 insertion points; continuity repairs (interview-to-mirror interval, passage-debt entry date, trial-counsel timeline, Sal's-lawyers date); two typographical fixes. |

## Constraints verified at the editor pass

Automated + read-through verification against `Continuity_Constraints` and the
§4.5 consent architecture:

- **A's brother in pretrial custody for the entire story clock** — held. Danny
  is taken before scene 1 and released on story day 31, the clock's final day
  (103 days in custody, stated consistently).
- **The ledger exists as a single physical original; any copy is an on-page
  event, never assumed** — held. The refusal to copy is stated explicitly on
  the record at the Ph7 proffer ("no copies exist — copying it was the one
  entry I always refused"). The only near-exception is a *decoding key* Elena
  writes in ch. 13, which is expressly not a copy of the ledger and is
  dramatized on the page as a distinct act.
- **B's task force operates under an active warrant from scene 1** — held
  (warrant noted active in ch. 1; the ch. 12 raid runs on a supplement).
- **A and D never meet without at least one witness until Phase 5** — held.
  Lucia, deputies, or family witnesses are present in every A/D scene through
  ch. 12; the first genuinely alone scene is ch. 14 (Phase 7), and the
  expiry of the constraint is dramatized in the text rather than merely
  observed.
- **Taboo list** — held. No on-page sexual coercion between the leads; all
  coercive pressure runs through D and the case. All intimacy is consent-gated
  per §4.5: C2 negotiated on-page (ch. 9) before the first kiss; C3/C4
  negotiated on-page (ch. 10) before first intimacy (ch. 11), with
  reaffirmation at the threshold; withdrawal (ch. 13) voids all standing
  grants at the moment the beat lands; intimacy resumes only after an explicit
  on-page re-grant with widened scope (ch. 15). `First_Kiss_Phase` = 5 and
  `First_Intimacy_Phase` = 6 are honored as scheduling priors *subordinate* to
  the grants, per §16.3.
- **L7 promise discipline** — held. CE-04's wording is quoted verbatim at
  origin (ch. 2) and at payoff (ch. 15); no paraphrase drift.
