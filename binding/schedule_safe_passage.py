"""Authored scene schedule for Seed 01KYF6MB0CBHSYJG5CC2TKW0WD — "Safe Passage".

Editorial layer of the offline binding configuration `offline-agent-v1`
(see binding/offline_client.py). 45 scenes over the Mafia/Dark reference
allocation E = [6,8,10,10,10,12,12,10,12], phase blocks scaled
proportionally to [3,4,5,5,5,6,6,5,6].

Book 2 of the Moretti Family series; the Book One ledger case is closed and
public, per Continuity_Constraints, and the transport arm is what is left of
the family.

Cast (engine node ids are the seed's own names A/B/C/D):
  A = Mira Dalca, 33     - owner-operator, Wisniewski Cartage; passage broker
  B = Adam Marek, 34     - former transport foreman; federal witness
  C = Benny Osei, 58     - yard mechanic and dispatcher; licence of record
  D = Gino Traversa, 55  - the family's road boss
  (off-node: the eleven names on Mira's list; AUSA Raman and the Northern
   District prosecution carried over from Book One; Adam's relocated family)

Route (Continuity_Constraints: physical and continuous, no scene relocates
the pair without an on-page leg):
  Chicago (Torrence Ave) -> Portage IN -> up the Lake Michigan shore ->
  the unlisted crossing -> across the mitten -> Alpena on Lake Huron
  (freighter layover) -> south on US-23 -> Port Huron border yard ->
  back to Chicago for the testimony date.

Story clock: 19 days anchored 2026-05-04. B's testimony date is day 19 and
never moves. The epilogue sits outside the clock (Epilogue_Included).

Consent architecture: the custody imbalance is named on the page (scene 19)
and voided before any contact above C1 — scene 21 gives B a real, funded,
no-strings exit and he declines it; only then do the Phase 4 kiss and the
Phase 5 negotiated grants become admissible. B withdraws all grants in
scene 39 (after the handover) and re-grants on his own initiative in scene
43, once he is a free man testifying under his own name.
"""

PHASE_BLOCKS = {
    0: (1, 3), 1: (4, 7), 2: (8, 12), 3: (13, 17), 4: (18, 22),
    5: (23, 28), 6: (29, 34), 7: (35, 39), 8: (40, 45),
}
ADVANCE_SCENES = {3, 7, 12, 17, 22, 28, 34, 39}
FRACTURE_SCENES = {34, 39}   # delivered to the yard / reversal complete

DISPLAY = {"A": "Mira Dalca", "B": "Adam Marek",
           "C": "Benny Osei", "D": "Gino Traversa"}

PROMISE_CE04 = ("Nothing I carry gets left on the road. You arrive on the day "
                "I said, on your own feet, with your own name on you.")


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
S(1, "Wisniewski Cartage", "A", 1, "the yard, Torrence Avenue, Chicago, 4 a.m.",
  "deflect_withhold", "A", "C", "the sign she never changed", "yard-open",
  "establish the yard, the licence, the debt that has never been called",
  ["CE-01"],
  [("A", "B", "fear", 0.04)],
  0.22,
  beats=["Four a.m. yard call: two box trucks out, sodium lights burning "
         "through lake fog off the Calumet",
         "The sign still reads WISNIEWSKI CARTAGE because changing a sign "
         "costs money and attracts reading",
         "Benny Osei runs dispatch off a licence in his own name — the yard "
         "is legal because he is; Mira has never been licensable",
         "A pre-dawn habit: she counts the doors and the exits of her own "
         "office before she sits down in it",
         "Under the floor of the dispatch shed, in a coffee tin, a folded "
         "list of eleven names she has never spoken aloud"],
  syn="Establish Mira, the yard, Benny, the licence, the unlisted routes, "
      "and the eleven-year debt nobody has yet named out loud."),
S(2, "Chain of Custody", "B", 1, "a safe house in Berwyn; then a truck bay",
  "probe_test", "B", "A", "the road behind", "taken",
  "establish the witness, the date, and the refusal to run",
  ["CE-02"],
  [("B", "A", "fear", 0.15), ("B", "A", "resentment", 0.05)],
  0.28,
  beats=["Six months of a protective agreement: a rented house, a marshal "
         "who plays cribbage, a testimony date fixed for the twenty-second",
         "Two men at the door at nine at night who know the marshal's "
         "shift change, which means somebody sold it",
         "Adam Marek does not fight, because he counted the exits at the "
         "door on his first day and there were two and both are covered",
         "He is put in a truck bay and told he is being helped out of the "
         "country - a story he does not believe and does not correct",
         "The one thing he will not do is miss the date; the record is the "
         "only thing he has made in his life that isn't freight"],
  syn="Adam from inside the witness apparatus; taken, not run, and holding "
      "one fixed intention."),
S(3, "The Passage, Called", "A", 1, "the yard office; D in the car outside",
  "demand_threaten", "D", "A", "the manifest, four pages", "debt-called",
  "the debt is named; she is handed a man and a fixed route",
  ["CE-01", "CE-02"],
  [("A", "B", "resentment", 0.06), ("A", "D", "fear", 0.10),
   ("A", "D", "resentment", 0.08), ("B", "A", "fear", 0.06)],
  0.44, hot={"A-D": 0.55},
  beats=["SET PIECE (Ph0): the passage debt is called in at the yard - Mira "
         "is handed B and a fixed route",
         "Gino Traversa does not come inside. He never has, in eleven years; "
         "he speaks to her through a lowered window while his second stands "
         "in her doorway with a four-page manifest",
         "The terms: one passage, one man, nineteen days, three yards, no "
         "deviation. Delivered at the border yard on the seventeenth. "
         "Discharged on delivery",
         "'You were carried once,' Traversa says. 'This is the carry back.'",
         "Adam Marek is walked into her yard at 5:40 a.m. and stands there "
         "counting her doors, and she watches him do it and recognizes the "
         "habit as her own"],
  syn="The mandated inciting incident: the debt named, the cargo delivered, "
      "the route fixed, and D established as a man who stays outside."),
# ---------------------------------------------------------------- Phase 1
S(4, "Cargo", "A", 1, "I-94 east, Chicago to Indiana", "deflect_withhold",
  "A", "B", "the mirror check", "first-leg",
  "state the rules; hold him at freight distance",
  ["CE-01"],
  [("A", "B", "respect", 0.04), ("B", "A", "respect", 0.05)],
  0.34,
  beats=["The rules, stated once, in the order she always states them: no "
         "phones, no names at fuel stops, you sleep when I say, you eat "
         "what I hand you, you do not get out unless I open the door",
         "He asks how long. She gives him a distance instead: three hundred "
         "and forty road miles to the first yard, and eleven hours she "
         "won't drive straight",
         "Her whole method: route people, don't know them. It has kept "
         "eleven people alive and every one of them at arm's length",
         "He rides where he can see the road behind them and she lets him, "
         "and neither says why"],
  syn="Forced proximity opens at maximum distance; her flaw stated as "
      "professional practice."),
S(5, "Terms of Delivery", "B", 2, "the first yard, Portage, Indiana",
  "bargain_trade", "B", "A", "the promise as a delivery term", "the-promise",
  "he asks the real question; she answers in freight",
  ["CE-04", "CE-02"],
  [("B", "A", "trust", 0.06), ("A", "B", "respect", 0.05),
   ("A", "B", "attraction_sexual", 0.05)],
  0.40,
  beats=["Steel dust and a chain-link yard under the Burns Harbor stacks; "
         "a scale house, a man with a clipboard, a forty-minute wait",
         "Adam, quietly: 'What happens if they change their minds about "
         "where I'm going?'",
         "The promise, in her only register (L7 verbatim): '" + PROMISE_CE04
         + "'",
         "He says thank you like a man signing something. She tells him "
         "not to thank a carrier before delivery",
         "The clipboard man looks at Adam twice and writes nothing down, "
         "which is the first wrong thing"],
  syn="CE-04 opens in her own grammar — a promise phrased as a delivery "
      "term, quotable at audit."),
