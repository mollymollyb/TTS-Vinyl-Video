# TTS-Vinyl-Video — agent video editor for vinyl TikTok Shop content

Raw vinyl showcase footage goes in; short, coherent, platform-ready cuts
and captions come out. The agent does the editing; humans make the
calls. Built for Molly B (Rostrum) with Sidney Swift.

**Agents: read `CLAUDE.md` first.** It's the brain — the media rules,
the pipeline, and the filing tree live there.

## How it works (60 seconds)

- **Git holds the brain** — skills, code, and per-release records
  (`release.json`, `analysis.json`, edit recipes, captions). Everything
  here is small text; pushing/pulling is instant.
- **The media root holds the bytes** — raw footage, proxies, draft
  renders, finals. It lives OUTSIDE git at the path in your
  `media.config.json`. Renders are regenerable from raw + recipe, so
  drafts are disposable.
- **The pipeline**: `vinyl-ingest` → `vinyl-analyze` (shot + sequence
  map) → `vinyl-edit` (2-3 variants) → `vinyl-review` (the system checks
  its own cuts) → `vinyl-caption`. The orchestrator `vinyl-intake` runs
  the whole chain. The one unbreakable editing law: **never cut inside a
  sequence** — a vinyl pull, a gatefold open, a tracklist pan always
  completes on screen.

## Setup (Molly: this is your onboarding)

```bash
git clone https://github.com/mollymollyb/TTS-Vinyl-Video.git
cd TTS-Vinyl-Video

# 1. Python environment (one time)
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# 2. Point the system at YOUR media folder (one time)
cp media.config.example.json media.config.json
#    then edit mediaRoot to your absolute path — e.g. your synced
#    Google Drive "Raw Vinyl Footage" parent, or a local folder.
#    Create raw/ derived/ work/ finals/ inside it and put the .MOV
#    files in raw/.

# 3. Optional keys (skip freely — everything still works)
cp .env.example .env   # add TWELVE_LABS_API_KEY if/when you have one
```

Then open this folder in Claude/Cursor and say things like:

- "Ingest the new footage" · "Analyze the Mac Miller KIDS release"
- "Make videos for Jean Dawson" (full pipeline)
- "Run the doctor" · "Run the janitor"

ffmpeg is required: `brew install ffmpeg`.

## Repo map

| Path | What |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | the brain (agents read first) |
| `releases/{slug}/` | one folder per vinyl product — records, recipes, captions |
| `knowledge/` | editing rules, release-type playbook, Molly's decisions |
| `library/` | the Python toolkit (ffmpeg, scene maps, EDLs, Twelve Labs) |
| `plugin/skills/` | the 11 agent skills (`.agents/skills` symlinks here) |
| `routines/` | prompts for scheduled runs (janitor, reflect, learn) |
| `operations/` | doctor script, health report, improvements ledger, sync map |
| `artifacts/dashboard.html` | live release dashboard |
| `project-overview.md` | file-by-file map, kept current as things are added |

Full provenance: editing/analysis machinery adapted from Sidney's
`auto-edit` lab spike (see `operations/improvements.md`).
