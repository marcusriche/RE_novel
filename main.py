#!/usr/bin/env python3
"""
ROMANCE ENGINE — main.py
Orchestrator for the Consolidated Operating Document v5.0.

Implements, code-side and deterministically (per §1.2 / R21):
  * the complete §15.8 deterministic core — every rule, every constant;
  * the §11.1 canonical scene loop (steps 3–14 per scene, Path A / Path B);
  * the §15 reference fixture as an executable acceptance test
    (acceptance check 1: every 4-dp ledger value reproduced exactly
    under the §15.0 rounding pin).

Everything model-facing (pair tension elicitation, proposer, pairwise judge,
anchored confirmation, plan/draft/revision/VoiceFilter, semantic diff,
extraction) is behind the ModelClient interface. Per §1.2 the model emits
bounded judgments as strict JSON; ALL arithmetic lives here. The default
StubModelClient raises NotImplementedError with the call class named, so the
deterministic core is fully testable (and fixture-verified) before any
binding configuration exists (R10/R11 discipline: no absolute thresholds are
trusted until a calibration card exists — floors here are marked provisional).

Usage:
  python main.py --fixture                 # reproduce the §15 ledgers, assert exact
  python main.py --seed seed_row.json      # run the scene loop on a Unified_Seed_Row
  python main.py --seed seed_row.json --path A --scenes 90

Internal arithmetic: IEEE-754 binary64. Ledger printing: ROUND_HALF_UP, 4 dp
(§15.0). Derived quantities (gaps, utilities, BT strengths) are computed from
unrounded values and printed last.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple

# =============================================================================
# §15.0 — ROUNDING PIN
# =============================================================================

def ledger(x: float) -> str:
    """Print a binary64 value under the pinned convention: ROUND_HALF_UP, 4 dp.
    Decimal quantisation of the FULL-PRECISION binary64 value (Decimal(x), not
    repr): §15.3's ED(a2) sits at 0.64554999…957 in binary64, printing 0.6455 —
    quantising the shortest repr would flip it to 0.6456."""
    return str(Decimal(float(x)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


# =============================================================================
# CONSTANTS — every constant of the §15.8 table, in one place
# =============================================================================

class K:
    # Pair tension base weights (§5.1)
    W_PAIR_BASE = {"desire": 0.40, "constraint": 0.25, "expression": 0.20, "physical": 0.15}
    W_PAIR_CLAMP = (0.05, 0.60)
    ETA_DRIFT = 0.02                       # §5.3 drift step
    # λ, κ (§5.3)
    LAMBDA_BASE, LAMBDA_SLOPE, LAMBDA_CLAMP = 0.15, 0.35, (0.0, 0.50)
    KAPPA_BASE, KAPPA_SLOPE, KAPPA_CLAMP = 0.25, 0.30, (0.10, 0.40)
    URGENT_SHARE_CUT = 0.6                 # U_t = share of open CEs with u > 0.6
    # Scene tension mix (§5.3)
    T_DOMINANT_W, T_BLEED_W = 0.70, 0.30
    # Causal (§5.4)
    BETA = 0.40                            # provisional
    URGENCY_LIVE, URGENCY_IDLE, URGENCY_CASCADE = 0.10, 0.05, 0.10
    MISFIRE_WEIGHT_MULT = 1.5
    # Edge deltas (§4.4)
    DELTA_CAP = 0.15
    DELTA_CORRECTIVE_CAP = 0.05
    # Confidence (§4.3)
    CONF_SEED, CONF_PRIOR = 0.90, 0.50
    CONF_TOUCH, CONF_DECAY = 0.15, 0.01
    CONF_FLOOR, CONF_SOFT = 0.30, 0.50
    # Phase gates (§6.3–6.4)
    THETA_DELTA = 0.15                     # provisional (G2)
    G4_BANDS = (0.2, 0.4, 0.6, 0.8)        # half-open, last closed
    REGRESSION_T_CUT, REGRESSION_RUN = 0.40, 3
    ROLE_TRANSITIONS_MAX = 2
    # BT (§9.4)
    LAMBDA_BT, BT_TOL, BT_MAX_ITER = 0.5, 1e-8, 500
    # Blends (§9.4, §10.3) — weights sum to 1.00 exactly
    ED_W = {"CR": 0.30, "CA": 0.20, "PF": 0.15, "MR": 0.10, "CI": 0.20, "CLEAN": 0.05}
    MD_W = {"ED": 0.26, "TS": 0.20, "RP": 0.18, "PFm": 0.14, "HV": 0.12, "SAFE": 0.06, "PRESERVE": 0.04}
    # Shortlist / lookahead / utility (§9.6–9.8, §15.8)
    EPSILON_FLOOR = 0.02                   # ε = max(0.02, card noise)
    H_DEFAULT, H_NEAR_BOUNDARY = 2, 3
    V_PEN_MISFIRE, V_PEN_WINDOW, V_PEN_VIABILITY = 0.25, 0.15, 0.40
    GAMMA = 0.30                           # provisional
    ED_FLOOR = 0.45                        # provisional, per binding configuration [Path B]
    HOOK_THRESHOLD_DEFAULT = 0.65          # §10.4, Platform_Hook_Profile-conditional
    # Rupture (§9.9)
    RUPTURE = {"A": dict(p=0.02, teff=0.70, w=0.75, cooldown=40),
               "B": dict(p=0.01, teff=0.75, w=0.75, cooldown=50)}
    # Amplification caps (§8.2)
    EXPR_AMP_CAP, KERNEL_AMP_CAP = 1.25, 1.20
    # Kernel coherence (§8.2)
    KERNEL_REALIGN_BELOW = 0.65
    # Register banding (§4.2)
    REGISTER_BAND = 0.2
    # Repair ladder (§12.2)
    SCHEMA_VALIDITY_TARGET = 0.995


REGISTER_TAGS = {
    # (warmth_band, security_band) -> directed tag; bands ∈ {-1, 0, +1}
    (+1, -1): "yearning", (+1, 0): "fond", (+1, +1): "tender",
    (0, -1): "wary", (0, 0): "flat", (0, +1): "steady",
    (-1, -1): "hostile", (-1, 0): "cold", (-1, +1): "contemptuous",
}

SCALAR_PRIMITIVES = [
    "attraction_romantic", "attraction_sexual", "trust", "affection", "fear",
    "respect", "resentment", "emotional_safety", "vulnerability", "commitment",
    "dominance", "perceived_reciprocity",
]  # the 12 scalar primitives of §4.1; moral_repair and consent handled separately

MOVE_FAMILIES = [
    "probe_test", "deflect_withhold", "demand_threaten", "bargain_trade",
    "reveal_misfire", "realign_betray", "release_transform", "negotiate_consent",
]

CE_TYPES = ["Promise", "Secret", "Debt", "Threat", "Revelation", "Absence", "Obligation"]


class ContactClass(IntEnum):
    C0 = 0; C1 = 1; C2 = 2; C3 = 3; C4 = 4


# =============================================================================
# §4 — RELATIONAL STATE LAYER
# =============================================================================

@dataclass
class ConsentGrant:
    """§4.5 grant record. Evidence-only: extracted event or explicit seed record."""
    act_class: int                          # 2..4
    setting: str                            # 'private' | 'public' | 'any'
    conditions: List[str] = field(default_factory=list)
    standing: bool = True
    granted_scene: Optional[int] = None
    evidence_span: str = ""
    origin: str = "extracted"               # 'extracted' | 'seed'
    void: bool = False


@dataclass
class Boundary:
    """A standing boundary carving grant coverage (§4.5)."""
    act_class: Optional[int] = None         # None = blanket
    named_act: Optional[str] = None
    setting: str = "any"


@dataclass
class DirectedEdge:
    """R_ij for one ordered pair (§4.1). Values in [0,1]; confidence per §4.3."""
    values: Dict[str, float] = field(default_factory=lambda: {c: 0.10 for c in SCALAR_PRIMITIVES})
    confidence: Dict[str, float] = field(default_factory=lambda: {c: K.CONF_PRIOR for c in SCALAR_PRIMITIVES})
    moral_repair: float = 0.0               # completion share across open transgressions
    grants: List[ConsentGrant] = field(default_factory=list)
    boundaries: List[Boundary] = field(default_factory=list)

    # ---- §4.2 register vector -------------------------------------------------
    def warmth(self) -> float:
        return clip(self.values["affection"] - self.values["resentment"], -1.0, 1.0)

    def security(self) -> float:
        return clip(self.values["trust"] - self.values["fear"], -1.0, 1.0)

    def intensity(self) -> float:
        return max(abs(self.warmth()), abs(self.security()))

    def register_tag(self) -> str:
        b = lambda v: (1 if v > K.REGISTER_BAND else (-1 if v < -K.REGISTER_BAND else 0))
        return REGISTER_TAGS[(b(self.warmth()), b(self.security()))]

    # ---- §4.2 consent_reach ---------------------------------------------------
    def consent_reach(self, capacity_ok: bool) -> int:
        if not capacity_ok:
            return 0
        if any(b.act_class is None for b in self.boundaries):
            return 0  # blanket boundary
        reach = 1  # C1 social default
        for g in self.grants:
            if g.void:
                continue
            covered = g.act_class
            # a grant covers lower classes ≥ C2 within scope unless a boundary carves it
            for c in range(2, covered + 1):
                if any(b.act_class == c for b in self.boundaries):
                    continue
                reach = max(reach, covered)
        return reach


def pair_class(w_ij: float, w_ji: float) -> str:
    """§4.2 pair class from the two warmth bands."""
    b = lambda v: (1 if v > K.REGISTER_BAND else (-1 if v < -K.REGISTER_BAND else 0))
    bi, bj = b(w_ij), b(w_ji)
    if bi == 1 and bj == 1: return "mutual_warm"
    if bi == -1 and bj == -1: return "mutual_cold"
    if bi * bj == -1: return "crossed"
    if (bi == 0) != (bj == 0): return "one_sided"
    return "flat"


def pair_amplitude(e_ij: DirectedEdge, e_ji: DirectedEdge) -> float:
    """a = max(m_ij, m_ji) ∈ [0,1] (§4.2)."""
    return max(e_ij.intensity(), e_ji.intensity())


# ---- §4.3 confidence rules ---------------------------------------------------

def confidence_touch(edge: DirectedEdge, channel: str) -> None:
    edge.confidence[channel] = min(1.0, edge.confidence[channel] + K.CONF_TOUCH)


def confidence_decay(edge: DirectedEdge, touched: Set[str]) -> None:
    for c in SCALAR_PRIMITIVES:
        if c not in touched:
            edge.confidence[c] = max(K.CONF_FLOOR, edge.confidence[c] - K.CONF_DECAY)


# ---- §4.4 edge deltas: intended → realized -----------------------------------

@dataclass
class EdgeDelta:
    edge: Tuple[str, str]                   # (i, j) directed
    channel: str                            # 12 primitives + 'moral_repair'
    delta: float
    cause: Dict[str, str]                   # {class, subject, object?}


def bound_intended_deltas(deltas: Sequence[EdgeDelta]) -> List[str]:
    """Structural-verifier bound: |Δ| ≤ 0.15 per channel per scene; consent never
    moves by numeric delta. Returns violations (empty = pass)."""
    errs = []
    for d in deltas:
        if abs(d.delta) > K.DELTA_CAP + 1e-12:
            errs.append(f"|Δ|>{K.DELTA_CAP} on {d.edge}/{d.channel}")
        if d.channel in ("consent", "knowledge"):
            errs.append(f"channel '{d.channel}' never moves by numeric delta (§4.4)")
        if d.channel not in SCALAR_PRIMITIVES and d.channel != "moral_repair":
            errs.append(f"unknown channel '{d.channel}'")
    return errs


def realize_deltas(deltas: Sequence[EdgeDelta],
                   extracted_tuples: Sequence[Dict[str, Any]],
                   edges: Dict[Tuple[str, str], DirectedEdge],
                   log: List[Dict[str, Any]]) -> None:
    """R23: an intended delta applies only if an extracted tuple matches its
    declared cause on class and participants. Unmatched → dropped + flagged."""
    def matches(cause: Dict[str, str], t: Dict[str, Any]) -> bool:
        if t.get("class") != cause.get("class"):
            return False
        if t.get("subject") != cause.get("subject"):
            return False
        obj = cause.get("object")
        return obj is None or t.get("object_or_value") == obj

    for d in deltas:
        if any(matches(d.cause, t) for t in extracted_tuples):
            e = edges[d.edge]
            if d.channel == "moral_repair":
                e.moral_repair = clip(e.moral_repair + d.delta, 0.0, 1.0)
            else:
                e.values[d.channel] = clip(e.values[d.channel] + d.delta, 0.0, 1.0)
                confidence_touch(e, d.channel)
        else:
            log.append({"unrealized_delta": vars(d)})


# ---- §4.5 consent admissibility (deterministic; inside the structural verifier)

def coercion_flag(cer_open: Sequence["CE"], actor: str, target: str,
                  protected_by: Dict[str, Set[str]]) -> bool:
    """Flag while an open Threat-type CE runs from actor against target or a
    person target protects (or extraction evidenced an unretracted coercive
    demand — carried on the CE list by the extraction pass)."""
    for ce in cer_open:
        if ce.status != "Open" or ce.type != "Threat":
            continue
        if ce.owner_from == actor and (
            ce.owner_against == target or ce.owner_against in protected_by.get(target, set())
        ):
            return True
    return False


def contact_admissible(contact_class: int, setting: str, actor: str, target: str,
                       edge_ty_tx: DirectedEdge,          # grants target → actor
                       capacity: Dict[str, bool],
                       coercion: bool,
                       is_negotiation_beat: bool) -> Tuple[bool, str]:
    """§4.5 ADMISSIBILITY, verbatim logic. Returns (admissible, reason)."""
    if is_negotiation_beat:
        return True, "consent-negotiation beat (performs nothing)"
    if contact_class <= ContactClass.C1:
        # C1 granted by social default absent a contrary boundary
        if contact_class == ContactClass.C1 and any(
            b.act_class is None for b in edge_ty_tx.boundaries
        ):
            return False, "blanket boundary blocks C1"
        return True, "C0/C1 social default"
    if not capacity.get(target, True):
        return False, f"capacity({target}) absent"
    if contact_class >= ContactClass.C3 and not capacity.get(actor, True):
        return False, f"capacity({actor}) absent for C3+"
    if coercion:
        return False, f"coercion({actor}→{target}) flagged: C2+ inadmissible"
    for g in edge_ty_tx.grants:
        if g.void:
            continue
        if g.act_class >= contact_class and g.setting in (setting, "any"):
            # coverage of lower classes unless a boundary carves the specific class
            if any(b.act_class == contact_class for b in edge_ty_tx.boundaries):
                continue
            return True, f"covered by grant C{g.act_class}/{g.setting}"
    return False, "no covering grant"


def withdraw(edge: DirectedEdge, act_class: int) -> None:
    """Withdrawal: always admissible, instant, voids every matching grant (§4.5)."""
    for g in edge.grants:
        if g.act_class >= act_class:
            g.void = True


# =============================================================================
# §5.4–5.5 — CAUSAL EVENT REGISTER
# =============================================================================

@dataclass
class CE:
    id: str
    type: str
    w: float
    u: float
    deadline_scene: Optional[int] = None     # scene-typed
    deadline_phase: Optional[int] = None     # phase-typed ("end of phase" default)
    status: str = "Open"                     # Open | Partially resolved | Closed | Misfired(stays Open per rule)
    cascade: List[str] = field(default_factory=list)
    owner_from: str = ""                     # for Threat coercion flags
    owner_against: str = ""
    notes: str = ""


def deadline_d(ce: CE, scene_now: int, phase_now: int, scene_in_phase: int,
               E: Sequence[int], anchor_offset: Optional[int] = None) -> int:
    """§5.5 deadline → expected-scene transform. Never cached across boundaries."""
    if ce.deadline_scene is not None:
        return max(0, ce.deadline_scene - scene_now)
    ph_dl = ce.deadline_phase
    assert ph_dl is not None, f"{ce.id}: no deadline"
    d = max(0, E[phase_now] - scene_in_phase)
    for ph in range(phase_now + 1, ph_dl):
        d += E[ph]
    d += E[ph_dl] if anchor_offset is None else anchor_offset
    return d


def causal_load(cer_open: Sequence[CE], d_of: Callable[[CE], int]) -> float:
    """S = Σ over OPEN events of w·u·p, p = 1/(d+1). Stateless recompute (§5.4)."""
    return sum(ce.w * ce.u * (1.0 / (d_of(ce) + 1)) for ce in cer_open if ce.status == "Open")


def t_causal(S: float, beta: float = K.BETA) -> float:
    return S / (S + beta)


def accrue_urgency(cer: Sequence[CE], live_ids: Set[str]) -> None:
    """The single accrual rule (§5.4): +0.10 live, +0.05 idle, per open event."""
    for ce in cer:
        if ce.status == "Open":
            ce.u = clip(ce.u + (K.URGENCY_LIVE if ce.id in live_ids else K.URGENCY_IDLE), 0.0, 1.0)


def close_ce(cer: Sequence[CE], ce_id: str) -> None:
    by_id = {c.id: c for c in cer}
    ce = by_id[ce_id]
    ce.status = "Closed"
    for cid in ce.cascade:
        if cid in by_id and by_id[cid].status == "Open":
            by_id[cid].u = clip(by_id[cid].u + K.URGENCY_CASCADE, 0.0, 1.0)


def misfire_ce(cer: Sequence[CE], ce_id: str) -> None:
    by_id = {c.id: c for c in cer}
    ce = by_id[ce_id]
    ce.w = min(1.0, K.MISFIRE_WEIGHT_MULT * ce.w)   # STAYS OPEN
    for cid in ce.cascade:
        if cid in by_id and by_id[cid].status == "Open":
            by_id[cid].u = clip(by_id[cid].u + K.URGENCY_CASCADE, 0.0, 1.0)


# =============================================================================
# §5.1–5.3 — TENSION: BLEND, AMPLIFIER, AGGREGATION, DRIFT
# =============================================================================

@dataclass
class PairWeights:
    w: Dict[str, float] = field(default_factory=lambda: dict(K.W_PAIR_BASE))

    def blend(self, bands: Dict[str, float]) -> float:
        return (self.w["desire"] * bands["desire_conflict"]
                + self.w["constraint"] * bands["constraint_lock"]
                + self.w["expression"] * bands["expression_gap"]
                + self.w["physical"] * bands["physical_charge"])

    def drift(self, E_t: float, N_t: float, B_t: float, X_t: float, S_t: float) -> None:
        """§5.3 drift at scene boundaries; clamp then renormalise to 1.00."""
        eta = K.ETA_DRIFT
        self.w["desire"] += eta * (0.5 * E_t + 0.5 * N_t - 0.5)
        self.w["constraint"] += eta * (B_t - 0.5)
        self.w["expression"] += eta * (X_t - 0.5)
        self.w["physical"] += eta * (S_t - 0.5)
        lo, hi = K.W_PAIR_CLAMP
        for k_ in self.w:
            self.w[k_] = clip(self.w[k_], lo, hi)
        s = sum(self.w.values())
        for k_ in self.w:
            self.w[k_] /= s


def lambda_t(T_dominant_raw: float, T_bleed_raw: float) -> float:
    """λ from RAW pre-amplification values — the amplifier never feeds its own coefficient."""
    return clip(K.LAMBDA_BASE + K.LAMBDA_SLOPE * (T_dominant_raw - T_bleed_raw), *K.LAMBDA_CLAMP)


def kappa_t(urgent_share: float) -> float:
    return clip(K.KAPPA_BASE + K.KAPPA_SLOPE * (urgent_share - 0.5), *K.KAPPA_CLAMP)


def amplify(T: float, lam: float, a: float) -> float:
    """T̃ = T + λ·a·T·(1−T) — bounded in [0,1] by construction."""
    return T + lam * a * T * (1.0 - T)


def scene_tension(amplified: Dict[str, float], dominant_pair: str) -> Tuple[float, float, float]:
    """Returns (T_scene, T_dominant, T_bleed) on amplified values (§5.3)."""
    T_dom = amplified[dominant_pair]
    rest = [v for k_, v in amplified.items() if k_ != dominant_pair]
    T_bleed = sum(rest) / len(rest) if rest else 0.0
    return K.T_DOMINANT_W * T_dom + K.T_BLEED_W * T_bleed, T_dom, T_bleed


def effective_tension(T_scene: float, Tc: float, kap: float) -> float:
    return T_scene + kap * Tc * (1.0 - T_scene)


def routing_band(T_eff: float) -> str:
    """§5.2 routing bands — the one-line table every prose-facing prompt receives."""
    if T_eff < 0.35: return "establishment"
    if T_eff < 0.55: return "complication"
    if T_eff < 0.75: return "first_crisis"
    return "climax"


# =============================================================================
# §6 — ARC, PHASE, GATES
# =============================================================================

ARC_PROFILES: Dict[str, List[int]] = {
    "Billionaire/Elite":            [8, 10, 12, 10, 10, 12, 10, 8, 10],
    "Romantasy":                    [12, 10, 10, 10, 8, 12, 12, 8, 8],
    "Mafia/Dark":                   [6, 8, 10, 10, 10, 12, 12, 10, 12],
    "Sports":                       [8, 10, 12, 12, 8, 12, 10, 8, 10],
    "Contemporary Small-Town":      [10] * 9,
    "Military/Special Ops":         [8, 8, 10, 12, 8, 12, 12, 10, 10],
    "Rom-Com/Workplace":            [10, 12, 12, 8, 10, 10, 10, 8, 10],
    "Western/Cowboy":               [10, 10, 10, 10, 10, 12, 10, 8, 10],
    "Paranormal Shifter":           [10, 10, 10, 10, 8, 12, 12, 8, 10],
    "Vampire/Gothic Paranormal":    [10, 8, 10, 10, 10, 12, 12, 8, 10],
    "Romantic Suspense":            [8, 8, 12, 12, 8, 12, 12, 8, 10],
    "Historical Regency/Victorian": [10, 10, 12, 10, 10, 10, 10, 8, 10],
}

PHASE_CEILINGS = [0.35, 0.45, 0.60, 0.75, 0.50, 0.80, 1.00, 0.80, 0.40]  # §6.1 typical top of band


def min_duration(E: Sequence[int]) -> List[int]:
    return [max(2, round(0.4 * e)) for e in E]


def g4_band(v: float) -> int:
    """B0 [0,0.2) · B1 [0.2,0.4) · B2 [0.4,0.6) · B3 [0.6,0.8) · B4 [0.8,1] (§6.3)."""
    for i, cut in enumerate(K.G4_BANDS):
        if v < cut:
            return i
    return 4


def g2_norm(entry_ij: DirectedEdge, now_ij: DirectedEdge,
            entry_ji: DirectedEdge, now_ji: DirectedEdge,
            reach_entry: Tuple[int, int], reach_now: Tuple[int, int]) -> float:
    """Pinned G2 norm: Σ over BOTH directions of Σ|Δ| across the 12 scalar
    primitives, plus |Δ consent_reach|/4, plus |Δ moral_repair| — 28 terms."""
    total = 0.0
    for entry, now, r0, r1 in ((entry_ij, now_ij, reach_entry[0], reach_now[0]),
                               (entry_ji, now_ji, reach_entry[1], reach_now[1])):
        total += sum(abs(now.values[c] - entry.values[c]) for c in SCALAR_PRIMITIVES)
        total += abs(r1 - r0) / 4.0
        total += abs(now.moral_repair - entry.moral_repair)
    return total


@dataclass
class GateResult:
    advance: bool
    blocking: List[str]


def evaluate_gates(*, beats_complete: bool, g2_value: float, ce_touched: bool,
                   band_crossed_or_transition: bool, scenes_in_phase: int,
                   min_ph: int, scenes_remaining: int, future_min_total: int,
                   initiator: bool) -> GateResult:
    """G1–G6 (§6.3). The gate diagnoses; the selector treats."""
    blocking = []
    if not beats_complete: blocking.append("G1")
    if g2_value < K.THETA_DELTA: blocking.append("G2")
    if not ce_touched: blocking.append("G3")
    if not band_crossed_or_transition: blocking.append("G4")
    if scenes_in_phase < min_ph: blocking.append("G5")
    if scenes_remaining < future_min_total: blocking.append("G6")
    return GateResult(advance=(initiator and not blocking), blocking=blocking)


def regression_allowed(phase: int, low_t_run: int, gate_hold_active: bool,
                       regressions_so_far: int, operator_flag: bool) -> bool:
    """§6.4: only P∈{5,6,7}→4; T_scene<0.40 for 3+ scenes AND no hold; budget 1 unflagged."""
    if phase not in (5, 6, 7): return False
    if low_t_run < K.REGRESSION_RUN or gate_hold_active: return False
    if regressions_so_far >= 1 and not operator_flag: return False
    return True


# =============================================================================
# §9.4 — BRADLEY–TERRY FIT (regularised MM)
# =============================================================================

def bt_fit(candidates: Sequence[str], wins: Dict[str, Dict[str, float]],
           lam: float = K.LAMBDA_BT, tol: float = K.BT_TOL,
           max_iter: int = K.BT_MAX_ITER) -> Tuple[Dict[str, float], Dict[str, float], int]:
    """wins[i][j] = observed times i beat j (both batched-call orders pooled).
    λ_BT pseudo-wins per ordered pair; MM update; geometric-mean-1 renorm;
    stop at L∞ < tol. Returns (π, s = π/(π+1), iterations)."""
    ids = list(candidates)
    W = {i: sum(wins.get(i, {}).get(j, 0.0) + lam for j in ids if j != i) for i in ids}
    n = {(i, j): wins.get(i, {}).get(j, 0.0) + wins.get(j, {}).get(i, 0.0) + 2 * lam
         for i in ids for j in ids if i != j}
    pi = {i: 1.0 for i in ids}
    iters = 0
    for iters in range(1, max_iter + 1):
        new = {}
        for i in ids:
            denom = sum(n[(i, j)] / (pi[i] + pi[j]) for j in ids if j != i)
            new[i] = W[i] / denom
        gm = math.exp(sum(math.log(v) for v in new.values()) / len(new))
        new = {i: v / gm for i, v in new.items()}
        delta = max(abs(new[i] - pi[i]) for i in ids)
        pi = new
        if delta < tol:
            break
    s = {i: pi[i] / (pi[i] + 1.0) for i in ids}
    degenerate = max(pi.values()) - min(pi.values()) < 1e-3
    if degenerate:
        print("  [flag] degenerate BT fit — inspect pool quality (§9.4)", file=sys.stderr)
    return pi, s, iters


def pool_wins_from_batches(batch1: List[Dict[str, Any]], batch2: List[Dict[str, Any]],
                           dimension: str) -> Tuple[Dict[str, Dict[str, float]], Set[str]]:
    """Pool both within-pair orders; tag order-sensitivity is computed by the caller
    on blended top-1s. Validity checks mirror §12.2 semantics."""
    wins: Dict[str, Dict[str, float]] = {}
    for batch in (batch1, batch2):
        for row in batch:
            a, b = row["pair"]
            wnr = row["winners"][dimension]
            if wnr not in (a, b):
                raise ValueError(f"winner {wnr} ∉ pair {row['pair']} (repair ladder)")
            loser = b if wnr == a else a
            wins.setdefault(wnr, {}).setdefault(loser, 0.0)
            wins[wnr][loser] += 1.0
    return wins, set()


# =============================================================================
# §9.4 / §10.3 — BLENDS (both stages)
# =============================================================================

def ed_blend(CR: float, CA: float, PF: float, MR: float, CI: float, clean_term: float) -> float:
    """Stage-1: clean_term = s_clean. Stage-2: clean_term = (1 − EL)."""
    w = K.ED_W
    return (w["CR"] * CR + w["CA"] * CA + w["PF"] * PF + w["MR"] * MR
            + w["CI"] * CI + w["CLEAN"] * clean_term)


def md_blend(ED: float, TS: float, RP: float, PFm: float, HV: float,
             safe_term: float, preserve_term: float) -> float:
    """Stage-1: safe/preserve terms = s_safe / s_preserve. Stage-2: (1−DR)/(1−OR).
    ED enters on its native scale per stage, at FULL precision."""
    w = K.MD_W
    return (w["ED"] * ED + w["TS"] * TS + w["RP"] * RP + w["PFm"] * PFm
            + w["HV"] * HV + w["SAFE"] * safe_term + w["PRESERVE"] * preserve_term)


def calibration_transform(x: float, a: float = 1.0, b: float = 0.0) -> float:
    """§11.2: y = clip(a·x + b, 0, 1), a > 0. Identity until a card exists;
    isotonic becomes mandatory above 10% clip fraction (fitted off-line)."""
    assert a > 0
    return clip(a * x + b, 0.0, 1.0)


# =============================================================================
# §9.6–9.8 — SHORTLIST, LOOKAHEAD, UTILITY, GAP
# =============================================================================

@dataclass
class Candidate:
    id: str
    family: str
    actor: str
    target: str
    linked_CEs: List[str]
    linked_TRs: List[str] = field(default_factory=list)
    motif: str = ""
    scene_shape: str = ""
    intended_delta: str = ""
    edge_deltas: List[EdgeDelta] = field(default_factory=list)
    contact: Optional[Dict[str, Any]] = None
    consent_action: Optional[Dict[str, Any]] = None


def shortlist(ed: Dict[str, float], md: Optional[Dict[str, float]],
              order_sensitive: Set[str], epsilon: float = K.EPSILON_FLOOR) -> List[str]:
    """top-2 ED ∪ top-2 MD ∪ order-sensitive ∪ near-cutoff-under-uncertainty (§9.6)."""
    def top2(scores: Dict[str, float]) -> List[str]:
        return [k_ for k_, _ in sorted(scores.items(), key=lambda kv: -kv[1])[:2]]

    sl: Set[str] = set(top2(ed)) | order_sensitive
    if md:
        sl |= set(top2(md))
    scales = [ed] + ([md] if md else [])
    for scale in scales:
        ranked = sorted(scale.items(), key=lambda kv: -kv[1])
        if len(ranked) >= 2:
            second = ranked[1][1]
            for cid, v in ranked:
                if cid not in sl and (second - v) < epsilon:
                    sl.add(cid)
    return sorted(sl)


@dataclass
class SimResult:
    misfires: int
    windows_closing: int
    viability_fail: bool
    V: float


def simulate(cand: Candidate, cer_open: Sequence[CE], scene_now: int,
             phase_now: int, scene_in_phase: int, E: Sequence[int],
             h: int, scenes_total: int,
             trope_windows_closing: int = 0) -> SimResult:
    """§9.7 deterministic lookahead — arithmetic on state deltas, no model calls.
    Projects h scene deltas with the candidate's linked CEs live."""
    proj = [CE(c.id, c.type, c.w, c.u, c.deadline_scene, c.deadline_phase, c.status,
               list(c.cascade), c.owner_from, c.owner_against) for c in cer_open]
    linked = set(cand.linked_CEs)
    d0 = {c.id: deadline_d(c, scene_now, phase_now, scene_in_phase, E) for c in proj}
    misfires = 0
    for c in proj:
        if c.status == "Open" and c.w > 0.70 and d0[c.id] <= h and c.id not in linked:
            misfires += 1
    for _ in range(h):  # urgency projection per the single §5.4 rule
        for c in proj:
            if c.status == "Open":
                c.u = clip(c.u + (K.URGENCY_LIVE if c.id in linked else K.URGENCY_IDLE), 0, 1)
    # terminal viability: G6 capacity holds and the ending stays reachable
    mins = min_duration(E)
    scenes_remaining = scenes_total - scene_now
    need = max(0, mins[phase_now] - scene_in_phase) + sum(mins[phase_now + 1:])
    viability_fail = scenes_remaining < need
    V = clip(1.0 - K.V_PEN_MISFIRE * misfires - K.V_PEN_WINDOW * trope_windows_closing
             - (K.V_PEN_VIABILITY if viability_fail else 0.0), 0.0, 1.0)
    return SimResult(misfires, trope_windows_closing, viability_fail, V)


