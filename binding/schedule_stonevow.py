"""Authored scene schedule for Seed 01KYG7SSJ4GP1XF3A7QYFR6F0D — "Stonevow".

Editorial layer of the offline binding configuration `offline-agent-v1`
(see binding/offline_client.py). 45 scenes over the Romantasy reference
allocation E = [12,10,10,10,8,12,12,8,8] (sum 90), halved to
[6,5,5,5,4,6,6,4,4] (sum 45) — the same scene-count discipline used for
Books 1-3 (all entries even, so the halving stays exact).

Cast (engine node ids are the seed's own names A/B/C/E and the literal
Antagonistic_Force name):
  A = Isla Vane, 31          - wardwright of the northern line; sole
                                practitioner since her mentor's death
  B = Aldric Marrow, 28      - orchard-keeper and grafter; bought his
                                sister's exemption with his own binding
  C = Tomas Renn, 19         - A's apprentice; next in line if B fails
  E = Sela Marrow            - B's sister; keeper of the grain record
  "the Rime"                 - the advancing cold (Antagonistic_Force; a
                                condition, not a person — it has no
                                intent and cannot be bargained with).
                                Institutional pressure (the rite-keepers,
                                the crown's ward-commissioner, Feld) is
                                dramatized through this node, exactly as
                                Book 3 routed the funding panel through
                                "the funding review".

POV: first_person_dual, past tense. The schedule's "pov" field alternates
"A"/"B" by chapter (not strictly every scene) — Isla narrates roughly
55% of the book, Aldric the rest, per the seed's dual-POV field. Neither
narrates the other's interiority directly; each infers the other only
through what the bond itself makes involuntarily legible.

Story clock: 88 days, anchored at first frost of Coldwake (Ward-Year 214,
internal calendar only — no real-world nation, place, or date is named
per Continuity_Constraints). The Rime's advance is tracked narratively
and never reverses.

CE lifecycle (per Initial_CER_Seed):
  CE-01 Obligation   Aldric's binding-debt (he bought Sela's exemption
                      with his own binding). Misfires scene 38 (the
                      solo-sacrifice attempt — the corrupted, one-sided
                      form of payment); closes scene 41 (the rite
                      rewritten, the debt discharged mutually).
  CE-02 Revelation    The rite's true, corrupted-from-mutual nature.
                      Discovered (not yet spoken) at Calder's Reach,
                      scene 23; CLOSES scene 32 — the first scene in
                      which either of them says it aloud, honoring the
                      constraint that no one states the mutual form
                      before Phase 6.
  CE-03 Threat        The bond is killing Aldric faster than the records
                      allow for (his numbing hand). Closes scene 41,
                      discharged by the same rewritten rite as CE-01.
  CE-04 Absence       Isla's unprocessed grief for her mentor, Ossian
                      Thale. Closes scene 24, at Calder's Reach, per the
                      seed's deadline (phase 4).

Consent architecture (§4.5): the rite's forced hand-binding (scene 1) is
never treated as a consent grant of any kind — it is C0 ritual necessity,
not permission, and the taboo clause ("the bond used as a substitute for
consent between the leads") is honored by requiring every escalation
past that to be separately, verbally negotiated with both leads unbound
in the moment. C2 (the first kiss) is negotiated scene 16, performed
scene 17 (First_Kiss_Phase 3). The mandatory consent negotiation before
first C3 contact lands scene 28 (Phase 5), granting C3/C4 private
contact realized at scene 30 (First_Intimacy_Phase 5). Aldric withdraws
his own standing grants at scene 38 (the vow renounced, to protect her);
both re-grant, chosen and mutual, at the climax, scene 40.
"""

PHASE_BLOCKS = {
    0: (1, 6), 1: (7, 11), 2: (12, 16), 3: (17, 21), 4: (22, 25),
    5: (26, 31), 6: (32, 37), 7: (38, 41), 8: (42, 45),
}
ADVANCE_SCENES = {6, 11, 16, 21, 25, 31, 37, 41}
FRACTURE_SCENES = {37, 41}   # ceilings 1.00 (Ph6) and 0.80 (Ph7): structurally
                             # unreachable naturally; caller-side override per
                             # run_book.py's install_fracture_initiator

DISPLAY = {"A": "Isla Vane", "B": "Aldric Marrow", "C": "Tomas Renn",
           "E": "Sela Marrow", "the Rime": "the Rime"}


def S(n, title, pov, day, loc, fam, actor, target, motif, shape, idelta,
      ces, deltas, t, hot=None, contact=None, consent=None, grants=None,
      close=None, misfire=None, withdraw=None, beats=None, syn=""):
    return dict(scene=n, title=title, pov=pov, day=day, loc=loc, family=fam,
                actor=actor, target=target, motif=motif, shape=shape,
                idelta=idelta, ces=ces, deltas=deltas, t=t, hot=hot or {},
                contact=contact, consent=consent, grants=grants or [],
                close=close or [], misfire=misfire or [],
                withdraw=withdraw or [], beats=beats or [], syn=syn)