S(6, "What He Was", "A", 2, "night leg, US-12 through the dunes",
  "reveal_misfire", "B", "A", "the confession she didn't ask for",
  "unwanted-truth",
  "he confesses; she refuses the transaction",
  ["CE-03"],
  [("A", "B", "resentment", 0.05), ("A", "B", "respect", 0.05),
   ("B", "A", "vulnerability", 0.06)],
  0.38,
  beats=["He starts talking at eleven at night the way men do in a dark "
         "cab, and his tic is that he says what he did before he says why",
         "'I drove for them eleven years. I never asked what was in the "
         "back. Once it was a person.' Then, only then, the why",
         "Mira does not absolve him and does not comfort him. She gives him "
         "a distance to the next fuel stop",
         "In her head, the arithmetic she will not say: she was in the back "
         "of a truck once too, and someone drove it, and she has spent "
         "fourteen years not wondering who"],
  syn="B's flaw in operation — confessing to be absolved — meeting A's "
      "flaw, which is to route people instead of knowing them."),
S(7, "The Way They Count", "B", 3, "the first yard, second visit; the water",
  "probe_test", "B", "A", "counted like freight", "first-wrongness",
  "the yard counts him wrong; the pair's first alignment",
  ["CE-02", "CE-01"],
  [("B", "A", "trust", 0.07), ("A", "B", "trust", 0.06),
   ("A", "B", "attraction_sexual", 0.05), ("B", "A", "attraction_sexual", 0.05)],
  0.54,
  beats=["The scale-house man walks the truck's length and looks at the "
         "water beyond the slip while he does it",
         "Adam, who ran yards for eleven years, knows exactly what that "
         "walk is: a man estimating a load he will handle later",
         "He tells her. She says nothing for four miles and then changes "
         "her fuel stop",
         "The first thing they do together is a small silent deviation, "
         "and neither of them names it",
         "Phase turns: this is no longer a delivery, it is a situation"],
  syn="Advance scene: the wrongness is confirmed by the one passenger in "
      "America qualified to read it."),
# ---------------------------------------------------------------- Phase 2
S(8, "The Return Allowance", "A", 3, "a truck stop outside Benton Harbor",
  "probe_test", "A", "D", "fuel math", "the-arithmetic",
  "she reads the manifest properly and finds the answer",
  ["CE-01", "CE-02"],
  [("A", "D", "fear", 0.08), ("A", "D", "resentment", 0.07),
   ("A", "B", "fear", -0.05)],
  0.44,
  beats=["Under a sodium light at a scale, with a cold coffee, she does what "
         "she has done since she was nineteen: she checks the numbers",
         "The manifest's fuel allowance is wrong. Not by much. By one "
         "person's weight and one leg's diesel",
         "The return allowance is written for a single occupant and a "
         "lighter truck",
         "Distance and fuel math surfacing under emotional load: she works "
         "it three times on the back of a fuel receipt because the answer "
         "keeps arriving and she keeps sending it back",
         "She burns the receipt in the ashtray of a truck that has never "
         "had a smoker in it"],
  syn="The disposal is discovered in the only language she completely "
      "trusts — arithmetic — twelve days before anyone says it out loud."),
S(9, "The Coffee Tin", "A", 4, "phone call to the yard; a rest area on I-196",
  "deflect_withhold", "A", "C", "eleven names", "the-list",
  "establish the list and what it costs",
  ["CE-03", "CE-01"],
  [("A", "C", "trust", 0.05), ("A", "B", "vulnerability", 0.04)],
  0.48,
  beats=["Benny on a burner from the dispatch shed: two men came to the "
         "yard asking about her routes, politely, with a clipboard",
         "The tin under the floor: eleven names, eleven dates, eleven "
         "places, in her hand, the only record she has ever kept",
         "What the eleven are: passengers the family sent her to move who "
         "were never meant to arrive, and who did",
         "Why she kept the list at all — the same reason anybody keeps a "
         "record: because if nobody wrote it down, it did not happen, and "
         "she needed it to have happened",
         "'Burn it,' Benny says. 'You've said that eleven times,' she says"],
  syn="Secret_A on the page: the list is her worst exposure and her only "
      "proof that her life has had a use."),
S(10, "Licence", "A", 4, "a gravel turnout; Traversa on the phone",
  "demand_threaten", "D", "A", "the licence in another man's name",
  "the-squeeze",
  "the threat names its instrument",
  ["CE-02", "CE-01"],
  [("A", "D", "fear", 0.09), ("A", "D", "resentment", 0.08),
   ("A", "C", "fear", 0.06), ("A", "B", "trust", 0.05)],
  0.56, hot={"A-D": 0.62, "C-D": 0.55},
  beats=["Traversa, pleasant, from somewhere with a television on: he hears "
         "she took a different fuel stop",
         "'Your yard runs on Osei's licence. A licence is a piece of paper "
         "with a man's name on it. Paper's fragile, Mira.'",
         "CE-02 armed by name: deviate and the instrument is Benny",
         "She gives him a distance and an arrival time instead of a "
         "reassurance, which is the only way she has ever known how to "
         "promise anything",
         "Adam watches her hands on the wheel afterward and counts, out "
         "loud, the number of times she checks the mirror in one mile: nine"],
  syn="CE-02's mechanism established — the threat runs through the licence, "
      "which is why she cannot simply drive away."),
S(11, "Two Vehicles", "B", 5, "US-31 north, Muskegon approach",
  "probe_test", "B", "A", "the road behind", "the-tail",
  "he finds the tail; the alliance becomes operational",
  ["CE-02"],
  [("B", "A", "respect", 0.07), ("B", "A", "trust", 0.06),
   ("A", "B", "respect", 0.07)],
  0.52,
  beats=["Adam has been sitting where he can see the road behind them since "
         "day one, and on day five it finally contains something",
         "A grey sedan that changes drivers at fuel stops and a box truck "
         "with the family's leasing sticker peeled off badly",
         "He tells her the way a foreman tells a dispatcher — plate "
         "fragments, spacing, shift pattern — and she realizes she is being "
         "briefed by a professional",
         "'You ran yards.' 'I ran their yards.' 'Then stop apologizing and "
         "start counting.'",
         "First scene in which they are, functionally, two people doing one "
         "job"],
  syn="Reluctant allies armed: his competence stops being a confession and "
      "starts being an asset."),
S(12, "The Unlisted Crossing", "A", 6, "a private cut through a sand "
  "operation; then the ferry road", "realign_betray", "A", "D",
  "the route nobody sold her", "first-deviation",
  "she leaves the manifest and loses the family's eyes",
  ["CE-01", "CE-02"],
  [("A", "B", "trust", 0.08), ("A", "B", "attraction_sexual", 0.06),
   ("B", "A", "trust", 0.08), ("A", "D", "resentment", 0.06)],
  0.66,
  beats=["SET PIECE (Ph2): first deviation - A takes an unlisted crossing "
         "and loses the family's eyes",
         "The cut: a haul road through a sand and gravel operation that "
         "runs private from the county line to the river, gate to gate, "
         "eleven minutes, no cameras and no county",
         "It is one of hers. Nobody sold it to her; she found it in 2019 "
         "with a woman and a child in the back and forty minutes",
         "Adam, watching the gate close behind them: 'How many of these do "
         "you have?' 'Enough.' 'That's not a number, Mira.' First time he "
         "uses her name",
         "Advance: from here the route is hers, and every consequence of "
         "that is also hers"],
  syn="Advance scene: the deviation that arms the whole back half — and the "
      "first time either of them uses a name."),