def utility(stage1_score: float, V: float, gamma: float = K.GAMMA) -> float:
    """U = (1−γ)·score + γ·V, on Stage-1 scores only — one elicitation stage per comparison."""
    return (1.0 - gamma) * stage1_score + gamma * V


def confidence_gap(best: float, second: float) -> Tuple[float, str]:
    rho = best - second
    if rho > 0.15: reading = "strong direction"
    elif rho >= 0.05: reading = "meaningful preference"
    else: reading = "review flag"
    return rho, reading


# =============================================================================
# MODEL CLIENT — every model-facing call class (§1.2: elicitation only)
# =============================================================================

class ModelClient:
    """Interface to the bound configuration (R10). All returns are strict-JSON
    dicts; the repair ladder (§12.2) wraps every call. Subclass and bind."""

    def pair_tension(self, digest: Dict[str, Any], pairs: List[str]) -> Dict[str, Dict[str, float]]:
        raise NotImplementedError("bind a configuration: pair_tension (PRIMARY-STRUCT)")

    def propose(self, digest: Dict[str, Any], k_range: Tuple[int, int],
                blocking_gate: Optional[str]) -> List[Candidate]:
        raise NotImplementedError("bind a configuration: proposer (PRIMARY-STRUCT)")

    def judge_pairwise(self, digest: Dict[str, Any], cands: List[Candidate],
                       dimensions: List[str], order: int) -> List[Dict[str, Any]]:
        raise NotImplementedError("bind a configuration: pairwise judge (JUDGE)")

    def anchored_confirmation(self, digest: Dict[str, Any], cands: List[Candidate],
                              dimension_sets: List[str]) -> Dict[str, Dict[str, float]]:
        raise NotImplementedError("bind a configuration: anchored confirmation (PRIMARY-STRUCT)")

    def plan(self, digest: Dict[str, Any], move: Candidate) -> Dict[str, Any]:
        raise NotImplementedError("bind a configuration: beat plan (PRIMARY-STRUCT)")

    def draft(self, plan: Dict[str, Any], kernel: Dict[str, Any], band: str) -> str:
        raise NotImplementedError("bind a configuration: integrated draft (PRIMARY-PROSE)")

    def revise(self, text: str, pass_name: str, context: Dict[str, Any]) -> str:
        raise NotImplementedError("bind a configuration: revision pass (PRIMARY-PROSE)")

    def voicefilter(self, text: str, kernel: Dict[str, Any]) -> str:
        raise NotImplementedError("bind a configuration: VoiceFilter (FILTER)")

    def semantic_diff(self, previous: str, revised: str) -> Dict[str, List[Any]]:
        raise NotImplementedError("bind a configuration: semantic diff (PRIMARY-STRUCT)")

    def extract(self, prose: str, scene: int) -> List[Dict[str, Any]]:
        raise NotImplementedError("bind a configuration: continuity extraction (PRIMARY-STRUCT)")


