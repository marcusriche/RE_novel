"""Authored scene schedule for Seed 01KYFVZ2V7QFV4DN2XRAAPHTQ3 — "Out of Office".

Editorial layer of the offline binding configuration `offline-agent-v1`
(see binding/offline_client.py). 45 scenes over the Rom-Com/Workplace
reference allocation E = [10,12,12,8,10,10,10,8,10] (sum 90), halved to
[5,6,6,4,5,5,5,4,5] (sum 45) — the same scene-count discipline used for
Books 1-2 of the Mafia/Dark line, applied here for the first time to a
different Arc_Profile so the halving stays exact (all entries even).

Cast (engine node ids are the seed's own names A/B/C/E and the literal
Antagonistic_Force name):
  A = Robyn Fyfe, 34         - station manager, Kelvin Row Radio; weekend presenter
  B = Nadia Quinn, 39        - overnight sound engineer; secretly "Static"
  C = Priya Shah, 17         - volunteer producer; runs the desk and the gossip
  E = Kirsty Lennox          - A's former co-presenter, now on the review panel
  "the funding review"       - the three-year community media renewal panel
                               (Antagonistic_Force; an institution, not a person)

POV: first_person_single (A/Robyn narrates every scene, present tense). The
schedule's "pov" field is "A" throughout; other characters' inner lives are
dramatized only as Robyn can see or infer them, per the seed's POV field.

Story clock: 46 days anchored 2026-09-07 (Monday). Six live Thursday
broadcasts fall on story days 4, 11, 18, 25, 32, 39. The funding decision
lands on day 44 (Tuesday) and cannot be brought forward. No epilogue
(Epilogue_Included = false) — Phase 8 is the book's last movement.

CE lifecycle (types per Initial_CER_Seed, renumbered from Books 1-2's
convention because this seed's own CE-01..04 typing differs):
  CE-01 Promise      "What's real off that mic stays off the record. Every
                      time. I promise you that." — made scene 11, misfires
                      at the black moment (scene 36), redeemed scene 40.
  CE-02 Revelation   Nadia is "Static" — revealed to Robyn alone, scene 32.
  CE-03 Absence      Robyn's unprocessed grief for her mother — closed
                      scene 30.
  CE-04 Obligation   The unanswered London job offer — closed scene 26.

Consent architecture: the on-air stunt kiss (scene 13, First_Kiss_Phase 2)
is negotiated and granted, scoped "public"/performance, at scene 11 — before
it happens, per the taboo clause that the fake relationship may never be
used to obtain anything from the other lead. A second, private C2 grant is
negotiated at scene 28 before any real off-mic kiss. The mandatory consent
negotiation before first C3 contact (scene 33, phase 6) grants C3 and C4
private contact, covering First_Intimacy_Phase 6 at scene 34.
"""

PHASE_BLOCKS = {
    0: (1, 5), 1: (6, 11), 2: (12, 17), 3: (18, 21), 4: (22, 26),
    5: (27, 31), 6: (32, 36), 7: (37, 40), 8: (41, 45),
}
ADVANCE_SCENES = {5, 11, 17, 21, 26, 31, 36, 40}
FRACTURE_SCENES = {36, 40}   # the black moment / the off-script finale

DISPLAY = {"A": "Robyn Fyfe", "B": "Nadia Quinn", "C": "Priya Shah",
           "E": "Kirsty Lennox", "the funding review": "the funding review"}

PROMISE_CE01 = ("What's real off that mic stays off the record. Every time. "
                "I promise you that.")


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
S(1, "The Panel", "A", 1, "a strip-lit committee room, Glasgow City Chambers annexe",
  "demand_threaten", "the funding review", "A", "the three-year renewal folder",
  "promise-made",
  "the promise made in error, on the record, in front of everyone",
  ["CE-04"],
  [("A", "the funding review", "fear", 0.10),
   ("A", "the funding review", "resentment", 0.04)],
  0.30,
  beats=["Robyn stands in front of the community media renewal panel with a "
         "folder of numbers that are, in every honest column, bad",
         "The phrase that comes out of her mouth before she has decided to "
         "say it: 'Yes, of course we have a new couples hour. Six weeks, "
         "live, Thursdays'",
         "Kirsty Lennox — E, on the panel now, in a blazer, not making eye "
         "contact — writes something down without looking up",
         "The panel's engagement metric is explicit: audience-identifiable "
         "relational content, or the licence doesn't renew",
         "Robyn walks out into the rain not knowing a single fact about the "
         "show she has just promised, including who is in it"],
  syn="Mandatory inciting incident: the promise made in error, in public, "
      "with nothing behind it yet."),
S(2, "The Roof Fund", "A", 1, "Kelvin Row Radio, the basement studio, tenement on Dumbarton Road",
  "deflect_withhold", "A", "C", "the leaking roof, priced in buckets", "aftermath",
  "the stakes made physical; the caretaker flaw stated as competence",
  ["CE-04"],
  [("A", "C", "trust", 0.05), ("A", "C", "respect", 0.04)],
  0.28,
  beats=["Down the basement stairs into condensation and the red ON AIR "
         "bulb, which has not worked properly since 2019 and glows amber "
         "instead of red",
         "Priya Shah, seventeen, running the desk on a Saturday because "
         "nobody pays her to and she does it anyway, three buckets under "
         "three separate leaks, labelled by size",
         "Robyn tells her what she's promised. Priya's face does the thing "
         "it does when she is about to say something Robyn will not enjoy",
         "'You don't have a couple,' Priya says. 'You have a roof problem "
         "and a Tuesday.'",
         "The number: renewal keeps the roof, the transmitter, and Priya's "
         "stipend, which is the only wage in the building"],
  syn="Establish the station, the roof, Priya, and the size of the hole "
      "Robyn has just promised to fill."),
S(3, "The Only Candidate", "A", 1, "the corridor outside the overnight studio, 11 p.m.",
  "probe_test", "A", "B", "eleven words in three years", "candidate-named",
  "she runs the list of who could possibly do this and there is one name",
  ["CE-04"],
  [("A", "B", "respect", 0.04), ("B", "A", "respect", 0.02)],
  0.32,
  beats=["Robyn runs the actual list at midnight: two presenters who'd "
         "overact it, one who'd tell everyone within a week, and Nadia, who "
         "engineers the overnight slot and has said roughly eleven words to "
         "Robyn in three years",
         "Four of those eleven words were about a cable",
         "Through the glass: Nadia at the desk with one headphone cup off, "
         "listening to the room the way she listens to levels, not looking "
         "up when Robyn stands in the doorway",
         "The case for Nadia, run coldly, the way Robyn runs everything: "
         "discreet, present six nights a week, has no other on-air identity "
         "to protect. Robyn does not yet know how wrong the last part is",
         "She does not knock. She stands there a full ten seconds working "
         "out how to ask a near-stranger to be her girlfriend for money "
         "the station doesn't have"],
  syn="The list narrows to one name, for reasons that are true and also "
      "not remotely sufficient."),
