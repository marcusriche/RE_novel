"""Authored scene schedule for Seed 01KYDG7NWVMNN9C7DTKZ76F54Q — "Clean Exit".

This is the editorial layer of the offline binding configuration
(`offline-agent-v1`, see binding/offline_client.py): a 45-scene rendering of
the 90-scene Mafia/Dark reference allocation (operator override, main.py
--scenes discipline), phase blocks scaled proportionally from the Arc
Profile E = [6,8,10,10,10,12,12,10,12] -> [3,4,5,5,5,6,6,5,6].

Every mandatory set piece lands in its seeded phase; First_Kiss_Phase = 5 and
First_Intimacy_Phase = 6 are honored through the consent architecture (grants
negotiated on-page one scene before any covered contact, since grants realize
at extraction when a scene ships); CE lifecycle events (close / misfire) are
scheduled against their seeded deadlines.

Cast (engine node ids are the seed's own names A/B/C/D):
  A = Elena Moretti, 29 - the family's bookkeeper
  B = Cole Brennan, 36  - federal investigator, organized-crime task force
  C = Lucia Ferro       - chef, Elena's confidant; owes the family a passage debt
  D = Nico Gravano      - family enforcer
  (off-node: Salvatore "Sal" Moretti, family head; Danny Moretti, Elena's
   brother, in pretrial custody for the whole clock)

Story clock: 31 days anchored 2026-02-02 (scene days below); the epilogue
(scene 45) sits outside the clock per Epilogue_Included.
"""

# Phase blocks: phase -> (first_scene, last_scene). Advance fires on the last
# scene of each block; scenes 34 and 39 advance on a logged constraint
# fracture / desire inversion (the 6.3 initiator main.py leaves to the caller).
PHASE_BLOCKS = {
    0: (1, 3), 1: (4, 7), 2: (8, 12), 3: (13, 17), 4: (18, 22),
    5: (23, 28), 6: (29, 34), 7: (35, 39), 8: (40, 45),
}
ADVANCE_SCENES = {3, 7, 12, 17, 22, 28, 34, 39}
FRACTURE_SCENES = {34, 39}   # warrant executed / reversal complete

DISPLAY = {"A": "Elena Moretti", "B": "Cole Brennan",
           "C": "Lucia Ferro", "D": "Nico Gravano"}

PROMISE_CE04 = ("You walk out of there owing nobody. I keep the books - "
                "I know exactly what's owed, and it isn't you.")


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
S(1, "The Weight of Ink", "A", 1, "La Bilancia, back office, night",
  "deflect_withhold", "A", "C", "green banker's lamp", "quiet-close",
  "hold the secret; establish the exit",
  ["CE-01", "CE-04"],
  [("A", "B", "fear", 0.06), ("A", "B", "resentment", 0.05)],
  0.22,
  beats=["Night close-out under the banker's lamp; the till is $60 short and "
         "Elena covers it from her own purse for Marco the busboy",
         "Records subpoena cover letter arrives - signed C. BRENNAN; she "
         "reads the name twice",
         "Danny's arraignment date circled on the wall calendar",
         "Lucia asks about the Amtrak timetable she found; Elena answers "
         "with a smaller question",
         "The ledger goes back into the floor safe; two turns of the dial"],
  syn="Establish Elena, the office, the ledger, the exit plan, and the name "
      "of the man coming for the books."),
S(2, "Case File", "B", 2, "Federal building, task-force room",
  "probe_test", "B", "A", "her handwriting", "file-study",
  "learn the bookkeeper before the interview",
  ["CE-01"],
  [("B", "A", "respect", 0.08), ("B", "A", "attraction_romantic", 0.04)],
  0.27,
  beats=["The Moretti file he requested himself; warrant active since day one",
         "Front-business filings: the only clean handwriting in a dirty "
         "operation - coded, disciplined, almost beautiful",
         "His dead witness and the partner who sold the last case, in one "
         "framed commendation he keeps face-down",
         "He schedules the on-the-record interview at the restaurant"],
  syn="Cole from inside the case; the ledger is already the axis of his "
      "investigation (Secret_B live from scene 2)."),
S(3, "On the Record", "A", 3, "La Bilancia, front of house, afternoon",
  "probe_test", "B", "A", "recorder on the tablecloth", "interview",
  "first contact under oath of tape",
  ["CE-01"],
  [("A", "B", "fear", 0.08), ("A", "B", "attraction_sexual", 0.07),
   ("B", "A", "attraction_sexual", 0.08), ("B", "A", "respect", 0.05)],
  0.42,
  beats=["SET PIECE (Ph0): on-the-record interview at a set table",
         "He cites the regulation instead of the reason; she answers "
         "dangerous questions with smaller questions",
         "He watches her hands; she never once touches the recorder",
         "She names his dead witness in one flat sentence; the silence held "
         "one beat past comfort",
         "Charge neither of them logs anywhere"],
  syn="The mandated meet-cute: adversaries, on the record, and the wanting "
      "already illegal in both directions."),
# ---------------------------------------------------------------- Phase 1
S(4, "Paper Cuts", "B", 4, "Fulton Market / canvass", "probe_test", "B", "C",
  "receipts", "canvass",
  "test the perimeter; the books deflect him everywhere",
  ["CE-01"],
  [("B", "A", "trust", -0.05), ("B", "A", "respect", 0.05)],
  0.32,
  beats=["Cole canvasses suppliers; every invoice foots perfectly",
         "Lucia gives him nothing in two languages",
         "He starts admiring the discipline of the person deflecting him - "
         "and trusting her less"],
  syn="The case as courtship by other means; the perfect books are her "
      "fingerprints."),
S(5, "A Visit from the Family", "A", 5, "Back office, two espressos",
  "demand_threaten", "D", "A", "two espressos", "veiled-threat",
  "the family's first squeeze",
  ["CE-02"],
  [("A", "B", "trust", 0.04), ("A", "D", "fear", 0.10)],
  0.38, hot={"A-D": 0.50},
  beats=["Nico brings Sal's regards and two espressos; Lucia stays in the "
         "doorway (never alone with him - she knows the arithmetic)",
         "The message: the feds came; you were wonderful; stay wonderful",
         "Danny's name set gently on the table like a weight",
         "That night she rereads Brennan's card instead of burning it"],
  syn="CE-02 armed in person; the card she keeps is the first crack."),