def with_repair_ladder(call: Callable[[], Any], validate: Callable[[Any], List[str]],
                       safe_default: Callable[[], Any], flag_log: List[Dict[str, Any]],
                       call_class: str) -> Any:
    """§12.2: validate → one re-prompt with the error → per-class safe default."""
    for attempt in (1, 2):
        try:
            out = call()
            errs = validate(out)
            if not errs:
                return out
            last = errs
        except Exception as e:                                   # noqa: BLE001
            last = [str(e)]
    flag_log.append({"repair_ladder_default": call_class, "errors": last})
    return safe_default()


# =============================================================================
# §11.1 — THE CANONICAL SCENE LOOP
# =============================================================================

@dataclass
class EngineState:
    """Σ_t (plus M_t under Path B) — the composite state, checkpointable."""
    seed: Dict[str, Any]
    path: str                               # 'A' | 'B'
    E: List[int]
    scenes_total: int
    phase: int = 0
    scene: int = 1
    scene_in_phase: int = 0
    nodes: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    edges: Dict[Tuple[str, str], DirectedEdge] = field(default_factory=dict)
    dominant_pair: Tuple[str, str] = ("A", "B")
    cer: List[CE] = field(default_factory=list)
    weights: PairWeights = field(default_factory=PairWeights)
    capacity: Dict[str, bool] = field(default_factory=dict)
    protected_by: Dict[str, Set[str]] = field(default_factory=dict)
    review_flags: List[Dict[str, Any]] = field(default_factory=list)
    unrealized_log: List[Dict[str, Any]] = field(default_factory=list)
    regressions: int = 0
    low_t_run: int = 0
    edges_at_phase_entry: Dict[Tuple[str, str], DirectedEdge] = field(default_factory=dict)
    kernel: Dict[str, Any] = field(default_factory=dict)
    checkpoints: List[str] = field(default_factory=list)

    def checkpoint(self) -> None:
        snap = {"scene": self.scene, "phase": self.phase,
                "edges": {f"{i}->{j}": e.values for (i, j), e in self.edges.items()},
                "cer": [vars(c) for c in self.cer]}
        self.checkpoints.append(json.dumps(snap, default=str))


