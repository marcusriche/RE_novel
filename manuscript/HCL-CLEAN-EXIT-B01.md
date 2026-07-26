# Human Contribution Log — HCL-CLEAN-EXIT-B01

Per-title IP log referenced by the seed row's `Human_Contribution_Log_Ref`
(§13.5, R22). Records operator decisions and the editorial provenance of
this title's production run.

| # | Date | Actor | Contribution |
|---|------|-------|--------------|
| 1 | 2026-07-26 | Operator (Claude agent session, on user instruction) | Selected the sole populated Seed-Matrix row (`01KYDG7NWVMNN9C7DTKZ76F54Q`) for production. |
| 2 | 2026-07-26 | Operator | Scene-count override: 45 scenes (vs the 90-scene reference allocation), phase blocks scaled proportionally. Recorded as an operator decision under the `--scenes` discipline of `main.py`. |
| 3 | 2026-07-26 | Operator | Word-count decision: abridged-length rendering (~20,300 words assembled) against the seed's 80,000-word target — an operator constraint of the offline production environment, logged here rather than silently mixed into the seed (derived/authored separation, §16.0). `Word_Count_Actual` = 20,344 (assembled manuscript, incl. front matter). |
| 4 | 2026-07-26 | Editorial (offline binding schedule) | Authored the 45-scene editorial schedule (`binding/schedule.py`): cast realization (A→Elena Moretti, B→Cole Brennan, C→Lucia Ferro, D→Nico Gravano), set-piece placement, CE lifecycle, consent-grant timeline, tension trajectory. |
| 5 | 2026-07-26 | PRIMARY-PROSE (bound agent) | Rendered all 45 scene briefs into prose under kernel VK-EN-MD-01 (16 chapters + epilogue). |
| 6 | 2026-07-26 | Editor pass 1 of 1 (R22 gate: `Editor_Pass_Count` = 1) | Full-manuscript QC: brand-lexicon ban sweep (1 hit fixed: "suddenly", ch. 9), dialogue-punctuation rule check (no semicolons in dialogue: clean), continuity repairs (interview-to-mirror interval, passage-debt entry date, trial-counsel timeline), one typographical fix. |

Constraints verified at the editor pass:

- A's brother in pretrial custody for the entire story clock (released
  story day 31, the clock's final day) — held.
- The ledger exists as a single physical original; the only transfer of
  custody happens on the page (Ch. 14 proffer, inventoried as Government
  Exhibit 1); no copy is ever made, and the refusal to copy is stated on
  the record — held.
- B's task force operates under an active warrant from scene 1 — held
  (warrant noted active in Ch. 1).
- A and D never meet without at least one witness until Phase 5 — held
  (Lucia/deputies through Ch. 8; first witnessed-only-by-family scenes at
  the Ph5 dinner; first true alone scene is Ch. 14, Phase 7).
- Taboo list: no on-page sexual coercion between leads; all intimacy
  consent-gated per §4.5 (grants negotiated on-page in Ch. 9/10 before any
  covered contact; withdrawal in Ch. 13 honored; re-grant in Ch. 15 before
  any further contact) — held.
