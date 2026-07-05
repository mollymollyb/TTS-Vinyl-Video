"""genmedia_ledger.py — per-release spend ledger for AI-generated media.

Molly/Sidney generate hooks, restyles, and b-roll through fal.ai (via the
external `genmedia` CLI — not part of this repo). This module is the
structured, git-committable twin of that work: one JSON record per fal
call (model, settings, cost) plus one record per finished composite that
lists which generations (and how much real footage) it's built from.
Tier 0 — no API keys, no fal integration. Cost is entered by whoever ran
the generation (read straight off the genmedia CLI's own cost output);
this module only stores, validates, and rolls it up.

Schema (releases/{slug}/genmedia.json):
    {
      "release": "wiz-khalifa-cabin-fever-trilogy",
      "generations": [
        {
          "id": "A1",                          # matches the ID used in
                                                # genmedia-experiments.md
          "batch": "A",                        # optional grouping label
          "date": "2026-07-03",
          "model": "seedance-2.0/fast/i2v",
          "operation": "i2v",                  # i2v | t2v | edit | composite
          "settings": {"resolution": "720p", "duration_seconds": 5},
          "inputs": ["seed_red_peak"],          # prior generation ids OR
                                                # freeform seed/asset names
          "output_units": {"quantity": 5, "unit": "video_seconds"},
          "unit_price_usd": 0.02,
          "cost_usd": 0.10,
          "cost_confidence": "exact",          # exact | estimated | unknown
          "status": "success",                 # success | failed
          "verdict": "used",                    # cool | meh | kill | used
          "output_path": "genmedia/A1.mp4",     # media-plane relative path
          "notes": "red disc spins, dolly-in, lens flare"
        }
      ],
      "finals": [
        {
          "id": "X1",
          "output_path": "genmedia/X1.mp4",
          "components": [
            {"type": "generated", "generation_id": "F2"},
            {"type": "raw_footage", "ref": "v3 edit", "seconds": 16.2}
          ],
          "notes": "F2 torn-cover hook -> real v3"
        }
      ]
    }

A final's cost is the SUM of every "generated" component's own cost_usd
PLUS its full upstream `inputs` lineage (e.g. F2 depends on B5), deduped
so a shared ancestor is only counted once. Unknown cost anywhere in a
final's lineage makes that final's total_cost_usd None rather than
silently under-counting — see final_cost().

CLI (from repo root):
    .venv/bin/python -m library.genmedia_ledger add-generation \\
        --release wiz-khalifa-cabin-fever-trilogy --json '{"id": "A8", ...}'
    .venv/bin/python -m library.genmedia_ledger add-final \\
        --release wiz-khalifa-cabin-fever-trilogy --json '{"id": "X4", ...}'
    .venv/bin/python -m library.genmedia_ledger summary --release wiz-khalifa-cabin-fever-trilogy
    .venv/bin/python -m library.genmedia_ledger global-summary
    .venv/bin/python -m library.genmedia_ledger validate
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from library.env_config import REPO_ROOT

RELEASES_DIR = REPO_ROOT / "releases"

VALID_STATUS = {"success", "failed"}
VALID_CONFIDENCE = {"exact", "estimated", "unknown"}
VALID_COMPONENT_TYPES = {"generated", "raw_footage"}


class LedgerError(Exception):
    """A generation/final record fails schema or reference validation."""


def ledger_path(slug: str) -> Path:
    return RELEASES_DIR / slug / "genmedia.json"


def load_ledger(slug: str) -> dict:
    path = ledger_path(slug)
    if not path.exists():
        return {"release": slug, "generations": [], "finals": []}
    return json.loads(path.read_text())


def save_ledger(slug: str, ledger: dict) -> Path:
    path = ledger_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, indent=2) + "\n")
    return path


def validate_generation(record: dict) -> list[str]:
    """Field-level checks for one generation record. No cross-references."""
    problems: list[str] = []
    label = record.get("id", "<missing id>")
    for field in ("id", "model", "operation", "status", "cost_confidence"):
        if not record.get(field):
            problems.append(f"generation '{label}': missing '{field}'")
    if record.get("status") not in (None, "") and record["status"] not in VALID_STATUS:
        problems.append(f"generation '{label}': status must be one of {sorted(VALID_STATUS)}")
    if record.get("cost_confidence") not in (None, "") and record["cost_confidence"] not in VALID_CONFIDENCE:
        problems.append(f"generation '{label}': cost_confidence must be one of {sorted(VALID_CONFIDENCE)}")
    if "cost_usd" not in record:
        problems.append(f"generation '{label}': missing 'cost_usd' (use null if unknown)")
    elif record["cost_usd"] is not None:
        try:
            if float(record["cost_usd"]) < 0:
                problems.append(f"generation '{label}': cost_usd cannot be negative")
        except (TypeError, ValueError):
            problems.append(f"generation '{label}': cost_usd must be a number or null")
    return problems


def validate_final(record: dict, known_generation_ids: set[str]) -> list[str]:
    """Field-level + reference checks for one final composite record."""
    problems: list[str] = []
    label = record.get("id", "<missing id>")
    if not record.get("id"):
        problems.append("final: missing 'id'")
    components = record.get("components")
    if not isinstance(components, list) or not components:
        return problems + [f"final '{label}': 'components' must be a non-empty list"]
    for index, component in enumerate(components):
        ctype = component.get("type")
        if ctype not in VALID_COMPONENT_TYPES:
            problems.append(
                f"final '{label}' component {index}: type must be one of {sorted(VALID_COMPONENT_TYPES)}"
            )
        if ctype == "generated":
            gid = component.get("generation_id")
            if not gid:
                problems.append(f"final '{label}' component {index}: missing 'generation_id'")
            elif gid not in known_generation_ids:
                problems.append(
                    f"final '{label}' component {index}: generation_id '{gid}' not in this release's generations"
                )
    return problems


def validate_ledger(ledger: dict) -> list[str]:
    """Whole-file validation: field checks + duplicate ids + references."""
    problems: list[str] = []
    seen_ids: set[str] = set()
    for generation in ledger.get("generations", []):
        problems.extend(validate_generation(generation))
        gid = generation.get("id")
        if gid:
            if gid in seen_ids:
                problems.append(f"duplicate generation id '{gid}'")
            seen_ids.add(gid)
    for final in ledger.get("finals", []):
        problems.extend(validate_final(final, seen_ids))
    return problems


def generation_cost(ledger: dict, generation_id: str, _seen: set[str] | None = None) -> float | None:
    """Cost of one generation INCLUDING its upstream `inputs` lineage,
    deduped so a shared ancestor is only counted once. None = unknown
    somewhere in the chain (missing cost_usd or a dangling reference)."""
    seen = _seen if _seen is not None else set()
    if generation_id in seen:
        return 0.0  # already counted via a sibling branch
    seen.add(generation_id)
    by_id = {g["id"]: g for g in ledger.get("generations", [])}
    generation = by_id.get(generation_id)
    if generation is None:
        return None
    own_cost = generation.get("cost_usd")
    if own_cost is None:
        return None
    total = float(own_cost)
    for input_id in generation.get("inputs") or []:
        if input_id not in by_id:
            continue  # freeform seed/asset name, not a costed generation
        upstream = generation_cost(ledger, input_id, seen)
        if upstream is None:
            return None
        total += upstream
    return total


def final_cost(ledger: dict, final_id: str) -> dict:
    """Cost + shot-count rollup for one final. total_cost_usd is None if
    any generated component's lineage has an unknown cost anywhere."""
    by_id = {f["id"]: f for f in ledger.get("finals", [])}
    final = by_id.get(final_id)
    if final is None:
        raise LedgerError(f"no final '{final_id}' in this ledger")
    seen: set[str] = set()
    known_total = 0.0
    unknown_ids: list[str] = []
    generated_count = 0
    raw_footage_count = 0
    for component in final["components"]:
        if component["type"] == "raw_footage":
            raw_footage_count += 1
            continue
        generated_count += 1
        gid = component["generation_id"]
        cost = generation_cost(ledger, gid, seen)
        if cost is None:
            unknown_ids.append(gid)
        else:
            known_total += cost
    return {
        "id": final_id,
        "total_cost_usd": None if unknown_ids else round(known_total, 4),
        "known_partial_cost_usd": round(known_total, 4),
        "generated_shot_count": generated_count,
        "raw_footage_shot_count": raw_footage_count,
        "unknown_cost_generation_ids": unknown_ids,
    }