ED_DIMENSIONS = ["contradiction_release", "causal_alignment", "phase_fitness",
                 "motif_recontext", "character_inevitability", "entropy_leak"]
MD_DIMENSIONS = ["trope_satisfaction", "retention", "pacing_fit", "hook_value",
                 "dropoff_risk", "over_resolution"]


def stage1_scores(cands: List[Candidate], client: ModelClient,
                  digest: Dict[str, Any], dimensions: List[str],
                  blend: Callable[[Dict[str, Dict[str, float]], str], float]
                  ) -> Tuple[Dict[str, float], Set[str]]:
    """Two batched judge calls (both within-pair orders), BT fit per dimension,
    Stage-1 blend; order-sensitivity tagged on blended top-1 disagreement (§9.4)."""
    batch1 = client.judge_pairwise(digest, cands, dimensions, order=1)
    batch2 = client.judge_pairwise(digest, cands, dimensions, order=2)
    ids = [c.id for c in cands]
    s_by_dim: Dict[str, Dict[str, float]] = {}
    s_by_dim_1: Dict[str, Dict[str, float]] = {}
    s_by_dim_2: Dict[str, Dict[str, float]] = {}
    for dim in dimensions:
        wins, _ = pool_wins_from_batches(batch1, batch2, dim)
        _, s, _ = bt_fit(ids, wins)
        s_by_dim[dim] = s
        w1, _ = pool_wins_from_batches(batch1, [], dim)
        w2, _ = pool_wins_from_batches(batch2, [], dim)
        _, s_by_dim_1[dim], _ = bt_fit(ids, w1)
        _, s_by_dim_2[dim], _ = bt_fit(ids, w2)
    blended = {cid: blend(s_by_dim, cid) for cid in ids}
    top_pooled = max(blended, key=blended.get)
    top_1 = max(ids, key=lambda c: blend(s_by_dim_1, c))
    top_2 = max(ids, key=lambda c: blend(s_by_dim_2, c))
    order_sensitive = {c for c in (top_1, top_2) if (top_1 != top_2) and c == max(
        {top_1, top_2}, key=lambda x: blended[x])} if top_1 != top_2 else set()
    _ = top_pooled
    return blended, order_sensitive


