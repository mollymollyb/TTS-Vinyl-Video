---
name: fatbeats-content-ingest
description: Register new raw vinyl footage as release records. Use when raw files were added to the media root, when the user says "ingest the new footage", "register these videos", or when a release folder is missing for a raw file. Probes metadata with ffprobe and writes releases/{slug}/release.json.
---

# Fatbeats-content ingest

1. Run `.venv/bin/python -m library.ingest --all` from the repo root
   (or `--file "Name.MOV"` for one file). It groups multi-take files
   ("... 1.MOV", "... 2.MOV") into one release and never moves raw bytes.
2. Read each new `releases/{slug}/release.json`. Sanity-check the
   artist/title parse and the `release_type` guess against
   `knowledge/release-types.md`. Fix obvious parse errors by editing the
   JSON (and add a filename alias in `library/ingest.py` if it will recur).
3. List every release whose `release_type_confirmed` is false in your
   report — Molly confirms types; we never silently trust the guess.
4. Same turn: update `releases/_board.md` and `artifacts/dashboard.html`.

New footage lands in the media root's `raw/` folder (flat, matching
Molly's Drive layout). If a filename fails to parse, ask rather than
guessing artist/title.