SCENES = [
# ---------------------------------------------------------------- Phase 0
S(1, "The Assembly", "A", 1, "Highstone Cairn, the rite-hall, first frost of Coldwake",
  "demand_threaten", "the Rime", "A", "a name read aloud at the binding",
  "rite-begins",
  "the mandatory inciting incident: the rite pairs A and B before the assembly",
  [],
  [("A", "the Rime", "fear", 0.10), ("A", "the Rime", "resentment", 0.05),
   ("A", "B", "resentment", 0.04), ("B", "A", "respect", 0.03)],
  0.32,
  beats=["Isla stands before the assembly at Highstone Cairn in the coat "
         "she wears to every binding, the one that still smells faintly of "
         "the last one, and does not let her face do anything at all",
         "Keeper Bram Ossory reads the rite in the old cadence — a "
         "wardwright to shape the stone, a hearth to feed it, a name read "
         "aloud so the village knows whose funeral to expect",
         "The name he reads is Aldric Marrow's. Isla has never spoken to "
         "him. She has seen him twice, at market, buying grafting wax",
         "He steps forward before the Keeper finishes speaking — not "
         "dragged, not chosen for him. Volunteered. Isla understands, "
         "watching his face, that he decided this before he ever knew "
         "who the wardwright would be",
         "Their hands are bound at the wrist with the rite-cord, and Isla "
         "feels something that is not quite touch and not quite anything "
         "she has a word for arrive in her chest and stay there"],
  syn="Mandatory inciting incident: the rite pairs Isla and Aldric before "
      "the assembly, and neither of them chose the other, exactly."),
S(2, "Cairns and Debts", "A", 1, "Highstone Cairn, the record-room",
  "deflect_withhold", "A", "C", "forty miles of standing stone", "aftermath",
  "the stakes made physical; the caretaker flaw stated as competence",
  [],
  [("A", "C", "trust", 0.05), ("A", "C", "respect", 0.04)],
  0.28,
  beats=["Down into the record-room, where the ledger of every cairn on "
         "the northern line hangs on the wall in a dead man's handwriting "
         "Isla has never once had copied over into her own",
         "Tomas Renn, nineteen, apprentice wardwright, already has the "
         "kettle on and the day's reports sorted by urgency, the way he "
         "always does, whether or not anyone asks him to",
         "'They bound you to the orchard-keeper,' Tomas says, careful, "
         "watching her face for the shape of how she feels about it",
         "'They bound me to a name and a hearth,' Isla says. 'The rest is "
         "paperwork.' She does not believe this even as she says it",
         "Forty-one cairns standing, forty miles of line, one wardwright. "
         "Isla has kept that arithmetic since she was twenty-six and it "
         "has never once come out even"],
  syn="Establish Isla's world: the cairns, Tomas, and the exact size of "
      "the thing she has been quietly carrying alone."),
S(3, "A Stranger's Weight", "A", 2, "the road below Highstone, midday",
  "probe_test", "A", "B", "grafting wax and an unfamiliar name", "first-real-meeting",
  "she takes his measure the only way she knows how: coldly, for facts",
  [],
  [("A", "B", "respect", 0.03), ("B", "A", "respect", 0.03),
   ("A", "B", "fear", -0.02)],
  0.30,
  beats=["Aldric finds her on the road rather than waiting to be sent for, "
         "which is already not what Isla expected from a man who "
         "volunteered to be spent",
         "He is broad and sun-marked despite the season, grafting scars "
         "across both thumbs, and he does not flinch from her the way "
         "most people do once they know what her hands are for",
         "'I know what I did,' he says, before she can ask. 'I'd rather "
         "you hear it from me than from the ledger'",
         "He tells her about Sela — the exemption, the trade, plainly, "
         "without asking for anything back for the telling",
         "Isla runs the same cold list she runs on everyone: what he can "
         "be trusted with, what he'll cost her, whether she can afford to "
         "let this be a person rather than an office. She does not reach "
         "an answer"],
  syn="The wary first real conversation: two strangers bound by a rite "
      "neither of them chose the shape of."),
S(4, "Ground Rules", "A", 2, "the wardwright's cottage, evening",
  "bargain_trade", "A", "B", "terms for a life neither of them asked for",
  "boundary-setting",
  "practical terms negotiated for how the bound pair will actually live",
  [],
  [("A", "B", "trust", 0.04), ("B", "A", "trust", 0.05),
   ("A", "B", "commitment", 0.03)],
  0.34,
  beats=["Aldric comes to the cottage because the rite requires proximity "
         "and neither of them has anywhere else the binding will hold "
         "properly",
         "Isla lays out terms the way she lays out a ledger: separate "
         "rooms, separate meals unless the rite calls them together, no "
         "pretending at anything the rite hasn't actually made true",
         "'I'm not asking you to want this,' Aldric says. 'I'm asking "
         "you to let me be useful in it, since I'm going to be here "
         "either way'",
         "She agrees to the terms. She notices, writing them down, that "
         "she has drawn up rules for a stranger with more care than she's "
         "drawn up anything for herself in six years"],
  syn="Two people who did not choose each other negotiate the practical "
      "shape of a life the rite has already decided for them."),
S(5, "Someone Else's Warmth", "A", 3, "the wardwright's cottage, before dawn",
  "bargain_trade", "B", "A", "a mended glove, left without comment", "quiet-care",
  "his acts-of-service love language meets her guarded exhaustion",
  [],
  [("B", "A", "affection", 0.06), ("A", "B", "trust", 0.08),
   ("A", "B", "fear", -0.07), ("B", "A", "respect", 0.04)],
  0.36,
  beats=["Isla's glove has been split at the seam for a fortnight; she "
         "has not mentioned it, because mentioning small cold things is "
         "not a habit she's ever let herself keep",
         "She finds it on the cottage step before dawn, stitched, warm "
         "from the fire it was mended beside, with no note and no comment "
         "waiting to be thanked for",
         "Aldric is already at the woodpile when she comes out, not "
         "looking at her, giving the moment nowhere to become a scene",
         "'You didn't have to,' Isla says. 'I know,' he says, and keeps "
         "splitting wood, and it is the first sentence anyone has said "
         "to her in years that asks for nothing back at all",
         "She goes back inside and sits with the mended glove in both "
         "hands for longer than the moment strictly requires"],
  syn="The first evidence of who Aldric actually is, offered quietly, "
      "at his own cost, asking nothing in return."),
S(6, "First Frost, First Crack", "A", 3, "the northern line, the nearest standing cairn",
  "reveal_misfire", "B", "A", "a flicker that isn't hers", "bond-first-speaks",
  "the bond does something involuntary for the first time",
  [],
  [("B", "A", "vulnerability", 0.10), ("A", "B", "trust", 0.12),
   ("A", "B", "fear", -0.08), ("B", "A", "affection", 0.06)],
  0.40,
  beats=["A routine inspection of the nearest cairn, Aldric come along "
         "because the rite pulls at him when she's too far from the "
         "line, an ache he describes badly and doesn't complain about",
         "Isla lays a hand on the standing stone to read its charge, and "
         "for one unguarded second she feels — not sees, not hears — the "
         "specific cold ache in Aldric's left hand, arriving in her own "
         "chest like a borrowed weather",
         "'You felt that,' Aldric says. Not a question. He's gone very "
         "still",
         "'I felt something,' Isla says, which is the closest to honest "
         "she's been with anyone in six years",
         "Neither of them names it. But something between them has "
         "shifted from arrangement into fact, the way weather shifts "
         "from forecast into rain"],
  syn="Advance scene: the bond speaks for the first time, involuntarily, "
      "and neither of them can pretend afterward that it's only paperwork."),
# ---------------------------------------------------------------- Phase 1
S(7, "The Ward-Commissioner's Ledger", "A", 5, "Highstone Cairn, the council room",
  "demand_threaten", "the Rime", "A", "a column of numbers called abandonment",
  "institutional-pressure",
  "the crown's ward-commissioner costs out the failure of the northern line",
  [],
  [("A", "the Rime", "fear", 0.06), ("A", "the Rime", "resentment", 0.05),
   ("A", "C", "trust", 0.03)],
  0.30,
  beats=["Commissioner Osric Feld visits with a ledger of his own, one "
         "that prices the northern line's abandonment in a column headed "
         "PROJECTED SAVINGS, and does not once ask how many cairns are "
         "actually standing",
         "'One practitioner and an apprentice for forty miles,' Feld says, "
         "in the tone of a man reciting a fact rather than a failure. "
         "'The crown will want this winter's numbers on the record'",
         "Isla says nothing that isn't strictly true and gives him "
         "nothing he can use, a skill she has been practicing since long "
         "before Feld had a title",
         "Tomas, listening from the doorway, goes very quiet in the "
         "specific way of a nineteen-year-old doing arithmetic about his "
         "own future",
         "Feld leaves a copy of the ledger behind, which Isla reads twice "
         "and burns once"],
  syn="Establish the institutional clock running alongside the Rime's "
      "own: two different kinds of cold, both advancing."),
S(8, "Thaw a Stranger's Byre", "B", 6, "the Hollow Farm, three miles off the line",
  "release_transform", "A", "B", "a byre thawed at her own unlogged cost",
  "quiet-heroism",
  "SAVE THE CAT: Isla thaws a stranger's byre at her own cost and tells no one",
  [],
  [("B", "A", "respect", 0.09), ("B", "A", "attraction_romantic", 0.05),
   ("A", "B", "trust", 0.04)],
  0.38,
  beats=["A farmer three miles off the line sends no formal request, only "
         "a boy running barefoot to say the byre's frozen solid and the "
         "stock won't survive the night",
         "It isn't a cairn. It isn't Isla's charge to spend anything on "
         "it. She goes anyway, and lays both hands on the byre wall, and "
         "gives it warmth that isn't the rite's to give and doesn't write "
         "the cost down anywhere",
         "Aldric follows without being asked and sees the whole of it — "
         "sees her go grey at the mouth afterward, sees her wave off the "
         "farmer's thanks like it's an accusation",
         "'You didn't log that,' Aldric says, on the walk back. 'It "
         "wasn't a ward,' Isla says. 'It doesn't go in the ledger.' He "
         "does not believe this is the whole reason and does not say so",
         "He watches her the rest of the walk with the specific attention "
         "of a man recognizing, in someone else, a shape he knows from "
         "the inside"],
  syn="Isla's defining act of quiet, uncounted self-spending — and the "
      "first time Aldric sees the exact flaw he shares with her, worn on "
      "someone else's face."),
S(9, "Touch-Starved", "A", 8, "the northern track, a frost-slick rise",
  "probe_test", "B", "A", "a hand caught before a fall", "incidental-contact",
  "an ordinary touch lands harder than either of them means it to",
  [],
  [("B", "A", "attraction_sexual", 0.06), ("A", "B", "attraction_sexual", 0.05),
   ("A", "B", "vulnerability", 0.05), ("B", "A", "trust", 0.05)],
  0.42,
  beats=["The track is bad after three days of new snow, and Isla goes "
         "down hard on a frost-slicked rise before Aldric's hand closes "
         "on her arm and simply — holds",
         "It is the ordinary kind of touch, the kind that means nothing "
         "between people who've known each other longer than a season, "
         "and it does not behave like an ordinary touch at all",
         "Neither of them lets go for a half-second longer than balance "
         "requires. Neither of them mentions it",
         "'You're colder than you should be,' Aldric says, meaning her "
         "hand, which he is still, technically, holding",
         "'I run cold on purpose,' Isla says, which isn't an answer, and "
         "he lets her have the non-answer, and they walk the rest of the "
         "rise not quite touching, on purpose, which does more work than "
         "touching would have"],
  syn="Touch-starved trope, armed: an incidental hand lasts one beat "
      "longer than incident requires, and both of them notice."),
S(10, "What the Ledger Doesn't Say", "B", 10, "the Marrow orchard, above the line",
  "deflect_withhold", "A", "E", "a grain-record that doesn't balance", "found-family-seed",
  "Sela Marrow, and what her exemption actually cost this family",
  [],
  [("A", "E", "trust", 0.05), ("A", "E", "respect", 0.04),
   ("B", "A", "affection", 0.05)],
  0.36,
  beats=["Aldric brings Isla up to the last orchard above the line for "
         "the first time, ostensibly to inspect a cairn nobody's checked "
         "since the snow, actually because he wants her to see where he's "
         "from before the rite decides that for her instead",
         "Sela Marrow, twenty-four, keeper of the grain record, looks at "
         "Isla the way a sister looks at the woman her brother's been "
         "bound to for someone else's sake — carefully, and not unkindly",
         "Sela shows Isla the record without being asked: what the "
         "exemption actually cost the household, in grain and in the "
         "specific silence that fell over the orchard the week Aldric put "
         "his own name forward instead of hers",
         "'He never told me the rest of it,' Sela says, meaning the "
         "binding, meaning the wardwright, meaning whatever this is now. "
         "'He never tells anyone the rest of anything'",
         "Isla files that sentence away with the rest of what she's "
         "learning about a man she did not choose and is starting to "
         "understand rather better than she planned to"],
  syn="Found family, armed early: Sela's ledger, and the first outside "
      "confirmation of Aldric's habit of paying quietly and alone."),
S(11, "Held Ground", "B", 14, "the wardwright's cottage, late",
  "release_transform", "A", "B", "a companionship neither will name yet", "advance",
  "wary distance settles, unnamed, into something neither of them corrects",
  [],
  [("A", "B", "trust", 0.10), ("B", "A", "trust", 0.09),
   ("A", "B", "respect", 0.08), ("B", "A", "affection", 0.07),
   ("A", "B", "resentment", -0.06)],
  0.50,
  beats=["A fortnight in, the cottage has quietly rearranged itself "
         "around two people instead of one — a second chair pulled to "
         "the fire, a mug that's become, without discussion, his",
         "They don't call it anything. Isla notices herself not calling "
         "it anything with the specific deliberateness of someone "
         "protecting a fact by refusing to name it",
         "'You've stopped flinching when I come in,' Aldric says, mild, "
         "not making a thing of it",
         "'I've stopped expecting you to cost me something every time "
         "you do,' Isla says, and hears, saying it, how much she's just "
         "admitted",
         "Neither corrects the sentence. The fire holds the room's whole "
         "attention for a while after that, which is its own kind of "
         "agreement"],
  syn="Advance scene: the wariness that opened the book has become "
      "ground held rather than ground defended, and neither will say so "
      "first."),
# ---------------------------------------------------------------- Phase 2
S(12, "Stone and Breath", "A", 15, "Highstone Cairn, the workshop",
  "probe_test", "A", "C", "a first joint ward, and the nerves before it",
  "pre-ritual",
  "logistics and nerves ahead of the first ward set together",
  [],
  [("A", "C", "trust", 0.04), ("A", "B", "vulnerability", 0.05)],
  0.44,
  beats=["Every ward Isla has ever set, she has set alone; the rite that "
         "bound her to Aldric requires, for the first time in her career, "
         "that she set one with a hearth actually present at the stone",
         "Tomas checks the cairn maps twice and asks, careful, whether "
         "he should come along in case something goes wrong, which is "
         "his way of saying he's frightened for her",
         "'Nothing's going to go wrong,' Isla says, in the tone she uses "
         "for things she hasn't finished believing yet",
         "She finds Aldric at the door already dressed for the cold, "
         "having assumed, correctly, that today was the day, without "
         "being told"],
  syn="The nerves before the mandatory set piece: the first ward either "
      "of them will ever set with the other actually standing at the "
      "stone."),
S(13, "What the Stone Takes", "A", 17, "the Long Reach cairn, on the northern line",
  "release_transform", "B", "A", "the first ward set together", "set-piece",
  "SET PIECE (mandatory, Ph2): A feels, through the bond, exactly what "
  "the stone takes out of B",
  [],
  [("B", "A", "vulnerability", 0.13), ("A", "B", "trust", 0.13),
   ("A", "B", "emotional_safety", -0.09), ("B", "A", "affection", 0.08)],
  0.56,
  beats=["SET PIECE (Ph2): Isla lays both hands on the Long Reach cairn "
         "and calls the ward the way she's called forty others, except "
         "this time there is a hearth actually feeding it, actually "
         "standing at the stone",
         "The cost leaves Aldric in a way Isla has only ever read about "
         "in older wardwrights' journals — heat drawn out through his "
         "palms into the standing stone — and the bond, unbidden, hands "
         "her the whole of what that costs him, not as knowledge but as "
         "sensation",
         "She has spent forty miles of cairns believing, professionally, "
         "in the price of the rite. She has never once, until this exact "
         "moment, felt it happen to a person she can see the face of",
         "Aldric goes white to the lips and does not make a sound. Isla "
         "very nearly breaks the ward mid-cast to stop it, and does not, "
         "because stopping mid-cast would cost him worse",
         "When it's done he sits down hard in the snow and says, "
         "'Now you know,' like a confession rather than a fact"],
  syn="Mandatory set piece: the bond stops being theory the moment Isla "
      "feels, in her own chest, exactly what the stone is taking out of "
      "the man standing beside her."),
S(14, "Aftermath, Underlit", "B", 17, "a shepherd's shelter below the Long Reach cairn",
  "reveal_misfire", "B", "A", "the cost admitted, once, plainly", "processing",
  "he admits, for the first time, that the cost is real and constant",
  [],
  [("B", "A", "vulnerability", 0.10), ("A", "B", "affection", 0.08),
   ("A", "B", "commitment", 0.05)],
  0.50,
  beats=["They shelter below the cairn until Aldric can stand without the "
         "ground doing something unreliable underneath him, Isla's coat "
         "over his shoulders because it is, absurdly, the warmer of the "
         "two",
         "'It's always like that,' Aldric admits, finally, into the "
         "quiet. 'Not always that bad. But always something. I didn't "
         "want you to know how much, because knowing wouldn't have "
         "changed the numbers'",
         "'It changes what I'm willing to ask of you,' Isla says, and "
         "means it in a way that surprises her more than it surprises "
         "him",
         "He doesn't argue with that. He just leans, slightly, into the "
         "coat and the cold and the fact of her sitting close enough to "
         "share both",
         "Neither says the word that's sitting in the shelter with them. "
         "It doesn't need saying yet to be true"],
  syn="The aftermath of the set piece: the first honest admission of "
      "cost, and the first time either of them lets that honesty change "
      "anything."),
S(15, "Tomas Watches", "A", 20, "Highstone Cairn, the kitchen",
  "probe_test", "C", "A", "a dry joke that lands like an accusation", "levity",
  "found family, continued: Tomas notices what neither of them will name",
  [],
  [("A", "C", "affection", 0.05), ("A", "B", "affection", 0.05)],
  0.40,
  beats=["Tomas has been keeping his own private ledger of the two of "
         "them for a fortnight and finally, over breakfast, decides to "
         "present his findings",
         "'You made him two mugs of tea before you made yourself one,' "
         "he says, entirely too pleased with himself for a nineteen-year-"
         "old. 'I'm simply reporting the data'",
         "'It's efficient,' Isla says, with the specific dignity of a "
         "woman who knows exactly how unconvincing that sounds",
         "'Very efficient,' Tomas agrees, in the tone of someone who has "
         "decided not to argue with a losing position out loud",
         "He goes back to his reports, satisfied, and Isla sits with her "
         "tea a moment longer than the tea requires, doing arithmetic on "
         "her own face that she doesn't much like the answer to"],
  syn="A lighter beat: found family and dry understatement, and the "
      "first outside confirmation that whatever this is, it shows."),
S(16, "Ask Before It Happens", "A", 25, "the cairn field above Highstone, dusk",
  "negotiate_consent", "A", "B", "a kiss, discussed before it happens", "grant-negotiated",
  "advance scene: the first kiss is negotiated and granted before it happens",
  [],
  [("A", "B", "trust", 0.11), ("B", "A", "trust", 0.10),
   ("A", "B", "commitment", 0.06), ("B", "A", "commitment", 0.05),
   ("A", "B", "vulnerability", 0.07)],
  0.66,
  consent={"kind": "ask", "act_class": "C2"},
  grants=[("A", "B", 2, "private"), ("B", "A", 2, "private")],
  beats=["Dusk over the cairn field, the light doing the particular "
         "flat-gold thing it does before the real cold sets in for the "
         "night",
         "'I want to ask you something plainly,' Isla says, 'because "
         "I've watched what the rite does when nobody asks plainly first, "
         "and I won't have that be us, whatever else we are'",
         "She asks him, in words, whether he wants this — not the "
         "binding, not the rite's cost-sharing, the actual thing sitting "
         "between them that neither has named",
         "'Yes,' Aldric says, no hesitation, no performance in it. 'Since "
         "before I knew your name, if I'm honest, which I'd rather be "
         "than not, with you specifically'",
         "Neither of them moves yet. The asking itself is the point — a "
         "vow quoted and taken apart word by word before either of them "
         "will let it become a single unexamined thing"],
  syn="Advance scene: consent asked and granted, plainly, in words, "
      "before the taboo against letting the bond stand in for it could "
      "ever be crossed."),
# ---------------------------------------------------------------- Phase 3
S(17, "The Kiss", "A", 26, "the cairn field above Highstone, full dark",
  "release_transform", "A", "B", "the first kiss", "first-kiss",
  "First_Kiss_Phase confirmed: her move, her timing, granted the evening before",
  [],
  [("A", "B", "attraction_romantic", 0.14), ("B", "A", "attraction_romantic", 0.13),
   ("A", "B", "attraction_sexual", 0.08), ("B", "A", "attraction_sexual", 0.09),
   ("A", "B", "vulnerability", 0.06)],
  0.58, contact={"class": "C2", "setting": "private"},
  beats=["Full dark, the cairn field gone silver, the cold doing nothing "
         "at all to either of them for once",
         "Isla is the one who closes the distance, which costs her "
         "something visible — a woman who has spent a decade taking "
         "costs silently, for once taking one out loud, on purpose, "
         "where it can be seen",
         "The kiss is not scripted, not negotiated moment to moment "
         "beyond the plain yes already given; it simply happens, the way "
         "a held breath finally happens into an exhale",
         "Aldric's hand at her jaw is careful in a way that has nothing "
         "to do with the cold and everything to do with a man who has "
         "spent his whole life being careful with things he's afraid of "
         "breaking",
         "Neither says anything after. There isn't a sentence built yet "
         "that would improve on the silence"],
  syn="First_Kiss_Phase realized: consented the evening before, chosen "
      "in the moment, entirely unlike anything the rite required of "
      "either of them."),
S(18, "Grafting Season", "B", 29, "the Marrow orchard, above the line",
  "bargain_trade", "B", "A", "an orchard named by what it's stopped doing", "his-world",
  "Aldric's world, properly shown: the last living trees above the line",
  [],
  [("B", "A", "affection", 0.07), ("A", "B", "respect", 0.05),
   ("A", "B", "trust", 0.04)],
  0.46,
  beats=["Aldric names every tree in the orchard by the season he "
         "grafted it, a private calendar nobody else has ever bothered "
         "to learn, and walks Isla through it like a man showing someone "
         "his actual handwriting for the first time",
         "'That one stopped fruiting the week the line moved,' he says, "
         "of a tree near the northern wall, in the same flat register he "
         "uses for everything that costs him. 'I kept it anyway. Didn't "
         "seem right, cutting down a thing for failing at something the "
         "cold did to it'",
         "Isla understands, hearing that, exactly which tree he actually "
         "means, and does not say so",
         "He puts himself between her and the wind without appearing to "
         "notice he's done it, the same reflex that put his own name "
         "forward at the rite instead of his sister's",
         "'You'd have liked the orchard whole,' he says. 'I'd have liked "
         "you whichever way I met you,' Isla says, and watches that land "
         "on him harder than she expected it to"],
  syn="Aldric's interior world, shown rather than told: an orchard that "
      "measures loss the same way its keeper does — quietly, and by what "
      "it keeps anyway."),
S(19, "The Commissioner's Deadline", "B", 32, "Highstone Cairn, the council room",
  "demand_threaten", "the Rime", "A", "a season's numbers, due in writing",
  "institutional-escalation",
  "Feld raises the stakes: the crown wants this season's failures on record",
  [],
  [("A", "the Rime", "fear", 0.05), ("B", "A", "affection", 0.05),
   ("A", "B", "trust", 0.04)],
  0.44,
  beats=["Feld returns with a second ledger, this one already half "
         "written, and asks Isla to confirm figures that read, plainly, "
         "as a recommendation to abandon the line",
         "'One binding isn't holding forty miles, Wardwright. The crown "
         "wants a plan for the apprentice, in case the current binding "
         "doesn't outlast the season'",
         "Aldric, present for the first time at one of these meetings, "
         "says nothing, but Isla feels, through the bond, the specific "
         "cold that goes through him at the word *doesn't*",
         "'The binding will outlast the season,' Isla says, which is not "
         "a fact yet, only a refusal to hand Feld the alternative",
         "Feld leaves without the figures he came for. It buys them time "
         "rather than safety, and both of them know the difference"],
  syn="Institutional pressure escalates alongside the personal stakes: "
      "the crown is already writing Tomas into the ledger as a backup "
      "plan."),
S(20, "What Tomas Is For", "A", 35, "Highstone Cairn, the workshop",
  "probe_test", "A", "C", "an apprentice training openly to replace a hearth",
  "tension-named",
  "Subplot A surfaces: Tomas trains openly to take Aldric's place if he fails",
  [],
  [("A", "C", "resentment", 0.04), ("A", "C", "trust", -0.03),
   ("A", "B", "vulnerability", 0.05)],
  0.48,
  beats=["Tomas has started drilling the binding-rite words in the "
         "evenings, quietly, on his own initiative, which Isla notices "
         "the way she notices everything she'd rather not",
         "'I'm not putting myself forward,' Tomas says, before she can "
         "ask. 'I'm just — making sure I'm ready, if it comes to that. "
         "Someone has to be'",
         "Isla cannot argue against the readiness without admitting the "
         "exact thing she isn't ready to admit: that she's been feeding "
         "the failing wards more than the rite alone accounts for, and "
         "doesn't know how much longer that arithmetic holds either",
         "She tells Tomas to keep drilling. It costs her more than "
         "telling him to stop would have",
         "Aldric finds her afterward and doesn't ask what's wrong, "
         "exactly, just sits with her in the kind of silence that isn't "
         "asking for anything back"],
  syn="The apprentice subplot sharpens: readiness that looks like "
      "prudence and reads, underneath, like a countdown neither woman "
      "in the room will name."),
S(21, "Held Breath", "B", 38, "the wardwright's cottage, night",
  "reveal_misfire", "B", "A", "a hand that won't quite close", "first-tell",
  "advance scene: the first visible sign of what the bond is truly costing him",
  [],
  [("B", "A", "vulnerability", 0.12), ("A", "B", "fear", 0.09),
   ("A", "B", "trust", 0.07), ("B", "A", "affection", -0.02)],
  0.80,
  beats=["Aldric drops a cup at dinner, ordinary enough, except his left "
         "hand doesn't close around the catch the way a hand simply "
         "does, and both of them notice it land wrong",
         "'Cold,' he says, before she can ask, flexing the hand like a "
         "man testing a fact he already knows and isn't ready to say out "
         "loud",
         "Isla doesn't push. She also doesn't look away, and something "
         "in not looking away tells him she's filed it, permanently, "
         "under things she intends to ask about properly, later",
         "'It's nothing the rite doesn't already account for,' Aldric "
         "says, which is, Isla will learn much later, the first outright "
         "untruth he's ever told her",
         "She lets the untruth stand, for tonight, and lies awake beside "
         "the memory of a stone taking heat out through a man's palms, "
         "doing arithmetic she does not like the shape of"],
  syn="Advance scene: the first crack in Aldric's carefully managed "
      "secret, small enough to explain away and large enough that Isla "
      "starts quietly building a different theory."),
# ---------------------------------------------------------------- Phase 4
S(22, "Beyond the Line", "A", 40, "the rime-line, three miles past the last standing cairn",
  "probe_test", "A", "B", "the line, crept forward again", "travel",
  "the Rime's advance made concrete: further, always further, never back",
  [],
  [("A", "B", "trust", 0.05), ("B", "A", "trust", 0.05)],
  0.46,
  beats=["The line has crept four miles since first frost, by Isla's own "
         "count, and does not care that her count exists",
         "They go out past the last standing cairn to check a rumor: a "
         "village, once inside the ward-line, now sitting past it, "
         "unaccounted for in any ledger Isla's ever kept",
         "The cold past the line does something specific to sound — it "
         "flattens it, the way a held breath flattens a room — and "
         "neither of them talks much on the walk in",
         "Aldric's hand finds hers without either of them deciding it "
         "should, and this time neither lets go for reasons that have "
         "nothing to do with balance",
         "The village comes into view exactly where the rumor said it "
         "would be, and it is entirely, perfectly still"],
  syn="The journey to the mandatory set piece: the Rime's advance made "
      "physical, and the first sight of what it leaves behind."),
S(23, "Calder's Reach", "A", 42, "Calder's Reach, beyond the rime-line",
  "reveal_misfire", "A", "B", "a predecessor's rite-record, frozen mid-sentence",
  "set-piece",
  "SET PIECE (mandatory, Ph4): the frozen village, and the rite-record "
  "found in its cairn",
  ["CE-02"],
  [("A", "B", "vulnerability", 0.11), ("B", "A", "trust", 0.09),
   ("A", "the Rime", "fear", 0.08)],
  0.40,
  beats=["SET PIECE (Ph4): Calder's Reach stands exactly as the cold left "
         "it — doors shut against weather that came anyway, a kettle "
         "still hung over a hearth that hasn't drawn breath in years",
         "The village cairn holds a record box, sealed, and inside it a "
         "predecessor wardwright's own hand — not Isla's line, an older "
         "one, writing about a rite that does not match the one Isla was "
         "taught",
         "The record describes cost taken in BOTH directions, shared, "
         "not spent one-sided into a single hearth — a mutual form, "
         "older than the version Isla learned at nineteen, corrupted "
         "somewhere in the generations between",
         "She cannot say the word for what she's reading yet, not "
         "properly, not where it would count — some part of her already "
         "knows this discovery isn't hers to speak aloud until she's "
         "certain, and being wrong here would cost more than being slow",
         "Aldric watches her read it twice, three times, her face doing "
         "the thing it does when an old grief and a new fact arrive in "
         "the same room together"],
  syn="Mandatory set piece and the book's central revelation, discovered "
      "but not yet spoken: the sacrificial rite Isla was taught is a "
      "corruption of an older, mutual one."),
S(24, "What the Record Doesn't Say", "A", 44, "Calder's Reach, the wardwright's house",
  "reveal_misfire", "A", "B", "Ossian Thale, six years unmourned", "grief-closes",
  "CE-04 closes: Isla's grief for her mentor, faced rather than filed",
  ["CE-04"],
  [("A", "B", "vulnerability", 0.12), ("B", "A", "affection", 0.09),
   ("A", "B", "trust", 0.07)],
  0.44,
  close=["CE-04"],
  beats=["The house the record came from was a wardwright's, same as "
         "Isla's own, and the shape of the life lived in it is close "
         "enough to hers that she has to sit down on its cold hearthstone "
         "for a while before she can read anything else",
         "'My mentor walked into the cold,' Isla says, out loud, for the "
         "first time to anyone who wasn't already at the funeral. 'I "
         "completed the rite that spent him. They thanked me for it "
         "afterward. Nobody asked whether I wanted to be thanked'",
         "Aldric doesn't offer comfort shaped like fixing. He sits with "
         "her on the cold stone and lets the grief be exactly as large as "
         "it actually is, which turns out to be the only thing that "
         "helps",
         "'You've been carrying that alone for six years,' he says, "
         "eventually. 'I know the shape of that particular weight'",
         "CE-04 closes here — not because the grief is gone, but because "
         "it has, for the first time, been said aloud to someone who "
         "didn't need her to be alright about it"],
  syn="Grief faced rather than filed: Isla says her mentor's name and "
      "the true cost of his death aloud, in the one house in the world "
      "shaped enough like her own to make it possible."),
S(25, "True Cost", "A", 46, "the road back from Calder's Reach", "release_transform",
  "B", "A", "exactly how much of him the stone has already taken",
  "midpoint",
  "MIDPOINT: the bond hands her the true, cumulative cost, all at once",
  [],
  [("B", "A", "vulnerability", 0.14), ("A", "B", "fear", 0.10),
   ("A", "B", "trust", 0.08), ("B", "A", "emotional_safety", -0.07)],
  0.62,
  beats=["Walking back, exhausted, the bond does the thing it did once "
         "at the Long Reach cairn, except larger, uncontrolled, and "
         "Isla feels — all at once, cumulative, undeniable — exactly "
         "how much of Aldric the last months of ward-setting have "
         "already spent",
         "It is not a single scene's cost. It is every ward since the "
         "binding, stacked, and it is considerably more than the record "
         "she's been keeping accounts for",
         "'How long have you been like this,' Isla says, and her voice "
         "does something she doesn't authorize",
         "'Since before you'd have noticed, if you weren't looking for "
         "it,' Aldric says, which is not quite an answer and is entirely "
         "an admission",
         "MIDPOINT (true cost revealed): whatever arrangement she "
         "thought she was managing, she understands now, walking a road "
         "in the dark with a man who's been quietly dying for her "
         "record-keeping, that the arrangement was never sustainable to "
         "begin with"],
  syn="Advance scene and structural midpoint: the true, cumulative cost "
      "lands all at once, and the story's central problem stops being "
      "theoretical."),
# ---------------------------------------------------------------- Phase 5
S(26, "Sela's Ledger", "B", 47, "the Marrow orchard, the grain-house",
  "probe_test", "A", "E", "a grain-record that finally balances the wrong way",
  "stakes-widen",
  "found family deepens: Sela's record shows exactly how dire the season is",
  [],
  [("A", "E", "trust", 0.06), ("B", "A", "affection", 0.06)],
  0.48,
  beats=["Sela shows Isla the winter grain count without being asked a "
         "second time, trusting her now the way she didn't at their first "
         "meeting",
         "The count is bad. Worse than bad if the line keeps its current "
         "pace, worse still if Aldric's binding fails before spring",
         "'He'd never tell you it's this close,' Sela says. 'He didn't "
         "tell me either, for months, when it was his exemption on the "
         "line instead of yours'",
         "Isla understands, hearing it, that she is looking at the "
         "family shape of Aldric's flaw — a household that has been "
         "quietly absorbing costs and calling it management for at least "
         "two generations",
         "'I'm not going to let this cost him what it cost your father,' "
         "Isla says, and means it as a promise before she's fully "
         "decided what she can actually do to keep it"],
  syn="Found family payoff building: the Marrow household's whole "
      "pattern of quiet self-spending, laid bare in a grain-record "
      "nobody wanted to show her."),
S(27, "What He Hasn't Said", "B", 49, "the wardwright's cottage, night",
  "deflect_withhold", "A", "B", "a hand that stays in his pocket too often",
  "probing",
  "Isla presses, gently, on the shape of what Aldric is still hiding",
  [],
  [("A", "B", "trust", -0.03), ("B", "A", "vulnerability", 0.06),
   ("A", "B", "vulnerability", 0.05)],
  0.50,
  beats=["Isla has started noticing the pattern rather than the "
         "incidents — the left hand kept in a pocket more evenings than "
         "not, the flexing he does when he thinks no one's watching, the "
         "specific care he takes never to need that hand for anything "
         "delicate anymore",
         "'Show me,' she says, finally, plainly, the way she asked him "
         "once whether he wanted her",
         "He doesn't, not fully, not yet — he shows her enough: two "
         "fingers gone entirely numb, a third going, a cold that doesn't "
         "thaw by the fire the way the rest of him does",
         "'It's not the whole of it,' Isla says. 'I know it isn't,' "
         "Aldric says, and for once doesn't try to make the admission "
         "smaller than it is",
         "Neither of them says the word HOW MUCH LONGER. It sits in the "
         "cottage with them anyway, taking up exactly as much room as if "
         "they had"],
  syn="The gap between them narrows without closing entirely: he gives "
      "her more of the truth than he's given anyone, and still not all "
      "of it."),
S(28, "Ask Me Properly", "B", 51, "the wardwright's cottage, late",
  "negotiate_consent", "A", "B", "consent asked in full, unbound by the rite",
  "set-piece",
  "SET PIECE (mandatory, Ph5): consent negotiated before first C3 contact",
  [],
  [("A", "B", "trust", 0.13), ("B", "A", "trust", 0.12),
   ("A", "B", "commitment", 0.08), ("B", "A", "commitment", 0.07)],
  0.56,
  consent={"kind": "ask", "act_class": "C3"},
  grants=[("A", "B", 3, "private"), ("B", "A", 3, "private"),
          ("A", "B", 4, "private"), ("B", "A", 4, "private")],
  beats=["SET PIECE (Ph5): before anything further happens between them, "
         "Isla makes them both say it in words, out loud, unbound — not "
         "the rite speaking, not the bond's compulsion, a person asking "
         "another person",
         "'I need to know this is you asking,' Aldric says, 'not the "
         "bond wanting company against the cold. I've watched what the "
         "bond can make either of us feel without meaning to'",
         "'It's me asking,' Isla says, and means it plainly enough that "
         "he hears the difference between a bond's pull and an actual "
         "choice, because she has learned, this whole book, exactly what "
         "that difference sounds like",
         "He asks her the same question back, in the same plain terms, "
         "and she gives him the same plain answer",
         "Nothing happens yet. The asking is the whole of the scene, "
         "and it is, both of them understand, the only foundation either "
         "of them is willing to build anything further on"],
  syn="Mandatory consent negotiation: both leads explicitly separate the "
      "bond's compulsion from their own choice, on the page, before "
      "anything past this point is allowed to happen."),
S(29, "Held, Not Spent", "A", 53, "the wardwright's cottage, evening",
  "bargain_trade", "B", "A", "an evening spent, deliberately, on nothing urgent",
  "tender-bridge",
  "a quiet evening between the negotiation and its consequence",
  [],
  [("B", "A", "affection", 0.08), ("A", "B", "emotional_safety", 0.07)],
  0.50,
  beats=["Nothing urgent happens, deliberately, by unspoken agreement — "
         "no ledgers, no cairns, no Feld, no numb hand mentioned once",
         "Aldric names the fire's shape after a grafting season, an old "
         "habit Isla's stopped finding strange and started finding, "
         "instead, like a language she's slowly learning to read",
         "'Tell me something that isn't about cost,' Isla says. 'Any of "
         "it. Something just yours'",
         "He tells her about the first tree he ever grafted badly, at "
         "eleven, and how his father let it grow crooked rather than "
         "cut it, on the grounds that a mistake you own is worth more "
         "than a straight line you didn't earn",
         "Isla falls asleep, for the first time in longer than she can "
         "place, without running a single column of arithmetic first"],
  syn="A held breath before the next escalation: an evening spent, on "
      "purpose, being simply two people rather than a wardwright and a "
      "hearth."),
S(30, "First Intimacy", "A", 55, "the wardwright's cottage, night", "release_transform",
  "A", "B", "chosen, unbound, entirely theirs", "first-intimacy",
  "First_Intimacy_Phase realized, on the page but not explicit",
  [],
  [("A", "B", "attraction_sexual", 0.13), ("B", "A", "attraction_sexual", 0.12),
   ("A", "B", "vulnerability", 0.10), ("B", "A", "vulnerability", 0.09),
   ("A", "B", "commitment", 0.06)],
  0.60, contact={"class": "C4", "setting": "private"},
  beats=["Everything that happens between them tonight has already been "
         "asked for, plainly, in words, days before — nothing here "
         "arrives compelled, borrowed, or bond-bright; it arrives chosen",
         "Isla is careful with him in the specific way of someone who "
         "has spent this whole book learning that care and cost are not "
         "the same instrument",
         "The bond, for once, stays quiet and lets the moment belong "
         "entirely to the two people actually in the room",
         "Afterward, Aldric's hand — the good one — finds hers in the "
         "dark, and neither of them says anything, because for the first "
         "time in either of their lives, nothing needs saying to be true",
         "It is not a cure for anything. It is not meant to be. It is, "
         "simply, theirs"],
  syn="First_Intimacy_Phase realized: chosen, consented, entirely "
      "outside the rite's reach — the one thing in the whole book that "
      "belongs to no ledger at all."),
S(31, "Morning, Unhidden", "B", 58, "the wardwright's cottage, dawn", "reveal_misfire",
  "B", "A", "a hand that won't hold a cup at all", "advance",
  "advance scene: the secret can no longer be managed away",
  [],
  [("B", "A", "vulnerability", 0.13), ("A", "B", "fear", 0.11),
   ("A", "B", "trust", 0.09), ("B", "A", "emotional_safety", -0.08)],
  0.86,
  beats=["Morning finds them unhurried, for once, until Aldric reaches "
         "for the tea and his whole left hand simply does not close, "
         "the cup falling and breaking against the hearthstone",
         "He looks at his own hand like a stranger's. Isla is already "
         "moving before she's decided to",
         "'How long has it been the whole hand,' she says, and this time "
         "there is no room in her voice for him to manage the answer "
         "smaller",
         "'A week,' Aldric admits, finally, all of it. 'Maybe longer. "
         "I stopped counting because counting wasn't going to change the "
         "number'",
         "Isla sits with him on the cold floor among the broken cup and "
         "understands, plainly, that whatever time she thought they had "
         "was never as much as she was budgeting for"],
  syn="Advance scene: the secret breaks open on its own, past managing, "
      "and the story's true deadline finally has a face on it."),
# ---------------------------------------------------------------- Phase 6
S(32, "The Mutual Form", "A", 59, "Highstone Cairn, the record-room", "reveal_misfire",
  "A", "B", "the older rite, finally spoken aloud", "revelation-spoken",
  "CE-02 closes: the mutual form is stated aloud for the first time",
  ["CE-02"],
  [("A", "B", "trust", 0.10), ("B", "A", "trust", 0.09),
   ("A", "B", "vulnerability", 0.08)],
  0.62,
  close=["CE-02"],
  beats=["Isla lays the predecessor's record beside her own training and "
         "says, finally, out loud, the thing she has been circling since "
         "Calder's Reach: 'The rite I was taught takes from one hearth "
         "alone. There's an older form. It shares the cost between both "
         "of us, instead of spending only you'",
         "Saying it changes the room. CE-02 closes here — not with proof "
         "yet, only with the words finally out where they can be tested "
         "against the world",
         "'Why has no one used it in generations,' Aldric asks, careful, "
         "already guessing at an answer he doesn't want",
         "'Because sharing the cost means the wardwright pays too,' Isla "
         "says. 'And every generation of rite-keepers since has found it "
         "easier to spend one hearth quietly than two wardwrights "
         "loudly'",
         "Aldric goes very still, hearing that, and Isla watches him "
         "understand, in real time, that she is proposing to spend "
         "herself for him exactly as visibly as he's been spending "
         "himself for everyone else"],
  syn="CE-02 closes: the rite's true, mutual, corrupted-from-shared "
      "nature is finally spoken aloud, honoring the constraint that no "
      "one could name it before Phase 6."),
S(33, "Matching Secrets", "B", 61, "the wardwright's cottage, night", "reveal_misfire",
  "A", "B", "two years of feeding the wards her own heat, admitted", "mutual-reveal",
  "Isla's own hidden cost surfaces alongside Aldric's, in the same conversation",
  [],
  [("A", "B", "vulnerability", 0.14), ("B", "A", "trust", 0.11),
   ("B", "A", "vulnerability", 0.08), ("A", "B", "emotional_safety", -0.06)],
  0.64,
  beats=["Aldric, turning the mutual-rite idea over, asks the plain "
         "question: if the wardwright pays too, what has Isla already "
         "been paying, alone, that the record doesn't show",
         "It is, she realizes, exactly the shape of question she asked "
         "him at the Long Reach cairn. She owes him the same answer she "
         "demanded of him",
         "'Two years,' Isla says. 'I've been feeding the failing wards "
         "my own heat, outside the rite, since before my mentor's death "
         "made me the only one left to do it. It isn't in any ledger. "
         "I didn't want it to be'",
         "Aldric doesn't look surprised. 'I wondered,' he says. 'You "
         "run cold on purpose, you said, the first week I knew you. I "
         "didn't understand what that actually cost until just now'",
         "They sit with the matching shape of it — two people who have "
         "each spent themselves in silence and called it discipline — "
         "and something between them deepens that has nothing left to "
         "hide behind"],
  syn="Both hidden costs surface in the same conversation: Isla's secret "
      "self-spending mirrors Aldric's exactly, and neither of them has "
      "anywhere left to hide it."),
S(34, "Feld's Deadline", "A", 63, "Highstone Cairn, the council room", "demand_threaten",
  "the Rime", "A", "an ultimatum, in writing, with a date on it",
  "institutional-peak",
  "Feld threatens to force Tomas into the rite if the line fails once more",
  [],
  [("A", "the Rime", "fear", 0.09), ("A", "C", "trust", -0.04)],
  0.58,
  beats=["Feld's letter is shorter than his usual ledgers and considerably "
         "more dangerous: one more failed cairn, and the crown will "
         "authorize the apprentice's binding regardless of Isla's "
         "objection",
         "'You've had a season to prove the current binding sufficient, "
         "Wardwright. The Rime doesn't extend courtesy for good intentions'",
         "Isla wants to tell him about the mutual rite and cannot — not "
         "without proof, not without risking Feld deciding the whole "
         "idea is exactly the kind of destabilizing nonsense a "
         "desperate wardwright would invent",
         "Tomas, told the contents afterward, goes quiet in a way that "
         "isn't fear exactly — closer to a young man doing sums about "
         "duty that nobody his age should have to do",
         "'I won't let it be you,' Isla tells him, and hears, saying it, "
         "exactly how much that promise is going to cost her to keep"],
  syn="Institutional stakes peak: the external clock and the internal "
      "crisis converge on the same deadline, from opposite directions."),
S(35, "The Cairn at Long Reach, Again", "B", 66, "the Long Reach cairn, on the northern line",
  "release_transform", "A", "B", "a ward set harder than the last, and worse",
  "ritual-repeat",
  "another ward set; the cost visibly, undeniably compounding",
  [],
  [("B", "A", "vulnerability", 0.12), ("A", "B", "fear", 0.10),
   ("A", "B", "trust", 0.06)],
  0.60,
  beats=["This time Isla feeds the ward everything she has held back "
         "before, trying to spare him even a fraction of what the Long "
         "Reach cairn wants, and it isn't enough, and she knows before "
         "she starts that it won't be",
         "Aldric's hand — the numb one, useless now for anything fine — "
         "still presses to the stone anyway, because the rite doesn't "
         "care which hand a hearth has left to give",
         "Afterward he can't stand without her arm under his, and "
         "neither of them says the word FAILING, though it's the only "
         "honest word available",
         "'This can't hold through the season,' Isla says, flat, to "
         "herself as much as to him",
         "'Then we don't hold it the old way,' Aldric says, and it is "
         "the first time either of them has said the mutual rite's name "
         "out loud as a plan rather than a discovery"],
  syn="Redundancy-tightened ritual repeat: the same ward, visibly worse, "
      "proving the old rite is no longer survivable on its current "
      "terms."),
S(36, "What the Rite Would Cost Him", "A", 69, "Highstone Cairn, the record-room",
  "probe_test", "A", "C", "an untested rite, and everything it could still cost",
  "doubt",
  "Isla's fear that the mutual rite, untested, could kill them both",
  [],
  [("A", "C", "trust", 0.05), ("A", "B", "fear", 0.08)],
  0.62,
  beats=["No wardwright alive has performed the mutual rite. Isla has a "
         "dead woman's account of it and nothing else, and the account "
         "does not say what happens if it's attempted wrong, or late, "
         "or by two people the rite-keepers never sanctioned to try it",
         "'You could tell the Keepers,' Tomas offers. 'Let them decide "
         "properly, with more than one record to go on'",
         "'The Keepers would take a season to decide properly,' Isla "
         "says. 'We don't have a season. We barely have the one cairn "
         "Aldric can still stand at'",
         "She does not tell Tomas the other fear underneath the first "
         "one — that the rite, attempted wrong, could spend them both "
         "at once, and that she is, for the first time in her life, "
         "more frightened of losing Aldric than of dying herself",
         "The record-room holds that fear with her a long while, in the "
         "specific silence of a room built entirely out of other "
         "people's endings"],
  syn="The doubt before the fracture: the mutual rite is the only "
      "answer left and entirely unproven, and the cost of being wrong "
      "could be everything."),
S(37, "The Cairn Cracks", "B", 72, "the Long Reach cairn, on the northern line",
  "reveal_misfire", "B", "A", "the northern cairn, splitting under its own cold",
  "fracture",
  "ALL IS LOST: the northern cairn cracks; Aldric nearly spent alone holding it",
  [],
  [("B", "A", "fear", 0.14), ("B", "A", "emotional_safety", -0.13),
   ("A", "B", "vulnerability", 0.12), ("A", "the Rime", "fear", 0.10)],
  0.90,
  beats=["ALL IS LOST: the Long Reach cairn cracks at dusk, a sound like "
         "the whole line taking a breath it can't let back out, and "
         "Aldric — alone at the stone, having gone out without waking "
         "her — throws everything he has left into holding it rather "
         "than let it fail outright",
         "Isla feels it through the bond before she hears it, a cold "
         "that isn't weather arriving all at once in her chest, and runs "
         "the whole three miles not entirely sure, until she arrives, "
         "that she isn't running toward a body",
         "She finds him upright, barely, one hand fused white to the "
         "cracked stone, the cairn holding by a margin so thin it isn't "
         "really holding at all",
         "'I wasn't going to let it be the one that finally breaks,' "
         "Aldric says, through it, which is not the same as saying he "
         "thought he'd survive making sure it didn't",
         "She gets him off the stone. The cairn holds, for now, cracked "
         "and ugly and standing, and both of them understand, in the "
         "walk back, that they have run out of time to do this the slow, "
         "careful, properly-sanctioned way"],
  syn="Fracture scene: the northern cairn cracks, Aldric nearly spends "
      "himself alone holding it, and the story's clock runs out."),
# ---------------------------------------------------------------- Phase 7
S(38, "Vow Renounced", "B", 73, "the wardwright's cottage, before dawn", "realign_betray",
  "B", "A", "the bond, renounced, to keep her out of the cost", "black-moment",
  "BLACK MOMENT: Aldric tries to void the bond alone, to protect her",
  ["CE-01"],
  [("B", "A", "emotional_safety", -0.14), ("A", "B", "trust", -0.10),
   ("B", "A", "resentment", 0.05)],
  0.72,
  misfire=["CE-01"],
  withdraw=[("B", "A", 3)],
  beats=["BLACK MOMENT: before Isla wakes, Aldric goes to Keeper Ossory "
         "alone and asks — not for the mutual rite, for the old one, "
         "finished, on his terms, to close the debt the corrupted way "
         "before it can take her down with him",
         "'The rite was mine to volunteer for,' he tells Ossory. 'Let it "
         "be mine to finish. Don't let her spend herself proving an "
         "untested form to save a hearth that's already this far gone'",
         "It is, Isla realizes when she finds the note he's left instead "
         "of himself, the exact corrupted shape of the rite he swore, "
         "with her, to rewrite — one hearth, alone, spent quietly, "
         "called noble instead of named for what it actually is",
         "CE-01 misfires here: his attempt to discharge the debt the old, "
         "one-sided way very nearly succeeds, in exactly the way that "
         "would have killed him",
         "He has withdrawn every grant he ever gave her, formally, "
         "through Ossory, believing — wrongly, the way his flaw always "
         "believes — that giving before being asked is the same thing as "
         "love"],
  syn="Black moment and breakup beat: Aldric renounces the bond and "
      "attempts the sacrifice alone, believing it the only way to keep "
      "Isla from paying a cost he's decided is his to carry by himself."),
S(39, "What She Won't Let Him Pay Alone", "A", 75, "Highstone Cairn, the rite-hall",
  "demand_threaten", "A", "B", "a debt she refuses to let be paid alone",
  "reversal",
  "Isla refuses the withdrawal and goes after him before the old rite completes",
  [],
  [("A", "B", "trust", 0.11), ("B", "A", "trust", 0.10),
   ("A", "B", "commitment", 0.09)],
  0.70,
  beats=["Isla reaches the rite-hall before Ossory can finish anything, "
         "and says the thing she has spent this whole book learning how "
         "to say instead of silently absorbing: 'You don't get to decide "
         "this alone. Not the cost, not the ending, not what I'm allowed "
         "to be spent on'",
         "'I renounced the grant,' Aldric says, hollow, meaning to make "
         "it simple. 'You don't have to—'",
         "'I don't have to,' Isla agrees. 'I'm choosing to. That's the "
         "whole of what the mutual rite actually means, and you don't "
         "get to protect me out of choosing it'",
         "Ossory, watching two wardwrights argue in his rite-hall over "
         "which one gets to be spent, does something neither of them "
         "expects: he sends for the record himself, and says he'll hear "
         "the mutual form argued properly, tonight, rather than let "
         "either of them decide anything alone",
         "It is not yet a rescue. It is, for the first time, a fight "
         "they're both actually in"],
  syn="The reversal: Isla refuses the martyrdom he's tried to claim for "
      "himself, and forces the choice back into the room where both of "
      "them actually stand."),
S(40, "The Great Northern Cairn", "A", 78, "the Long Reach cairn, on the northern line",
  "release_transform", "A", "B", "the rite, rewritten, on the page", "climax",
  "CLIMAX: the great northern cairn is re-set by the mutual rite",
  [],
  [("A", "B", "trust", 0.14), ("B", "A", "trust", 0.14),
   ("A", "B", "commitment", 0.13), ("B", "A", "commitment", 0.12),
   ("A", "B", "vulnerability", 0.10), ("B", "A", "vulnerability", 0.09)],
  0.78,
  consent={"kind": "ask", "act_class": "C4"},
  grants=[("A", "B", 3, "private"), ("B", "A", 3, "private"),
          ("A", "B", 4, "private"), ("B", "A", 4, "private")],
  beats=["SET PIECE (mandatory, climax): both hands from both of them on "
         "the cracked Long Reach cairn, the predecessor's mutual rite "
         "spoken whole for the first time in generations, Ossory and "
         "Tomas both come out to the line to witness it done properly "
         "rather than alone",
         "'Ask me again,' Aldric says, at the stone, echoing the "
         "cottage, echoing every asking that's come before this one. "
         "'Properly. Unbound. So there's no version of tonight where "
         "either of us claims the other one didn't choose it'",
         "Isla asks. He asks back. Both grants renewed, chosen, on "
         "purpose, in front of witnesses this time instead of only each "
         "other",
         "The stone takes from both of them, evenly, for the first time "
         "in the northern line's long, corrupted history — a cost that "
         "halves rather than concentrates, shared the way the "
         "predecessor's record always said it should be",
         "The cairn holds. Not perfectly. Not without a mark left on "
         "either of them. But it holds, standing, on terms neither the "
         "Rime nor the old rite ever offered either of them before"],
  syn="Climax: the mutual rite performed on the page, chosen and "
      "witnessed, the great northern cairn re-set on entirely new terms."),
S(41, "Cost Shared", "B", 82, "the wardwright's cottage, the morning after",
  "release_transform", "B", "A", "a cost that halves instead of consuming", "fracture",
  "the immediate aftermath: both marked, both alive, both spent evenly",
  [],
  [("B", "A", "affection", 0.13), ("A", "B", "affection", 0.12),
   ("B", "A", "emotional_safety", 0.11), ("A", "B", "commitment", 0.09)],
  0.74,
  close=["CE-01", "CE-03"],
  beats=["Aldric wakes with feeling returned to three fingers he'd "
         "written off for good, and a cold in the other two that will, "
         "the healer says, likely never fully thaw — a mark, not a "
         "cure, and neither of them pretends otherwise",
         "CE-01 and CE-03 close here, together: the debt discharged "
         "mutually rather than paid alone, the threat of his being "
         "spent to death answered by a rite that no longer asks one "
         "hearth to carry what two can share",
         "'You're not fixed,' Isla says, meaning the hand, meaning all "
         "of it. 'I know,' Aldric says. 'I wasn't asking to be fixed. I "
         "was asking to still be here, which is a considerably lower "
         "bar and one we've actually cleared'",
         "Isla feels her own cost too, now, properly, for the first "
         "time in two years of quietly spending herself uncounted — "
         "tired in a way that has weight rather than shame attached to "
         "it",
         "They sit with the shared ache of it, in a cottage that has "
         "fully, finally, rearranged itself around two people rather "
         "than one, and neither of them reaches for a ledger to explain "
         "why that feels like enough"],
  syn="Fracture scene and immediate aftermath: CE-01 and CE-03 both "
      "close as the rewritten rite's cost lands, shared and survivable, "
      "on both of them at once."),
# ---------------------------------------------------------------- Phase 8
S(42, "What the Line Costs Now", "A", 83, "Highstone Cairn, the council room",
  "bargain_trade", "A", "the Rime", "a precedent, argued into the record",
  "institutional-resolution",
  "the mutual rite is argued into standing precedent before Feld and Ossory",
  [],
  [("A", "the Rime", "resentment", -0.05), ("A", "E", "trust", 0.05)],
  0.44,
  beats=["Feld comes for his figures and gets, instead, a rite-record "
         "with two names on it and a season's worth of cairns still "
         "standing to prove the method works",
         "'This isn't sanctioned,' Feld says, which is true, and "
         "considerably weaker than it would have sounded a season ago",
         "'It's precedented,' Ossory says, before Isla has to. 'Older "
         "than the version the crown's been funding. I'll take that up "
         "with whoever above you wants to argue geology with a standing "
         "stone'",
         "Feld leaves with less than he came for and no date set for "
         "abandoning anything. It is not a victory with a bow on it. It "
         "is, this once, enough",
         "Sela's exemption stands regardless, secured now on a "
         "foundation that no longer depends on any single hearth failing "
         "quietly to hold it up"],
  syn="Institutional resolution: the mutual rite becomes precedent "
      "rather than anomaly, and the external clock finally stops running "
      "against them specifically."),
S(43, "Tomas's Choice", "A", 85, "Highstone Cairn, the workshop", "bargain_trade",
  "A", "C", "an apprenticeship no longer shaped like a countdown", "found-family-payoff",
  "found family pays off: Tomas's future secured on his own terms",
  [],
  [("A", "C", "trust", 0.08), ("A", "C", "respect", 0.07)],
  0.42,
  beats=["Tomas asks, carefully, whether he's still needed now that the "
         "line holds on new terms, in a voice that's trying hard not to "
         "sound like it's hoping for a particular answer",
         "'You were never needed as a spare hearth,' Isla says. 'You're "
         "needed as the next wardwright, on whatever timeline actually "
         "suits you, which was always the job I meant to offer you'",
         "He doesn't quite believe it right away, the way people raised "
         "on a countdown don't always trust a clock that's stopped, and "
         "Isla lets him take the time to believe it properly instead of "
         "insisting",
         "'I'd like to learn the mutual form,' Tomas says, eventually. "
         "'Properly. From the start, this time, not stitched together "
         "out of a dead woman's journal at the last possible hour'",
         "'That's the job,' Isla agrees, and means, underneath it, that "
         "the whole northern line is finally being handed forward "
         "instead of merely survived"],
  syn="Found family payoff: Tomas's future stops being a contingency "
      "plan for someone else's failure and becomes, simply, his own."),
S(44, "Grafting Days", "B", 87, "the Marrow orchard, above the line", "bargain_trade",
  "B", "A", "a crooked tree, kept on purpose", "tender-return",
  "a quiet return to Aldric's world, now shared rather than merely shown",
  [],
  [("B", "A", "affection", 0.12), ("A", "B", "affection", 0.11),
   ("A", "B", "commitment", 0.08)],
  0.46,
  beats=["Spring is not close, not truly, but the orchard has stopped "
         "sounding like a countdown and started sounding, again, like a "
         "place things are grafted rather than merely endured",
         "Aldric grafts a new branch onto the crooked tree from his "
         "childhood, two fingers still slow to answer him, working "
         "around it rather than pretending it isn't there",
         "'Name this one,' he says, handing Isla the knife, an act of "
         "trust considerably larger than it looks",
         "She names it for the day the cairn held — not the day it "
         "cracked, the day after, the day they walked back from it "
         "still standing, both of them, on their own two feet",
         "Sela watches the two of them from the grain-house door and "
         "says nothing at all, which is, from her, the highest praise "
         "available"],
  syn="A tender return to Aldric's world, no longer merely shown to "
      "Isla but shared, grafted, kept on purpose the way he keeps "
      "everything he's decided is worth the trouble."),
S(45, "Cost Shared Openly", "A", 88, "the Long Reach cairn, on the northern line",
  "release_transform", "A", "B", "a vow, reframed, chosen in the open", "resolution",
  "RESOLUTION: the vow stands, mutual and chosen, cost shared openly",
  [],
  [("A", "B", "commitment", 0.13), ("B", "A", "commitment", 0.12),
   ("A", "B", "affection", 0.10), ("B", "A", "affection", 0.10),
   ("A", "B", "perceived_reciprocity", 0.12), ("B", "A", "perceived_reciprocity", 0.11)],
  0.50,
  beats=["The line has crept another mile since first frost, because the "
         "Rime never once, in eighty-eight days, gave any of them "
         "reason to believe it would stop advancing. Forty-one cairns "
         "still stand anyway",
         "Isla and Aldric set the season's last ward together at the "
         "Long Reach cairn, the crack in the stone visible under new "
         "frost, the cost between them ordinary now, in the way a "
         "shared thing becomes ordinary once it's stopped being a "
         "secret",
         "'For everyone who's been someone else's warmth,' Aldric says, "
         "at the stone, an old blessing he's altering as he says it, "
         "'and wanted, once, to be kept'",
         "'Kept,' Isla agrees, and lays her hand over his marked one, "
         "and means the whole of what the word costs and offers both",
         "No proposal, no crown's blessing, no ending the ledger would "
         "ever call complete. Just two hearths, sharing one winter, "
         "openly, on purpose, for as long as the line needs holding"],
  syn="Resolution: the vow stands rewritten, mutual, and chosen in the "
      "open — cost shared rather than spent, for as long as either of "
      "them is asked to hold it."),
]

