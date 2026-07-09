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

**MEDIA NEVER ENTERS GIT.** The `.gitignore` blocks `media` (whether a
real folder or a symlink) and all video extensions. A render is regenerable from `raw file + EDL`, so drafts are
disposable. If you are about to write ANY media file, resolve its
destination through `library/media_paths.py` — never invent a path.

Media lifecycle rules: `raw/` = never modify or delete. `derived/` =
regenerable, safe to delete. `work/` = ephemeral drafts, janitor prunes
after 14 days. `finals/` = approved keepers.

## Getting started (pull, install, connect the media folder)

Do this at the start of a session on any machine — every step is
idempotent, so re-running is always safe:

1. **Pull the latest brain:** `git pull`. The repo is text-only, so
   this is instant — Molly and Sidney both push here.
2. **Install dependencies (first run on a machine):**
   `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
   ffmpeg/ffprobe are system deps: `brew install ffmpeg`. Optional keys:
   `cp .env.example .env` (see capability tiers — never required).
3. **Connect the media folder to Google Drive:** `mediaRoot` in
   `media.config.json` (per-machine, gitignored) must point at the
   synced Google Drive media folder — raw footage arrives there and
   finals are delivered back there. No config yet?
   `cp media.config.example.json media.config.json`, then set
   `mediaRoot` to the Drive folder's absolute path (it should contain
   `raw/ derived/ work/ finals/`). On macOS the synced Drive folder
   lives at `~/Library/CloudStorage/GoogleDrive-{email}/My Drive/...` —
   find the user's actual path with `ls ~/Library/CloudStorage/`.
4. **Symlink `media/` in the repo root to that same Drive folder** so
   the footage is browsable in the editor (per-machine, gitignored,
   same path as `mediaRoot`):
   `ln -s "/path/to/GoogleDrive/My Drive/media" media`.
   If `media` already exists here but shows as an unreadable text/binary
   file, it's a Finder alias (made via Finder's "Make Alias") — tools
   can't follow those. Delete it and create the symlink instead
   (`rm media` removes only the alias/link, never the Drive contents).
   A correct symlink lists `raw/ derived/ work/ finals/` via `ls media/`.
5. **Verify:** `.venv/bin/python operations/doctor.py` (read-only)
   confirms the venv, the media config, and git hygiene in one shot.

**If there is no media folder** — `media.config.json` missing, or
`mediaRoot` pointing at a path that doesn't exist on this machine —
STOP and tell the user to add the Google Drive media folder: install
Google Drive for desktop, sync the shared media folder, then point
`media.config.json` at it. Never invent a local media folder as a
substitute, and don't run ingest/edit/render work until the Drive
folder is connected.

## Capability tiers (keys are optional, never required)

- **Tier 0 — no keys:** ffmpeg everything (ingest, proxies, scene maps,
  frames, EDL validation, rendering).
- **Tier 1 — no keys:** agent labels the sampled frames itself by Reading
  them (`fatbeats-content-analyze` fallback). Full pipeline still works.
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

1. `fatbeats-content-ingest` — register raw files, probe metadata, guess release type
   (draft — Molly confirms).
2. `fatbeats-content-analyze` — proxy, scene map, frames, labels; then the agent
   groups shots into **sequences** (one event, e.g. "pulls vinyl 2 out"),
   each with a hard never-cut-inside boundary. Writes `analysis.json`.
3. `fatbeats-content-edit` — 2-3 EDL variants honoring `knowledge/editing-rules.md`;
   render drafts to `work/`.
4. `fatbeats-content-review` — verify no cut lands inside a sequence, check the
   ending, inspect cut-boundary frames. Re-edit until clean.
5. `fatbeats-content-caption` — caption + product description into `caption.md`.
6. Molly approves → copy render to `finals/`, status `final`,
   `fatbeats-content-learn` captures why the winning variant won.

## Filing decision tree

- "Full run" / "do everything for this release" / "deliver the social
  pack" → `fatbeats-content-social-pack` (chains the whole pipeline + gen wing into
  ~10 post-ready videos with per-video cost in
  `releases/{slug}/social-pack.md`).
- New raw footage arrived → `fatbeats-content-ingest`, then update `releases/_board.md`.
- Molly gave feedback ("use v2, hate the ending") → `knowledge/decisions/`
  via `fatbeats-content-learn`, and fold durable rules into
  `knowledge/editing-rules.md`.
- A new editing insight or vinyl-format quirk → `knowledge/editing-rules.md`
  or `knowledge/release-types.md`.
- One-off task (not a release, not recurring) → `work/YYYY-MM-DD-{name}/`
  in git (text only).
- Same manual process done twice → promote via `fatbeats-content-skillify` into
  `plugin/skills/`.
- System friction (routing, checks, templates) → `fatbeats-content-reflect` →
  `operations/improvements.md`.
- Generative AI work on a release → the gen wing: `fatbeats-content-genmedia`
  (mechanics, always first) → `fatbeats-content-gen-video` (make the generations) →
  `fatbeats-content-gen-composite` (cut them into finished posts).
- Ran anything through fal (the `genmedia` CLI) → log it in
  `releases/{slug}/genmedia.json` (model, settings, cost) via
  `library.genmedia_ledger add-generation`, and when a composite ships,
  `add-final` so its shot/cost rollup is queryable. Never let this go
  stale — it's the only way to tell if AI generation is worth it at scale.
- Writing generation prompts or captions for an artist → skim
  `knowledge/artists/{artist}.md` first (verified product facts, recent
  arc, iconography, moderation guardrails). Pull at most 1–2 details
  and note which in the ledger. File missing? Create it via
  `fatbeats-content-artist-context` (recent, not career-wiki).

## Never-stale contract

If you touch a release, update ITS `README.md` + `release.json` status,
`releases/_board.md`, and `artifacts/dashboard.html` in the same turn.
If you add a file or module, log it in `project-overview.md`. The
`fatbeats-content-janitor` skill (weekly routine) is the safety net, not the excuse.

## Commands (run from repo root; use .venv)

```bash
.venv/bin/python -m library.ingest --all
.venv/bin/python -m library.analyze --release {slug} [--take N] [--no-tl]
.venv/bin/python -m library.edl_render releases/{slug}/edits/v1.edl.json
.venv/bin/python -m library.genmedia_ledger summary --release {slug}  # fal spend for one release
.venv/bin/python -m library.genmedia_ledger global-summary             # fal spend across everything
.venv/bin/python operations/doctor.py          # read-only health check
```

Setup on a new machine: see "Getting started" above (venv + pip install,
ffmpeg, media.config.json pointed at the Google Drive media folder, and
a `media` symlink in the repo root pointing at that same folder).

## Hard rules

- Never commit media. Verify with `git status` before any commit.
- Never modify or delete anything in `media/raw/`.
- Never let an engagement metric choose cuts (Tier 3 is a tiebreaker only).
- Renders always cut from the RAW file; proxies are for analysis only.
- Every inferred fact (release type, target length) ships as
  "draft — confirm" until Molly confirms it.