S(6, "Visiting Hours", "A", 6, "MCC Chicago, visitation", "probe_test",
  "A", "B", "glass between", "visit-and-call",
  "the promise renewed; a test call placed",
  ["CE-04", "CE-01"],
  [("A", "B", "trust", 0.05), ("A", "B", "attraction_romantic", 0.05),
   ("B", "A", "attraction_romantic", 0.05)],
  0.35,
  beats=["Danny through glass: thinner, joking, scared; says trust no one",
         "The promise, verbatim, again: '" + PROMISE_CE04 + "' (L7)",
         "From the steps she calls Brennan's cell from a payphone: one "
         "question about pretrial protective status; hangs up on his answer",
         "He doesn't log the call. She knows he won't. Neither examines why"],
  syn="CE-04 quoted for the ledger; the first off-record thread between them."),
S(7, "Courthouse Steps", "B", 7, "Dirksen courthouse, after Danny's hearing",
  "probe_test", "B", "A", "his card, second time", "collision",
  "second offer, second refusal, first heat",
  ["CE-01", "CE-04"],
  [("A", "B", "attraction_sexual", 0.08), ("A", "B", "fear", -0.05),
   ("B", "A", "attraction_sexual", 0.08), ("B", "A", "attraction_romantic", 0.06)],
  0.52,
  beats=["Continuance for Danny; the family's lawyer steers Elena out",
         "Cole peels off the escort with two lines of statute",
         "Offer: 'Call me before it gets worse.' Counter: 'Worse for whom?'",
         "The card changes hands and their fingers don't touch on purpose",
         "Phase turns: complication is now personal"],
  syn="Advance scene: the adversaries have a private channel neither will "
      "name."),
# ---------------------------------------------------------------- Phase 2
S(8, "Quiet Corrections", "A", 8, "Back office", "deflect_withhold", "A", "D",
  "red ink", "stall",
  "refuse the marked money without saying no",
  ["CE-01", "CE-02"],
  [("A", "B", "trust", 0.03), ("A", "D", "resentment", 0.08)],
  0.42,
  beats=["An envelope of cash to wash through catering invoices; serial "
         "bands too crisp, sequence too new - it smells like bait",
         "She stalls it in a drawer with a lie about quarterlies",
         "Lucia: 'Nico counts your lights from the street.' - 'Then I'll "
         "leave them on.'"],
  syn="She recognizes the marked payment for what it is; stalling it is the "
      "first act of quiet war."),
S(9, "Off Channel", "B", 9, "His apartment, 2 a.m.", "reveal_misfire",
  "B", "A", "phone at 2 a.m.", "line-crossing",
  "he warns her before the system does",
  ["CE-02"],
  [("B", "A", "attraction_romantic", 0.07), ("B", "A", "trust", 0.05),
   ("A", "B", "trust", 0.08), ("A", "B", "fear", -0.05)],
  0.50,
  beats=["SET PIECE (Ph2): word reaches the task force - Danny Moretti "
         "'slipped in a stairwell': two cracked ribs, a message in bone "
         "(Nico's staging)",
         "Cole calls her before the official notification will - a "
         "violation he commits with the regulation number still in his mouth",
         "Her silence on the line; then: 'Which stairwell has cameras?' - "
         "the bookkeeper auditing the lie",
         "First crack in his procedural armour, on the record of no one"],
  syn="The staged threat lands; his warning is a felony-shaped kindness."),
S(10, "Ward Rules", "A", 9, "County hospital custody ward",
  "demand_threaten", "D", "A", "visitor badge", "explicit-threat",
  "the threat says its own name",
  ["CE-02"],
  [("A", "D", "fear", 0.10), ("A", "B", "trust", 0.04),
   ("A", "B", "vulnerability", 0.04)],
  0.55, hot={"A-D": 0.60},
  beats=["Danny sedated behind custody glass; deputy at the door, Lucia at "
         "her elbow (witnesses, always witnesses)",
         "Nico, softly, over vending-machine coffee: stairwells are "
         "slippery; sentences are long; silence is medicine",
         "She goes still; both hands flat on the ledge - warning, not calm",
         "In the parking garage she almost dials Brennan; doesn't; the "
         "almost is new"],
  syn="CE-02 explicit; her body language vocabulary established under load."),
S(11, "Hypotheticals", "A", 10, "Payphone, Clark & Grand", "probe_test",
  "A", "B", "if someone kept records", "hypothetical",
  "she tests him with a fiction",
  ["CE-01", "CE-02"],
  [("A", "B", "attraction_sexual", 0.06), ("A", "B", "trust", 0.05),
   ("A", "B", "vulnerability", 0.05), ("B", "A", "trust", 0.06)],
  0.52,
  beats=["'Hypothetically. If someone kept records the family never saw - "
         "what would that someone be to you?' - 'Evidence.' - 'Wrong "
         "answer.' - 'A reason to keep someone alive.' - 'Better.'",
         "Each hears the other breathing through two blocks of static",
         "She hangs up before wanting more becomes wanting him"],
  syn="The ledger enters their private language as a hypothetical; trust "
      "moves on both edges."),
S(12, "Ice Out", "B", 11, "Riverwalk under the Kinzie Street rail bridge",
  "bargain_trade", "B", "A", "river ice breaking", "offer-refused",
  "protection for cooperation; refused; near-touch",
  ["CE-01", "CE-02"],
  [("B", "A", "attraction_sexual", 0.07), ("B", "A", "commitment", 0.05),
   ("A", "B", "attraction_romantic", 0.07), ("A", "B", "emotional_safety", 0.05)],
  0.66,
  beats=["Locale signature: river ice breaking up under the rail bridge, "
         "sound like knuckles cracking",
         "His terms: cooperation, protection, a future with a witness "
         "number instead of a name. Her terms: no",
         "'I've seen your protection. I audit its funerals.' - the dead "
         "witness stands between them",
         "Her glove and his sleeve; a near-touch neither books",
         "Advance: rising action is now a two-body problem"],
  syn="Advance scene: the bargain fails but the bond doesn't; the river "
      "motif opens."),