S(4, "The Ask", "A", 2, "the overnight studio, gone midnight",
  "bargain_trade", "A", "B", "a cable and a cup of tea", "the-ask",
  "the ask lands badly; the first no",
  ["CE-04"],
  [("A", "B", "vulnerability", 0.06), ("A", "B", "trust", 0.08),
   ("B", "A", "resentment", 0.05), ("B", "A", "fear", 0.04)],
  0.38,
  beats=["Robyn over-explains for ninety seconds before Nadia has said a "
         "single word — the roof, the metric, the panel, Priya's stipend, "
         "the whole indispensable-caretaker machinery running at full speed",
         "Nadia lets her finish. Then: 'No.'",
         "Robyn keeps going, because stopping when told no is not a skill "
         "she has, and lists it again, differently, as though the shape of "
         "the ask was the problem and not the ask itself",
         "'You're not hearing me,' Nadia says, flat. 'I heard you the first "
         "time. I'm engineering that segment because nobody looks at me "
         "while I do it. You're asking me to be looked at on purpose'",
         "Robyn goes quiet, which surprises them both, and says the one "
         "true thing she has: 'I know. I'm asking anyway, because I've run "
         "out of people I'd rather ask'"],
  syn="Grumpy-sunshine opens at maximum distance: the ask exposes both "
      "flaws in one exchange — hers to manage, hers to withhold."),
S(5, "Terms", "B", 2, "the overnight studio, half past midnight", "negotiate_consent",
  "B", "A", "a list on the back of a cue sheet", "terms-agreed",
  "she agrees, with conditions, stated like a technical spec",
  ["CE-04"],
  [("B", "A", "trust", 0.08), ("A", "B", "trust", 0.06),
   ("A", "B", "respect", 0.05), ("B", "A", "respect", 0.05)],
  0.42, hot={"A-B": 0.44},
  beats=["Nadia takes a cue sheet off the desk and writes on the back of "
         "it, in block capitals, while Robyn watches: three conditions",
         "One: nothing physical that isn't discussed first, on air or off. "
         "Two: her actual job — the overnight desk, the fringe theatre "
         "contract — doesn't get mentioned, ever, as colour for the show. "
         "Three: if she says stop, on air or off, the segment ends there "
         "and nobody argues about it live",
         "'Say roughly eleven words to me in three years and then hand me "
         "a legal document,' Robyn says. 'That tracks'",
         "'Four of them were about a cable,' Nadia says, and it is the "
         "first thing resembling a joke either of them has made",
         "She signs nothing, because there is nothing to sign, but she "
         "reads the three lines back once, out loud, and that is the whole "
         "of the contract"],
  syn="Advance scene: the terms are set in Nadia's own register before "
      "either of them can call it a relationship of any kind."),
# ---------------------------------------------------------------- Phase 1
S(6, "On the Level", "A", 3, "the small meeting room off the kitchen",
  "probe_test", "A", "B", "a segment nobody has named yet", "format-meeting",
  "building the show; the name lands by accident",
  ["CE-04"],
  [("A", "B", "affection", 0.04), ("B", "A", "affection", 0.03)],
  0.34,
  beats=["A whiteboard, a kettle that takes four minutes, and forty "
         "minutes of trying to build a couples-advice format neither of "
         "them has ever done",
         "Nadia keeps answering hypothetical caller questions with levels "
         "and timings — 'that's a forty-second answer, tops, you'll lose "
         "the room' — which turns out to be, functionally, excellent "
         "producing",
         "Robyn tries a name — Thursday Hour, Two of Us, The Chat — and "
         "Nadia says, without looking up from the fader she's cleaning, "
         "'Call it On the Level. It's what the desk says when a signal's "
         "honest,' and doesn't notice she's said the whole premise of the "
         "show out loud",
         "It sticks before either of them decides it should"],
  syn="Workplace proximity opens: the show gets built out of one person's "
      "professional vocabulary and the other's desperation."),
S(7, "Three A.M.", "A", 4, "the yard behind the tenement; then the overnight studio",
  "deflect_withhold", "A", "C", "a roster with a hole in it", "shift-covered",
  "save-the-cat: she covers a shift herself rather than ask",
  [],
  [("A", "C", "trust", 0.04), ("A", "B", "respect", 0.05),
   ("B", "A", "respect", 0.04)],
  0.30,
  beats=["SAVE THE CAT: a volunteer cancels a three-a.m. slot with two "
         "hours' notice and Robyn takes it herself rather than wake anyone "
         "or ask for help, which is the whole of her flaw stated in action",
         "She is bad at it — wrong fader, wrong cart, a silence that runs "
         "eleven seconds too long — and Nadia, in mid-shift, fixes it from "
         "the next desk without comment, sliding a level across without "
         "being asked",
         "They sit in the dead hour after, two mugs of tea going cold, "
         "and don't talk about the show at all, which is the first time "
         "that's happened",
         "'You didn't have to do that,' Nadia says, meaning the shift, not "
         "the tea. 'I know,' Robyn says. 'I don't know how to not'"],
  syn="Robyn's flaw dramatized outside the fake-dating frame entirely, and "
      "witnessed by the one person who'll clock exactly what it costs her."),
S(8, "The Backstory", "A", 4, "the small meeting room", "bargain_trade",
  "A", "B", "an anniversary neither of them had", "rehearsal",
  "rehearsing a shared history that doesn't exist",
  [],
  [("A", "B", "affection", 0.05), ("B", "A", "affection", 0.04)],
  0.36,
  beats=["Building the cover story: how they met (true — the station), how "
         "long (a fabricated eight months, backdated to a date Priya picks "
         "for them off a rota), what they argue about (agreed: the radio, "
         "safely, because it's real)",
         "Nadia is better at lying specifically than Robyn expected, and "
         "worse at small talk than anyone Robyn has ever met, and the "
         "combination is very funny",
         "A rehearsed argument about whose turn it is to do the washing-up "
         "turns unexpectedly real for four seconds before either of them "
         "notices",
         "Robyn writes it all on an index card. Nadia reads it back once, "
         "flatly, and gets every beat of the joke exactly right, which "
         "should not be as unsettling as it is"],
  syn="Trope engine: fake-dating scaffolding built in a room, one comedic "
      "beat away from becoming true."),
S(9, "The Panel, Again", "A", 5, "the station foyer", "probe_test", "E", "A",
  "a blazer and a professional smile", "old-friend-distance",
  "Kirsty surfaces; the old wound named without being explained",
  [],
  [("A", "E", "resentment", 0.05), ("A", "E", "trust", -0.03)],
  0.40,
  beats=["Kirsty Lennox comes by 'to see the format in person,' which "
         "means the panel sent her, and stands in the foyer like someone "
         "who used to have a key",
         "Eight years ago they co-presented breakfast together for three "
         "years. Kirsty left for national radio. Robyn stayed, because "
         "someone had to, and has never once said out loud that she "
         "minded",
         "Kirsty is warm and professional and calls her 'Robyn' in the "
         "exact tone you'd use for someone you used to know",
         "Nadia watches the whole exchange from the desk without being "
         "introduced, and afterward says nothing about it, which Robyn "
         "notices and doesn't ask about either"],
  syn="Wound_A surfaces sideways: the person who left, being professionally "
      "kind about the person who stayed."),
S(10, "Four Words About a Cable", "A", 5, "the overnight studio, late", "reveal_misfire",
  "B", "A", "a podcast never named", "oblique-reveal",
  "Nadia gestures at the reason for the guard without opening it",
  ["CE-02"],
  [("B", "A", "vulnerability", 0.06), ("A", "B", "trust", 0.04)],
  0.38,
  beats=["Nadia, unprompted, at gone midnight: 'Before this goes further, "
         "there's a reason I don't do my voice in public and I'm not going "
         "to explain it. I need you to not need me to'",
         "Robyn, whose entire personality is managing other people's "
         "problems for them, does not manage this one. She says, 'Okay,' "
         "and means it, and doesn't ask again",
         "It costs Nadia visibly to have said even that much, and she "
         "changes the subject to a fader that's been sticking since March",
         "Robyn's restraint here is the first evidence of a version of "
         "herself she doesn't recognize"],
  syn="Nadia's flaw and Robyn's growth arc meet in the same four seconds: "
      "one edits in real time, the other, for once, doesn't manage it."),
