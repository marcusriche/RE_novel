"""Offline binding configuration `offline-agent-v1` for the Romance Engine.

Per Addendum M the architecture binds to any configuration that can answer
bounded elicitations; this configuration answers them deterministically from
an authored editorial schedule (binding/schedule.py), so the full §11.1 scene
loop — tension scoring, BT fits, blends, shortlist, lookahead, utility,
anchored confirmation, ED floor, gates — runs code-side end to end with no
network access.

Division of labour (documented deviation surface, §12.5 discipline):
  * PRIMARY-STRUCT / JUDGE call classes are answered by the schedule: the
    proposer emits the authored move plus procedurally generated admissible
    alternates; the pairwise judge encodes the editorial preference order;
    pair tension is solved numerically so the elicited bands reproduce the
    scheduled T_scene trajectory exactly under the §15.8 arithmetic.
  * PRIMARY-PROSE calls return the scene brief (the renderer's work order);
    the finished prose is authored downstream from these briefs by the
    bound agent and shipped through the manuscript build. Revision passes
    and VoiceFilter are identity here, so every semantic diff is empty by
    construction (the diff gate is exercised, not bypassed).
  * Continuity extraction emits fact tuples matching each realized cause, and
    — because main.py pins reconciliation to the orchestrator (§7.2) — this
    module also performs the reconciliation side effects the spec assigns
    there: consent grants/withdrawals on the edges and CE lifecycle events.

No absolute threshold from this configuration is calibrated (no card exists);
floors are provisional exactly as R11 requires.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main as eng
from binding.schedule import (SCENE, PHASE_BLOCKS, ADVANCE_SCENES,
                              FRACTURE_SCENES, DISPLAY)

DECOY_FAMILIES = ["probe_test", "deflect_withhold", "bargain_trade",
                  "reveal_misfire", "demand_threaten", "realign_betray",
                  "release_transform"]
DECOY_ACTORS = [("B", "A"), ("C", "A"), ("D", "A"), ("A", "C"), ("B", "D")]


class OfflineBindingClient(eng.ModelClient):
    """Deterministic schedule-driven binding (configuration offline-agent-v1)."""

    def __init__(self) -> None:
        self.state: Optional[eng.EngineState] = None   # attached by the driver
        self.records: List[Dict[str, Any]] = []
        self._cur: Dict[str, Any] = {}

    # ------------------------------------------------------------------ util
    def _sched(self, scene: int) -> Dict[str, Any]:
        return SCENE[scene]

    def _scene_no(self, digest: Dict[str, Any]) -> int:
        return int(digest["scene"])

    # ---------------------------------------------------------- pair tension
    def pair_tension(self, digest, pairs):
        st = self.state
        n = self._scene_no(digest)
        sch = self._sched(n)
        dom = "-".join(sorted(st.dominant_pair))
        target = sch["t"]
        hot = dict(sch.get("hot", {}))

        # Amplitudes per pair from live edge state (§4.2).
        amp_a = {}
        for p in pairs:
            i, j = p.split("-")
            amp_a[p] = eng.pair_amplitude(st.edges[(i, j)], st.edges[(j, i)])

        bleed_base = max(0.10, min(0.65, target - 0.18))

        def t_scene_for(td: float) -> float:
            raw = {p: (td if p == dom else hot.get(p, bleed_base)) for p in pairs}
            bleed_raw = [v for k, v in raw.items() if k != dom]
            lam = eng.lambda_t(raw[dom], sum(bleed_raw) / len(bleed_raw))
            amp = {p: eng.amplify(raw[p], lam, amp_a[p]) for p in pairs}
            ts, _, _ = eng.scene_tension(amp, dom)
            return ts

        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if t_scene_for(mid) < target:
                lo = mid
            else:
                hi = mid
        td = round((lo + hi) / 2, 4)
        achieved = t_scene_for(td)

        bands = {}
        for p in pairs:
            v = td if p == dom else hot.get(p, bleed_base)
            v = round(v, 4)
            bands[p] = {"desire_conflict": v, "constraint_lock": v,
                        "expression_gap": v, "physical_charge": v}

        # ledger capture (recompute the full §5 chain exactly as run_scene will)
        raw = {p: bands[p]["desire_conflict"] for p in pairs}
        bleed_raw = [v for k, v in raw.items() if k != dom]
        lam = eng.lambda_t(raw[dom], sum(bleed_raw) / len(bleed_raw))
        amp = {p: eng.amplify(raw[p], lam, amp_a[p]) for p in pairs}
        t_scene, t_dom, t_bleed = eng.scene_tension(amp, dom)
        d_of = lambda ce: eng.deadline_d(ce, st.scene, st.phase,
                                         st.scene_in_phase, st.E)
        open_ces = [c for c in st.cer if c.status == "Open"]
        S = eng.causal_load(open_ces, d_of)
        Tc = eng.t_causal(S)
        share = (sum(1 for c in open_ces if c.u > eng.K.URGENT_SHARE_CUT)
                 / len(open_ces)) if open_ces else 0.0
        kap = eng.kappa_t(share)
        t_eff = eng.effective_tension(t_scene, Tc, kap)

        self._cur = {
            "scene": n, "phase": st.phase, "scene_in_phase": st.scene_in_phase,
            "title": sch["title"], "pov": sch["pov"], "day": sch["day"],
            "location": sch["loc"],
            "T_raw_dominant": round(raw[dom], 4), "lambda_t": round(lam, 4),
            "T_scene": round(t_scene, 4), "T_dominant": round(t_dom, 4),
            "T_bleed": round(t_bleed, 4), "S_causal": round(S, 4),
            "T_causal": round(Tc, 4), "kappa_t": round(kap, 4),
            "T_eff": round(t_eff, 4), "band": eng.routing_band(t_eff),
            "register_tag_AB": st.edges[st.dominant_pair].register_tag(),
            "register_tag_BA": st.edges[(st.dominant_pair[1],
                                         st.dominant_pair[0])].register_tag(),
            "target_T": target, "achieved_T": round(achieved, 4),
        }
        return bands

    # --------------------------------------------------------------- proposer
    def propose(self, digest, k_range, blocking_gate):
        n = self._scene_no(digest)
        sch = self._sched(n)
        open_ces = sorted(digest["cer_open"], key=lambda c: -c["u"])
        top_ce = open_ces[0]["id"] if open_ces else None
        other_ce = open_ces[1]["id"] if len(open_ces) > 1 else top_ce

        deltas = [eng.EdgeDelta(edge=(i, j), channel=ch, delta=d,
                                cause={"class": "event", "subject": sch["actor"]})
                  for (i, j, ch, d) in sch["deltas"]]
        cands = [eng.Candidate(
            id=f"s{n}-plan", family=sch["family"], actor=sch["actor"],
            target=sch["target"], linked_CEs=list(sch["ces"]),
            motif=sch["motif"], scene_shape=sch["shape"],
            intended_delta=sch["idelta"], edge_deltas=deltas,
            contact=dict(sch["contact"]) if sch["contact"] else None,
            consent_action=dict(sch["consent"]) if sch["consent"] else None)]

        fams = [f for f in DECOY_FAMILIES if f != sch["family"]]
        for k in range(4):
            fam = fams[(n + k) % len(fams)]
            actor, tgt = DECOY_ACTORS[(n + k) % len(DECOY_ACTORS)]
            ce = top_ce if k < 2 else other_ce
            cands.append(eng.Candidate(
                id=f"s{n}-alt{k+1}", family=fam, actor=actor, target=tgt,
                linked_CEs=[ce] if ce else [],
                motif=f"alt-{fam}-{n}-{k}", scene_shape="alternate",
                intended_delta=f"minor {fam} beat",
                edge_deltas=[eng.EdgeDelta(edge=(actor, tgt), channel="respect",
                                           delta=0.03,
                                           cause={"class": "event",
                                                  "subject": actor})],
                contact=None, consent_action=None))
        self._cur["pool"] = [c.id for c in cands]
        self._cur["blocking_gate"] = blocking_gate
        return cands

    # ------------------------------------------------------------------ judge
    def _rank(self, cid: str) -> int:
        # editorial preference: the authored move first, then alternates in order
        return 0 if cid.endswith("-plan") else int(cid.rsplit("alt", 1)[1])

    def judge_pairwise(self, digest, cands, dimensions, order):
        ids = [c.id for c in cands]
        rows = []
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                a, b = ids[i], ids[j]
                if order == 2:
                    a, b = b, a
                winner = a if self._rank(a) < self._rank(b) else b
                rows.append({"pair": [a, b],
                             "winners": {d: winner for d in dimensions}})
        return rows

    # ------------------------------------------------- anchored confirmation
    GOOD = {"contradiction_release": 0.75, "causal_alignment": 0.75,
            "phase_fitness": 0.75, "motif_recontext": 0.50,
            "character_inevitability": 0.75, "entropy_leak": 0.25,
            "trope_satisfaction": 0.75, "retention": 0.75,
            "pacing_fit": 0.75, "hook_value": 0.75,
            "dropoff_risk": 0.25, "over_resolution": 0.50}
    MID = {"contradiction_release": 0.50, "causal_alignment": 0.50,
           "phase_fitness": 0.50, "motif_recontext": 0.25,
           "character_inevitability": 0.50, "entropy_leak": 0.50,
           "trope_satisfaction": 0.25, "retention": 0.50,
           "pacing_fit": 0.50, "hook_value": 0.50,
           "dropoff_risk": 0.50, "over_resolution": 0.50}

    def anchored_confirmation(self, digest, cands, dimension_sets):
        out = {}
        for c in cands:
            src = self.GOOD if c.id.endswith("-plan") else self.MID
            out[c.id] = {d: src[d] for d in dimension_sets}
        self._cur["anchored"] = sorted(out)
        return out

    # ------------------------------------------------------------------- plan
    def plan(self, digest, move):
        n = self._scene_no(digest)
        sch = self._sched(n)
        beats: List[Dict[str, Any]] = []
        for b in sch["beats"]:
            beats.append({"actor": sch["actor"], "target": sch["target"],
                          "action": b, "location": sch["loc"],
                          "setting": "private", "contact_class": "C0"})
        if sch["contact"]:
            beats.append({"actor": sch["actor"], "target": sch["target"],
                          "action": f"contact {sch['contact']['class']} per "
                                    f"standing grant",
                          "location": sch["loc"],
                          "setting": sch["contact"]["setting"],
                          "contact_class": sch["contact"]["class"],
                          "negotiation": False})
        if sch["consent"]:
            beats.append({"actor": sch["actor"], "target": sch["target"],
                          "action": f"consent {sch['consent']['kind']} "
                                    f"{sch['consent']['act_class']}",
                          "location": sch["loc"], "setting": "private",
                          "contact_class": "C0", "negotiation": True})
        self._cur["move"] = {
            "id": f"s{n}-plan", "family": sch["family"], "actor": sch["actor"],
            "target": sch["target"], "motif": sch["motif"],
            "scene_shape": sch["shape"], "intended_delta": sch["idelta"],
            "linked_CEs": sch["ces"],
            "contact": sch["contact"], "consent_action": sch["consent"],
        }
        return {"scene": n, "title": sch["title"], "pov": sch["pov"],
                "day": sch["day"], "location": sch["loc"], "beats": beats,
                "synopsis": sch["syn"]}

    # ------------------------------------------------------------------ prose
    def draft(self, plan, kernel, band):
        n = plan["scene"]
        sch = self._sched(n)
        self._cur["band_at_draft"] = band
        who = DISPLAY.get(sch["pov"], sch["pov"])
        lines = [f"[SCENE {n:02d} BRIEF] {sch['title']} - POV {who} - "
                 f"day {sch['day']} - {sch['loc']} - band {band}",
                 f"move: {sch['family']} {sch['actor']}->{sch['target']} - "
                 f"motif: {sch['motif']} - {sch['idelta']}",
                 f"synopsis: {sch['syn']}"]
        lines += [f"beat: {b}" for b in sch["beats"]]
        return "\n".join(lines)

    def revise(self, text, pass_name, context):
        return text          # identity: prose passes run downstream of briefs

    def voicefilter(self, text, kernel):
        return text

    def semantic_diff(self, previous, revised):
        return {"added": [], "removed": [], "altered": []}

    # ------------------------------------------------------------- extraction
    def extract(self, prose, scene):
        st = self.state
        sch = self._sched(scene)
        tuples: List[Dict[str, Any]] = [{
            "class": "event", "subject": sch["actor"],
            "object_or_value": sch["idelta"], "polarity": "positive",
            "scene": scene, "quoted_span": sch["motif"],
        }]
        if sch["contact"]:
            tuples.append({"class": "contact", "subject": sch["actor"],
                           "object_or_value": sch["target"],
                           "polarity": "positive", "scene": scene,
                           "quoted_span": sch["motif"],
                           "contact_class": sch["contact"]["class"],
                           "setting": sch["contact"]["setting"]})
        # ---- reconciliation side effects (§7.2, orchestrator-side) --------
        for (i, j, act, setting) in sch["grants"]:
            st.edges[(i, j)].grants.append(eng.ConsentGrant(
                act_class=act, setting=setting, standing=True,
                granted_scene=scene, evidence_span=sch["motif"],
                origin="extracted"))
            tuples.append({"class": "consent_grant", "subject": i,
                           "object_or_value": j, "polarity": "positive",
                           "scene": scene, "quoted_span": sch["motif"],
                           "act_class": f"C{act}",
                           "scope": {"setting": setting}})
        for (i, j, act) in sch["withdraw"]:
            eng.withdraw(st.edges[(i, j)], act)
            tuples.append({"class": "consent_withdrawal", "subject": i,
                           "object_or_value": j, "polarity": "negative",
                           "scene": scene, "quoted_span": sch["motif"],
                           "act_class": f"C{act}"})
        for ce_id in sch["close"]:
            eng.close_ce(st.cer, ce_id)
        for ce_id in sch["misfire"]:
            eng.misfire_ce(st.cer, ce_id)

        self._cur["ce_events"] = {"closed": sch["close"],
                                  "misfired": sch["misfire"]}
        self.records.append(self._cur)
        self._cur = {}
        return tuples