# ---------------------------------------------------------------- Phase 3
S(13, "Nine Hours", "B", 6, "east across the mitten, US-10 to Clare",
  "probe_test", "B", "A", "the cab", "proximity",
  "forced proximity does its work",
  ["CE-03"],
  [("B", "A", "affection", 0.06), ("B", "A", "attraction_romantic", 0.05),
   ("A", "B", "affection", 0.05)],
  0.58,
  beats=["Nine hours in a cab is a room with no doors and a view that keeps "
         "changing, and there is nothing to do in it but be a person",
         "They discover the boring things: he cannot sleep sitting up; she "
         "cannot eat and drive; both of them hate the radio and neither "
         "will say so first",
         "He asks where she's from. She gives him a distance — twelve "
         "hundred miles from a port to a port — and then, because it is "
         "hour seven, she gives him the port",
         "Constanța. Nineteen. A container ship and then a truck and then "
         "a yard in Chicago, and a debt she did not agree to and has never "
         "stopped paying",
         "He goes very quiet, and she does not understand why for another "
         "four days"],
  syn="Forced_proximity pays inside its window; her passage stated aloud "
      "for the first time, in front of the one man it implicates."),
S(14, "The Yard She Doesn't Stop At", "A", 7, "Bay City approach, US-10 east",
  "deflect_withhold", "A", "D", "an exit not taken", "skipped-yard",
  "the second deviation compounds the first",
  ["CE-01", "CE-02"],
  [("A", "D", "fear", 0.07), ("A", "B", "commitment", 0.06),
   ("B", "A", "commitment", 0.05)],
  0.62, hot={"A-D": 0.58},
  beats=["Yard two is a shuttered marine hardware lot with a leased office "
         "and three men in it who were not on the manifest",
         "She drives past the exit at sixty-two miles an hour and neither "
         "of them says anything for nine minutes",
         "Benny, on the burner: two more men at the Chicago yard, and the "
         "state has begun 'reviewing' his licence, which takes about eleven "
         "days and which nobody in Lansing initiated by themselves",
         "The deviation now has a price with a name and a clock on it"],
  syn="The cost of the deviation lands on the person who cannot drive away "
      "from it."),
S(15, "What She Carries", "B", 8, "a motel lot, Standish; the truck's floor",
  "probe_test", "B", "A", "the compartment", "seen",
  "he finds the evidence of what she is and does not ask",
  ["CE-03"],
  [("B", "A", "respect", 0.08), ("B", "A", "affection", 0.06),
   ("A", "B", "vulnerability", 0.06), ("A", "B", "emotional_safety", 0.05)],
  0.66,
  beats=["Changing a tire at six a.m. he finds it: a false floor behind the "
         "bulkhead, big enough for one adult lying down, with a vent, a "
         "bottle holder, and a reading light somebody installed by hand",
         "The reading light is the detail that takes his legs out. Somebody "
         "built a hiding place and then thought about the dark",
         "He puts the panel back. He says nothing at breakfast, and nothing "
         "at the fuel stop, and nothing all day",
         "She knows he found it. He knows she knows. Neither of them opens "
         "it, and the not-opening is the most intimate exchange either has "
         "had in a decade"],
  syn="Morally-gray heroine armed: he sees exactly what she is and declines "
      "to make her explain it."),
S(16, "Road Boss", "A", 8, "a gravel yard outside Tawas; Traversa's men",
  "demand_threaten", "D", "A", "two men and a clipboard", "the-real-squeeze",
  "the threat arrives in person, in D's language",
  ["CE-02", "CE-01"],
  [("A", "D", "fear", 0.10), ("A", "D", "resentment", 0.09),
   ("A", "C", "fear", 0.08), ("A", "B", "trust", 0.06)],
  0.70, hot={"A-D": 0.70, "C-D": 0.60},
  beats=["Two of Traversa's men are waiting at a yard she did not tell "
         "anyone she was using, which means the family has bought somebody "
         "in her own supply chain",
         "They do not touch her. They give her a photograph of Benny Osei "
         "walking into a licensing office in Chicago, taken that morning",
         "'Gino says you're eleven hours behind the manifest. Gino says "
         "he's a patient man.' The rules of the language: never a threat, "
         "always a forecast",
         "Adam stays in the cab because she told him to, and watches the "
         "whole thing in the mirror, and this is the scene in which he "
         "decides what he is going to do about it"],
  syn="D's apparatus reaches the road; the constraint holds — still no "
      "room shared, still only weather."),
S(17, "The One Who Drove", "B", 9, "the shore road, Au Gres, after dark",
  "reveal_misfire", "B", "A", "eleven years of not asking", "near-touch",
  "he tells the truest thing he has; she nearly reaches",
  ["CE-03"],
  [("B", "A", "vulnerability", 0.08), ("B", "A", "attraction_romantic", 0.07),
   ("A", "B", "affection", 0.08), ("A", "B", "attraction_sexual", 0.07),
   ("A", "B", "emotional_safety", 0.05)],
  0.78,
  beats=["Pulled over on the shore road with the engine off because the "
         "alternator is making a sound she wants to hear properly",
         "He tells it without the absolution move for the first time: the "
         "night in 2019, the load he was told not to open, the sound, the "
         "decision he made to keep driving, the week he spent afterward "
         "and the federal building he walked into on the eighth day",
         "'I'm not telling you so you'll say it's alright. I'm telling you "
         "because you're the only person alive who knows what the back of "
         "that truck is like.' He does not know yet how exactly true that is",
         "Her hand on the door frame and his on the seat back and eleven "
         "inches between them, and neither books it",
         "Advance to Phase 4: the crisis is now interior"],
  syn="Advance scene: B's growth arc turns — accountability without erasure "
      "— and the pair reaches its first real near-touch."),
# ---------------------------------------------------------------- Phase 4
S(18, "Alpena", "A", 10, "the port town; a room above a chandlery",
  "deflect_withhold", "A", "B", "one bed", "layover",
  "the boat is three days out; the room has one bed",
  ["CE-01", "CE-03"],
  [("A", "B", "emotional_safety", 0.05), ("B", "A", "emotional_safety", 0.05)],
  0.42,
  beats=["The unlisted route she has been driving toward: a berth on a "
         "cement carrier out of Alpena, crew papers, three days of water "
         "and no roads at all",
         "The boat is late. Weather at the Soo. Three days become the "
         "layover the whole book has been driving toward",
         "A room above a chandlery that smells of rope and diesel, rented "
         "from a woman who does not ask names and takes cash",
         "ONLY ONE BED, and neither of them mentions it for four hours",
         "She counts the doors and exits of the room on entry — two, and "
         "one is a window over a fire escape — and he watches her do it "
         "and says: 'You always do that.' 'Yes.' 'Me too.'"],
  syn="The false-resolution dip and the only_one_bed trope, both arriving "
      "in the same room."),