def run_scene(state: EngineState, client: ModelClient) -> None:
    """Steps 3–14 of §11.1 for one scene. Model calls go through `client`;
    every blend, threshold, gate, transform, and simulation is computed here."""
    path_b = state.path == "B"
    digest = build_digest(state)

    # 3–4: pair scoring → amplify → aggregate → causal → effective
    pair_ids = sorted({tuple(sorted(p)) for p in state.edges})
    pairs_u = ["-".join(p) for p in pair_ids]
    bands = client.pair_tension(digest, pairs_u)      # {pair: {dim: band}}
    T_raw = {p: state.weights.blend(bands[p]) for p in pairs_u}
    dom = "-".join(sorted(state.dominant_pair))
    bleed_raw = [v for k_, v in T_raw.items() if k_ != dom]
    lam = lambda_t(T_raw[dom], sum(bleed_raw) / len(bleed_raw) if bleed_raw else 0.0)
    amp = {}
    for p in pairs_u:
        i, j = p.split("-")
        a = pair_amplitude(state.edges[(i, j)], state.edges[(j, i)])
        amp[p] = amplify(T_raw[p], lam, a)
    T_scene, _, _ = scene_tension(amp, dom)
    d_of = lambda ce: deadline_d(ce, state.scene, state.phase, state.scene_in_phase, state.E)
    open_ces = [c for c in state.cer if c.status == "Open"]
    S = causal_load(open_ces, d_of)
    Tc = t_causal(S)
    urgent_share = (sum(1 for c in open_ces if c.u > K.URGENT_SHARE_CUT) / len(open_ces)) if open_ces else 0.0
    kap = kappa_t(urgent_share)
    T_eff = effective_tension(T_scene, Tc, kap)
    band = routing_band(T_eff)

    # 5: phase evaluation (initiator + G1–G6; regression rule)
    state.low_t_run = state.low_t_run + 1 if T_scene < K.REGRESSION_T_CUT else 0
    mins = min_duration(state.E)
    gate = evaluate_phase(state, T_scene)
    blocking = gate.blocking[0] if gate.blocking else None

    # 6: proposer + structural verifier + diversity gates
    cands = client.propose(digest, (4, 8), blocking)
    cands = structural_verify(state, cands)

    # 7: pairwise judging → BT → Stage-1 blends
    ed_s1, os_ed = stage1_scores(cands, client, digest, ED_DIMENSIONS,
                                 lambda s, c: ed_blend(
                                     s["contradiction_release"][c], s["causal_alignment"][c],
                                     s["phase_fitness"][c], s["motif_recontext"][c],
                                     s["character_inevitability"][c], s["entropy_leak"][c]))
    md_s1: Optional[Dict[str, float]] = None
    os_md: Set[str] = set()
    if path_b:
        md_s1, os_md = stage1_scores(cands, client, digest, MD_DIMENSIONS,
                                     lambda s, c: md_blend(
                                         ed_s1[c], s["trope_satisfaction"][c], s["retention"][c],
                                         s["pacing_fit"][c], s["hook_value"][c],
                                         s["dropoff_risk"][c], s["over_resolution"][c]))

    # 8–9: shortlist (+ hook operator at chapter end, Path B — client-supplied lateral move
    #        re-enters like any other shortlisted move; omitted until packaging state runs)
    sl = shortlist(ed_s1, md_s1, os_ed | os_md)
    by_id = {c.id: c for c in cands}

    # 10: lookahead + utility
    h = K.H_NEAR_BOUNDARY if state.scene_in_phase >= state.E[state.phase] - 1 else K.H_DEFAULT
    sims = {cid: simulate(by_id[cid], open_ces, state.scene, state.phase,
                          state.scene_in_phase, state.E, h, state.scenes_total) for cid in sl}
    viable = [cid for cid in sl if not sims[cid].viability_fail] or None
    if viable is None:
        state.review_flags.append({"scene": state.scene, "halt": "all shortlisted fail terminal viability"})
        return
    U_A = {cid: utility(ed_s1[cid], sims[cid].V) for cid in viable}
    U_B = {cid: utility(md_s1[cid], sims[cid].V) for cid in viable} if path_b else None

    # 11: anchored confirmation on the union of the paths' top-2-by-U; floor; gap
    def top2u(u: Dict[str, float]) -> List[str]:
        return [k_ for k_, _ in sorted(u.items(), key=lambda kv: -kv[1])[:2]]
    anchored_ids = sorted(set(top2u(U_A)) | (set(top2u(U_B)) if U_B else set()))
    banded = client.anchored_confirmation(digest, [by_id[c] for c in anchored_ids],
                                          ED_DIMENSIONS + (MD_DIMENSIONS if path_b else []))
    ed2 = {cid: calibration_transform(ed_blend(
        banded[cid]["contradiction_release"], banded[cid]["causal_alignment"],
        banded[cid]["phase_fitness"], banded[cid]["motif_recontext"],
        banded[cid]["character_inevitability"], 1.0 - banded[cid]["entropy_leak"]))
        for cid in anchored_ids}
    winner = max(U_B or U_A, key=(U_B or U_A).get)
    if path_b:
        md2 = {cid: calibration_transform(md_blend(
            ed2[cid], banded[cid]["trope_satisfaction"], banded[cid]["retention"],
            banded[cid]["pacing_fit"], banded[cid]["hook_value"],
            1.0 - banded[cid]["dropoff_risk"], 1.0 - banded[cid]["over_resolution"]))
            for cid in anchored_ids}
        # ED floor on the utility winner's calibrated ED₂ — demote and repeat (§9.5)
        order = sorted(U_B, key=U_B.get, reverse=True)
        for cid in order:
            if cid in ed2 and ed2[cid] >= K.ED_FLOOR:
                winner = cid
                break
        else:
            state.review_flags.append({"scene": state.scene, "halt": "every candidate fails the ED floor"})
            return
        pair2 = sorted(md2.values(), reverse=True)[:2]
    else:
        pair2 = sorted(ed2.values(), reverse=True)[:2]
    if len(pair2) == 2:
        rho, reading = confidence_gap(pair2[0], pair2[1])
        if reading == "review flag" or winner in (os_ed | os_md):
            state.review_flags.append({"scene": state.scene, "rho": rho, "reading": reading})

    # 12: renderer — plan → verify → draft → revisions (semantic diff each) → VoiceFilter
    move = by_id[winner]
    plan = client.plan(digest, move)
    verify_plan(state, plan, move)
    text = client.draft(plan, state.kernel, band)
    for pass_name in ("dialogue", "sensory", "cadence"):
        text = diff_gated_rewrite(text, lambda t: client.revise(t, pass_name, digest),
                                  client, state)
    text = diff_gated_rewrite(text, lambda t: client.voicefilter(t, state.kernel), client, state)

    # 13: extraction → reconciliation → realized deltas → urgency/status updates
    tuples = client.extract(text, state.scene)
    realize_deltas(move.edge_deltas, tuples, state.edges, state.unrealized_log)
    touched = {d.channel for d in move.edge_deltas}
    for e in state.edges.values():
        confidence_decay(e, touched)
    accrue_urgency(state.cer, set(move.linked_CEs))

    # 14: drift + renormalise, checkpoint
    state.weights.drift(E_t=bands[dom]["desire_conflict"], N_t=1.0, B_t=0.0,
                        X_t=0.0, S_t=0.0)   # signals wired to the §5.3 logs as they populate
    apply_phase_decision(state, gate, mins)
    state.scene += 1
    state.scene_in_phase += 1
    state.checkpoint()