# ---------------------------------------------------------------- Phase 3
S(13, "Sunday Gravy", "A", 13, "Sal Moretti's house, family table",
  "deflect_withhold", "A", "D", "the long table", "family-dinner",
  "surveillance wears a napkin",
  ["CE-02", "CE-03"],
  [("A", "B", "emotional_safety", 0.04), ("A", "D", "fear", 0.06)],
  0.58, hot={"A-D": 0.55},
  beats=["Sal at the head; Nico blessed aloud as 'looking after our Elena'",
         "Sal, warmly, of Lucia: 'We brought her over. Passage is a "
         "kindness that remembers.' (CE-03 armed in one sentence)",
         "Elena performs niece, bookkeeper, loyalty - and counts exits",
         "Thought that frightens her at the stove: Brennan would hate this "
         "room, and she'd feel safer in it if he were here"],
  syn="The family's warmth as leverage inventory; Lucia's debt is now "
      "visible on the table."),
S(14, "Flip Her", "B", 14, "Task force, SAC's office", "deflect_withhold",
  "B", "A", "source protocol", "institutional-pressure",
  "he shields her from the flip order",
  ["CE-01"],
  [("B", "A", "commitment", 0.06), ("B", "A", "trust", 0.04)],
  0.60,
  beats=["The SAC wants the bookkeeper flipped and wired - 'she's the "
         "spine of the paper case'",
         "Cole recites source-safety protocol like scripture to slow it; "
         "his real reason has her eyes and he won't look at it",
         "He takes the subpoena duty himself to keep other hands off her",
         "Fear named: the last witness he flipped is a case number and a "
         "grave"],
  syn="B bends the institution around her, calling it procedure."),
S(15, "Clean Hands", "A", 15, "Back office; production of records",
  "deflect_withhold", "A", "B", "boxes of paper", "production",
  "she gives him everything that says nothing",
  ["CE-01"],
  [("B", "A", "respect", 0.08), ("B", "A", "attraction_romantic", 0.07),
   ("A", "B", "trust", 0.06), ("A", "B", "vulnerability", 0.06)],
  0.65,
  beats=["Subpoena served; she produces flawless legal books, box after box",
         "He checks the marked-payment window in the catering account: the "
         "correction she stalled isn't there - she didn't wash it",
         "He says nothing. She watches him not say it. Complicity, "
         "double-entry",
         "'Your books are beautiful.' - 'They're accurate.' - 'That's what "
         "I said.'"],
  syn="Mutual moral grayness ratified in silence; desire routed through "
      "professional awe."),
S(16, "Passage Due", "A", 16, "Kitchen after close", "realign_betray",
  "D", "C", "knife roll", "debt-called",
  "the confidant becomes the family's instrument",
  ["CE-03"],
  [("A", "B", "attraction_romantic", 0.05), ("C", "A", "fear", 0.06)],
  0.70, hot={"C-D": 0.50},
  beats=["Nico finds Lucia alone rolling knives; the passage debt called "
         "in: watch Elena, report Elena, or the kindness is repriced",
         "Lucia's hands keep rolling; her yes is one syllable and costs her "
         "face",
         "Elena, oblivious, catches herself reaching for the phone to hear "
         "Brennan's voice about nothing; puts it down; the wanting is now "
         "domestic",
         "Dramatic irony armed: the reader holds what Elena doesn't (L6)"],
  syn="CE-03 fires: her only confidant is turned; the reader knows, she "
      "doesn't."),
S(17, "Cover Story", "B", 16, "West Loop street, night", "reveal_misfire",
  "A", "B", "performed contempt", "seen-together",
  "a lie performed in public, the truth said in private",
  ["CE-01", "CE-02"],
  [("A", "B", "attraction_sexual", 0.09), ("A", "B", "emotional_safety", 0.07),
   ("B", "A", "attraction_sexual", 0.08), ("B", "A", "trust", 0.05)],
  0.80,
  beats=["A family soldier clocks them on the same corner; Elena improvises "
         "loudly: harassment, badge numbers, her lawyer - performed contempt "
         "with real fear under it",
         "The soldier, satisfied, reports a bookkeeper being loyal",
         "Doorway after: 'You lie well.' - 'I keep books.' - the first "
         "true thing they've traded at one foot's distance",
         "First crisis peak: both now conspirators in the pretense of enmity",
         "Advance to False Resolution"],
  syn="Advance scene: enemies-in-public becomes the cover story for "
      "something neither will name."),
# ---------------------------------------------------------------- Phase 4
S(18, "The Ticket", "A", 17, "Union Station, then her apartment",
  "deflect_withhold", "A", "C", "unbought ticket", "almost-gone",
  "she doesn't leave, and doesn't say why",
  ["CE-04"],
  [("A", "B", "attraction_romantic", 0.06), ("A", "B", "commitment", 0.04)],
  0.42,
  beats=["Danny stabilizing; Nico quiet; the window to run is open",
         "She stands under the departures board with cash for the ticket "
         "she's priced for years - and walks out with her hands empty",
         "Tells Lucia it's about Danny's hearing dates. It is not only that",
         "Exits named before they are used: 'Gate F, the 6:40, Carbondale "
         "then gone.' Naming it is how she doesn't take it"],
  syn="False resolution: the exit plan survives on paper only; the reason "
      "has a name she won't write."),
S(19, "Redirection", "B", 18, "Task force", "realign_betray", "B", "D",
  "org chart", "quiet-steering",
  "he aims the case at the enforcer",
  ["CE-01", "CE-02"],
  [("B", "A", "commitment", 0.08), ("B", "A", "trust", 0.04)],
  0.44,
  beats=["Cole re-weights the target package: Gravano's crew, the "
         "stairwell, the muscle ledger - away from the bookkeeper",
         "It is good casework and it is also not neutral, and he knows the "
         "difference now",
         "The org chart on the wall: her photo moved one column left, by "
         "his hand, at midnight"],
  syn="Procedure bent a second time; his protection acquires a paper trail."),