S(19, "The Imbalance", "B", 10, "the room above the chandlery, night",
  "negotiate_consent", "B", "A", "the named thing", "boundary",
  "the custody problem is stated out loud and made a rule",
  ["CE-03"],
  [("B", "A", "emotional_safety", 0.07), ("B", "A", "trust", 0.06),
   ("A", "B", "emotional_safety", 0.07), ("A", "B", "respect", 0.06)],
  0.44, consent={"kind": "boundary", "act_class": "C2"},
  beats=["The bed, negotiated at eleven p.m. like a freight problem: she "
         "takes the floor, he objects, she points out she has slept in a "
         "cab for nine days and a floor is an upgrade",
         "Then the real negotiation, because he will not leave it: 'I want "
         "to say a thing out loud so it's said. You can open that door and "
         "I can't. That's not nothing and I'm not going to pretend it is.'",
         "Mira, flatly, because it is the only way she knows how to be "
         "honest: 'You're in my truck because you can't get out of it. "
         "Nothing happens between us while that's true. Not a look I have "
         "to wonder about. Nothing.'",
         "Agreed, both directions, as a standing boundary — logged, in "
         "their own registers, and kept",
         "They sleep six feet apart with a lake wind coming in and both of "
         "them awake for a long time"],
  syn="The taboo requirement performed structurally: the custody imbalance "
      "named on the page and converted into a standing boundary."),
S(20, "The Long Grey Seam", "A", 11, "the breakwater, Alpena, first light",
  "reveal_misfire", "A", "B", "where the channel meets the breakwater",
  "truth-trade",
  "both secrets on the table",
  ["CE-03", "CE-01"],
  [("A", "B", "trust", 0.09), ("A", "B", "vulnerability", 0.08),
   ("A", "B", "resentment", -0.10), ("B", "A", "vulnerability", 0.09),
   ("B", "A", "resentment", -0.10), ("B", "A", "trust", 0.07)],
  0.46, close=["CE-03"],
  beats=["SET PIECE (Ph4): freighter layover — A and B trade the truth "
         "about what the delivery is",
         "Locale signature: the long grey seam where the freighter channel "
         "meets the breakwater, a thousand-foot carrier standing off in "
         "the fog with its deck lights on",
         "She gives him the arithmetic: the return allowance is written for "
         "one. 'They're not paying me to deliver you. They're paying me to "
         "be the last person who saw you.'",
         "He takes it without a flicker, because he has known since the "
         "scale-house man walked the truck, and has been letting her arrive "
         "at it herself",
         "Then his: 'In 2012 I ran the Constanța line out of the Montreal "
         "yard. Nineteen-year-old girl, container to Toronto, truck to "
         "Chicago, priced at eleven thousand dollars against future work.' "
         "He looks at the water. 'I routed you. I'm the one who drove.'",
         "CE-03 closes on the breakwater; neither of them says anything "
         "for a long time, and the fog takes the boat"],
  syn="Secret_B detonates into Secret_A: the man in her custody is the man "
      "who priced her, and both of them find it out on the same rock."),
S(21, "The Door", "A", 11, "the chandlery room; then the bus depot",
  "bargain_trade", "A", "B", "a name and a route", "the-real-exit",
  "she gives him a genuine way out; he declines it",
  ["CE-01", "CE-04"],
  [("A", "B", "affection", 0.09), ("A", "B", "commitment", 0.07),
   ("B", "A", "affection", 0.09), ("B", "A", "commitment", 0.08),
   ("B", "A", "resentment", -0.08)],
  0.48, consent={"kind": "ask", "act_class": "C2"},
  grants=[("A", "B", 2, "private"), ("B", "A", 2, "private")],
  beats=["She does not apologize and she does not forgive him. She does "
         "arithmetic, because it is the only apparatus she has: what he is "
         "worth alive and free, and what she can spend",
         "The offer, itemized: four thousand two hundred dollars, a name "
         "that will hold for three years, a route she has never sold to "
         "anybody and will never use again, and a woman in Thunder Bay who "
         "owes her nothing and will do it anyway",
         "'Twelve hours from now you're a man nobody is looking for. No "
         "strings, no invoice, and I never see you again.' The bus depot "
         "timetable on the table between them",
         "He looks at it for a long time. 'If I disappear, the case dies "
         "and the road stays open and they do it to somebody else next "
         "year.' He pushes it back. 'I'm going to the twenty-second.'",
         "The custody is over. Whatever happens now is chosen, and both of "
         "them know exactly what that changes",
         "So she reopens the scene-19 boundary and asks, in terms, standing "
         "in a rented room with a bus timetable on the table: 'The rule was "
         "for while you couldn't leave. You can leave. Do I have your "
         "permission to want this out loud.' He gives it, and gives her "
         "his, and neither of them performs a single thing tonight"],
  syn="The consent architecture's precondition, dramatized: the exit is "
      "made real, funded, and refused — and only then is a mutual C2 grant "
      "negotiated, which is what makes scene 22 admissible at all."),
S(22, "First", "B", 12, "the chandlery room, evening",
  "release_transform", "A", "B", "her hand on his jaw", "first-kiss",
  "the kiss, her initiative, after the door exists",
  ["CE-01"],
  [("A", "B", "attraction_romantic", 0.09), ("A", "B", "emotional_safety", 0.08),
   ("A", "B", "affection", 0.08), ("B", "A", "attraction_romantic", 0.09),
   ("B", "A", "emotional_safety", 0.07), ("B", "A", "affection", 0.07)],
  0.64, contact={"class": "C2", "setting": "private"},
  beats=["A day of ordinary things: laundry, a alternator belt, a boat "
         "that is still not coming, an argument about the radio finally "
         "conducted out loud and won by neither",
         "The grant from last night stands and neither of them has "
         "mentioned it all day, which is its own kind of noise",
         "'You gave me permission to want it out loud,' she says. 'So: I "
         "want to kiss you.' 'Then that's two of us.'",
         "First_Kiss_Phase 4, honored, her move, her timing, with a real "
         "exit standing open behind him the entire time",
         "TR reluctant_allies_to_lovers -> paying off; advance to Phase 5"],
  syn="Advance scene: the trope pays inside its window and the consent "
      "architecture is satisfied on the page, not asserted."),
# ---------------------------------------------------------------- Phase 5
S(23, "Waiting on Water", "A", 12, "the chandlery room; the harbor office",
  "probe_test", "A", "C", "a boat that isn't coming", "plan-fails",
  "the water route dies; the road is the only road",
  ["CE-01", "CE-02"],
  [("A", "B", "trust", 0.06), ("A", "C", "trust", 0.05),
   ("B", "A", "trust", 0.06)],
  0.58,
  beats=["The carrier's crew berth is gone: the mate who owed her took a "
         "transfer, and the man who replaced him has a cousin in Chicago, "
         "which is the entire reason the family's road business works",
         "Benny, on the burner, in a voice she has not heard from him in "
         "twenty years: the licence review has become a suspension hearing "
         "and two men have started parking outside his house",
         "The water route is dead. Which leaves the road, which is theirs, "
         "which means the border yard on the seventeenth",
         "She lays the whole route out on the bed with a road atlas and a "
         "pen, and for the first time in her life she does it in front of "
         "somebody"],
  syn="The escape route closes; the pair is committed to the ordered route "
      "with eight days on the clock."),
S(24, "Fuel Math", "B", 13, "US-23 south, the shore road",
  "probe_test", "B", "A", "her tic, read correctly", "shared-work",
  "he learns to read her under load",
  ["CE-01"],
  [("B", "A", "affection", 0.08), ("B", "A", "attraction_sexual", 0.06),
   ("A", "B", "attraction_sexual", 0.06), ("A", "B", "emotional_safety", 0.06)],
  0.62,
  beats=["She has started giving him distances when she is frightened, and "
         "he has started answering them, and by day thirteen it is a "
         "language: 'Two hundred and six miles.' 'Okay.' 'Four hours if the "
         "bridge is clear.' 'Okay, Mira.'",
         "He drives four hours so she can sleep, the first time she has "
         "let anyone drive her truck since Benny",
         "She sleeps against the window and wakes with his jacket over her "
         "and the mirrors adjusted back to her settings, which he did on "
         "purpose so she would not have to ask",
         "Acts of service in both directions; neither of them has a word "
         "for it and both of them keep doing it"],
  syn="The love languages find each other in the middle of an escalating "
      "pursuit."),