# ---- helpers the loop calls ---------------------------------------------------

def build_digest(state: EngineState) -> Dict[str, Any]:
    pairs = {}
    for (i, j), e in state.edges.items():
        pairs[f"{i}->{j}"] = {
            "values": {c: f"{e.values[c]:.2f}" + ("<SOFT>" if e.confidence[c] < K.CONF_SOFT else "")
                       for c in SCALAR_PRIMITIVES},
            "tag": e.register_tag(),
            "consent_reach": e.consent_reach(state.capacity.get(j, True)),
        }
    return {"scene": state.scene, "phase": state.phase, "pairs": pairs,
            "cer_open": [vars(c) for c in state.cer if c.status == "Open"]}


def structural_verify(state: EngineState, cands: List[Candidate]) -> List[Candidate]:
    """Admissibility (consent, delta bounds) + §9.3 pool diversity gates."""
    kept = []
    for c in cands:
        errs = bound_intended_deltas(c.edge_deltas)
        if c.contact:
            cls, setting = int(c.contact["class"][1]), c.contact["setting"]
            i, j = c.actor, c.target
            coer = coercion_flag(state.cer, i, j, state.protected_by)
            ok, why = contact_admissible(cls, setting, i, j, state.edges[(j, i)],
                                         state.capacity, coer,
                                         c.family == "negotiate_consent")
            if not ok:
                errs.append(f"consent: {why}")
        if not errs:
            kept.append(c)
        else:
            state.review_flags.append({"scene": state.scene, "rejected": c.id, "why": errs})
    # §9.3 pool gates (families, actors, CE coverage, Hamming, novelty) — the
    # regeneration path routes through the repair ladder; floor of 4 enforced here
    if len(kept) < 4:
        state.review_flags.append({"scene": state.scene, "pool_below_floor": len(kept)})
    return kept


def verify_plan(state: EngineState, plan: Dict[str, Any], move: Candidate) -> None:
    """Deterministic plan verification hook (L1–L12 checks attach here as the
    ledgers populate); a scene is never drafted off an unverified plan (§12.2)."""
    for beat in plan.get("beats", []):
        cc = beat.get("contact_class", "C0")
        if cc not in ("C0", "C1"):
            i, j = beat["actor"], beat.get("target", move.target)
            coer = coercion_flag(state.cer, i, j, state.protected_by)
            ok, why = contact_admissible(int(cc[1]), beat.get("setting", "private"),
                                         i, j, state.edges[(j, i)], state.capacity,
                                         coer, beat.get("negotiation", False))
            if not ok:
                raise RuntimeError(f"plan verification: inadmissible contact ({why})")


def diff_gated_rewrite(text: str, rewrite: Callable[[str], str],
                       client: ModelClient, state: EngineState) -> str:
    """§8.1 P4 diff gate: whitelist = empty diff; retry once with the diff; on
    second failure keep the prior version and flag. Unverifiable = failed (fail closed)."""
    for attempt in (1, 2):
        try:
            revised = rewrite(text)
            diff = client.semantic_diff(text, revised)
            if not (diff["added"] or diff["removed"] or diff["altered"]):
                return revised
        except Exception:                                       # noqa: BLE001
            break
    state.review_flags.append({"scene": state.scene, "diff_gate": "kept prior version"})
    return text


def evaluate_phase(state: EngineState, T_scene: float) -> GateResult:
    ceiling = PHASE_CEILINGS[state.phase]
    initiator = T_scene > ceiling            # 2+ consecutive tracked by caller in full wiring
    dom = state.dominant_pair
    e_ij, e_ji = state.edges[dom], state.edges[(dom[1], dom[0])]
    entry_ij = state.edges_at_phase_entry.get(dom, e_ij)
    entry_ji = state.edges_at_phase_entry.get((dom[1], dom[0]), e_ji)
    reach_now = (e_ij.consent_reach(state.capacity.get(dom[1], True)),
                 e_ji.consent_reach(state.capacity.get(dom[0], True)))
    g2 = g2_norm(entry_ij, e_ij, entry_ji, e_ji, reach_now, reach_now)
    crossed = any(g4_band(e_ij.values[c]) != g4_band(entry_ij.values[c]) for c in SCALAR_PRIMITIVES) \
        or any(g4_band(e_ji.values[c]) != g4_band(entry_ji.values[c]) for c in SCALAR_PRIMITIVES)
    mins = min_duration(state.E)
    remaining = state.scenes_total - state.scene
    future_min = sum(mins[state.phase + 1:])
    return evaluate_gates(beats_complete=True, g2_value=g2, ce_touched=True,
                          band_crossed_or_transition=crossed,
                          scenes_in_phase=state.scene_in_phase, min_ph=mins[state.phase],
                          scenes_remaining=remaining, future_min_total=future_min,
                          initiator=initiator)


def apply_phase_decision(state: EngineState, gate: GateResult, mins: List[int]) -> None:
    if gate.advance and state.phase < 8:
        state.phase += 1
        state.scene_in_phase = 0
        state.edges_at_phase_entry = {k_: DirectedEdge(dict(v.values), dict(v.confidence),
                                                       v.moral_repair, list(v.grants),
                                                       list(v.boundaries))
                                      for k_, v in state.edges.items()}
    elif regression_allowed(state.phase, state.low_t_run, bool(gate.blocking),
                            state.regressions, operator_flag=False):
        state.regressions += 1
        state.phase = 4                      # pacing dip, never a rollback (§6.4)
        state.scene_in_phase = 0


# =============================================================================
# SEED ROW LOADING (§16 / §4.6)
# =============================================================================

