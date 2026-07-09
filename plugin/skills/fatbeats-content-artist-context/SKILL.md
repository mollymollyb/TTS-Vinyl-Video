---
name: fatbeats-content-artist-context
description: Research and maintain knowledge/artists/{artist}.md - verified recent-arc facts, product details, iconography, and moderation guardrails that feed generation prompts and captions. Use when the user says "research the artist", "get context on", "what's their recent stuff", or when fatbeats-content-gen-video or fatbeats-content-caption needs a context thread and no file exists.
---

# Fatbeats-content artist-context

One file per artist at `knowledge/artists/{artist-slug}.md`. It exists
to make prompts and captions SHARPER, not longer — consumers pull at
most 1-2 threads per prompt and cite which in the ledger.

## Research rules

- **Recent, not career-wiki.** The user's words. Target the last
  12-18 months: releases, tours, collabs, memes, what fans are
  actually talking about. Wikipedia-tier biography is noise.
- Web-search with the current year in queries. Verify anything that
  will appear on screen (track titles, credits, pressing details)
  against two sources or the release's own footage/metadata.
- The PRODUCT is primary: pressing variant, track count, real track
  titles, features, producers, label, what's footage-confirmed about
  each sleeve. This section powers text overlays, so it must be exact.
- Never fake numbers (chart stats, sales, streams).

## File template (sections in order)

1. **Purpose header** — "use sparingly, 1-2 details per prompt,
   product stays the hero" + `Refreshed: {date}` line.
2. **The big thread** — the ONE currently-active story that connects
   artist moment to this product (e.g. Cabin Fever: 2026 blog era boyz
   has the same producers as the 2011 tape → "you used to download
   this, now it's on wax").
3. **This product** — verified pressing/track/feature facts.
4. **Evergreen iconography** — visual prompt fuel that reads instantly
   as the artist (colors, motifs, city, crew name).
5. **Recent arc (dated — decays fast)** — bulleted, each line dated.
6. **Guardrails (learned the hard way)** — likeness rules (never
   render the artist), substance/brand-safety lines, audio-moderation
   triggers specific to this artist's world.
7. **How to use** — the 1-2-threads rule restated for the consumer.

## Maintenance

- Re-verify "Recent arc" items older than ~2 months before using them
  in a prompt; update `Refreshed:` whenever touched.
- When a generation wins BECAUSE of a context thread, note that in the
  artist file too — proven threads outrank speculative ones.
- New artist on the board → create the file during release intake, not
  mid-generation. Log the new file in `project-overview.md`.