S(11, "The Night Before", "A", 6, "the fire escape, above the studio", "negotiate_consent",
  "A", "B", "a stunt kiss, discussed like a cue", "grant-negotiated",
  "the on-air kiss is negotiated and granted before it happens",
  ["CE-01"],
  [("A", "B", "trust", 0.12), ("B", "A", "trust", 0.10),
   ("A", "B", "commitment", 0.06), ("B", "A", "commitment", 0.05),
   ("A", "B", "vulnerability", 0.06)],
  0.48, contact=None,
  consent={"kind": "ask", "act_class": "C2"},
  grants=[("A", "B", 2, "public"), ("B", "A", 2, "public")],
  beats=["Rain moving up the Clyde in sheets, seen from the fire escape; "
         "the ON AIR bulb glowing amber through the condensation two "
         "floors below",
         "'If the segment wants a kiss at the end of the hour, for the "
         "show, is that on the table,' Robyn asks, out loud, off mic, "
         "the night before broadcast one, because the taboo she will not "
         "cross is doing this to anyone without asking first",
         "Nadia thinks about it properly, the way she thinks about "
         "everything, and says yes, on the record between them: scripted, "
         "on air, at the end of the hour, nowhere else, and if it ever "
         "stops being that she says so",
         "PROMISE (CE-01, verbatim): 'What's real off that mic stays off "
         "the record. Every time. I promise you that,' Robyn says, meaning "
         "it as the actual foundation the fake thing sits on",
         "Neither of them names what a strange promise that is to need"],
  syn="Advance scene: consent negotiated in terms, on the page, before "
      "the taboo could ever be crossed — and a promise made that the plot "
      "will spend the whole book testing."),
# ---------------------------------------------------------------- Phase 2
S(12, "Sound Check", "A", 7, "the basement studio, 6 p.m., an hour to air",
  "probe_test", "C", "A", "a rundown with three question marks on it",
  "pre-broadcast",
  "nerves, texture, Priya running the desk like a small furious adult",
  [],
  [("A", "C", "trust", 0.04), ("A", "B", "vulnerability", 0.05)],
  0.42,
  beats=["Priya at the desk, headset on, treating the whole enterprise "
         "with the deadly seriousness of someone who has never once been "
         "allowed to be in charge of anything this size before",
         "The rundown: three questions from pre-screened callers, two "
         "musical stings, one planned kiss at 54 minutes",
         "Robyn checks her own reflection in a dark monitor and does not "
         "recognize the version of her face that's nervous about a fake "
         "thing",
         "Nadia, headphone cup off on one side as always, says, 'Levels "
         "are good. So are you,' and goes back to the desk before Robyn "
         "can do anything with that sentence"],
  syn="The pre-broadcast texture scene: the machinery of the fake thing, "
      "and one sentence that isn't."),
S(13, "On the Level (Broadcast One)", "A", 7, "the basement studio, live, 7-8 p.m.",
  "release_transform", "A", "B", "the stunt kiss, at 54 minutes", "first-broadcast",
  "SET PIECE (mandatory, Ph2): the first broadcast; the on-air kiss lands "
  "and something under the performance sparks",
  ["CE-01"],
  [("A", "B", "attraction_romantic", 0.14), ("B", "A", "attraction_romantic", 0.12),
   ("A", "B", "attraction_sexual", 0.08), ("B", "A", "attraction_sexual", 0.10),
   ("A", "B", "vulnerability", 0.08), ("B", "A", "vulnerability", 0.06)],
  0.58, contact={"class": "C2", "setting": "public"},
  beats=["SET PIECE (Ph2): On the Level goes out live for the first time. "
         "It is, against every reasonable expectation, good — three "
         "callers, one genuine laugh, Nadia dry and exact in a way that "
         "reads as devastating on air",
         "At 54 minutes, on cue, scripted, granted the night before on a "
         "fire escape: the kiss",
         "It lasts one second longer than the cue called for and neither "
         "of them corrects it in the room",
         "First_Kiss_Phase confirmed: performed, consented, on the record "
         "— and entirely unlike either of them expected a performance to "
         "feel",
         "Off mic, a half-second of eye contact that the microphone, for "
         "once, does not carry"],
  syn="The trope's engine turns over for real: the fake kiss is admissible, "
      "consented, public — and immediately, privately, not only that."),
S(14, "Backstage Static", "A", 7, "the corridor outside the studio, straight after air",
  "deflect_withhold", "B", "A", "a broadcast link used as a deflection", "aftermath",
  "both of them talk about the show instead of the kiss",
  [],
  [("A", "B", "respect", 0.04), ("B", "A", "respect", 0.03)],
  0.40,
  beats=["Off air, in the corridor, both of them talking very fast about "
         "the RUNDOWN, the STINGS, whether the second caller's story "
         "landed, anything with a technical name",
         "Broadcast links as deflection: Nadia does the outro voice one "
         "more time, unnecessarily, as a joke that is also clearly a way "
         "of not saying anything else",
         "Priya, watching both of them do this, says nothing, which from "
         "a seventeen-year-old is its own kind of commentary",
         "Neither says the word kiss out loud all evening"],
  syn="Signature move deployed: sound (the outro, the links, the levels) "
      "used to avoid faces and what's on them."),
S(15, "The Numbers Come In", "A", 8, "the office, next morning", "bargain_trade",
  "the funding review", "A", "a listener metric, better than expected", "reprieve",
  "the show works, on paper; the institution eases, provisionally",
  ["CE-04"],
  [("A", "the funding review", "fear", -0.05)],
  0.30,
  beats=["Overnight listenership up, for a Thursday slot that used to run "
         "a repeat of the shipping forecast",
         "An email from the panel's admin, not Kirsty: 'encouraging early "
         "engagement metrics,' which in panel language is the warmest "
         "sentence available",
         "Robyn allows herself, for about ninety seconds, to believe this "
         "might actually work, on every level she meant it to and one she "
         "didn't budget for",
         "Priya has already made a spreadsheet"],
  syn="Institutional texture: the fake thing is, structurally, succeeding."),
S(16, "Two A.M. Arithmetic", "A", 8, "Robyn's flat, alone, can't sleep", "probe_test",
  "A", "B", "a kiss, replayed in real time", "rumination", "anxious replay",
  [],
  [("A", "B", "vulnerability", 0.05)],
  0.36,
  beats=["Robyn's attachment style on full display: lying awake reverse-"
         "engineering one second of extra kiss for what it might have "
         "meant, running it the way she runs the roof budget, for meaning "
         "that isn't there to be found by arithmetic",
         "She drafts three texts to Nadia about it and sends none of them",
         "The flat is quiet in the specific way a flat is quiet when "
         "someone lives there entirely alone and has arranged it so that's "
         "comfortable",
         "She falls asleep still doing the sum"],
  syn="Fear_Profile_A in its native habitat: asking nobody anything, at "
      "volume, internally, at two in the morning."),