def add_generation(slug: str, record: dict) -> Path:
    ledger = load_ledger(slug)
    existing_ids = {g["id"] for g in ledger["generations"]}
    if record.get("id") in existing_ids:
        raise LedgerError(f"generation id '{record.get('id')}' already exists in {slug}")
    problems = validate_generation(record)
    if problems:
        raise LedgerError("; ".join(problems))
    record.setdefault("date", dt.date.today().isoformat())
    ledger["generations"].append(record)
    return save_ledger(slug, ledger)


def add_final(slug: str, record: dict) -> Path:
    ledger = load_ledger(slug)
    if record.get("id") in {f["id"] for f in ledger["finals"]}:
        raise LedgerError(f"final id '{record.get('id')}' already exists in {slug}")
    gen_ids = {g["id"] for g in ledger["generations"]}
    problems = validate_final(record, gen_ids)
    if problems:
        raise LedgerError("; ".join(problems))
    ledger["finals"].append(record)
    return save_ledger(slug, ledger)


def release_summary(slug: str) -> dict:
    ledger = load_ledger(slug)
    generations = ledger.get("generations", [])
    known_costs = [g["cost_usd"] for g in generations if g.get("cost_usd") is not None]
    by_model: dict[str, float] = {}
    for generation in generations:
        if generation.get("cost_usd") is not None:
            model = generation["model"]
            by_model[model] = by_model.get(model, 0.0) + generation["cost_usd"]
    finals = [final_cost(ledger, final["id"]) for final in ledger.get("finals", [])]
    return {
        "release": slug,
        "generation_count": len(generations),
        "total_spend_usd": round(sum(known_costs), 4),
        "unknown_cost_generation_count": len(generations) - len(known_costs),
        "spend_by_model": {
            model: round(amount, 4)
            for model, amount in sorted(by_model.items(), key=lambda kv: -kv[1])
        },
        "finals": finals,
    }


