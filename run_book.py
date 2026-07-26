#!/usr/bin/env python3
"""Run the Romance Engine scene loop on the Seed-Matrix row under the
offline-agent-v1 binding configuration and emit the production artifacts.

Usage:
  python run_book.py [--seed seed/seed_row.json] [--scenes 45] [--path B]

Outputs (artifacts/):
  scene_ledger.json  - the per-scene structural ledger (tension chain, band,
                       selected move, CE lifecycle, dominant-edge state)
  scene_briefs.md    - the renderer work orders (PRIMARY-PROSE input)
  run_summary.md     - run report: phase geometry, gates, flags

main.py is used as-is (its §15 fixture remains the acceptance instrument).
The one caller-side completion: main.py's evaluate_phase computes the §6.3
initiator from T_scene only and notes that fracture/inversion initiators are
"tracked by caller in full wiring" — this driver supplies that wiring for the
two scheduled fracture scenes (warrant executed; reversal complete).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import main as eng
from binding.offline_client import OfflineBindingClient
from binding.schedule import (SCENE, PHASE_BLOCKS, FRACTURE_SCENES, CHAPTERS,
                              DISPLAY)

ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"


def expected_phase(scene: int) -> int:
    for ph, (a, b) in PHASE_BLOCKS.items():
        if a <= scene <= b:
            return ph
    raise ValueError(scene)


def install_fracture_initiator() -> None:
    orig = eng.evaluate_phase

    def evaluate_phase(state, T_scene):
        res = orig(state, T_scene)
        if state.scene in FRACTURE_SCENES and not res.advance:
            if not res.blocking:
                return eng.GateResult(advance=True, blocking=[])
        return res

    eng.evaluate_phase = evaluate_phase


def edge_snapshot(state: eng.EngineState) -> dict:
    out = {}
    dom = state.dominant_pair
    for (i, j) in (dom, (dom[1], dom[0])):
        e = state.edges[(i, j)]
        out[f"{i}->{j}"] = {
            "values": {c: round(e.values[c], 4) for c in eng.SCALAR_PRIMITIVES},
            "register_tag": e.register_tag(),
            "grants": [f"C{g.act_class}/{g.setting}"
                       for g in e.grants if not g.void],
            "moral_repair": round(e.moral_repair, 4),
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="seed/seed_row.json")
    ap.add_argument("--scenes", type=int, default=45)
    ap.add_argument("--path", choices=["A", "B"], default="B")
    args = ap.parse_args()

    seed = eng.load_seed(args.seed)
    assert int(seed.get("Editor_Pass_Count", 1)) >= 1, "R22 gate"
    state = eng.init_state(seed, args.path)
    state.scenes_total = args.scenes
    state.kernel = {
        "id": seed["VK_Kernel_ID"],
        "SYN": seed["Sentence_Rhythm_Targets"],
        "LEX": {"preferred": seed["Brand_Lexicon"]["preferred"],
                "banned": seed["Brand_Lexicon"]["banned"],
                "lyricality": seed["Lyricality"]},
        "ATT": ["hands", "money/paper", "exits", "sound"],
        "COMP": 0.65,
        "REG": 0.7,
        "signature_moves": seed["Signature_Moves"],
        "pov": seed["POV"], "tense": seed["Tense"],
        "register": seed["Register"],
    }
    install_fracture_initiator()

    client = OfflineBindingClient()
    client.state = state

    print(f"Seed {seed['Seed_ID']} - {seed['Title']} - {seed['Subgenre']} - "
          f"Path {args.path} - {state.scenes_total} scenes - E={state.E}")

    problems = []
    while state.scene <= state.scenes_total and state.phase <= 8:
        n = state.scene
        want_ph = expected_phase(n)
        if state.phase != want_ph:
            problems.append(f"scene {n}: phase {state.phase}, expected {want_ph}")
        eng.run_scene(state, client)
        if not client.records or client.records[-1]["scene"] != n:
            problems.append(f"scene {n}: no ledger record (halted?)")
            break
        rec = client.records[-1]
        rec["phase_after"] = state.phase
        rec["edges"] = edge_snapshot(state)
        rec["cer"] = [{"id": c.id, "status": c.status, "w": round(c.w, 4),
                       "u": round(c.u, 4)} for c in state.cer]
        if rec["move"]["id"] != f"s{n}-plan":
            problems.append(f"scene {n}: selector chose {rec['move']['id']}")

    ok_scenes = len(client.records)
    print(f"{ok_scenes} scenes shipped - final phase {state.phase} - "
          f"{len(state.review_flags)} review flags - "
          f"{len(state.unrealized_log)} unrealized deltas")
    for f in state.review_flags:
        print("  flag:", f)
    for p in problems:
        print("  PROBLEM:", p)

    ART.mkdir(exist_ok=True)
    (ART / "scene_ledger.json").write_text(json.dumps({
        "seed_id": seed["Seed_ID"], "title": seed["Title"],
        "binding_configuration": "offline-agent-v1",
        "path": args.path, "scenes_total": state.scenes_total,
        "arc_profile_E": state.E,
        "review_flags": state.review_flags,
        "unrealized_deltas": state.unrealized_log,
        "scenes": client.records,
    }, indent=2), encoding="utf-8")

    # -------- renderer work orders ------------------------------------
    lines = ["# Scene Briefs - Clean Exit (Seed 01KYDG7NWVMNN9C7DTKZ76F54Q)",
             "",
             "PRIMARY-PROSE work orders emitted by the scene loop under the",
             "offline-agent-v1 binding. One block per shipped scene; the",
             "manuscript renders these under kernel VK-EN-MD-01.", ""]
    by_scene = {r["scene"]: r for r in client.records}
    for ch_no, ch_title, scene_ids in CHAPTERS:
        head = f"Epilogue - {ch_title}" if ch_no is None else \
               f"Chapter {ch_no} - {ch_title}"
        lines += [f"## {head}", ""]
        for sid in scene_ids:
            sch = SCENE[sid]
            rec = by_scene.get(sid, {})
            pov = DISPLAY.get(sch["pov"], sch["pov"])
            lines += [
                f"### Scene {sid:02d} - {sch['title']}",
                f"- POV: {pov} (close third, past) - story day {sch['day']}"
                f" - {sch['loc']}",
                f"- phase {rec.get('phase', '?')} - band {rec.get('band')}"
                f" - T_scene {rec.get('T_scene')} - T_eff {rec.get('T_eff')}",
                f"- move: {sch['family']} {sch['actor']}->{sch['target']}"
                f" - motif: {sch['motif']}",
                f"- registers: A->B {rec.get('register_tag_AB')}, "
                f"B->A {rec.get('register_tag_BA')}",
                f"- synopsis: {sch['syn']}",
                "- beats:",
            ]
            lines += [f"  - {b}" for b in sch["beats"]]
            lines.append("")
    (ART / "scene_briefs.md").write_text("\n".join(lines), encoding="utf-8")

    # -------- run summary ----------------------------------------------
    ph_geom = {}
    for r in client.records:
        ph_geom.setdefault(r["phase"], []).append(r["scene"])
    summary = ["# Run summary - Clean Exit", "",
               f"- binding configuration: offline-agent-v1 (no calibration "
               f"card; floors provisional per R11)",
               f"- scenes shipped: {ok_scenes}/{state.scenes_total}",
               f"- final phase: {state.phase}",
               f"- review flags: {len(state.review_flags)}",
               f"- unrealized deltas dropped: {len(state.unrealized_log)}",
               f"- schedule problems: {problems if problems else 'none'}",
               "", "## Phase geometry", ""]
    for ph in sorted(ph_geom):
        s = ph_geom[ph]
        summary.append(f"- phase {ph}: scenes {s[0]}-{s[-1]} ({len(s)})")
    summary += ["", "## CE lifecycle (final)", ""]
    for c in state.cer:
        summary.append(f"- {c.id}: {c.status} (w={c.w:.2f}, u={c.u:.2f})")
    (ART / "run_summary.md").write_text("\n".join(summary) + "\n",
                                        encoding="utf-8")
    print("artifacts written:", ", ".join(p.name for p in sorted(ART.iterdir())))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