S(17, "Levels", "A", 9, "the overnight studio, a quiet night", "release_transform",
  "B", "A", "a level, held a beat too long", "held-look",
  "advance scene: the grumpy-sunshine dynamic softens, on Nadia's terms",
  ["CE-01"],
  [("B", "A", "affection", 0.14), ("A", "B", "affection", 0.10),
   ("B", "A", "trust", 0.10), ("A", "B", "trust", 0.08)],
  0.66, hot={"A-B": 0.66},
  beats=["Robyn brings tea down to the overnight desk unasked, which she "
         "has never once done for anyone she wasn't managing",
         "Nadia addresses the kiss exactly once, dryly, in her own "
         "register: 'that ran fifty-five seconds over a fifty-four-second "
         "cue. For the record'",
         "'For the record,' Robyn says",
         "A level held on the fader a beat longer than the desk requires, "
         "and Nadia looking up at exactly the same moment, and neither of "
         "them says one further word about it",
         "Advance: something between them has moved and both of them "
         "know it moved, even flat-footed and unwilling to name it"],
  syn="Grumpy-sunshine's promised payoff begins, entirely in Nadia's "
      "vocabulary, which is the only one she trusts."),
# ---------------------------------------------------------------- Phase 3
S(18, "The Brief for Broadcast Two", "A", 10, "the small meeting room", "probe_test",
  "A", "B", "a caller's letter about a shared bank account", "prep",
  "settling into a working rhythm; the bit gets easier and realer at once",
  [],
  [("A", "B", "affection", 0.05), ("B", "A", "affection", 0.04)],
  0.38,
  beats=["Prepping broadcast two off a genuinely tricky caller letter (a "
         "couple arguing about a shared account), which neither of them "
         "has to fake having an opinion about",
         "Nadia's producing instincts turn out to be excellent — she cuts "
         "two of Robyn's planned jokes for time and both cuts are correct",
         "A running bit forms without either of them building it on "
         "purpose: Nadia mutters the technical truth into the talkback "
         "and Robyn repeats it on air as though it were her own wisdom",
         "It stops feeling like homework"],
  syn="Trope payoff window opens (grumpy_sunshine arm phase1): the format "
      "becomes a real collaboration before it becomes a real relationship."),
S(19, "On the Level (Broadcast Two)", "A", 11, "the basement studio, live",
  "bargain_trade", "A", "B", "the shared-account caller, resolved kindly", "broadcast",
  "the second broadcast, told briefly, per the redundancy tightening on Ph2/Ph4",
  [],
  [("A", "B", "respect", 0.05), ("B", "A", "respect", 0.04)],
  0.44,
  beats=["Second broadcast, kept tight on the page: the caller's account "
         "problem turns out to have a real answer, and Nadia gives it, in "
         "character, better than the script had it",
         "No stunt beat this week — deliberately, so the show doesn't "
         "template into a kiss-of-the-week format, which both of them "
         "agree, off mic, would be worse for everyone including them",
         "A small crowd of regulars has started phoning in just to hear "
         "the two of them argue about the studio thermostat",
         "Priya's spreadsheet gets a second tab"],
  syn="Second broadcast deliberately understated, to keep the on-air "
      "framing from templating (Redundancy_Rules, Ph2/Ph4 windows)."),
S(20, "Not For the Show", "A", 12, "a chip shop on Byres Road, off shift",
  "release_transform", "A", "B", "chips, eaten on a wall, unfilmed", "voluntary",
  "the first hangout neither of them needed to have",
  [],
  [("A", "B", "affection", 0.08), ("B", "A", "affection", 0.07),
   ("A", "B", "commitment", 0.05), ("B", "A", "commitment", 0.04)],
  0.46,
  beats=["Off shift, off air, no contract requiring it: chips on a wall "
         "outside a chip shop on Byres Road, because Nadia said she was "
         "hungry and Robyn, for once, didn't turn it into a task",
         "Sound described before faces: the fryer's roar through the open "
         "door, a bus changing gear on the hill, rain starting somewhere "
         "up the street before it reaches them — and then, only then, "
         "Nadia's face, unguarded, laughing at something small",
         "Nothing about the show is discussed for forty minutes, which is "
         "a record",
         "Walking back, their hands are near enough to touch and don't, "
         "on purpose, by mutual unspoken agreement, which is its own kind "
         "of held note"],
  syn="Signature move (sound before faces) deployed on the page for the "
      "first time in a scene that owes nothing to the performance."),
S(21, "The Contract Offer", "B", 12, "the overnight studio, after the chip shop",
  "reveal_misfire", "B", "A", "a fringe theatre contract, unopened on the desk",
  "vulnerable-admission",
  "Nadia names the exit she keeps refusing to take",
  [],
  [("B", "A", "vulnerability", 0.14), ("A", "B", "trust", 0.10),
   ("B", "A", "trust", 0.08), ("A", "B", "vulnerability", 0.06)],
  0.78, hot={"A-B": 0.78},
  beats=["An envelope on the overnight desk Robyn hasn't noticed before: a "
         "touring theatre company's contract, sound designer, six months, "
         "unopened for three weeks",
         "'I keep telling everyone I don't want it,' Nadia says. 'I've "
         "told you that. It isn't true. I don't want to want it, which "
         "isn't the same thing and I know it isn't'",
         "The real fear surfaces at an angle: touring put her in front of "
         "people, and being in front of people is what the podcast turned "
         "into something she still can't fully talk about",
         "'Why haven't you opened it,' Robyn asks. 'Because there's a "
         "reason to stay that isn't the roof,' Nadia says, and doesn't "
         "finish the sentence, and doesn't have to",
         "Advance: the vulnerability admitted is real, unscheduled, and "
         "costs Nadia more than anything on air ever has"],
  syn="Advance scene: Subplot_B's exit door is named out loud, and so, "
      "obliquely, is the reason it stays shut."),
# ---------------------------------------------------------------- Phase 4
S(22, "London Calling, Again", "A", 13, "Robyn's flat, an email re-opened", "probe_test",
  "E", "A", "a five-week-old job offer", "reminder",
  "the secret resurfaces; the obligation clock starts visibly ticking",
  ["CE-04"],
  [("A", "E", "resentment", 0.04), ("A", "B", "vulnerability", -0.02)],
  0.42,
  beats=["A calendar reminder Robyn set herself and forgot about: 'answer "
         "London,' five weeks old, still sitting there",
         "Kirsty, texting 'just checking in about the format, no pressure "
         ":)', which is somehow the most pressure available in the English "
         "language",
         "The London job: senior producer, national reach, twice the "
         "money, a version of the career she thought she wanted at "
         "twenty-six",
         "She doesn't tell Nadia it's resurfaced. She notices herself not "
         "telling her, which is new"],
  syn="Secret_A's clock restarts, publicly adjacent (via E) though not yet "
      "disclosed to B."),
S(23, "On the Level (Broadcast Three)", "A", 14, "the basement studio, live",
  "reveal_misfire", "A", "B", "a caller who asks the real question", "call-in",
  "SET PIECE (mandatory, Ph4): the listener call-in neither can answer in character",
  ["CE-01"],
  [("A", "B", "vulnerability", 0.10), ("B", "A", "vulnerability", 0.10),
   ("A", "B", "trust", 0.06), ("B", "A", "trust", 0.06)],
  0.46,
  beats=["SET PIECE (Ph4): a caller — real, unscreened, patched through by "
         "mistake — asks, 'how did you know you could trust each other "
         "completely,' meaning it, waiting for an answer",
         "The scripted answer is on the rundown. Neither of them reaches "
         "for it",
         "What comes out instead is true and un-cued and about the "
         "overnight desk and the three-a.m. shift and a fader slid across "
         "without being asked, none of which the audience knows the "
         "context for and all of which is real",
         "MIDPOINT: the performance becomes true off mic — except this "
         "time it happens on mic, half a beat, before either of them "
         "catches it and cues the next segment",
         "Off air, both of them are shaking slightly and neither says why"],
  syn="Midpoint set piece: the performance and the truth touch, live, in "
      "front of an audience, for about four unscripted seconds."),