S(20, "Family Meal", "B", 19, "La Bilancia, snowed-in staff meal",
  "probe_test", "B", "A", "staff meal", "snowbound",
  "an hour with no case in it",
  ["CE-04", "CE-01"],
  [("A", "B", "affection", 0.10), ("A", "B", "emotional_safety", 0.08),
   ("A", "B", "resentment", -0.08),
   ("B", "A", "affection", 0.09), ("B", "A", "emotional_safety", 0.06),
   ("B", "A", "resentment", -0.08), ("B", "A", "commitment", 0.07)],
  0.40,
  beats=["Lake-effect snow shuts the street; he's inside 'coordinating "
         "compliance' when the kitchen feeds the stranded",
         "She sets a bowl in front of him herself - acts of service, "
         "unbudgeted",
         "Gallows humor about wire taps and dessert; Lucia watches them "
         "and her report gets one line shorter (guilt, first installment)",
         "One hour where nobody is an adversary; both notice; neither exits"],
  syn="The quiet scene that still carries package value: intimacy advanced "
      "under weather cover."),
S(21, "The Leak", "A", 20, "Back office audit", "probe_test", "A", "C",
  "columns that don't foot", "audit",
  "she finds the leak and misreads it",
  ["CE-03"],
  [("A", "B", "trust", 0.04), ("A", "B", "commitment", 0.07),
   ("A", "D", "resentment", 0.06)],
  0.46,
  beats=["Till patterns off by minutes, not money: someone reconstructs "
         "her day after close",
         "She audits everyone and misreads the trail as Nico's street watch "
         "(false belief, L6 divergence armed)",
         "Never once prices Lucia - some accounts she refuses to open",
         "Decides the ledger needs a second custodian if she falls: the "
         "thought wears Brennan's coat"],
  syn="The surveillance is found but misattributed; her trust migrates "
      "toward Cole by elimination."),
S(22, "Terms", "A", 21, "Neutral diner, Ohio Street", "bargain_trade",
  "A", "B", "two coffees, one napkin", "midpoint-alliance",
  "she proposes the alliance; midpoint",
  ["CE-01", "CE-02", "CE-04"],
  [("A", "B", "trust", 0.10), ("A", "B", "commitment", 0.08),
   ("A", "B", "resentment", -0.10),
   ("B", "A", "trust", 0.08), ("B", "A", "commitment", 0.08),
   ("B", "A", "resentment", -0.10)],
  0.56,
  beats=["MIDPOINT (uneasy alliance): she offers a timeline of the family's "
         "structure - no ledger, no names in her own hand - for Danny's "
         "protective transfer and a clean lane out for the innocents on "
         "payroll",
         "Terms on a napkin, initialed with a pen from his breast pocket; "
         "off-book and both know what that costs him",
         "'This isn't trust.' - 'No. It's terms.' - 'Good. Terms I can "
         "audit.'",
         "Advance: the deepening begins as a signed hypothetical"],
  syn="Advance scene: adversaries become co-conspirators with terms; the "
      "napkin is the first joint entry."),
# ---------------------------------------------------------------- Phase 5
S(23, "Night Ledgers", "A", 22, "Back office, two chairs", "probe_test",
  "A", "B", "two chairs, one lamp", "working-nights",
  "proximity as method",
  ["CE-01", "CE-02"],
  [("A", "B", "emotional_safety", 0.05), ("A", "B", "attraction_sexual", 0.06),
   ("A", "B", "affection", 0.08),
   ("B", "A", "attraction_sexual", 0.06), ("B", "A", "emotional_safety", 0.05)],
  0.58,
  beats=["Nights decoding the front-business flows under the banker's lamp; "
         "his chair migrates an inch per session",
         "She explains laundering like a love language; he follows like a "
         "man learning one",
         "Hands near the same page; the lamp's green circle is the only "
         "country where they're legal",
         "Surface block honored: the near-touch is new each time or not at "
         "all"],
  syn="Deepening by shared work; the office becomes theirs at night."),
S(24, "Name the Exit", "A", 23, "Back office doorway, 1 a.m.",
  "negotiate_consent", "A", "B", "the named door", "consent-c2",
  "the almost-kiss stopped and negotiated",
  ["CE-01"],
  [("A", "B", "emotional_safety", 0.07), ("A", "B", "vulnerability", 0.06),
   ("A", "B", "affection", 0.06),
   ("B", "A", "emotional_safety", 0.06), ("B", "A", "trust", 0.05)],
  0.64,
  consent={"kind": "ask", "act_class": "C2"},
  grants=[("A", "B", 2, "private"), ("B", "A", 2, "private")],
  beats=["The almost-kiss at the doorway; her palm flat on his sternum: "
         "'Not yet. Name the exit first.'",
         "Terms, spoken like clauses: this never buys testimony; the case "
         "stays outside that door; either of us can call it off in one word",
         "'Then ask me.' He asks. She says yes to kissing and nothing "
         "further tonight; he repeats her terms back verbatim - the "
         "regulation reflex, finally pointed at the right law",
         "Nothing is performed tonight; the grant is the scene"],
  syn="On-page mutual C2 consent negotiation - explicit, in character, "
      "terms-first for a woman who prices everything."),
S(25, "First", "A", 24, "Back office, after close", "release_transform",
  "A", "B", "ink-stained fingers", "first-kiss",
  "the kiss, on her initiative",
  ["CE-01"],
  [("A", "B", "attraction_romantic", 0.08), ("A", "B", "emotional_safety", 0.08),
   ("A", "B", "affection", 0.12), ("A", "B", "resentment", -0.10),
   ("B", "A", "attraction_romantic", 0.08), ("B", "A", "affection", 0.07)],
  0.68, contact={"class": "C2", "setting": "private"},
  beats=["A small win: Danny's protective transfer confirmed (his napkin "
         "term, kept)",
         "She crosses the office and kisses him - First_Kiss_Phase 5, her "
         "move, her timing",
         "Ink on his jaw where her fingers held it; he doesn't wipe it off",
         "One beat of silence past comfort, then both of them laughing "
         "once, quietly, like conspirators",
         "TR enemies_to_lovers -> paying off"],
  syn="The trope pays inside its window; initiative hers, per her arc."),