def global_summary() -> dict:
    slugs = sorted({path.parent.name for path in RELEASES_DIR.glob("*/genmedia.json")})
    per_release = {slug: release_summary(slug) for slug in slugs}
    by_model: dict[str, float] = {}
    for summary in per_release.values():
        for model, amount in summary["spend_by_model"].items():
            by_model[model] = by_model.get(model, 0.0) + amount
    costed_finals = [
        final for summary in per_release.values() for final in summary["finals"]
        if final["total_cost_usd"] is not None
    ]
    avg_cost_per_final = (
        round(sum(f["total_cost_usd"] for f in costed_finals) / len(costed_finals), 4)
        if costed_finals else None
    )
    return {
        "release_count": len(per_release),
        "total_spend_usd": round(sum(s["total_spend_usd"] for s in per_release.values()), 4),
        "spend_by_model": {
            model: round(amount, 4)
            for model, amount in sorted(by_model.items(), key=lambda kv: -kv[1])
        },
        "finals_with_known_cost": len(costed_finals),
        "avg_cost_per_final_usd": avg_cost_per_final,
        "per_release": per_release,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    add_gen = sub.add_parser("add-generation", help="Append one fal generation record")
    add_gen.add_argument("--release", required=True)
    add_gen.add_argument("--json", required=True, dest="record_json", help="Generation record as a JSON object")

    add_fin = sub.add_parser("add-final", help="Append one finished composite record")
    add_fin.add_argument("--release", required=True)
    add_fin.add_argument("--json", required=True, dest="record_json", help="Final record as a JSON object")

    summary_parser = sub.add_parser("summary", help="Spend summary for one release")
    summary_parser.add_argument("--release", required=True)

    sub.add_parser("global-summary", help="Spend summary across every release")

    validate_parser = sub.add_parser("validate", help="Schema-check one release's ledger (or all)")
    validate_parser.add_argument("--release", help="Limit to one release; omit to check every release")

    args = parser.parse_args()

    if args.command == "add-generation":
        try:
            path = add_generation(args.release, json.loads(args.record_json))
        except (LedgerError, json.JSONDecodeError) as err:
            print(f"error: {err}", file=sys.stderr)
            return 1
        print(f"added -> {path.relative_to(REPO_ROOT)}")
        return 0

    if args.command == "add-final":
        try:
            path = add_final(args.release, json.loads(args.record_json))
        except (LedgerError, json.JSONDecodeError) as err:
            print(f"error: {err}", file=sys.stderr)
            return 1
        print(f"added -> {path.relative_to(REPO_ROOT)}")
        return 0

    if args.command == "summary":
        print(json.dumps(release_summary(args.release), indent=2))
        return 0

    if args.command == "global-summary":
        print(json.dumps(global_summary(), indent=2))
        return 0

    if args.command == "validate":
        slugs = [args.release] if args.release else sorted(
            {path.parent.name for path in RELEASES_DIR.glob("*/genmedia.json")}
        )
        if not slugs:
            print("no releases/*/genmedia.json files found.")
            return 0
        ok = True
        for slug in slugs:
            problems = validate_ledger(load_ledger(slug))
            if problems:
                ok = False
                print(f"{slug}: {len(problems)} problem(s)")
                for problem in problems:
                    print(f"  - {problem}")
            else:
                print(f"{slug}: OK")
        return 0 if ok else 1

    return 1


if __name__ == "__main__":
    sys.exit(main())
