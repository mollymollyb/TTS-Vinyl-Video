# Project overview — file map

Log every new file/module here with its purpose (house rule). Janitor
verifies this stays current.

## Root

- `CLAUDE.md` — the brain: media rules, tiers, pipeline, filing tree. `AGENTS.md` symlinks to it.
- `README.md` — human entry point + Molly's onboarding.
- `media.config.example.json` / `media.config.json` (gitignored) — per-machine media root pointer.
- `.env.example` / `.env` (gitignored) — optional API keys (Twelve Labs, tribe-viral).
- `requirements.txt` — Python deps (`twelvelabs`, `httpx`).

## library/ — single-purpose Python modules (run `python3 -m library.{mod}`)

- `env_config.py` — the one .env loader; typed optional-key accessors.
- `media_paths.py` — the ONLY media path resolver (raw/derived/work/finals).
- `ffprobe.py` — duration + metadata probing.
- `scene_detect.py` — ffmpeg scene filter → shot intervals (+ long-shot splitting).
- `proxy.py` — 720p working copies (analysis runs on these; renders never do).
- `frame_sample.py` — midpoint/cut-context JPEG extraction for labeling and review.
- `edl.py` — EDL schema, validation, `check_sequence_integrity` (the never-cut law).
- `edl_render.py` — EDL → mp4 (per-segment re-encode + concat). CLI.
- `motion_filters.py` — ffmpeg filter builders for optional per-segment
  `motion` (eased zoompan punch-in/pull-back) and `speed` (setpts/atempo).
  Taste caps shared with `edl.py` validation.
- `twelvelabs_client.py` — the ONLY Twelve Labs import; `is_available()` gates Tier 2.
- `ingest.py` — raw files → `releases/{slug}/release.json`. CLI.
- `analyze.py` — orchestrator: proxy → scenes → frames → labels → `analysis.json`. CLI.

## Workspace

- `releases/{slug}/` — release.json, analysis.json, `edits/vN.edl.json`, caption.md, README. `_board.md` = pipeline snapshot.
- `knowledge/editing-rules.md` — the editing law. `release-types.md` — format playbook. `decisions/` — Molly's feedback ledger.
- `plugin/` — vinyl-os plugin; skills in `plugin/skills/` (intake, ingest, analyze, edit, review, caption, doctor, janitor, learn, reflect, skillify).
- `.agents/skills` → symlink to `plugin/skills` (Cursor/Codex discovery).
- `routines/` — janitor/reflect/compound-learn prompts + armed index.
- `operations/` — `doctor.py` (mechanical health check), `health.md`, `improvements.md`, `sync.md`.
- `artifacts/dashboard.html` — live release dashboard.
- `work/` — dated one-off text work (not media renders).