S(24, "Processing the Four Seconds", "A", 14, "the corridor, straight after air",
  "bargain_trade", "A", "B", "the four seconds that weren't in the rundown",
  "aftermath",
  "both scared and thrilled by what nearly happened out loud",
  [],
  [("A", "B", "affection", 0.06), ("B", "A", "affection", 0.05)],
  0.44,
  beats=["'That wasn't in the rundown,' Nadia says, which from her is "
         "practically a confession",
         "'No,' Robyn agrees. Neither elaborates for a while",
         "They stand in the corridor not quite looking at each other, "
         "both aware something has shifted that a rundown can't route "
         "around anymore",
         "Priya, walking past with a mic stand, says, 'you two are "
         "insufferable,' with real affection, and keeps walking"],
  syn="A held beat: the near-miss processed without either of them being "
      "brave enough yet to name what it was."),
S(25, "The Voicemail", "A", 15, "Robyn's flat; her mother's old answering machine",
  "deflect_withhold", "A", "A", "a tape nobody has played since the funeral",
  "private-grief",
  "the absence surfaces; not yet resolved",
  ["CE-03"],
  [("A", "the funding review", "fear", 0.03)],
  0.36,
  beats=["A box from the loft, opened for an unrelated reason (looking "
         "for an old contract of her own, ironically), with an answering "
         "machine tape of her mother's voice on it, unplayed since the "
         "funeral",
         "Robyn's whole adult architecture, laid bare for one page: she "
         "became indispensable at nineteen because someone had to be, and "
         "has never once stopped since, not even to grieve on a fixed "
         "schedule",
         "She doesn't play the tape. She puts it back in the box. She "
         "does, for the first time in years, let herself cry about it for "
         "four minutes with the timer on her phone running, because that "
         "is the only way she knows how to permit herself anything",
         "She tells nobody. Not yet"],
  syn="CE-03 (Absence) surfaces properly for the first time: private, "
      "unwitnessed, and structurally overdue."),
S(26, "Answering London", "A", 16, "Kelvin Row Radio, the office, after hours",
  "release_transform", "A", "the funding review", "an email, finally sent",
  "obligation-closed",
  "she declines the offer; the first time she states a want out loud",
  ["CE-04"],
  [("A", "the funding review", "fear", -0.06), ("A", "B", "trust", 0.10),
   ("B", "A", "trust", 0.08), ("A", "B", "vulnerability", 0.08)],
  0.54,
  close=["CE-04"],
  beats=["Robyn writes the email declining London properly, for real "
         "reasons this time and not out of inertia: the station, the "
         "roof, and — she makes herself type it — a reason she isn't "
         "ready to say out loud yet but is ready to act on",
         "She tells Nadia about the offer for the first time, the whole "
         "of it, including that it sat unanswered for five weeks because "
         "answering it felt like asking for something and being told no",
         "Nadia doesn't perform relief and doesn't manage the moment for "
         "her. She just listens, all the way through, which is its own "
         "kind of answer",
         "Growth_Arc_A beat: the first time in the book Robyn states a "
         "want — staying — out loud, to someone, without it being "
         "necessary for the show",
         "Advance: obligation discharged, and something realer put in "
         "its place"],
  syn="CE-04 closes: the job offer answered, and the answer is itself the "
      "book's first honest declaration of desire."),
# ---------------------------------------------------------------- Phase 5
S(27, "On the Level (Broadcast Four)", "A", 18, "the basement studio, live", "probe_test",
  "A", "B", "a caller argument about chores, gently mediated", "broadcast",
  "kept light-touch, per the Ph2/Ph4 redundancy tightening extended by habit",
  [],
  [("A", "B", "respect", 0.04), ("B", "A", "respect", 0.03)],
  0.42,
  beats=["Fourth broadcast, brief on the page by now, both of them "
         "genuinely good at it: a chores argument mediated with real "
         "warmth, no stunt beat, no near-miss",
         "The show has stopped needing engineering. It just runs, which "
         "terrifies Robyn slightly more than when it didn't",
         "A listener writes in asking where they got engaged, which "
         "neither of them has an answer prepared for and both of them "
         "improvise past, badly, live, laughing"],
  syn="A quiet, competent broadcast — the calm before the deepening that's "
      "about to happen off mic."),
S(28, "Off the Air, For Real", "A", 19, "Nadia's flat, a genuinely off-duty evening",
  "negotiate_consent", "A", "B", "a real kiss, asked for first", "private-grant",
  "a private consent negotiation, distinct from the performance grant",
  [],
  [("A", "B", "trust", 0.10), ("B", "A", "trust", 0.10),
   ("A", "B", "vulnerability", 0.08), ("B", "A", "vulnerability", 0.08)],
  0.50,
  consent={"kind": "ask", "act_class": "C2"},
  grants=[("A", "B", 2, "private"), ("B", "A", 2, "private")],
  beats=["Nadia's flat: a record player, a kettle that takes even longer "
         "than the station's, no cameras, no cue sheet",
         "'If I wanted to do that again,' Robyn says, 'not for the show, "
         "not at 54 minutes — would that be alright,' because the terms "
         "from the fire escape were scoped to the broadcast and she isn't "
         "going to assume they cover this",
         "Nadia takes the question as seriously as she takes everything, "
         "and says yes, and means it as something new, private, hers to "
         "give this time rather than agreed-to as a segment",
         "A private grant, standing, distinct from the public one — the "
         "book's second consent negotiation, quieter than the first"],
  syn="A second, private grant, deliberately distinct from the performance "
      "one: real consent for a real thing, asked for in its own right."),
S(29, "The Real One", "A", 19, "Nadia's flat, later the same evening", "release_transform",
  "A", "B", "a kiss with nobody counting the seconds", "real-kiss",
  "the private kiss, under the new grant, unhurried",
  [],
  [("A", "B", "attraction_romantic", 0.10), ("B", "A", "attraction_romantic", 0.10),
   ("A", "B", "commitment", 0.08), ("B", "A", "commitment", 0.08)],
  0.52, contact={"class": "C2", "setting": "private"},
  beats=["The kiss that isn't for a rundown, doesn't hit a cue, and isn't "
         "over in fifty-five seconds because nobody's counting",
         "Nadia laughs afterward, once, an unguarded sound Robyn has "
         "never heard her make on air or off",
         "Neither of them reaches for a broadcast link to deflect with. "
         "There isn't one available, and for the first time that's a "
         "relief rather than a problem",
         "It is very quietly the best evening either of them can name"],
  syn="The private grant realized: a kiss with no audience, no timing, and "
      "no performance in it at all."),