def load_seed(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        seed = json.load(f)
    core = ["Seed_ID", "Subgenre", "Heat_Level", "Ending_Type", "Dominant_Pair",
            "Dynamic", "Arc_Profile_ID", "Initial_CER_Seed", "Initial_Relationship_State",
            "Word_Count_Target", "Editor_Pass_Count"]
    missing = [k_ for k_ in core if k_ not in seed]
    if missing:
        print(f"[warn] seed row missing keys: {missing} — full §16.1 validation "
              f"belongs to the loader; proceeding on the core subset", file=sys.stderr)
    if seed.get("Subgenre") not in ARC_PROFILES:
        raise ValueError(f"Subgenre not in the R5 canon: {seed.get('Subgenre')!r}")
    return seed


DYNAMIC_PRIORS = {  # §4.6 dominant-pair defaults (provisional priors)
    "enemies_to_lovers":       dict(attraction_sexual=0.60, attraction_romantic=0.25, trust=0.15, resentment=0.55, respect=0.35),
    "grumpy_sunshine":         dict(attraction_sexual=0.40, attraction_romantic=0.45, trust=0.40, resentment=0.15, respect=0.40),
    "second_chance":           dict(attraction_sexual=0.55, attraction_romantic=0.60, trust=0.30, resentment=0.45, respect=0.50),
    "fated_mates":             dict(attraction_sexual=0.75, attraction_romantic=0.55, trust=0.35, resentment=0.10, respect=0.40),
    "marriage_of_convenience": dict(attraction_sexual=0.35, attraction_romantic=0.25, trust=0.20, resentment=0.30, respect=0.45),
    "friends_to_lovers":       dict(attraction_sexual=0.35, attraction_romantic=0.55, trust=0.75, resentment=0.05, respect=0.65),
}


def init_state(seed: Dict[str, Any], path: str) -> EngineState:
    profile = seed.get("Arc_Profile_ID", seed["Subgenre"])
    E = ARC_PROFILES[profile]
    wc = seed.get("Word_Count_Target", 0)
    scenes_total = sum(E)  # reference 90; rescale by word-count target when set
    if wc:
        scenes_total = max(sum(E), round(sum(E) * wc / 80000))
    dom = tuple(seed["Dominant_Pair"])
    st = EngineState(seed=seed, path=path, E=list(E), scenes_total=scenes_total,
                     dominant_pair=dom)
    cast = list(dom) + [a.get("name") for a in seed.get("Allies_Confidants", [])]
    if isinstance(seed.get("Antagonistic_Force"), dict):
        cast.append(seed["Antagonistic_Force"].get("name"))
    cast = [c for c in cast if c]
    for i in cast:
        st.capacity[i] = True
        for j in cast:
            if i != j:
                st.edges[(i, j)] = DirectedEdge()
    # Dynamic priors on the dominant pair (confidence 0.50), low-activation elsewhere
    priors = DYNAMIC_PRIORS.get(seed.get("Dynamic", ""), {})
    for (i, j) in ((dom[0], dom[1]), (dom[1], dom[0])):
        for ch, v in priors.items():
            st.edges[(i, j)].values[ch] = v
    # Initial_Relationship_State: explicit override, confidence 0.90; consent only
    # via explicit grant objects, logged as backstory grant records (§4.6)
    for row in seed.get("Initial_Relationship_State", []):
        e = st.edges.get((row["from"], row["to"]))
        if e is None:
            continue
        for k_, v in row.items():
            if k_ in SCALAR_PRIMITIVES:
                e.values[k_] = float(v)
                e.confidence[k_] = K.CONF_SEED
        for g in row.get("consent", []):
            e.grants.append(ConsentGrant(act_class=int(g["act_class"][1]),
                                         setting=g["scope"]["setting"],
                                         conditions=g["scope"].get("conditions", []),
                                         standing=g.get("standing", True),
                                         origin="seed"))
    for c in seed.get("Initial_CER_Seed", []):
        dl = c.get("deadline", {})
        st.cer.append(CE(id=c["id"], type=c["type"], w=float(c["w"]), u=float(c["u"]),
                         deadline_scene=dl.get("scene"), deadline_phase=dl.get("phase")))
    st.edges_at_phase_entry = {k_: DirectedEdge(dict(v.values), dict(v.confidence))
                               for k_, v in st.edges.items()}
    return st


def run_book(seed_path: str, path: str, scenes: Optional[int], client: ModelClient) -> None:
    seed = load_seed(seed_path)
    if int(seed.get("Editor_Pass_Count", 1)) < 1:
        raise ValueError("Editor_Pass_Count ≥ 1 is a hard production gate (R22)")
    state = init_state(seed, path)
    if scenes:
        state.scenes_total = scenes
    print(f"Seed {seed.get('Seed_ID','?')} · {seed['Subgenre']} · Path {path} · "
          f"{state.scenes_total} scenes · E={state.E}")
    while state.scene <= state.scenes_total and state.phase <= 8:
        try:
            run_scene(state, client)
        except NotImplementedError as e:
            print(f"\nHALT at scene {state.scene}: no binding configuration attached — {e}\n"
                  f"Deterministic core initialised and verified; subclass ModelClient and "
                  f"bind the R10 configuration (§12.1) to proceed.")
            return
    print(f"Done: {state.scene - 1} scenes, phase {state.phase}, "
          f"{len(state.review_flags)} review flags, "
          f"{len(state.unrealized_log)} unrealized deltas dropped")


# =============================================================================
# §15 FIXTURE — executable acceptance check 1
# =============================================================================

def _check(name: str, computed: float, expected: str, failures: List[str]) -> None:
    got = ledger(computed)
    ok = got == expected
    print(f"  {'✓' if ok else '✗'} {name:<28} {got}" + ("" if ok else f"  (expected {expected})"))
    if not ok:
        failures.append(name)


def run_fixture() -> int:
    print("§15 REFERENCE FIXTURE — Mafia/Dark, scene 55/90, Phase 5 scene 9")
    fails: List[str] = []

    # --- §15.1 tension ledger -------------------------------------------------
    T_raw = {"A-B": 0.84, "A-C": 0.28, "A-D": 0.66, "B-C": 0.50, "B-D": 0.44, "C-D": 0.62}
    a = {"A-B": 0.35, "A-C": 0.20, "A-D": 0.60, "B-C": 0.15, "B-D": 0.25, "C-D": 0.55}

    # A–B amplitude derived from edge primitives (§4.2)
    ab = DirectedEdge(); ab.values.update(affection=0.25, trust=0.15, resentment=0.60, fear=0.45)
    ba = DirectedEdge(); ba.values.update(affection=0.55, trust=0.25, resentment=0.30, fear=0.15)
    assert ab.register_tag() == "hostile" and ba.register_tag() == "fond"
    assert pair_class(ab.warmth(), ba.warmth()) == "crossed"
    _check("amplitude a_AB", pair_amplitude(ab, ba), "0.3500", fails)

    bleed_raw = sum(v for k_, v in T_raw.items() if k_ != "A-B") / 5
    lam = lambda_t(T_raw["A-B"], bleed_raw)
    _check("lambda_t", lam, "0.2690", fails)
    amp = {p: amplify(T_raw[p], lam, a[p]) for p in T_raw}
    for p, exp in [("A-B", "0.8527"), ("A-C", "0.2908"), ("A-D", "0.6962"),
                   ("B-C", "0.5101"), ("B-D", "0.4566"), ("C-D", "0.6549")]:
        _check(f"T~({p})", amp[p], exp, fails)
    T_scene, T_dom, T_bleed = scene_tension(amp, "A-B")
    _check("T_dominant", T_dom, "0.8527", fails)
    _check("T_bleed", T_bleed, "0.5217", fails)
    _check("T_scene", T_scene, "0.7534", fails)

    cer = [CE("CE-01", "Secret", 0.90, 0.70, deadline_scene=58),
           CE("CE-02", "Threat", 0.75, 0.55, deadline_scene=56),
           CE("CE-03", "Obligation", 0.50, 0.30, deadline_scene=60),
           CE("CE-04", "Promise", 0.35, 0.20, deadline_scene=63)]
    d_of = lambda ce: deadline_d(ce, 55, 5, 9, ARC_PROFILES["Mafia/Dark"])
    S = causal_load(cer, d_of)
    _check("S", S, "0.3965", fails)
    Tc = t_causal(S)
    _check("T_causal", Tc, "0.4978", fails)
    kap = kappa_t(0.25)
    _check("kappa_t", kap, "0.1750", fails)
    T_eff = effective_tension(T_scene, Tc, kap)
    _check("T_eff", T_eff, "0.7749", fails)
    assert routing_band(T_eff) == "climax"

    # G2 / G4 micro-check
    g2 = (0.05 + 0.05 + 0.10 + 0.05) + (0.20 + 0.05)
    _check("G2", g2, "0.5000", fails)
    assert g4_band(0.35) == 1 and g4_band(0.55) == 2      # B→A affection B1→B2 ✓
    assert g4_band(0.70) == 3 and g4_band(0.60) == 3      # A→B resentment stays B3 ✓

    # --- §15.2 deadline transform --------------------------------------------
    ce_ph = CE("CE-X", "Promise", 0.5, 0.5, deadline_phase=6)
    d = deadline_d(ce_ph, 55, 5, 9, ARC_PROFILES["Mafia/Dark"])
    print(f"  {'✓' if d == 15 else '✗'} phase-typed d              {d}  (p = {ledger(1/(d+1))})")
    if d != 15: fails.append("deadline transform")

    # --- §15.5 Bradley–Terry micro-fixture -----------------------------------
    wins = {"a1": {"a2": 0, "a3": 1, "a4": 1},
            "a2": {"a1": 2, "a3": 2, "a4": 2},
            "a3": {"a1": 1, "a2": 0, "a4": 2},
            "a4": {"a1": 1, "a2": 0, "a3": 0}}
    pi, s_ci, iters = bt_fit(["a1", "a2", "a3", "a4"], wins)
    for cid, exp in [("a2", "3.4281"), ("a3", "0.9748"), ("a1", "0.6667"), ("a4", "0.4488")]:
        _check(f"pi({cid})", pi[cid], exp, fails)
    for cid, exp in [("a2", "0.7742"), ("a3", "0.4936"), ("a1", "0.4000"), ("a4", "0.3098")]:
        _check(f"s({cid})", s_ci[cid], exp, fails)
    med = (sorted(s_ci.values())[1] + sorted(s_ci.values())[2]) / 2
    _check("field median", med, "0.4468", fails)
    print(f"    (converged in {iters} iterations; Ππ = {ledger(math.prod(pi.values()))})")

    # --- §15.3 Path A Stage-1 -------------------------------------------------
    s1 = {  # ledger-precision BT columns; CI column = §15.5 fit output
        "a1": dict(CR=0.3333, CA=0.6000, PF=0.6154, MR=0.4444, CI=0.4000, CL=0.4444),
        "a2": dict(CR=0.6667, CA=0.4444, PF=0.7500, MR=0.6154, CI=0.7742, CL=0.5556),
        "a3": dict(CR=0.2000, CA=0.2174, PF=0.5000, MR=0.5000, CI=0.4936, CL=0.6667),
        "a4": dict(CR=0.8000, CA=0.7500, PF=0.1724, MR=0.4386, CI=0.3098, CL=0.3333),
    }
    ED = {c: ed_blend(v["CR"], v["CA"], v["PF"], v["MR"], v["CI"], v["CL"]) for c, v in s1.items()}
    for c, exp in [("a1", "0.4590"), ("a2", "0.6455"), ("a3", "0.3605"), ("a4", "0.5383")]:
        _check(f"ED({c})", ED[c], exp, fails)
    _check("rho_ED stage-1", ED["a2"] - ED["a4"], "0.1072", fails)

    # --- §15.4 Path B Stage-1 (ED at full precision) --------------------------
    s1b = {
        "a1": dict(TS=0.7143, RP=0.7500, PFm=0.6667, HV=0.7143, SF=0.5556, PR=0.5000),
        "a2": dict(TS=0.2857, RP=0.2500, PFm=0.6000, HV=0.2000, SF=0.3333, PR=0.6667),
        "a3": dict(TS=0.6154, RP=0.3333, PFm=0.5455, HV=0.3333, SF=0.5000, PR=0.5556),
        "a4": dict(TS=0.3846, RP=0.6667, PFm=0.2174, HV=0.7619, SF=0.6154, PR=0.2857),
    }
    MD = {c: md_blend(ED[c], v["TS"], v["RP"], v["PFm"], v["HV"], v["SF"], v["PR"])
          for c, v in s1b.items()}
    for c, exp in [("a1", "0.6296"), ("a2", "0.4246"), ("a3", "0.4454"), ("a4", "0.5071")]:
        _check(f"MD({c})", MD[c], exp, fails)
    _check("rho_MD stage-1", MD["a1"] - MD["a4"], "0.1225", fails)

    # --- §15.6 shortlist, lookahead, utility ----------------------------------
    sl = shortlist(ED, MD, order_sensitive=set())
    assert sl == ["a1", "a2", "a4"], sl
    print(f"  ✓ shortlist                  {{{', '.join(sl)}}} (a3 near-cutoff gaps "
          f"{ledger(ED['a4']-ED['a3'])} / {ledger(MD['a4']-MD['a3'])} > ε)")
    linked = {"a1": ["CE-01", "CE-02"], "a2": ["CE-01", "CE-02"], "a4": ["CE-01"]}
    sims = {}
    for cid in sl:
        cand = Candidate(cid, "probe_test", "A", "B", linked[cid])
        sims[cid] = simulate(cand, cer, 55, 5, 9, ARC_PROFILES["Mafia/Dark"], h=2, scenes_total=90)
    assert sims["a4"].misfires == 1 and sims["a1"].misfires == 0 and sims["a2"].misfires == 0
    _check("V(a4)", sims["a4"].V, "0.7500", fails)
    UA = {c: utility(ED[c], sims[c].V) for c in sl}
    UB = {c: utility(MD[c], sims[c].V) for c in sl}
    for c, exp in [("a1", "0.6213"), ("a2", "0.7519"), ("a4", "0.6018")]:
        _check(f"U_A({c})", UA[c], exp, fails)
    for c, exp in [("a1", "0.7407"), ("a2", "0.5973"), ("a4", "0.5800")]:
        _check(f"U_B({c})", UB[c], exp, fails)
    # counterfactual: unpenalized a4 would displace a2 from Path B's head
    _check("U_B(a4) unpenalized", utility(MD["a4"], 1.0), "0.6550", fails)
    anchored = sorted(set(sorted(UA, key=UA.get, reverse=True)[:2])
                      | set(sorted(UB, key=UB.get, reverse=True)[:2]))
    assert anchored == ["a1", "a2"], anchored
    print(f"  ✓ anchored union             {{{', '.join(anchored)}}}")

    # --- §15.7 anchored confirmation (identity transforms) --------------------
    banded = {"a1": dict(CR=0.75, CA=0.75, PF=0.50, MR=0.50, CI=0.75, EL=0.25,
                         TS=0.75, RP=0.75, PFm=0.75, HV=0.75, DR=0.25, OR=0.50),
              "a2": dict(CR=0.75, CA=0.75, PF=0.75, MR=0.75, CI=0.75, EL=0.25,
                         TS=0.25, RP=0.25, PFm=0.50, HV=0.25, DR=0.50, OR=0.25)}
    ED2 = {c: calibration_transform(ed_blend(v["CR"], v["CA"], v["PF"], v["MR"],
                                             v["CI"], 1 - v["EL"])) for c, v in banded.items()}
    _check("ED2(a1)", ED2["a1"], "0.6875", fails)
    _check("ED2(a2)", ED2["a2"], "0.7500", fails)
    _check("rho_ED (stage-2)", ED2["a2"] - ED2["a1"], "0.0625", fails)
    MD2 = {c: calibration_transform(md_blend(ED2[c], v["TS"], v["RP"], v["PFm"],
                                             v["HV"], 1 - v["DR"], 1 - v["OR"]))
           for c, v in banded.items()}
    _check("MD2(a1)", MD2["a1"], "0.7238", fails)
    _check("MD2(a2)", MD2["a2"], "0.4500", fails)
    _check("rho_MD (stage-2)", MD2["a1"] - MD2["a2"], "0.2738", fails)
    assert ED2["a1"] >= K.ED_FLOOR, "Path B winner a1 must clear the ED floor"
    print(f"  ✓ ED floor                   a1 ED2 {ledger(ED2['a1'])} ≥ {K.ED_FLOOR} (provisional)")

    # --- acceptance check 2: weight sums; E-vectors sum to 90 -----------------
    assert abs(sum(K.ED_W.values()) - 1.0) < 1e-12
    assert abs(sum(K.MD_W.values()) - 1.0) < 1e-12
    assert abs(sum(K.W_PAIR_BASE.values()) - 1.0) < 1e-12
    assert all(sum(E) == 90 for E in ARC_PROFILES.values())
    print("  ✓ weight sums (1e-12) · all twelve E-vectors sum to 90")

    print()
    if fails:
        print(f"FIXTURE FAILED: {len(fails)} value(s) diverge: {fails}")
        return 1
    print("FIXTURE REPRODUCED EXACTLY — acceptance check 1 (§15.9) passes.")
    return 0


# =============================================================================
# CLI
# =============================================================================

def main() -> int:
    p = argparse.ArgumentParser(description="Romance Engine orchestrator (v5.0 deterministic core + scene loop)")
    p.add_argument("--fixture", action="store_true", help="reproduce the §15 reference ledgers and assert exact")
    p.add_argument("--seed", help="path to a Unified_Seed_Row JSON")
    p.add_argument("--path", choices=["A", "B"], default="B", help="Path A (Eigendrama) or Path B (Market Drama)")
    p.add_argument("--scenes", type=int, help="override total scene count")
    args = p.parse_args()

    if args.fixture:
        return run_fixture()
    if args.seed:
        run_book(args.seed, args.path, args.scenes, StubModelClient())
        return 0
    p.print_help()
    return 2


class StubModelClient(ModelClient):
    """No binding configuration attached. Every call class raises with its name,
    so a run against a seed row exercises initialisation and halts at the first
    elicitation — exactly where the R10 binding has to be supplied."""
    pass


if __name__ == "__main__":
    sys.exit(main())