S(25, "Terms", "A", 14, "a cabin court outside Port Sanilac",
  "negotiate_consent", "A", "B", "spoken clauses", "consent-c3c4",
  "the explicit negotiation before anything further",
  ["CE-01"],
  [("A", "B", "vulnerability", 0.08), ("A", "B", "emotional_safety", 0.08),
   ("A", "B", "attraction_sexual", 0.07), ("B", "A", "vulnerability", 0.08),
   ("B", "A", "emotional_safety", 0.08), ("B", "A", "trust", 0.07)],
  0.66, contact={"class": "C2", "setting": "private"},
  consent={"kind": "ask", "act_class": "C3"},
  grants=[("A", "B", 3, "private"), ("B", "A", 3, "private"),
          ("A", "B", 4, "private"), ("B", "A", 4, "private")],
  beats=["SET PIECE (Ph5): consent negotiation before first C3 contact",
         "Two beds this time, in a cabin court with a lake wind, and the "
         "distance between them is now a decision instead of a rule",
         "She does it as terms because that is her only fluent register, "
         "and he lets her, and then makes her say the unfluent version too",
         "Named on the page, both directions: everything, on her schedule; "
         "one word stops it from either side, any time, no grievance; the "
         "job stays outside the door after dark; and — his clause — 'you "
         "don't route me. If you're going to decide something about my "
         "life, you say it to my face first.'",
         "She agrees to it, and it is the only clause in the book she will "
         "break",
         "Nothing above C2 performed tonight; the agreement is the scene"],
  syn="Mutual C3/C4 grants negotiated explicitly and in character; B's "
      "clause plants the black moment."),
S(26, "Berth", "B", 14, "the cabin court, later",
  "release_transform", "B", "A", "the driver's tan that stops at the wrist",
  "first-night",
  "first intimacy under standing grants",
  ["CE-01"],
  [("A", "B", "attraction_sexual", 0.07), ("A", "B", "vulnerability", 0.07),
   ("A", "B", "affection", 0.08), ("A", "B", "resentment", -0.10),
   ("B", "A", "attraction_sexual", 0.07), ("B", "A", "affection", 0.08),
   ("B", "A", "resentment", -0.10), ("B", "A", "trust", 0.06)],
  0.72, contact={"class": "C4", "setting": "private"},
  beats=["First_Intimacy_Phase 5, honored: the grants from scene 25 govern; "
         "'still yes?' at the door and 'still yes' — reaffirmation, not "
         "renegotiation",
         "Heat 4 rendering: explicit in feeling, precise in consent, "
         "cadence compressed",
         "The inventory neither of them intended: her cargo-strap scars, "
         "his driver's tan that stops at the wrist, the eleven years and "
         "the fourteen years lying in the same bed",
         "Words of affirmation from a man who has only ever been told what "
         "he was; acts of service from a woman who has never been asked "
         "what she wanted",
         "And the thing neither says: that in three days they arrive at a "
         "yard on the border with a schedule in it"],
  syn="The intimacy payoff under explicit standing grants, with the clock "
      "audible under it."),
S(27, "Eleven Names, Out Loud", "A", 15, "the cabin court, before dawn",
  "reveal_misfire", "A", "B", "the coffee tin", "the-list-spoken",
  "she says the list aloud for the first time",
  ["CE-03", "CE-02"],
  [("A", "B", "vulnerability", 0.09), ("A", "B", "trust", 0.08),
   ("B", "A", "respect", 0.09), ("B", "A", "affection", 0.06)],
  0.76,
  beats=["Four a.m., the hour she has been awake at her whole adult life, "
         "and for once somebody is awake in it with her",
         "She tells him the eleven. Not the names — the *shape*: a woman "
         "and a child in 2019, two brothers in 2021, a man in 2022 who "
         "cried for four hours in the false floor and then said thank you "
         "in a language she does not speak",
         "'Eleven people the family sent me to move and never meant to see "
         "again. Eleven times I made the delivery somewhere else.'",
         "Adam, understanding all of it at once: 'That's what the false "
         "floor is. That's what the reading light is.'",
         "'If Gino ever finds that tin, eleven people who have jobs and "
         "kids and mortgages get found the same week. That's what I'm "
         "carrying. That's what's actually in the truck.'"],
  syn="Secret_A given voluntarily, in full, to the one person who can "
      "price it — the deepest exposure either has performed."),
S(28, "The Order", "A", 15, "a turnout north of Lexington; Traversa's call",
  "demand_threaten", "D", "A", "delivery terms, said plainly",
  "order-explicit",
  "the disposal order is stated; the debt comes due unpayable",
  ["CE-01", "CE-02"],
  [("A", "D", "fear", 0.10), ("A", "D", "resentment", 0.10),
   ("A", "B", "commitment", 0.08), ("B", "A", "commitment", 0.08)],
  0.84, hot={"A-D": 0.78}, misfire=["CE-01"],
  beats=["Traversa says it out loud for the first time in eleven years, "
         "because the man is finally close enough to the water to be "
         "described: 'You bring him into the yard on the seventeenth and "
         "you drive out on the eighteenth and the passage is finished.'",
         "'Finished how, Gino.' 'Finished, Mira.'",
         "And then the part that closes the box: 'Osei's hearing is the "
         "nineteenth. Funny how the calendar works.'",
         "CE-01 misfires — the debt has come due in a currency she cannot "
         "pay and will not default on; it stays open and gets heavier",
         "Adam, who has heard the whole call on a speaker she did not turn "
         "off: 'Okay.' 'That's all you're going to say?' 'You heard it too. "
         "Now we both did.'",
         "Advance to Phase 6 with eight days spent and two remaining"],
  syn="Advance scene: the order made explicit, the debt misfired, and the "
      "clock reduced to a date and a yard."),
# ---------------------------------------------------------------- Phase 6
S(29, "The Nineteenth", "A", 16, "a payphone outside a hardware store",
  "reveal_misfire", "C", "A", "a licence hearing", "benny",
  "the instrument of the threat is executed",
  ["CE-02", "CE-01"],
  [("A", "C", "trust", 0.06), ("A", "D", "resentment", 0.09),
   ("A", "B", "trust", 0.06)],
  0.78, hot={"C-D": 0.68},
  beats=["Benny's voice, and behind it a room with other people's "
         "conversations in it: they took the licence file, the hearing is "
         "the nineteenth, and a man came to the shed and sat in the chair "
         "she has sat in since 2015",
         "'He asked me what's under the floor, Mira.'",
         "Everything she has built runs on a piece of paper with another "
         "man's name on it and now the paper is in a room in Springfield "
         "and the man is in a chair in her shed",
         "'Burn the tin, Benny.' A pause. 'No,' says Benny Osei, fifty-eight "
         "years old, who has never once refused her. 'You'll want it. Not "
         "for them. For you.'"],
  syn="CE-02 executes; the confidant refuses the safe instruction and "
      "plants the ending."),
