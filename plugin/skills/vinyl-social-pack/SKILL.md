---
name: vinyl-social-pack
description: The full run - take one release from raw footage to a costed pack of ~10 ready-to-post social videos. Use when the user says "full run", "do everything for this release", "deliver the social pack", or "10 videos for {release}". Chains vinyl-analyze, vinyl-artist-context, vinyl-edit, vinyl-review, vinyl-gen-video, vinyl-gen-composite, vinyl-caption, and ships releases/{slug}/social-pack.md with a dollar figure on every video.
---

# Vinyl social-pack — the full run

One command's worth of intent: footage in, ~10 post-ready videos out,
every video traced to what it cost. This skill sequences the other
skills and owns the deliverable contract; it invents no new mechanics.

## 0. Scope + budget gate (before anything renders)

- Confirm the release has raw footage ingested (`release.json`).
- Default pack: **10+ videos and every one FULL** — a deliverable is
  ≥13s with hook → hold → payoff (learned 2026-07-05: a pack padded
  with 2s hooks and short cuts reads "mid"). Hooks are ingredients,
  not deliverables. Default mix: 3 real edits, 3-4 scripted
  generations (≥1 two-parter chain, ≥1 comedy), 2-3 meme formats
  (vinyl-gen-meme: chaos edit / slideshow / freeze reaction /
  rapid-fire), 1-2 supercuts. Rebalance to the footage and say so in
  the manifest.
- Estimate fal spend for the gen slate BEFORE submitting (via
  `genmedia pricing`); over ~$10, pause and confirm with the user.
  Real edits and composites are $0 marginal (ffmpeg).

## 1. Watch (vinyl-analyze)

Machine pass per take, then YOUR sequence pass (dense-probe the
showcases; organizing hands are dead space). Multi-take releases:
analyze every take — sequences from any take are fair game for edits
and seeds.

## 2. Research (vinyl-artist-context)

Create or refresh `knowledge/artists/{artist}.md` BEFORE writing
prompts or captions. Product facts also sanity-check the release-type
guess from ingest.

## 3. Submit the gen slate early (vinyl-gen-video)

Generations render for 8-15 min — submit the whole slate async FIRST,
then do the real edits while fal works. Slate shape: 2-3 scripted 15s
4K videos (≥1 pulling a context thread, ≥1 pure product-first) + 2-3
fast 720p i2v hooks from money-still seeds. Log every submission in
both ledgers immediately (vinyl-genmedia rules).

## 4. Real edits (vinyl-edit + vinyl-review)

2-3 EDL variants honoring the sequence map, rendered from RAW,
self-reviewed until they pass (integrity → visual boundaries → energy
pass). A variant that fails 3 re-edit rounds is discarded, not shipped.

## 5. Composites (vinyl-gen-composite)

When generations land: verify each (preview stills, honest read), then
cut the composite layer — hook+real openers, the supercut, select cuts
of the strongest generations. Captions per the composite skill's
standards; never caption over generated end cards.

## 5b. Viral pass (vinyl-scrollstop + vinyl-sound-design)

After the core pack exists, run the feed-mechanics layer — it is
nearly all $0:
- 2-3 scrollstop formats (UI parody / genre theft / black-slam /
  4th-wall — pick interrupts the pack doesn't already use).
- 1 perfect loop (palindrome $0, or gen loop via
  image_url == end_image_url at 1080p/10s).
- 1 ASMR cut (real macro beats + mmaudio foley).
- 1 comment magnet (a real open question — variant mystery, hot
  take, "wrong answers only").
- An A/B pair: one existing asset re-hooked with a different first
  second.
- Ship `sound-map.md` (music alignment per video) and
  `molly-hooks.md` (5-6 selfie cold-open scripts) with the pack.

## 6. Captions + the manifest (the deliverable)

- `vinyl-caption` writes the release's caption.md (post copy is per
  release, not per video).
- Write `releases/{slug}/social-pack.md`: one row per video — id,
  file (media-plane path), duration, what it is (one line), suggested
  caption line, and **cost_usd** (from `genmedia_ledger` final/gen
  rollups; $0.00 for pure-real cuts; "unknown" only when a lineage
  cost is unknown — never guess). Include the pack total and the
  `summary --release {slug}` output.
- Every video in the manifest must actually exist on the media plane
  at the stated path, verified with ffprobe (duration matches).

## 7. Ship

Ledger `validate`, release README + `_board.md` + dashboard updated,
`project-overview.md` if files were added, commit + push (media stays
out of git). Report to the user: pack table, total spend, and the
open human decisions (type confirmation, winner picks, post order).

## Walls → skills

If any step has no skill and you improvise more than twice, stop and
write the skill (vinyl-skillify rules), then continue THROUGH it.