S(26, "Garage Level 3", "B", 24, "Parking structure, night",
  "demand_threaten", "D", "B", "engine ticking", "warned-off",
  "touch her and the family buries you both",
  ["CE-02"],
  [("B", "A", "commitment", 0.08), ("B", "D", "resentment", 0.08)],
  0.72, hot={"B-D": 0.65},
  beats=["Nico steps out from between cars, hands loose: 'Whatever you "
         "think she is to your case - she's ours. Touch her and the river "
         "does the paperwork.'",
         "Cole, level: 'Threatening a federal officer. Say it again slower "
         "for the transcript.'",
         "Nobody blinks; the threat inverts the trope - the family holds "
         "the touch-her-and-die card and just played it at the wrong man",
         "He drives to her street and sits two minutes with the engine off. "
         "Then goes home. Protection without surveillance - the distinction "
         "now matters to him"],
  syn="touch_her_and_die pays inverted: the menace is the family's, and it "
      "prices Cole in."),
S(27, "The Long Table", "A", 25, "Sal's dining room", "deflect_withhold",
  "A", "D", "the old book named aloud", "dinner-confrontation",
  "she lies to the head of the family at his own table",
  ["CE-01", "CE-02"],
  [("A", "B", "commitment", 0.06), ("A", "D", "fear", 0.08),
   ("A", "D", "resentment", 0.07)],
  0.78, hot={"A-D": 0.70}, close=["CE-02"],
  beats=["SET PIECE (Ph5): family dinner confrontation over the ledger. "
         "Sal, over the roast: 'People say my brother kept an old book. "
         "People say it walks. Where does it sleep, Elena?'",
         "Both hands flat on the tablecloth: 'In the same grave as his "
         "debts. I burned the loose pages myself the year his hands went.' "
         "A lie with perfect posture",
         "Nico watches her the whole length of the table; Lucia refills "
         "glasses with a shaking wrist (she knows the safe was full)",
         "Sal toasts her; the threat against Danny stands down - the "
         "family believes its bookkeeper (CE-02 closed: spent, not kind)",
         "Cost registered in her hands only she can read"],
  syn="The seeded confrontation; her lie buys Danny's safety and arms the "
      "endgame - Lucia's report will price this lie."),
S(28, "Terms of Surrender", "A", 26, "Her apartment", "negotiate_consent",
  "B", "A", "coat on the hook", "consent-c3c4",
  "the negotiation before anything further",
  ["CE-01"],
  [("A", "B", "emotional_safety", 0.08), ("A", "B", "vulnerability", 0.08),
   ("A", "B", "attraction_sexual", 0.07), ("A", "B", "resentment", -0.08),
   ("B", "A", "emotional_safety", 0.07), ("B", "A", "vulnerability", 0.07),
   ("B", "A", "resentment", -0.06)],
  0.85, contact={"class": "C2", "setting": "private"},
  consent={"kind": "ask", "act_class": "C3"},
  grants=[("A", "B", 3, "private"), ("B", "A", 3, "private"),
          ("A", "B", 4, "private"), ("B", "A", 4, "private")],
  beats=["SET PIECE (Ph5): consent negotiation before first C3 contact - "
         "on the page, in their own registers",
         "He asks in plain words, regulation citations surrendered at the "
         "door; she answers in terms: yes to everything, on her schedule, "
         "her terms, and the case never crosses the threshold after dark",
         "Boundaries named and logged (no leverage, no questions about the "
         "ledger in this room; one word stops everything, any time)",
         "Tonight: kissing, the coat on the hook, and the agreement itself "
         "as the intimacy - anticipation as structure",
         "Advance: the climax phase opens with every grant explicit"],
  syn="Advance scene and set piece: full mutual C3/C4 grants negotiated "
      "explicitly; nothing above C2 performed tonight."),
# ---------------------------------------------------------------- Phase 6
S(29, "The Window", "B", 26, "Task force, evening", "deflect_withhold",
  "B", "D", "raid clock", "boxed-in",
  "the raid window opens; he is out of lanes",
  ["CE-01"],
  [("B", "A", "commitment", 0.06), ("B", "A", "vulnerability", 0.05)],
  0.78,
  beats=["The marked payment surfaces on a wire intercept - the bait he "
         "didn't know about found its way into the family's noise",
         "A raid window on La Bilancia's records is provisionally cut for "
         "week's end; his redirection didn't hold",
         "Warn her: felony. Stay silent: she burns. He files the dilemma "
         "under insomnia",
         "He requests the affidavit duty himself - one hand still on the "
         "wheel"],
  syn="The case outruns him; CE-01's deadline pressure becomes his body's "
      "problem."),
S(30, "Inventory of Scars", "A", 27, "Her apartment, night",
  "release_transform", "A", "B", "reading glasses", "first-night",
  "first full intimacy under standing terms",
  ["CE-01"],
  [("A", "B", "vulnerability", 0.08), ("A", "B", "attraction_sexual", 0.06),
   ("A", "B", "trust", 0.06), ("A", "B", "resentment", -0.06),
   ("B", "A", "vulnerability", 0.08), ("B", "A", "affection", 0.08),
   ("B", "A", "attraction_sexual", 0.06), ("B", "A", "trust", 0.05)],
  0.76, contact={"class": "C4", "setting": "private"},
  beats=["First_Intimacy_Phase 6, honored: the standing grants from scene "
         "28 govern; his 'still yes?' at the threshold and her 'still yes' "
         "- reaffirmation, not renegotiation",
         "Heat 4 rendering: explicit in feeling, precise in consent, "
         "cadence compressed; her stillness finally reads as calm",
         "Inventory of scars traded like disclosures: her father's "
         "handwriting in her, his partner's ghost in him",
         "Both still holding one secret each in the same bed; the dread "
         "shares the pillow",
         "The reading glasses on her nightstand: his, left, deliberate"],
  syn="The intimacy payoff under explicit standing consent; secrets "
      "interleaved with tenderness."),
S(31, "What Lucia Carried", "A", 28, "Kitchen, dawn", "reveal_misfire",
  "C", "A", "flour on the pass", "confession",
  "the confidant confesses the debt and the reports",
  ["CE-03", "CE-01"],
  [("A", "C", "trust", -0.10), ("A", "B", "trust", 0.05),
   ("A", "B", "fear", 0.04)],
  0.82, hot={"A-C": 0.55}, close=["CE-03"],
  beats=["Lucia, hands in flour, not looking up: 'They called the passage. "
         "I've been telling Nico your hours since the night it snowed.'",
         "The dinner lie is therefore blown or about to be: Nico knows the "
         "safe was full the week Elena swore ashes",
         "Elena's stillness; then the bookkeeper's question: 'What exactly, "
         "line by line?' - grief conducted as an audit",
         "CE-03 closed: the debt is spent, the leverage burned by "
         "confession; what remains is repair, later, if they live",
         "Elena empties the floor safe into her coat: the ledger rides "
         "with her now (possession event, L3)"],
  syn="Betrayal_exposed part one - the friend, not the lover; the ledger "
      "leaves the safe."),