S(30, "The Number", "B", 16, "the shore road south, Lexington to Lakeport",
  "bargain_trade", "B", "A", "ten digits on a fuel receipt", "the-channel",
  "he gives her the only asset he has",
  ["CE-02", "CE-04"],
  [("B", "A", "trust", 0.09), ("B", "A", "commitment", 0.09),
   ("A", "B", "trust", 0.07), ("A", "B", "vulnerability", 0.06)],
  0.76,
  beats=["He writes ten digits on the back of a fuel receipt: a duty line "
         "at the Northern District, and under it a name — the AUSA who "
         "built the Moretti prosecution off a bookkeeper's ledger last year",
         "'This is the only thing I own. If it goes wrong at the yard, that "
         "number is what's left of me.'",
         "What he does not say and she hears anyway: *and it can be what's "
         "left of you, if you use it*",
         "She puts the receipt in the tin's place in her coat, over her "
         "ribs, where the list would be if she carried the list",
         "Two hundred and six miles to the border yard and neither of them "
         "proposes a plan, because they have both understood for a day "
         "that there is only one and it costs her everything"],
  syn="The channel handed over; the shape of the ending exists now and "
      "neither will say it."),
S(31, "The Twelfth Name", "A", 17, "a lay-by above the water, dawn",
  "probe_test", "A", "B", "her own name on her own list",
  "the-realization",
  "she understands what she has been leaving off the page",
  ["CE-01", "CE-03"],
  [("A", "B", "emotional_safety", 0.07), ("A", "B", "affection", 0.07),
   ("B", "A", "affection", 0.07)],
  0.80,
  beats=["She writes the eleven out from memory on the back of the atlas, "
         "in order, with dates, the way she writes everything",
         "And stops, holding the pen, at the bottom of the column, because "
         "the arithmetic will not close",
         "2012. Constanța. Nineteen. Eleven thousand dollars against future "
         "work. A container, a truck, a yard, a debt she never agreed to",
         "'There are twelve,' she says. Adam, not asking what she means, "
         "because he has known since the breakwater: 'Yes.'",
         "The whole architecture of her life re-reads in one motion: she "
         "has spent fourteen years believing she was the carrier, and she "
         "has been on the manifest the entire time",
         "Growth arc turns: a debt for something that was done to you is "
         "not a debt"],
  syn="The keystone: Goal_Internal_A named — to stop being something that "
      "is owed — and the instrument of it discovered in her own handwriting."),
S(32, "Port Huron", "B", 17, "the border yard, seen from the road",
  "deflect_withhold", "B", "A", "the seam", "arrival",
  "the destination made physical",
  ["CE-01", "CE-02"],
  [("B", "A", "fear", 0.07), ("A", "B", "fear", 0.06),
   ("A", "B", "commitment", 0.06)],
  0.86,
  beats=["The yard: eleven acres of gravel and containers under the bridge "
         "approach, a scale house, a slip, and the long grey seam where "
         "the freighter channel meets the breakwater on the other side of "
         "the fence",
         "Water on two sides and one gate. Adam counts it out loud, "
         "professionally, the way he counted doors on his first day in a "
         "safe house: 'One in. Everything else is the river.'",
         "They sit in a diner across the highway for two hours and do not "
         "eat, and she draws the yard on a napkin from memory of a place "
         "she has never been, because she has been in forty of them",
         "'Say the thing you're not saying,' he tells her. She doesn't"],
  syn="The climax's geography established, and the first term of the "
      "scene-25 clause broken by omission."),
S(33, "No Play", "A", 17, "the diner lot; three phones",
  "demand_threaten", "D", "A", "everything closing at once", "boxed",
  "every route closes",
  ["CE-01", "CE-02"],
  [("A", "D", "fear", 0.10), ("A", "B", "fear", 0.08),
   ("A", "B", "commitment", 0.07)],
  0.90, hot={"A-D": 0.82}, misfire=["CE-02"],
  beats=["Three phone calls in forty minutes",
         "Benny: two men in the shed, the hearing moved up, and he is not "
         "answering the third time she calls",
         "Traversa's second: the gate opens at eight, and Gino would "
         "appreciate her being punctual, he has always admired that about her",
         "A number she does not recognize, which she does not answer, and "
         "which is not Adam's federal duty line",
         "The arithmetic, run once and refusing to change: if she runs, "
         "Benny loses the licence and probably more, the eleven get audited "
         "into the open, and Adam gets found in a week by people with more "
         "yards than she has routes",
         "CE-02 misfires: the threat is executing and there is nothing left "
         "to trade for it"],
  syn="The pool of options empties; the black moment is arithmetic, not "
      "cowardice."),
S(34, "Delivered", "B", 17, "the border yard, eight p.m.",
  "realign_betray", "A", "D", "the gate closing behind the truck",
  "all-is-lost",
  "she carries out the order",
  ["CE-01", "CE-02"],
  [("B", "A", "trust", -0.15), ("B", "A", "resentment", 0.15),
   ("B", "A", "fear", 0.10), ("A", "B", "vulnerability", 0.07),
   ("A", "D", "resentment", 0.08)],
  0.94, hot={"A-D": 0.88},
  beats=["ALL IS LOST (delivered_to_the_yard): she drives in at eight and "
         "the gate rolls shut behind the truck",
         "First room shared by A and D in the whole book (Phase 6; the "
         "constraint expires exactly here): a scale house with a space "
         "heater, Gino Traversa inside a building with her for the first "
         "time in eleven years, which is how she knows how this is meant "
         "to end",
         "Adam is walked out of the cab by two men. He does not fight. He "
         "looks back once — not at the men, at her — and she does not "
         "look up from the manifest she is signing",
         "'You were carried,' Traversa says, taking the pen back. 'Now "
         "you've carried. That's the whole business, Mira. Nobody gets to "
         "be the only one who was helped.'",
         "Breakup beat (orders_obeyed): she signs, she takes the yard "
         "receipt, and she drives out through the gate alone",
         "Fracture: her flaw completing itself — she routed him instead of "
         "knowing him, exactly as she has done to every person she ever "
         "saved"],
  syn="The black moment played straight: no trick, no secret plan yet. She "
      "obeys, and the phase fractures into Reversal."),
# ---------------------------------------------------------------- Phase 7
S(35, "Two Miles", "A", 17, "the shoulder of the bridge approach, 8:20 p.m.",
  "release_transform", "A", "B", "the ten digits", "the-turn",
  "she stops the truck and stops being a carrier",
  ["CE-01", "CE-04"],
  [("A", "B", "commitment", 0.12), ("A", "B", "affection", 0.08)],
  0.74,
  beats=["Two miles from the gate she pulls onto the shoulder under the "
         "bridge approach with the engine running and the receipt in her "
         "hand",
         "The arithmetic she has run her whole life: what it costs, who "
         "pays, what arrives. It comes out the same as it always has and "
         "for the first time in fourteen years she refuses the answer",
         "'I don't lose freight,' she says, out loud, to nobody, in an "
         "empty cab — and hears what she has actually been saying since "
         "she was nineteen, which is that people are not freight and she "
         "has been surviving by pretending otherwise",
         "She dials the ten digits at 8:31 p.m.",
         "'My name is Mira Dalca. I own a yard on Torrence Avenue in "
         "Chicago. I want to report a homicide that is happening right "
         "now, and I want to tell you who I am, and I am going to start "
         "in 2012.'"],
  syn="Reversal: the desire inversion inverts — the router becomes the "
      "witness, and gives her own name first."),