S(30, "The Tape", "A", 20, "Robyn's flat, evening", "bargain_trade", "B", "A",
  "an old cassette player, borrowed without being asked", "grief-witnessed",
  "the absence is given real space, not solved",
  ["CE-03"],
  [("A", "B", "trust", 0.10), ("B", "A", "affection", 0.08),
   ("A", "B", "vulnerability", 0.10)],
  0.56,
  close=["CE-03"],
  beats=["Nadia turns up with a cassette player from the station store "
         "cupboard, unasked, because Robyn mentioned the tape once, in "
         "passing, and Nadia's love language is doing the practical thing "
         "rather than saying the soft one",
         "Robyn plays four seconds of her mother's voice and then turns "
         "it off, and Nadia doesn't fill the silence and doesn't fix it "
         "and doesn't tell her it's alright, she just sits there, present, "
         "for as long as it takes",
         "'You don't have to be the reliable one in this room,' Nadia "
         "says, eventually. 'I'm not going anywhere because you cried at "
         "a cassette player'",
         "CE-03 closes here — not resolved, not tidied, just witnessed, "
         "which turns out to be the entire thing Robyn actually needed"],
  syn="CE-03 (Absence) closes through acts of service and simple presence, "
      "rather than through any fix."),
S(31, "Interrupted", "A", 21, "the overnight studio, later that week", "probe_test",
  "A", "B", "a hand, half raised, and a phone going off", "almost",
  "advance scene: the charge peaks and is interrupted, deliberately unresolved",
  [],
  [("A", "B", "attraction_romantic", 0.12), ("B", "A", "attraction_romantic", 0.12),
   ("A", "B", "attraction_sexual", 0.10), ("B", "A", "attraction_sexual", 0.10)],
  0.84, hot={"A-B": 0.84},
  beats=["A quiet night at the desk, both of them working late for no "
         "practical reason except that neither wants to leave",
         "The room narrows the way a room does; Robyn's hand goes to "
         "Nadia's jaw, unhurried, and Nadia leans into it before either of "
         "them has said a word",
         "Priya's key in the front door lock, badly timed, entirely "
         "innocent, ends it before it becomes anything more than that",
         "Both of them laugh about it, too loudly, too fast, in the "
         "specific way of two people who were about a second from "
         "something neither has said out loud yet",
         "Advance: the anticipation is doing more work now than any "
         "single scene could"],
  syn="Advance scene: maximum private charge, interrupted on purpose, "
      "just ahead of the phase that will finally let it land."),
# ---------------------------------------------------------------- Phase 6
S(32, "Static", "A", 22, "Nadia's flat, very late", "reveal_misfire", "B", "A",
  "a segment's real author, named for the first time", "identity-revealed",
  "CE-02 closes: Nadia tells her the truth about Static",
  ["CE-02"],
  [("B", "A", "vulnerability", 0.15), ("B", "A", "emotional_safety", 0.06),
   ("A", "B", "trust", 0.14), ("B", "A", "trust", 0.10)],
  0.62,
  close=["CE-02"],
  beats=["'Before anything else happens,' Nadia says, 'there's a thing I "
         "need you to know, and I need to say it once, and I don't want "
         "you to make a face about it while I do'",
         "REVELATION (CE-02): Nadia is the anonymous voice behind Static, "
         "the station's most-loved late-night segment — has been for two "
         "years, unpaid, uncredited, because being unseen was the entire "
         "point",
         "The reason, finally in full: the touring years, the "
         "relationship that ended in public, the podcast made about it "
         "that still exists and that she has never once listened to all "
         "the way through",
         "'I stopped being a person people talked about and started being "
         "a voice with a desk in front of it. It's the only shift I've "
         "ever felt safe on'",
         "Robyn does not make a face about it. She says, 'I know exactly "
         "which nights Static ran and which nights you looked like you "
         "hadn't slept,' which is its own kind of answer"],
  syn="Advance scene: Secret_B disclosed privately, ahead of any public "
      "reveal — the trust the whole rest of the book will be tested on."),
S(33, "Before Anything Else", "A", 22, "Nadia's flat, the same night", "negotiate_consent",
  "A", "B", "the terms for something real, said in full", "grant-negotiated",
  "SET PIECE (mandatory, Ph6): the consent negotiation before first C3 contact",
  [],
  [("A", "B", "trust", 0.10), ("B", "A", "trust", 0.10),
   ("A", "B", "emotional_safety", 0.10), ("B", "A", "emotional_safety", 0.10)],
  0.58,
  consent={"kind": "ask", "act_class": "C3"},
  grants=[("A", "B", 3, "private"), ("A", "B", 4, "private"),
          ("B", "A", 3, "private"), ("B", "A", 4, "private")],
  beats=["SET PIECE (Ph6): a full, unhurried conversation about what they "
         "both actually want, off any mic, with both fears named plainly "
         "— Nadia's, of being loved as a bit rather than as herself; "
         "Robyn's, of asking for something and being told no where it "
         "could be counted",
         "'This isn't for the panel,' Robyn says. 'I need you to hear "
         "that as its own sentence.' 'I know,' Nadia says. 'I wouldn't be "
         "here if I thought it was'",
         "Consent given fully, mutually, in words, for whatever comes "
         "next, with the same seriousness Nadia brought to a cue sheet in "
         "week one",
         "Both fear profiles named out loud in the same room, which is "
         "itself the growth-arc payoff arriving early, before the plot "
         "has finished testing it"],
  syn="Mandatory set piece: consent is not assumed from the earlier private "
      "kiss — it is asked for again, in full, before anything further."),
S(34, "First, and Real", "A", 22, "Nadia's flat, that night", "release_transform",
  "A", "B", "the first time neither of them is performing anything",
  "first-intimacy",
  "First_Intimacy_Phase confirmed, closed-door per Heat 2",
  [],
  [("A", "B", "attraction_romantic", 0.12), ("B", "A", "attraction_romantic", 0.12),
   ("A", "B", "commitment", 0.14), ("B", "A", "commitment", 0.14),
   ("A", "B", "emotional_safety", 0.08), ("B", "A", "emotional_safety", 0.08)],
  0.60, contact={"class": "C4", "setting": "private"},
  beats=["What happens next happens off the page, in the specific way "
         "Heat 2 asks for: the door closes on the scene at the point "
         "where anything further belongs to them and not to the reader",
         "What's on the page instead: two people who have spent six weeks "
         "performing a couple for an audience, finally alone, with no "
         "audience, no cue sheet, and nothing left to fake",
         "Morning finds them still there, unhurried, neither one first up "
         "to leave"],
  syn="First_Intimacy_Phase 6 realized, closed-door, under the full grant "
      "negotiated the same evening."),
S(35, "The Morning After, Actually", "A", 23, "Nadia's flat, morning", "bargain_trade",
  "A", "B", "a plan to tell the truth on their own terms, eventually",
  "tender-morning",
  "real, happy, and quietly planning to control their own disclosure",
  [],
  [("A", "B", "affection", 0.10), ("B", "A", "affection", 0.10),
   ("A", "B", "commitment", 0.06), ("B", "A", "commitment", 0.06)],
  0.48,
  beats=["Tea, badly made, on a kitchen counter that has never once been "
         "photographed for the show",
         "They talk, properly, about telling the truth eventually — to "
         "the panel, to the listeners — on their own timeline, once the "
         "contract's six weeks are up and nobody can call it a stunt",
         "'Two more broadcasts,' Nadia says. 'Then it's just us, and we "
         "decide what anyone gets told, and when'",
         "Dramatic irony sits quietly in the room with them, entirely "
         "unnoticed"],
  syn="A held, happy, ordinary morning — the calm directly before the "
      "black moment, structured to make the fall further."),