S(32, "Chain of Custody", "B", 28, "Evidence annex, night",
  "reveal_misfire", "B", "A", "one page, folded once", "evidence",
  "her handwriting in the marked chain; he palms the page",
  ["CE-01"],
  [("B", "A", "trust", -0.06), ("B", "A", "commitment", 0.07),
   ("B", "A", "vulnerability", 0.06)],
  0.86,
  beats=["The wire's paper trail lands: a catering invoice in her coding "
         "wraps the marked bills - dated the week she stalled it. To a "
         "grand jury it reads as laundering; to him it reads as refusal, "
         "if anyone lets him testify to handwriting",
         "He takes the one duplicate page out of the sorted stack and "
         "folds it into his breast pocket - evidence handling violation, "
         "witnessed by fluorescent light and nobody",
         "Morally gray paid inside its window: the by-the-book man, "
         "off the book, for her",
         "He drafts a duress memorandum he can't file yet; the folded page "
         "ticks in his pocket like a debt"],
  syn="His third and unforgivable procedural break - the one that will "
      "cost and save."),
S(33, "Carry It", "A", 29, "Back office; then the street", "deflect_withhold",
  "A", "D", "empty safe, open door", "searched",
  "D searches; the ledger is already on her body",
  ["CE-01", "CE-04"],
  [("A", "B", "trust", 0.05), ("A", "B", "commitment", 0.05),
   ("A", "D", "fear", 0.09), ("A", "D", "resentment", 0.08)],
  0.90, hot={"A-D": 0.75},
  beats=["Nico with two soldiers 'helps her look' for discrepancies; the "
         "floor safe swings open on cash and nothing - her ledger is "
         "against her spine under wool",
         "'Sal wants the book, Elena. Whatever you burned, burn it again "
         "in front of me.' - 'Bring matches next time.' Both hands flat "
         "on the desk",
         "Lucia's tip half-paid: he knows it exists; he doesn't know it "
         "walked in on her body and will walk out the same way",
         "She books the only next move: trade it to Brennan's people for "
         "Danny - before the family or the raid finds it first"],
  syn="The noose closes from both sides with the ledger in transit; her "
      "decision to trade it is made alone."),
S(34, "Service", "B", 29, "La Bilancia, dinner service; the raid",
  "realign_betray", "B", "A", "warrant on the pass", "all-is-lost",
  "the warrant executes mid-service; the betrayal reveal",
  ["CE-01"],
  [("A", "B", "resentment", 0.15), ("A", "B", "trust", -0.15),
   ("A", "B", "fear", 0.10), ("B", "A", "vulnerability", 0.07),
   ("B", "A", "commitment", 0.06)],
  0.93, misfire=["CE-01"],
  beats=["ALL IS LOST (warrant_executed): the task force takes the "
         "restaurant mid-service - lights, vests, inventory teams; the "
         "SAC moved the window without telling the compromised agent until "
         "the vans rolled",
         "Cole arrives with the second wave because absence would have "
         "burned him worse; she sees him inside the perimeter, badge out",
         "On the inventory control sheet in an open folder: her ledger's "
         "description, target item one, sought since the case opened - "
         "Secret_B detonates; the interview, the river, the bed: re-audited "
         "in one breath (desire inversion - fracture initiator)",
         "She is detained in the sweep - his one visible act is stepping "
         "between her and cuffs: 'Material witness. Nobody hooks her.'",
         "The ledger, against her spine, undiscovered: a search of the "
         "premises, not persons; CE-01 misfires - exposed, unresolved, "
         "heavier (w 0.9 -> 1.0)",
         "Breakup beat (betrayal_reveal): her face closes like a book"],
  syn="The black moment: everything true reads as a lie; phase fractures "
      "into Reversal."),
# ---------------------------------------------------------------- Phase 7
S(35, "Smaller Questions", "A", 29, "Field office, interview room B",
  "deflect_withhold", "A", "B", "the recorder, again", "mirror-interview",
  "scene 3 mirrored; consent withdrawn",
  ["CE-01", "CE-04"],
  [("A", "B", "trust", -0.10), ("A", "B", "emotional_safety", -0.12),
   ("A", "B", "resentment", 0.05), ("B", "A", "vulnerability", 0.05)],
  0.74, consent={"kind": "withdraw", "act_class": "C2"},
  withdraw=[("A", "B", 2), ("B", "A", 2)],
  beats=["Motif recontext (two-phase gap, changed tension): the recorder "
         "on the table again, but the roles inverted - he needs her to "
         "speak and she answers questions with smaller questions",
         "'Did you know about my ledger at the restaurant, the first "
         "day?' is her only real question. His pause is the answer. 'The "
         "case knew,' he says. Wrong answer; the right one existed",
         "One word ends everything, any time - she uses it: 'Withdrawn.' "
         "All standing grants void the moment the beat lands (4.5)",
         "Danny's lawyer arrives; she leaves as a material witness, "
         "uncharged, unowned, carrying the ledger past the metal detector "
         "she was never taken through",
         "His hands stay flat on the table until the door closes - her "
         "gesture, learned, too late"],
  syn="The reversal's cold center: withdrawal honored to the letter; the "
      "mirror of the meet."),
S(36, "The Page", "B", 30, "SAC's office, 7 a.m.", "release_transform",
  "B", "A", "the folded page, unfolded", "costly-proof",
  "he surrenders his own violation to save her standing",
  ["CE-01"],
  [("B", "A", "commitment", 0.09), ("B", "A", "vulnerability", 0.08)],
  0.68,
  beats=["Reunion_Mode = costly_proof, opening move: he lays the folded "
         "duplicate page, the duress memorandum, and his own conduct "
         "report on the SAC's desk - self-surrender before OPR asks",
         "The analysis he attaches proves the invoice coding is a refusal "
         "pattern, not laundering: she stalled the marked money; the "
         "family's own wire says so if you know her hand. He is the only "
         "one who knows her hand",
         "Price tag: off the case, badge on the desk pending review, the "
         "task force keeps his work and loses his name",
         "'Why?' the SAC asks. 'Judgment,' he says, and for once cites no "
         "regulation"],
  syn="Growth arc lands: judgment over procedure, paid in career; the "
      "proof begins costing."),
