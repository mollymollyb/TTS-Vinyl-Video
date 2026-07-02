# Vinyl Video Editor OS — the brain

Agent-run video editing system for Rostrum's TikTok Shop vinyl videos
(Molly B). Raw phone footage of vinyl showcases goes in; short, coherent,
platform-ready cuts come out — plus captions. Molly and Sidney both pull
this repo; all heavy video bytes stay OUT of git.

## The two planes (the most important rule in this file)

| Plane | Where | What lives there |
|---|---|---|
| **Git** (this repo) | GitHub `mollymollyb/TTS-Vinyl-Video` | skills, library code, `releases/{slug}/` records (release.json, analysis.json, EDLs, captions), knowledge, dashboards |
| **Media** (never git) | path in `media.config.json` (local folder or Google Drive) | `raw/` originals, `derived/{slug}/` proxies+frames, `work/{slug}/{date}/` draft renders, `finals/{slug}/` approved videos |

**MEDIA NEVER ENTERS GIT.** The `.gitignore` blocks `media/` and all video
extensions. A render is regenerable from `raw file + EDL`, so drafts are
disposable. If you are about to write ANY media file, resolve its
destination through `library/media_paths.py` — never invent a path.

Media lifecycle rules: `raw/` = never modify or delete. `derived/` =
regenerable, safe to delete. `work/` = ephemeral drafts, janitor prunes
after 14 days. `finals/` = approved keepers.

## Capability tiers (keys are optional, never required)

- **Tier 0 — no keys:** ffmpeg everything (ingest, proxies, scene maps,
  frames, EDL validation, rendering).
- **Tier 1 — no keys:** agent labels the sampled frames itself by Reading
  them (`vinyl-analyze` fallback). Full pipeline still works.
- **Tier 2 — `TWELVE_LABS_API_KEY`:** programmatic shot labels; enables
  unattended runs.
- **Tier 3 — `SWIFT_LABS_TRIBE_API_KEY` (optional):** engagement score used
  ONLY to rank already-coherent variants. It never chooses cuts —
  optimizing engagement alone produces incoherent edits (proven in the
  auto-edit spike this library came from).

Missing key = run the fallback silently. Never error out over a key.

## The release lifecycle

Each vinyl product is a **release** at `releases/{slug}/`, moving through
statuses in `release.json`: `raw → analyzed → editing → review → final`.

1. `vinyl-ingest` — register raw files, probe metadata, guess release type
   (draft — Molly confirms).
2. `vinyl-analyze` — proxy, scene map, frames, labels; then the agent
   groups shots into **sequences** (one event, e.g. "pulls vinyl 2 out"),
   each with a hard never-cut-inside boundary. Writes `analysis.json`.
3. `vinyl-edit` — 2-3 EDL variants honoring `knowledge/editing-rules.md`;
   render drafts to `work/`.
4. `vinyl-review` — verify no cut lands inside a sequence, check the
   ending, inspect cut-boundary frames. Re-edit until clean.
5. `vinyl-caption` — caption + product description into `caption.md`.
6. Molly approves → copy render to `finals/`, status `final`,
   `vinyl-learn` captures why the winning variant won.

## Filing decision tree

- New raw footage arrived → `vinyl-ingest`, then update `releases/_board.md`.
- Molly gave feedback ("use v2, hate the ending") → `knowledge/decisions/`
  via `vinyl-learn`, and fold durable rules into
  `knowledge/editing-rules.md`.
- A new editing insight or vinyl-format quirk → `knowledge/editing-rules.md`
  or `knowledge/release-types.md`.
- One-off task (not a release, not recurring) → `work/YYYY-MM-DD-{name}/`
  in git (text only).
- Same manual process done twice → promote via `vinyl-skillify` into
  `plugin/skills/`.
- System friction (routing, checks, templates) → `vinyl-reflect` →
  `operations/improvements.md`.

## Never-stale contract

If you touch a release, update ITS `README.md` + `release.json` status,
`releases/_board.md`, and `artifacts/dashboard.html` in the same turn.
If you add a file or module, log it in `project-overview.md`. The
`vinyl-janitor` skill (weekly routine) is the safety net, not the excuse.

## Commands (run from repo root; use .venv)

```bash
.venv/bin/python -m library.ingest --all
.venv/bin/python -m library.analyze --release {slug} [--take N] [--no-tl]
.venv/bin/python -m library.edl_render releases/{slug}/edits/v1.edl.json
.venv/bin/python operations/doctor.py          # read-only health check
```

Setup on a new machine: `python3 -m venv .venv && .venv/bin/pip install -r
requirements.txt`, copy `media.config.example.json` → `media.config.json`
(set your path), optionally copy `.env.example` → `.env` (add keys).

## Hard rules

- Never commit media. Verify with `git status` before any commit.
- Never modify or delete anything in `media/raw/`.
- Never let an engagement metric choose cuts (Tier 3 is a tiebreaker only).
- Renders always cut from the RAW file; proxies are for analysis only.
- Every inferred fact (release type, target length) ships as
  "draft — confirm" until Molly confirms it.
