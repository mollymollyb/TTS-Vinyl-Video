---
name: vinyl-intake
description: Orchestrate the whole vinyl video pipeline end to end. Use when new raw footage arrives, when the user says "make videos for this release", "run the pipeline", "process the new footage", or names a release without a more specific ask. Chains ingest, analyze, edit, review, and caption, and keeps the boards current.
---

# Vinyl intake — the auto-manage loop

Run the pipeline for one release (or every release whose status is behind),
stopping only where a human decision is required.

1. **Ingest.** If the release has no `releases/{slug}/release.json`, run
   `.venv/bin/python -m library.ingest --all`. Confirm the release type
   guess against `knowledge/release-types.md`; leave
   `release_type_confirmed: false` for Molly.
2. **Analyze.** Follow `vinyl-analyze` (machine pass + your sequence pass).
3. **Edit.** Follow `vinyl-edit` to produce and render 2-3 variants.
4. **Review.** Follow `vinyl-review` on every variant; re-edit until each
   passes or is discarded.
5. **Caption.** Follow `vinyl-caption` once at least one variant passes.
6. **Update state in the same turn:** `release.json` status, the release
   `README.md`, `releases/_board.md`, `artifacts/dashboard.html`.
7. **Report** per release: variants rendered (paths under the media
   `work/` folder), review outcomes, caption draft, and exactly what needs
   Molly's eyes (type confirmation, variant pick).

Never present a variant that failed review. Never touch `media/raw/`.