S(37, "His Own Page", "A", 30, "La Bilancia, shuttered, night",
  "bargain_trade", "A", "D", "his own page, turned toward him",
  "secret-leverage",
  "she prices the enforcer with his own line items",
  ["CE-01"],
  [("A", "D", "fear", -0.08), ("A", "D", "dominance", 0.10),
   ("A", "B", "trust", 0.04)],
  0.78, hot={"A-D": 0.80},
  beats=["Nico, alone now - no witnesses left to keep (Phase >= 5; the "
         "constraint has expired and both know what that means)",
         "He wants the ledger to ransom himself out of the collapsing "
         "family. She opens it on the desk to a page and turns it toward "
         "him: his skims, dated, priced - eleven years of them",
         "SECRET_LEVERAGE pays: 'Walk out of Chicago tonight and this page "
         "goes with the rest to people who'll be busy with Sal. Touch me, "
         "and it goes to Sal.' The bookkeeper's math, said once",
         "His hands, for the first time, are the still ones. He leaves - "
         "cornered by arithmetic, not courage",
         "Her trust in Cole ticks up against her will: his people never "
         "searched her; someone kept that line"],
  syn="The enforcer priced out with the ledger's own ink - her competence "
      "as the weapon, no rescue required."),
S(38, "Disposition", "A", 31, "US Attorney proffer room", "release_transform",
  "A", "B", "the ledger on the table", "proffer",
  "the ledger's disposition resolves on the page",
  ["CE-01", "CE-04"],
  [("A", "B", "trust", 0.10), ("A", "B", "resentment", -0.15),
   ("B", "A", "trust", 0.08), ("B", "A", "respect", 0.07)],
  0.76, close=["CE-01"],
  beats=["SET PIECE (Ph7): the ledger's disposition resolves on the page - "
         "proffer session, Danny's counsel present, the AUSA across the "
         "table, Cole's duress memorandum already in the file doing its "
         "quiet work",
         "She slides the single physical original across the table; "
         "inventory number read aloud; her signature on the transfer - "
         "every motion on the record (single-original constraint honored "
         "to the last page)",
         "Her coding, decoded by her, on the record: the charged "
         "transactions route around Danny - his name was borrowed ink; "
         "the true weight lands on Sal's chair and Nico's skims",
         "Terms: full use immunity, Danny's release motion joined by the "
         "government, and she testifies under her own name - the clean "
         "exit traded for a true one (sacrifice registered)",
         "CE-01 closes on the page; across the table, they do not touch; "
         "respect moves where consent hasn't returned"],
  syn="Climax mode confrontation_and_sacrifice: she buys Danny with the "
      "book and pays with her anonymity."),
S(39, "Ice Out II", "B", 31, "Riverwalk, dusk", "release_transform",
  "B", "A", "river running clear", "reckoning",
  "one honest number; the reversal completes",
  ["CE-04"],
  [("A", "B", "emotional_safety", 0.08), ("A", "B", "affection", 0.08),
   ("A", "B", "resentment", -0.15), ("A", "B", "fear", -0.10),
   ("B", "A", "emotional_safety", 0.07), ("B", "A", "affection", 0.07)],
  0.70,
  beats=["Motif recontext: the Kinzie bridge again, ice gone, river "
         "running dark and clear - two phases and one ruin since the "
         "offer she refused here",
         "He gives her the full accounting, unprompted, dates included: "
         "when the case first touched the ledger (before he met her), when "
         "he knew, every lie of omission itemized - 'one honest number,' "
         "audited aloud",
         "No ask attached. He turns to go - proof, not payment",
         "'Brennan.' Her voice. 'The 6:40 to Carbondale. I never bought "
         "it.' The exit named, retired in front of him",
         "Nothing granted tonight but the future tense (fracture: desire "
         "inversion inverts back; phase turns to Resolution)"],
  syn="The costly proof lands; forgiveness starts as an audit that "
      "balances."),
# ---------------------------------------------------------------- Phase 8
S(40, "Owed to No One", "A", 31, "MCC Chicago, release door, morning",
  "release_transform", "A", "C", "the promise, kept verbatim",
  "promise-payoff",
  "Danny walks; the promise is quoted and closed",
  ["CE-04"],
  [("A", "B", "trust", 0.06), ("A", "B", "affection", 0.06),
   ("A", "B", "resentment", -0.10),
   ("B", "A", "affection", 0.06)],
  0.38, close=["CE-04"],
  beats=["Danny through the release door, squinting at daylight, ribs "
         "still taped; Lucia waits by the car because Elena asked her to "
         "be there - the first stitch of repair",
         "The promise paid in its exact wording (L7 discipline): '" +
         PROMISE_CE04 + "' - 'You said that through the glass,' he says. "
         "'I wrote it down,' she says",
         "Government motion joined; charges collapsing as the true weight "
         "shifts to Sal and the fled enforcer",
         "Across the street, at distance, Cole watches one minute and "
         "leaves without being seen - present tense, no claim",
         "CE-04 closes: owed to no one, at last, in both directions"],
  syn="Resolution opens with the promise kept letter-perfect."),
S(41, "Findings", "B", 31, "OPR hearing room, midday", "deflect_withhold",
  "B", "A", "the letter of reprimand", "findings",
  "he takes the letter and keeps the judgment",
  ["CE-04"],
  [("B", "A", "commitment", 0.07), ("B", "A", "vulnerability", 0.06)],
  0.34,
  beats=["OPR findings: violations sustained (the warning call, the page); "
         "mitigation sustained too (the duress memo cracked the case; the "
         "witness lived) - letter of reprimand, reassignment offered",
         "Offered the soft story - 'operational necessity' - he declines "
         "to sign it: 'It wasn't necessity. It was judgment. Write that.'",
         "He keeps the badge on his own terms: financial-crimes desk, "
         "training agents to read handwriting",
         "The framed commendation goes home face-up for the first time - "
         "his dead witness finally an honored debt, not a hidden one"],
  syn="His arc closes: procedure survives as a tool, not armour."),