S(36, "What She Spends", "A", 17, "the shoulder; the call, continued",
  "release_transform", "A", "D", "the twelfth name", "the-trade",
  "she pays with herself, not with the eleven",
  ["CE-01", "CE-02"],
  [("A", "B", "trust", 0.08), ("A", "C", "moral_repair", 0.10)],
  0.70,
  beats=["Twenty-two minutes on a shoulder with the flashers on, talking to "
         "a duty AUSA who has been waiting eleven months for somebody "
         "inside the transport arm to pick up a telephone",
         "What they want: the routes, the yards, the names of everyone she "
         "has moved. What that would cost: eleven people who have jobs and "
         "children and a decade of quiet",
         "What she gives instead: her own passage in 2012, priced and "
         "documented; eleven years of Traversa's manifests, which are all "
         "in her yard and all in her hand; the border yard, tonight, with "
         "a federal witness inside it",
         "'I'm not giving you the people. I'm giving you the roads and I'm "
         "giving you me. If that's not enough, hang up and I'll go back in "
         "alone and you can read about it.'",
         "It is enough. It is forty minutes from enough — Port Huron is "
         "not Chicago and nothing federal moves at eight-fifty at night",
         "'Forty minutes,' the voice says. 'Can you give us forty minutes?'"],
  syn="Save-the-cat inverted and paid: she spends her own cover, and refuses "
      "to spend anyone else's."),
S(37, "Back Through the Gate", "A", 17, "the border yard, 8:56 p.m.",
  "bargain_trade", "A", "D", "an empty cab, driven in", "the-return",
  "she drives back in with nothing but time to sell",
  ["CE-01", "CE-02"],
  [("A", "D", "dominance", 0.10), ("A", "D", "fear", -0.06),
   ("A", "B", "commitment", 0.08)],
  0.80, hot={"A-D": 0.85},
  beats=["She takes the gate at eight fifty-six with the headlights on and "
         "the window down and both hands where they can be seen, which is "
         "how you enter a yard you are not welcome in",
         "The story she sells at the scale house: the manifest is wrong. "
         "The receipt Traversa signed does not discharge the debt because "
         "the passage was priced against future work and the arithmetic "
         "has eleven years of interest in it that nobody has ever run",
         "It is the most Traversa-shaped argument available and it is also "
         "true, and she has forty minutes of it, itemized, in a coat "
         "pocket, because she prepared it in a diner",
         "Adam, in a container office across the yard, hearing her voice "
         "through a wall and understanding — with a completeness that will "
         "take him a year to describe — what she is doing with it",
         "The clock: 8:56. The federal team is at 9:36"],
  syn="The climax's mechanism: not a rescue, a delay, bought in the only "
      "currency she has ever been fluent in."),
S(38, "The Handover", "A", 17, "the scale house and the slip, 9:00-9:40 p.m.",
  "release_transform", "A", "D", "the manifest, read aloud", "handover",
  "the handover resolves on the page",
  ["CE-01", "CE-02"],
  [("A", "D", "dominance", 0.10), ("A", "D", "fear", -0.08),
   ("A", "B", "commitment", 0.10), ("B", "A", "respect", 0.08),
   ("B", "A", "fear", -0.10)],
  0.78, close=["CE-02"],
  beats=["SET PIECE (Ph7): the handover at the border yard resolves on the "
         "page",
         "Forty minutes of a woman doing arithmetic out loud to a road boss "
         "who has never once been made to sit and listen to a number",
         "She reads eleven years of his own manifests back at him from "
         "memory: the loads, the allowances, the four hundred and six "
         "thousand dollars of freight he has moved off the family's books "
         "since 2019, which she has been reconciling for him without "
         "comment since the year Sal Moretti went to trial",
         "Traversa understands at minute nineteen that he is not being "
         "argued with, he is being *held*, and by then there are lights on "
         "the bridge approach",
         "The tell that ends it: Gino Traversa, for the first time in "
         "eleven years, walks outside. Onto gravel. Where the federal "
         "team, coming through a gate designed to admit one vehicle at a "
         "time, can see him",
         "CE-02 closes; nobody in that yard has to be brave, which is the "
         "point, and which is what she would say afterward every time "
         "anyone called it brave"],
  syn="Climax mode handover_subverted: the delivery completes exactly as "
      "ordered and the thing delivered turns out to be the road boss."),
S(39, "The Seam", "B", 18, "the breakwater at Port Huron, first light",
  "release_transform", "B", "A", "water on two sides", "withdrawal",
  "he is alive, and he withdraws",
  ["CE-01"],
  [("B", "A", "trust", -0.10), ("B", "A", "emotional_safety", -0.12),
   ("A", "B", "vulnerability", 0.08), ("A", "B", "resentment", -0.10)],
  0.70, close=["CE-01"],
  consent={"kind": "withdraw", "act_class": "C2"},
  withdraw=[("A", "B", 2), ("B", "A", 2)],
  beats=["Six a.m. on the breakwater with the channel running grey and a "
         "thousand-foot carrier coming down under the bridge, and both of "
         "them alive, which neither has finished believing",
         "Motif recontext (two-phase gap, changed pressure): the long grey "
         "seam again, and the truth being traded again, and this time it is "
         "the harder one",
         "'You signed the manifest.' 'Yes.' 'You looked at the paper "
         "instead of at me, and you drove out.' 'Yes.' 'Say the rest.' 'I "
         "routed you. That's what I do to people I'm trying to keep alive. "
         "It's what I did to eleven other people and none of them ever got "
         "to object.'",
         "'You broke the only clause I asked for,' Adam says. 'You decided "
         "something about my life and you didn't say it to my face.'",
         "'Withdrawn.' All standing grants void at the moment the beat "
         "lands (4.5). He says it while holding her coat around her "
         "shoulders, which is the part she will think about for weeks",
         "CE-01 closes: the debt is discharged — voided rather than paid — "
         "and the phase turns to Resolution"],
  syn="Advance scene: rescue does not undo delivery. Consent withdrawn, in "
      "his register, for the clause she actually broke."),
# ---------------------------------------------------------------- Phase 8
S(40, "Day Nineteen", "B", 19, "the Dirksen building, Chicago",
  "release_transform", "B", "A", "his own name on the record",
  "testimony",
  "the promise pays verbatim",
  ["CE-04"],
  [("B", "A", "respect", 0.08), ("A", "B", "affection", 0.07),
   ("B", "A", "affection", 0.05), ("B", "A", "fear", -0.12),
   ("B", "A", "resentment", -0.10)],
  0.38, close=["CE-04"],
  beats=["Nineteen days after two men took him out of a rented house in "
         "Berwyn, Adam Marek walks into a federal courtroom on his own "
         "feet at 9:40 in the morning",
         "'State your name for the record.' He says it. It takes him two "
         "tries, and the second one is steady, and it is the first thing "
         "he has ever put into the world that was not freight",
         "The promise paid in its exact wording (L7): '" + PROMISE_CE04 +
         "' — she said it in a scale-house yard in Portage on day two and "
         "he has been carrying it since",
         "Four hours of the transport arm's routes, in the voice of the "
         "man who drove them, with the woman who ran the last one sitting "
         "in the second row where he can see her without turning around",
         "CE-04 closes: delivered, on the day she said, on his own feet, "
         "with his own name on him"],
  syn="Finale part one — testimony_and_reckoning; the promise honored "
      "verbatim at payoff."),