SCENE = {s["scene"]: s for s in SCENES}

CHAPTERS = [
    (1,  "The Assembly", [1]),
    (2,  "Cairns and Debts", [2, 3]),
    (3,  "Ground Rules", [4, 5]),
    (4,  "First Frost, First Crack", [6]),
    (5,  "The Ward-Commissioner's Ledger", [7]),
    (6,  "Thaw a Stranger's Byre", [8]),
    (7,  "Touch-Starved", [9]),
    (8,  "What the Ledger Doesn't Say", [10]),
    (9,  "Held Ground", [11, 12]),
    (10, "What the Stone Takes", [13]),
    (11, "Aftermath, Underlit", [14, 15]),
    (12, "Ask Before It Happens", [16]),
    (13, "The Kiss", [17]),
    (14, "Grafting Season", [18]),
    (15, "The Commissioner's Deadline", [19]),
    (16, "What Tomas Is For", [20]),
    (17, "Held Breath", [21]),
    (18, "Beyond the Line", [22]),
    (19, "Calder's Reach", [23]),
    (20, "What the Record Doesn't Say", [24]),
    (21, "True Cost", [25]),
    (22, "Sela's Ledger", [26]),
    (23, "What He Hasn't Said", [27]),
    (24, "Ask Me Properly", [28, 29]),
    (25, "First Intimacy", [30]),
    (26, "Morning, Unhidden", [31]),
    (27, "The Mutual Form", [32]),
    (28, "Matching Secrets", [33]),
    (29, "Feld's Deadline", [34]),
    (30, "The Cairn at Long Reach, Again", [35]),
    (31, "What the Rite Would Cost Him", [36]),
    (32, "The Cairn Cracks", [37]),
    (33, "Vow Renounced", [38]),
    (34, "What She Won't Let Him Pay Alone", [39]),
    (35, "The Great Northern Cairn", [40]),
    (36, "Cost Shared", [41]),
    (37, "What the Line Costs Now", [42]),
    (38, "Tomas's Choice", [43]),
    (39, "Grafting Days", [44]),
    (40, "Cost Shared Openly", [45]),
]