S(36, "Hot Mic", "A", 23, "Kelvin Row Radio, the tech cupboard; then everywhere",
  "realign_betray", "the funding review", "B", "a private line, aired by accident",
  "black-moment",
  "the private moment gets broadcast; Nadia's exact fear made literal",
  ["CE-01"],
  [("B", "A", "fear", 0.15), ("B", "A", "emotional_safety", -0.15),
   ("B", "A", "trust", -0.10), ("A", "B", "vulnerability", 0.10),
   ("A", "the funding review", "fear", 0.10)],
  0.55, hot={"A-B": 0.30},
  misfire=["CE-01"],
  beats=["BLACK MOMENT (Ph6, mandatory beat category: private moment "
         "broadcast): a recording of the two of them talking — real, "
         "private, made in the tech cupboard weeks ago while testing a "
         "mic, never meant to leave the machine it was on — plays out "
         "over the station's automated overnight feed",
         "It is nobody's malice. Priya, updating the automation queue, "
         "drags the wrong file. It is the single most ordinary kind of "
         "accident there is, and it does not matter that it's ordinary",
         "What airs includes Nadia's own voice, unguarded, saying things "
         "about the podcast and about being loved as a bit that she has "
         "never said to anyone else in the world, now sitting on a public "
         "feed with a timestamp on it",
         "ALL IS LOST (adjacent): within the hour, the panel's office "
         "calls to say the renewal is being reconsidered — 'manufactured "
         "content becoming a liability' — the review effectively refused",
         "The promise misfires here, through nobody's fault and every "
         "fault at once: what was real off that mic did not, this once, "
         "stay off the record, and Nadia does not care that it was an "
         "accident. She shuts the door on the overnight studio and does "
         "not come out"],
  syn="Fracture: the black moment lands exactly on Nadia's stated fear, "
      "and the promise that was supposed to prevent it breaks by accident, "
      "which is somehow worse than on purpose."),
# ---------------------------------------------------------------- Phase 7
S(37, "The Door Stays Shut", "A", 24, "outside the overnight studio, the next three days",
  "deflect_withhold", "B", "A", "a door that doesn't open", "estrangement",
  "Nadia retreats completely; Robyn is refused at every attempt",
  [],
  [("B", "A", "resentment", 0.08), ("A", "B", "vulnerability", 0.10)],
  0.50,
  beats=["Three days of a closed studio door, texts read and not "
         "answered, and Nadia doing her actual shifts with headphones on "
         "and both cups sealed for the first time since Robyn has known "
         "her",
         "The theatre contract, still on the desk, no longer quite so "
         "unopened",
         "Robyn tries every register she owns — apology, explanation, "
         "silence, more apology — and every one of them lands as "
         "management, which is exactly the thing Nadia asked her, at the "
         "very start, never to make this",
         "'I'm not asking you to fix it,' Nadia says, once, through a "
         "half-open door. 'I'm asking you to understand that you can't'"],
  syn="Estrangement beat: Robyn's caretaker instinct, the thing that got "
      "them here, is now precisely the thing that can't get them out."),
S(38, "What Kirsty Said", "A", 25, "a coffee shop near the Chambers", "reveal_misfire",
  "E", "A", "an apology eight years overdue", "outside-perspective",
  "Kirsty's own guilt reframes the choice between performing and choosing",
  [],
  [("A", "E", "resentment", -0.06), ("A", "E", "trust", 0.06)],
  0.46,
  beats=["Kirsty, off the clock, admits she left breakfast radio eight "
         "years ago partly because staying meant being seen failing at it "
         "in public, and national radio let her fail privately instead",
         "'I've spent eight years telling myself I made the ambitious "
         "choice,' Kirsty says. 'I made the safe one and called it "
         "ambition. You're the one who stayed and did the hard, visible, "
         "unglamorous thing, and I've never once said that to you "
         "properly'",
         "It isn't absolution and it isn't really about Nadia at all, but "
         "it hands Robyn the exact distinction she's been missing: "
         "performing safety versus actually choosing something, out loud, "
         "where it can be refused",
         "Robyn leaves the coffee shop knowing what she has to do and "
         "still not knowing if it will work"],
  syn="An unexpected redemptive beat from the institution's human face: "
      "the choice reframed from safety-versus-risk to performance-versus-"
      "truth."),
S(39, "What She's Not Rehearsing", "A", 26, "outside Nadia's flat, evening",
  "release_transform", "A", "B", "a key, held out, not used", "reaching-out",
  "Robyn reaches for something costly and real, cautiously received",
  [],
  [("A", "B", "vulnerability", 0.14), ("B", "A", "trust", 0.06),
   ("B", "A", "vulnerability", 0.04), ("B", "A", "resentment", 0.06)],
  0.60,
  beats=["Robyn goes to the flat with nothing rehearsed for the first "
         "time in the whole book — no cue sheet, no format, no managed "
         "line",
         "'I can't fix what happened to you,' she says, through the "
         "closed door. 'I'm not going to try. I'm asking for one thing: "
         "Thursday. Not for the panel. Because it's the last scheduled "
         "show and I would like it to be honest, and I can't make it "
         "honest without you, and I know that's not fair to ask'",
         "The door doesn't open. But it doesn't stay silent either — "
         "'I'll think about it' is the whole answer, delivered flatly, "
         "through wood, and it is the first uncertain yes the book has "
         "had",
         "Robyn walks home not knowing, which — for a woman who manages "
         "everything to a known outcome — is itself a kind of growth"],
  syn="Fracture-adjacent: the reach for something real, costly, and "
      "explicitly not guaranteed to work."),
S(40, "On the Level (Broadcast Six)", "A", 26, "the basement studio, live, the final scheduled show",
  "release_transform", "B", "A", "the mic, handed over, on purpose", "off-script-finale",
  "CE-01 closes: the promise redeemed on air, live, on the record, by choice",
  ["CE-01"],
  [("B", "A", "vulnerability", 0.15), ("A", "B", "trust", 0.14),
   ("B", "A", "trust", 0.15), ("A", "B", "commitment", 0.12),
   ("B", "A", "commitment", 0.14), ("B", "A", "fear", -0.14),
   ("B", "A", "resentment", -0.10)],
  0.85,
  close=["CE-01"],
  beats=["SET PIECE (mandatory, Ph7, Climax_Mode: off_script_broadcast): "
         "Nadia is at the desk at 6:58 p.m., in headphones, both cups on "
         "this time, and says nothing except, 'we're live in ninety "
         "seconds, get to the desk'",
         "The rundown is abandoned in the first two minutes. Robyn hands "
         "the show over — literally hands Nadia the second mic — and "
         "says, on air, live, 'this is Nadia. She's been Static for two "
         "years and she's about to tell you why, if she wants to, and if "
         "she doesn't, that's the whole segment and we'll play a song'",
         "REUNION (public_correction): Nadia takes the mic, and chooses, "
         "on her own terms and in her own words, to tell the truth about "
         "Static, about the podcast, about being loved as a bit and "
         "deciding, live, not to be that anymore — the reveal Continuity_"
         "Constraints held back through Phase 6, released now because she "
         "is choosing it",
         "PROMISE REDEEMED (verbatim): 'What's real off that mic stays "
         "off the record,' Robyn says again, on air, 'and everything "
         "she's just told you, she chose to put on the record herself. "
         "That's the difference, and it's the only one that matters'",
         "CE-01 closes: not by nothing bad ever happening again, but by "
         "the choice, this time, belonging entirely to the person it's "
         "about"],
  syn="Climax set piece: the final broadcast runs off script, on the "
      "record, and the promise that misfired in the black moment is "
      "redeemed in the open, live, by handing over the exact control that "
      "was taken from Nadia by accident."),
