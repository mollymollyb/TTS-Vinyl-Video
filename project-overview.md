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
- `genmedia_ledger.py` — per-release AI-generation spend ledger: one record
  per fal.ai call (model, settings, cost) + one per finished composite
  (which generations/shots it's built from). Cost lineage rollup dedupes
  shared ancestors. Tier 0, no fal integration — cost is entered by hand
  off the `genmedia` CLI's own output. CLI: `python3 -m
  library.genmedia_ledger {add-generation|add-final|summary|global-summary|validate}`.

## Workspace

- `releases/{slug}/` — release.json, analysis.json (+`analysis-takeN.json`
  for multi-take releases), `edits/vN.edl.json`, `genmedia.json`
  (AI-generation spend ledger, when the release uses fal-generated
  media), `genmedia-experiments.md`, caption.md, `social-pack.md` (the
  full-run deliverable: every video + per-video cost), README.
  `_board.md` = pipeline snapshot.
- `knowledge/editing-rules.md` — the editing law. `release-types.md` — format playbook. `decisions/` — Molly's feedback ledger.
- `knowledge/artists/wiz-khalifa.md`, `knowledge/artists/jean-dawson.md` — verified artist+product context for generation prompts/captions (recent arc, iconography, moderation guardrails). One file per artist; pull 1–2 details max per prompt.
- `plugin/` — vinyl-os plugin; skills in `plugin/skills/` (intake, ingest, analyze, edit, review, caption, doctor, janitor, learn, reflect, skillify).
- `plugin/skills/vinyl-genmedia/` — core fal.ai genmedia mechanics: seeds, uploads, async runs, cost checks, mandatory dual-ledger logging.
- `plugin/skills/vinyl-gen-video/` — full scripted AI videos (prompt = timestamped edit script), operation chooser, context threads, 30s continuation chaining.
- `plugin/skills/vinyl-gen-composite/` — ffmpeg edit bay for AI+real composites: hooks, supercuts, select cuts, two-parter stitches, caption standards.
- `plugin/skills/vinyl-artist-context/` — research + maintain `knowledge/artists/{artist}.md` (recent arc, product facts, guardrails).
- `plugin/skills/vinyl-social-pack/` — THE FULL RUN: one release from raw footage to a costed pack of ~10 post-ready videos (chains analyze → context → gens → edits → composites → captions → manifest).
- `plugin/skills/vinyl-gen-meme/` — meme formats: nano-banana meme stills, ken-burns slideshows, freeze-frame reactions, stutter repeats, chaos edits, rapid-fire text; the gen-z caption voice rules.
- `.agents/skills` → symlink to `plugin/skills` (Cursor/Codex discovery).
- `routines/` — janitor/reflect/compound-learn prompts + armed index.
- `operations/` — `doctor.py` (mechanical health check), `health.md`, `improvements.md`, `sync.md`.
- `artifacts/dashboard.html` — live release dashboard.
- `work/` — dated one-off text work (not media renders).
