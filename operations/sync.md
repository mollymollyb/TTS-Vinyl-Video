# Sync map — what owns what

| Store | Owns | Notes |
|---|---|---|
| **This repo (git)** | code, skills, release RECORDS (release.json, analysis.json, EDLs, captions), knowledge, boards | GitHub `mollymollyb/TTS-Vinyl-Video`; both Sidney and Molly push/pull |
| **Media root** (per-machine path in `media.config.json`) | all video BYTES: `raw/`, `derived/`, `work/`, `finals/` | never in git |
| **Google Drive "Raw Vinyl Footage"** (Molly's, shared with Sidney) | the canonical source of raw footage | flat folder of .MOV files |
| **TikTok Shop** | published posts, captions as posted | system drafts; Molly posts |

## Raw footage flow

Molly shoots → uploads to the Drive folder → each machine gets the files
into its own `{mediaRoot}/raw/` (Drive desktop sync or manual download)
→ `vinyl-ingest` registers them. Filenames are the join key between
Drive, `raw/`, and `release.json` — don't rename raw files after ingest.

## Open item

Decide whether each machine's media root should BE the synced Drive
folder (Drive desktop) or a local copy (current setup on Sidney's
machine: local copy at `TTS-Vinyl-Video/media/`, gitignored). Either
works — `media.config.json` is the only thing that changes.