S(41, "The Twelfth Witness", "A", 19, "an interview room, same building",
  "release_transform", "A", "B", "2012, priced at eleven thousand",
  "her-record",
  "she puts her own passage on the record",
  ["CE-01"],
  [("A", "B", "emotional_safety", 0.08), ("A", "B", "trust", 0.06),
   ("A", "C", "moral_repair", 0.10)],
  0.36,
  beats=["Her own statement, taken by a woman named Raman who built the "
         "Moretti prosecution off a bookkeeper's ledger a year ago and who "
         "asks her, at the end, the only question that matters: 'Why not "
         "the other eleven?'",
         "'Because they didn't agree to be moved and they didn't agree to "
         "be evidence, and I've done the first one to people. I'm not "
         "doing the second one.'",
         "The immunity is narrow and hard-won and Okafor argues it for "
         "three hours; the eleven are never named in any document",
         "And the finding that costs the government nothing and costs her "
         "everything to hear said out loud in a beige room: a passage "
         "priced against a nineteen-year-old's future work is not a debt. "
         "It never was one. There has been nothing to discharge since 2012",
         "She sits with that for a while, in a chair, in a building, with "
         "her hands flat on a table"],
  syn="Growth arc lands: self_worth_reclaimed, on the record, in her own "
      "name — the debt not paid but voided."),
S(42, "Wisniewski Cartage", "A", 19, "the yard, Torrence Avenue, evening",
  "release_transform", "C", "A", "a licence, restored", "repair",
  "the yard, the licence, the tin",
  ["CE-04"],
  [("A", "C", "moral_repair", 0.15), ("A", "C", "trust", 0.09),
   ("A", "B", "affection", 0.05)],
  0.30,
  beats=["Benny Osei in the shed with the chair turned the wrong way "
         "around and a licence suspension vacated on a Thursday by a "
         "hearing officer who had read the morning's news",
         "'Two men sat in my chair,' he says. 'I want you to know I gave "
         "them nothing, and I want you to know I would have.' 'I know. "
         "That's what a debt is for.'",
         "The tin comes up out of the floor and does not go into any "
         "envelope: eleven names, read aloud once between the two of them "
         "in an empty shed, and then burned in the same bin they burn the "
         "oil rags in",
         "What replaces it: a licence application in her own name, filled "
         "out in her own hand, which she has been legally able to file for "
         "six years and has never once believed she was allowed to",
         "Benny signs as her sponsor and does not make a thing of it"],
  syn="Moral repair with the confidant, and the practical instrument of "
      "her freedom filed in her own name."),
S(43, "Ask Me", "B", 19, "the yard gate, after dark",
  "negotiate_consent", "B", "A", "a man arriving at a gate",
  "consent-regrant",
  "he re-grants, on his own initiative, as a free man",
  ["CE-04"],
  [("B", "A", "emotional_safety", 0.10), ("B", "A", "trust", 0.09),
   ("B", "A", "affection", 0.09), ("B", "A", "fear", -0.15),
   ("A", "B", "emotional_safety", 0.09),
   ("A", "B", "trust", 0.08), ("A", "B", "affection", 0.08),
   ("A", "B", "fear", -0.10)],
  0.28, consent={"kind": "offer", "act_class": "C2"},
  grants=[("A", "B", 2, "any"), ("B", "A", 2, "any")],
  beats=["He comes to the gate on foot, at night, from a bus, which is the "
         "entire argument: nobody drove him, nobody delivered him, and he "
         "arrived",
         "'I withdrew it on a breakwater when I was a man who'd been in "
         "somebody's custody for nineteen days. That was the right call "
         "then. I've been a free man for eleven hours and I'd like to say "
         "it again from here.'",
         "The re-grant, his initiative, his words, scope widened: "
         "'Anywhere. In front of anybody. I've spent my whole life being "
         "moved quietly.'",
         "Her terms in return, and she makes herself say the unfluent "
         "version: 'I don't want to route you. I want to know you. I'm "
         "going to be bad at it for about a year.'",
         "Nothing performed at the gate; the reopening of the account is "
         "the scene",
         "TR morally_gray_heroine and secret_debt both retire here"],
  syn="Consent re-established on the page, by the party who withdrew it, "
      "under the only conditions that make it meaningful."),
S(44, "Safe Passage", "A", 19, "the yard office, late",
  "release_transform", "A", "B", "the sign, and what she puts under it",
  "hea",
  "the title recontextualized; the HEA lands",
  ["CE-04"],
  [("A", "B", "commitment", 0.12), ("A", "B", "attraction_romantic", 0.09),
   ("B", "A", "commitment", 0.12), ("B", "A", "attraction_romantic", 0.08),
   ("B", "A", "fear", -0.12), ("B", "A", "resentment", -0.10)],
  0.25, contact={"class": "C2", "setting": "private"},
  beats=["The office at eleven at night with the fog coming off the "
         "Calumet and the sodium lights doing what they have done every "
         "night since 1961",
         "The sign will keep saying WISNIEWSKI CARTAGE, because she has "
         "grown fond of a name that belonged to a man who is not owed "
         "anything by anybody. Under it, a second line, painted by hand: "
         "and her own name, small, in the corner where the licence number "
         "goes",
         "Adam, who has been offered a dispatcher's job by a woman who "
         "does not know how to offer anything except as a delivery term: "
         "'Six a.m. Wednesday. Bring a coat you can sleep in.'",
         "'Is that the job or the other thing?' 'It's both. I told you I'd "
         "be bad at this.'",
         "The kiss under the standing 'anywhere' grant, in her own yard, "
         "under her own light, with nobody's manifest on either of them",
         "HEA: a yard, a licence, a road that is only a road"],
  syn="Title recontext: safe passage is not a route out — it is arriving "
      "somewhere and being allowed to stay."),
S(45, "Epilogue: Open Water", "A", 0, "the yard, October", "release_transform",
  "A", "B", "an envelope with no return address", "epilogue",
  "five months on; the books are clean",
  [],
  [("A", "B", "commitment", 0.05), ("B", "A", "commitment", 0.05)],
  0.18, contact={"class": "C2", "setting": "private"},
  beats=["October, outside the story clock (Epilogue_Included): the fog "
         "comes earlier now and the yard runs eleven trucks, all of them "
         "legal, all of them boring",
         "Traversa's trial is scheduled for spring; Mira will testify in "
         "it under her own name and has stopped rehearsing",
         "Adam dispatches Tuesdays through Saturdays and is, to the "
         "documented irritation of every driver on the board, extremely "
         "good at it",
         "An envelope arrives with no return address and a Thunder Bay "
         "postmark: a photograph of a girl in a graduation gown, no note, "
         "no names — the only kind of receipt the eleven will ever send, "
         "and the only one she will ever keep",
         "Last entry: a manifest for the morning, in her own hand, in her "
         "own name, with a licence number in the corner. Two drivers. One "
         "load. Nothing owed."],
  syn="The HEA audited one season on: everyone arriving, nobody carried, "
      "the last document of the book a legal manifest with her name on it."),
]

SCENE = {s["scene"]: s for s in SCENES}

CHAPTERS = [
    (1, "Wisniewski Cartage", [1, 2, 3]),
    (2, "Terms of Delivery", [4, 5, 6]),
    (3, "The Way They Count", [7, 8]),
    (4, "The Coffee Tin", [9, 10, 11]),
    (5, "The Unlisted Crossing", [12, 13]),
    (6, "What She Carries", [14, 15, 16]),
    (7, "The One Who Drove", [17, 18]),
    (8, "The Imbalance", [19, 20]),
    (9, "The Door", [21, 22]),
    (10, "Waiting on Water", [23, 24, 25]),
    (11, "Berth", [26, 27, 28]),
    (12, "The Twelfth Name", [29, 30, 31]),
    (13, "Delivered", [32, 33, 34]),
    (14, "Two Miles", [35, 36, 37]),
    (15, "The Handover", [38, 39]),
    (16, "Day Nineteen", [40, 41, 42]),
    (17, "Safe Passage", [43, 44]),
    (None, "Epilogue: Open Water", [45]),
]