S(42, "Ask Me Again", "A", 31, "Riverwalk, late afternoon",
  "negotiate_consent", "A", "B", "the same railing, new terms",
  "consent-regrant",
  "she reopens the account on new terms",
  ["CE-04"],
  [("A", "B", "trust", 0.08), ("A", "B", "emotional_safety", 0.10),
   ("A", "B", "affection", 0.10), ("A", "B", "resentment", -0.12),
   ("A", "B", "fear", -0.12),
   ("B", "A", "emotional_safety", 0.08), ("B", "A", "trust", 0.06),
   ("B", "A", "affection", 0.08)],
  0.30, consent={"kind": "offer", "act_class": "C2"},
  grants=[("A", "B", 2, "any"), ("B", "A", 2, "any")],
  beats=["She finds him at the railing (his quality time is standing "
         "where she might walk)",
         "'Withdrawn isn't the same as closed,' she says. 'Ask me again.' "
         "He asks - plain words, no citations, terms hers to set",
         "New grant, new scope: 'anywhere,' she says. 'I'm done pricing "
         "rooms.' - consent re-established on the page, wider than before",
         "Nothing performed tonight; the reopening of the account is the "
         "intimacy - the architecture honored to the last entry",
         "They stand not touching with the whole width of permission "
         "between them, grinning like fools at a river"],
  syn="The withdrawal honored, the re-grant earned and explicit; scope "
      "'any' - she stops hiding the account."),
S(43, "Kitchen Accounts", "A", 31, "La Bilancia kitchen, evening",
  "release_transform", "C", "A", "two aprons", "repair",
  "Lucia's amends; the repair ledger opens",
  ["CE-04"],
  [("A", "C", "moral_repair", 0.15), ("A", "C", "trust", 0.08),
   ("A", "B", "affection", 0.04)],
  0.28,
  beats=["The restaurant in receivership limbo; the kitchen still theirs "
         "by habit and key",
         "Lucia's amends offered in full: every report itemized, dates and "
         "contents, nothing softened - an accounting, because she knows "
         "what Elena respects",
         "Elena accepts: 'You paid a debt with my hours. I've paid debts "
         "with worse.' Moral repair: breach -> acknowledged -> amends "
         "offered -> accepted, stages on the record",
         "Forgiving Lucia rehearses the harder entry: forgiving herself "
         "for Danny (growth arc: self_forgiveness, keystone laid)",
         "Two aprons on one hook; flour handprint on Elena's shoulder"],
  syn="The confidant repaired through the same bookkeeping grammar; her "
      "self-forgiveness arc completes through it."),
S(44, "Clean Exit", "A", 31, "Empty storefront on the river, night",
  "release_transform", "A", "B", "her name on a lease", "hea",
  "the title recontextualized; the HEA lands",
  ["CE-04"],
  [("A", "B", "commitment", 0.12), ("A", "B", "attraction_romantic", 0.08),
   ("A", "B", "affection", 0.10), ("A", "B", "fear", -0.10),
   ("B", "A", "commitment", 0.12), ("B", "A", "attraction_romantic", 0.06),
   ("B", "A", "affection", 0.08)],
  0.25, contact={"class": "C2", "setting": "private"},
  beats=["A small dark storefront, river-facing, lease pages on a crate; "
         "her own name on every line - no family co-signer, no borrowed "
         "ink (earned_exit)",
         "'Clean exit,' he reads. 'You're staying.' - 'That's what it "
         "means now. Leaving was the old ledger.'",
         "The green banker's lamp, carried from the old office, set on "
         "the crate and lit: one circle of light, owned outright",
         "The kiss under the standing 'anywhere' grant - unhurried, "
         "uncounted, nobody's evidence",
         "HEA on the page: keys, lamp, river, him; a drawer promised for "
         "his reading glasses"],
  syn="Title recontext: the clean exit was never the train - it's a life "
      "unowed; commitment moves double-entry."),
S(45, "Epilogue: Thaw", "A", 0, "The new place, mid-May", "release_transform",
  "A", "B", "river running clear", "epilogue",
  "spring; the books balance",
  [],
  [("A", "B", "commitment", 0.05), ("B", "A", "commitment", 0.05)],
  0.18, contact={"class": "C2", "setting": "private"},
  beats=["Mid-May, outside the story clock (Epilogue_Included): the ice "
         "long gone, the river running clear past new glass lettered "
         "ELENA'S - BOOKS BALANCED, DINNER AT SIX",
         "Danny waits tables and studies for the CPA exam out of spite; "
         "Lucia runs the kitchen as a partner, papers filed under her own "
         "name",
         "Sal's trial calendar on the news with her name in it; she reads "
         "it like weather - she will testify in June and sleep in July",
         "Cole at the corner table at five fifty-five, off duty, reading "
         "glasses on; his drawer upstairs has been full for weeks",
         "Last entry, her hand, the old habit turned kind: a ledger line "
         "for the day - two covers, one lamp, nothing owed"],
  syn="The HEA audited one season later: everyone solvent, everything "
      "chosen; the last line of the book is a balanced entry."),
]

SCENE = {s["scene"]: s for s in SCENES}

# Chapter map for the manuscript build.
CHAPTERS = [
    (1, "The Weight of Ink", [1, 2, 3]),
    (2, "Regards from the Family", [4, 5, 6]),
    (3, "Off Channel", [7, 8, 9]),
    (4, "Hypotheticals", [10, 11, 12]),
    (5, "Sunday Gravy", [13, 14, 15]),
    (6, "Cover Story", [16, 17]),
    (7, "The Ticket", [18, 19, 20]),
    (8, "Terms", [21, 22]),
    (9, "Night Ledgers", [23, 24, 25]),
    (10, "The Long Table", [26, 27, 28]),
    (11, "Inventory of Scars", [29, 30, 31]),
    (12, "Service", [32, 33, 34]),
    (13, "Smaller Questions", [35, 36]),
    (14, "Disposition", [37, 38, 39]),
    (15, "Owed to No One", [40, 41, 42]),
    (16, "Clean Exit", [43, 44]),
    (None, "Epilogue: Thaw", [45]),
]