# ---------------------------------------------------------------- Phase 8
S(41, "Off Air, For the Last Time That Matters", "A", 26, "the basement studio, straight after",
  "release_transform", "A", "B", "a hand, not half raised this time", "private-reunion",
  "the private reunion completes what the public one started",
  [],
  [("A", "B", "affection", 0.10), ("B", "A", "affection", 0.12),
   ("A", "B", "commitment", 0.08), ("B", "A", "commitment", 0.08)],
  0.40,
  beats=["The ON AIR bulb goes dark — amber, still, never fixed — and the "
         "two of them stand in a basement that smells of damp and cable "
         "insulation and say nothing useful for a while",
         "'You didn't have to hand me the mic,' Nadia says. 'I know,' "
         "Robyn says. 'I wanted you to have it before you decided whether "
         "you wanted it'",
         "Whatever finishes here finishes privately, off any record, "
         "which is exactly and only how either of them would have wanted "
         "it"],
  syn="The private half of the reunion, deliberately undramatized, kept "
      "off the record on purpose, as the promise's whole point demanded."),
S(42, "The Phones Don't Stop", "A", 27, "Kelvin Row Radio, the next morning", "bargain_trade",
  "the funding review", "A", "a voicemail box, full by nine a.m.", "public-reaction",
  "the honest finale resonates; institutional fear starts to thaw",
  [],
  [("A", "the funding review", "fear", -0.08), ("A", "the funding review", "resentment", -0.04)],
  0.36,
  beats=["The voicemail box is full by nine, mostly listeners, mostly "
         "kind, several of them naming their own version of being loved "
         "as a bit and being glad to hear someone say it back",
         "A regional paper runs 220 words under the headline COMMUNITY "
         "RADIO'S HONEST FINALE, which is not the coverage a stunt "
         "usually gets",
         "Priya's spreadsheet gets a third tab, entirely unprompted, "
         "titled simply GOOD NEWS",
         "The panel's silence, for once, does not read as a threat"],
  syn="Texture scene: public and institutional reaction to the finale, "
      "setting up the renegotiated terms."),
S(43, "Terms Renegotiated", "A", 44, "the committee room, Glasgow City Chambers annexe",
  "negotiate_consent", "A", "the funding review", "a licence, on different terms",
  "resolution-mode",
  "RESOLUTION (mandatory clock beat): the funding decision lands, unmoved from day 44",
  [],
  [("A", "the funding review", "fear", -0.10), ("A", "E", "trust", 0.08),
   ("A", "E", "resentment", -0.06)],
  0.34,
  beats=["Day 44, exactly where the clock always said it would land: the "
         "renewal is approved, not on the original engagement metric but "
         "on a rewritten one — Static named and funded outright, a "
         "dedicated line item, no longer something that has to hide "
         "inside a stunt to survive",
         "Kirsty argues for it in the room, plainly, on the record, in a "
         "way that costs her something with the rest of the panel",
         "Afterward, in the corridor: 'I should have said what I said in "
         "the coffee shop a long time ago,' Kirsty says. 'For what it's "
         "worth, I'm glad you stayed.' 'I'm glad you're saying it now,' "
         "Robyn says, and means it, and that's the whole repair either of "
         "them needs",
         "RESOLUTION_MODE confirmed: terms renegotiated, not simply "
         "restored — the show survives changed, not merely spared"],
  syn="Mandatory clock beat: the funding decision, unmoved from day 44, "
      "resolved as a renegotiation rather than a rescue."),
S(44, "The Roster, Fixed", "A", 45, "Kelvin Row Radio, the following week",
  "bargain_trade", "C", "A", "a roster with no holes in it", "station-family",
  "Priya's arc closes; the caretaker learns to delegate",
  [],
  [("A", "C", "trust", 0.08), ("A", "C", "respect", 0.06),
   ("C", "A", "trust", 0.06)],
  0.32,
  beats=["Priya, formally paid now out of the renegotiated budget, hires "
         "two more volunteers off her own initiative and hands Robyn a "
         "finished roster instead of a problem",
         "'You didn't have to run this past me,' Robyn says. 'I know,' "
         "Priya says. 'That was the point. Try it — not asking'",
         "Robyn tries it. It's uncomfortable, and she does it anyway, "
         "which is the whole of Growth_Arc_A completed in one small "
         "administrative act",
         "Nadia, at the desk, headphone cup off on one side as always, "
         "doesn't say anything, just catches Robyn's eye across the room "
         "in the exact way she did in week one, except everything about "
         "what it means has changed"],
  syn="Subplot_A resolved: the caretaker delegates, on purpose, and "
      "survives the discomfort of it."),
S(45, "Out of Office", "A", 46, "the basement studio, an ordinary Thursday, off air",
  "release_transform", "A", "B", "a sign on a door, finally accurate", "hfn",
  "HFN: no performance left standing between them; the title recontextualized",
  [],
  [("A", "B", "commitment", 0.10), ("B", "A", "commitment", 0.10),
   ("A", "B", "affection", 0.08), ("B", "A", "affection", 0.08)],
  0.30,
  beats=["An ordinary Thursday with nothing scheduled: the amber bulb "
         "still not fixed, the kettle still taking four minutes, Priya "
         "running a roster that no longer needs Robyn in it",
         "Growth_Arc_B payoff: asked, plainly, how she is, Nadia answers "
         "the actual question for once, in words, not levels — 'Good. "
         "Better than good. I keep waiting for the segment to end and it "
         "doesn't,' — the verbal tic finally, deliberately, set aside",
         "Robyn writes a sign for the studio door as a joke that isn't "
         "entirely a joke: OUT OF OFFICE, in Priya's careful hand, "
         "propped against the amber bulb whenever the two of them are "
         "actually off the clock, which is a category that exists now "
         "and didn't used to",
         "Title recontext: out of office was never about being away from "
         "the desk. It's the one hour a week that belongs to nobody's "
         "audience but them",
         "HFN, not HEA: no proposal, no five-years-later — just two "
         "people who have stopped performing anything for anyone, "
         "including, finally, each other, choosing to come back to the "
         "same room on purpose, with nothing to broadcast"],
  syn="Title recontext and HFN close: the fake thing is entirely gone, "
      "and what's left is smaller, realer, and chosen daily rather than "
      "scripted once."),
]

SCENE = {s["scene"]: s for s in SCENES}

CHAPTERS = [
    (1, "The Panel", [1, 2]),
    (2, "The Only Candidate", [3, 4]),
    (3, "Terms", [5]),
    (4, "On the Level", [6, 7]),
    (5, "The Backstory", [8, 9]),
    (6, "Four Words About a Cable", [10, 11]),
    (7, "Sound Check", [12, 13, 14]),
    (8, "The Numbers Come In", [15, 16]),
    (9, "Levels", [17]),
    (10, "The Brief for Broadcast Two", [18, 19]),
    (11, "Not For the Show", [20, 21]),
    (12, "London, Again", [22, 23]),
    (13, "The Voicemail", [24, 25]),
    (14, "Answering London", [26]),
    (15, "Off the Air, For Real", [27, 28, 29]),
    (16, "The Tape", [30, 31]),
    (17, "Static", [32, 33]),
    (18, "First, and Real", [34, 35]),
    (19, "Hot Mic", [36]),
    (20, "The Door Stays Shut", [37, 38]),
    (21, "What She's Not Rehearsing", [39]),
    (22, "On the Level (Broadcast Six)", [40, 41]),
    (23, "Terms Renegotiated", [42, 43]),
    (24, "Out of Office", [44, 45]),
]
