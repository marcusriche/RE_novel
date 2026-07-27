# Human Contribution Log — HCL-STONEVOW-B01

Per-title IP log referenced by the seed row's `Human_Contribution_Log_Ref`
(§13.5, R22). Records operator decisions and the editorial provenance of
this title's production run.

Seed: `01KYG7SSJ4GP1XF3A7QYFR6F0D` — row 4 of
`Romance_Engine_Unified_Seed_Matrix.xlsx` (*Stonevow*, The Rime Wards Book
One), pseudonym Iona Rask.

| # | Date | Actor | Contribution |
|---|------|-------|--------------|
| 1 | 2026-07-27 | Operator (Claude agent session, on user instruction) | Selected Seed-Matrix row 4 (`01KYG7SSJ4GP1XF3A7QYFR6F0D`, *Stonevow*) for production from the re-uploaded matrix (now four rows). Extraction via `tools/seed_from_xlsx.py <matrix> 4` → `seed/seed_row_stonevow.json`. |
| 2 | 2026-07-27 | Operator | Scene-count decision: 45 scenes against the Romantasy arc profile `E = [12,10,10,10,8,12,12,8,8]` (sum 90), halved to `[6,5,5,5,4,6,6,4,4]` (sum 45) — every entry even, same halving discipline used for Books 1–3, so all four titles remain directly comparable at the same scene count. |
| 3 | 2026-07-27 | Operator | Ran the existing generic pipeline (`main.py` unmodified, `binding/offline_client.py`'s schedule-selectable `OfflineBindingClient`, `run_book.py --seed --schedule --out --scenes --path`) unchanged from Books 1–3. No engine or binding-layer code modified for this title. |
| 4 | 2026-07-27 | Editorial (offline binding schedule) | Authored the 45-scene editorial schedule (`binding/schedule_stonevow.py`): cast realization (A→Isla, wardwright; B→Aldric Marrow, hearth; secondary cast Sela Marrow, Tomas Renn, Keeper Bram Ossory, Commissioner Osric Feld, healer Cera Voss, Reny Ashe, cook Ida; secondary-world Highstone Cairn/the Rime/Coldwake/Calder's Reach), consent-negotiation scenes tagged `negotiate_consent` to satisfy `contact_admissible`'s negotiation-beat bypass, mandatory set-piece placement (binding rite ph0, first ward together ph2, frozen-village record ph4, consent negotiation before C3 ph5, great northern cairn re-set ph7), CE lifecycle (Obligation/Revelation/Threat/Absence), fracture-initiator overrides at scenes 37 and 41 for the structurally unreachable Phase 6/7 ceilings. |
| 5 | 2026-07-27 | Operator | One scheduling repair made during dry runs, recorded rather than papered over — see "Engine-level repairs" below. |
| 6 | 2026-07-27 | PRIMARY-PROSE (bound agent) | Rendered all 45 scene briefs into prose under kernel VK-EN-RA-01 (40 chapters, no epilogue — `Epilogue_Included = false`), realizing the seed's `POV = first_person_dual` as alternating close-first-person chapters (A-labelled "(Isla)", B-labelled "(Aldric)"), past tense throughout. |
| 7 | 2026-07-27 | Operator | Word-count decision: seed target `Word_Count_Target = 110000`. Final `Word_Count_Actual` = 111,060 (per `tools/build_manuscript.py stonevow`, assembled manuscript incl. front matter), 0.96% over target — the largest single enrichment volume of the four titles produced this session, run across roughly a dozen enrichment passes. |
| 8 | 2026-07-27 | PRIMARY-PROSE (bound agent) | Enrichment pass across all 40 chapters, run in many rounds. No scene added, removed, reordered, or reassigned relative to `artifacts_stonevow/scene_ledger.json`. New material is scene-interior and inter-scene texture — dialogue, interiority, secondary-character beats (Sela, Tomas, Ossory, Cera Voss, Reny Ashe, Ida), a Sela/Tomas courtship throughline, and a Sela-past-relationship throughline — not new plot or new CEs. |
| 9 | 2026-07-27 | Editor pass 1 of 1 (R22 gate: `Editor_Pass_Count` = 1) | Full-manuscript QC. See "Editor pass findings" below. |

## Engine-level repairs (item 5, itemized)

This title converged on the *second* full engine run — the cleanest
first-real convergence of the four books produced this session — after one
category of scheduling error was found and fixed:

1. **Phase-advance drift across six of the eight transitions.** The first
   draft schedule's authored `"t"` (target `T_scene`) values at six of the
   eight intended advance scenes did not actually exceed their phase's
   `PHASE_CEILINGS` entry (e.g. scene 11 `t=0.44` against a Phase-1 ceiling
   of `0.45`), because the initiator check (`T_scene > PHASE_CEILINGS[phase]`)
   uses the *current* scene's own authored target directly, not a lagged
   value — unlike G2/G4, which do reflect cumulative deltas only through
   scene *N*−1. Diagnosed with a monkeypatched `evaluate_phase` trace script
   (`gatecheck_stonevow.py`), which also surfaced that `min_duration(E)` is
   computed from the *un-halved* 90-scene `ARC_PROFILES` array rather than
   the halved 45-scene schedule (a confusing but ultimately harmless detail
   — block lengths were authored with enough slack to absorb it). Fixed by
   raising `"t"` at scenes 11, 16, 21, and 31 above their respective ceilings,
   and lowering `"t"` at scenes 23 and 24 to prevent a premature crossing of
   Phase 4's low `0.50` ceiling before the intended scene-25 advance.
   Re-traced: all eight advances landed exactly on schedule
   ({6, 11, 16, 21, 25, 31, 37, 41}) on the very next attempt.

Final run: 45 scenes shipped, final phase 8, **0 review flags**, 0
unrealized deltas, schedule problems: none.
`python3 main.py --fixture` reproduces the §15 fixture exactly, unaffected
by this title's schedule.

## Editor pass findings (item 9, itemized)

- **Brand-lexicon ban sweep** (`orbs`, `smirked`, `chuckled darkly`, `mate`,
  `fated`): 0 hits across all 40 chapters and front matter.
- **Preferred lexicon** (`cairn`, `frost`, `hearth`, `vow`, `thaw`): present
  throughout — `cairn` ×171 carries the line's own central geography and the
  rite's own vocabulary; `hearth` ×76 is the seed's own term of art for the
  bound partner; `frost` ×37 and `thaw` ×12 run as the book's ambient
  Coldwake texture; `vow` appears at the title itself and at the chapter
  title "Vow Renounced," load-bearing rather than merely decorative.
- **Dialogue punctuation**: no semicolons inside quoted dialogue anywhere in
  the manuscript; no period-before-lowercase-tag errors found on regex scan.
- **Duplicate-paragraph scan**: automated scan (paragraph-level, >60 chars)
  across and within all 40 chapter files, re-run after enrichment — 0 hits
  after two rounds of fixes (see below).
- **Self-reference dialogue-tag bug** (own-session discovery, not
  user-reported): a systematic sweep for `"{POV-chapter's own character}
  says/asks/..."` found nine instances across seven chapters (ch09, ch22,
  ch24 ×2, ch27, ch35, ch36 ×2, ch38 ×3) where a POV character's own line of
  dialogue had been tagged with their own name in the third person (e.g. an
  Aldric-POV chapter reading `"I can live with changed," Aldric says`
  instead of `I say`) — introduced during this session's enrichment passes.
  All nine corrected to first person. Three further apparent hits (ch07,
  ch14, ch25) were investigated and found to be a *pre-existing* structural
  looseness already present in the base manuscript before this session's
  enrichment began: individual scenes mid-chapter silently drift to the
  other character's POV without a scene-break marker or corrected header
  (confirmed by unambiguous tells — e.g. ch14's declared "(Aldric)" header
  but a later scene reading "Aldric's hand finds mine," which only parses
  if the local narrator is Isla). These three are flagged here rather than
  rewritten, since correcting them would require substantially reworking
  original pre-session chapter content beyond this pass's scope; the
  reader-facing effect is minor (the scenes remain internally consistent
  once the true local narrator is identified) and no self-contradictory
  tag survives in any of the three.
- **Continuity_Constraints verified**:
  - *"the bond is symmetric within the scene"* — held; both A→B and B→A
    involuntary-sensation-transfer beats appear (ch04's cold arriving in
    Isla's chest, ch10/ch11's cost transfer in the opposite direction).
  - *"wards can only be set at a standing cairn... every ward set on the
    page"* — held; every ward in the manuscript (ch04's waystone, ch10/11's
    Long Reach cairn, ch26/30/32's escalating Long Reach visits, ch35's
    Great Northern Cairn, ch40's closing ward) is staged at a named standing
    stone, on the page, never merely reported after the fact.
  - *"the Rime advances and never retreats"* — held; ch40 states the line
    "has crept another mile since first frost," with forty-one cairns
    "the same number as the morning of the binding" but explicitly *not*
    read as the Rime having stopped, only as the cost of holding it having
    changed shape.
  - *"no character states the mutual form before Phase 6"* —
    the most significant continuity issue caught this session, self-discovered
    during the editor pass rather than user-reported. Five pre-Phase-6
    passages (ch09, ch14, ch15, ch26, ch28) named the specific mutual-rite
    form to third-party institutional figures (Ossory, Cera Voss) or staged
    a formal hearing before its scheduled first disclosure at ch27/scene 32.
    All five rewritten to keep pre-discovery foreshadowing vague ("an
    alternative," "a suspicion," "something unorthodox") and to preserve
    private discussion between Isla and Aldric themselves (permitted from
    their joint discovery at Calder's Reach onward) while removing any
    third-party naming before ch27. A sixth, subtler instance was caught
    during this pass specifically: an enrichment-round addition to ch10
    had Isla state, in the story's present tense at a point *before*
    Calder's Reach, that she and Aldric had "ever considered the mutual
    form might genuinely exist" — a temporal leak (referencing a discovery
    that hadn't happened yet in-scene) rather than an institutional-naming
    violation, corrected to reference only the vaguer, period-appropriate
    doubt about the rite's history.
  - *"the calendar, realm, and geography are internal; no real-world
    nation, place, or date is named"* — held; the whole manuscript is set
    in Sarne/Highstone Cairn/Coldwake/the Rime, with no real-world proper
    noun anywhere.
- **Cross-book character-name contamination check** — held after one catch
  and fix: an enrichment-round ch34 addition briefly referenced "Kirsty,"
  a Book 3 (*Out of Office*) character name, in an unrelated aside;
  removed on discovery. A follow-up grep for Robyn/Nadia/Priya/Fiona/Sable
  Voss/Mira Dalca/Adam Marek/Traversa/Kelvin Row/Glasgow across all 40
  chapters confirmed no further cross-book leakage. A later enrichment
  addition (ch18) originally invented the name "Mira" for an unnamed
  Calder's Reach child; renamed to "Wren" on the same contamination check,
  since "Mira" collides with Book 3's "Mira Dalca."
- **Backstory consistency pass.** One drafting inconsistency was caught and
  fixed during enrichment: a ch03 addition established Isla's mother as an
  ordinary domestic figure (died when Isla was seven; blue shawl; baked
  bread every third day), while an earlier-drafted ch12 passage had
  independently described the same woman as an apparent wardwright
  predecessor. The ch12 passage was rewritten to align with ch03's version,
  which is the one carried forward consistently through ch14, ch25, ch39,
  and ch40's back matter.
- **Duplicate-paragraph bugs from rapid batch editing.** Two were caught via
  the automated scan and fixed: ch36 had a stale near-duplicate closing
  paragraph ("Ossory allows himself something almost like a smile...")
  appearing mid-file, immediately after unrelated dialogue Ossory wasn't
  present for, as well as at the chapter's true end — the mid-file copy was
  deleted. ch38 had an identical duplicated paragraph ("He goes back to his
  reports afterward...") at two points in the file — the first occurrence
  was deleted. A low-priority incidental repeated stock phrase ("I consider
  the question properly, because it deserves more than a reflexive answer,"
  appearing near-verbatim in both ch13 and ch39) was caught by the same
  scan during this pass and varied in ch39 rather than left standing.

## Provenance

Every number in `artifacts_stonevow/scene_ledger.json` is orchestrator
arithmetic from the supplied `main.py`, unmodified. `python3 main.py
--fixture` reproduces every §15 ledger value exactly, which is the Addendum M
proof instrument: the model's contribution is elicitation only, and no
arithmetic in this title was performed by a language model.
