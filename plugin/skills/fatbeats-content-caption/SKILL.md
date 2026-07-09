---
name: fatbeats-content-caption
description: Write the TikTok Shop caption and product description for a release. Use when a variant passes review, or when the user says "write the caption", "product description for this vinyl". Grounded in release.json and analysis.json — never invented product facts.
---

# Fatbeats-content caption

Write `releases/{slug}/caption.md` with two sections.

## Caption (TikTok Shop post)

- Ground every claim in `release.json` + `analysis.json` (artist, title,
  format, variant color if a variant-reveal sequence exists). NEVER invent
  pressing details, colors, or edition sizes.
- Voice: Molly's — direct, collector-to-collector, zero corporate filler.
  Check `knowledge/decisions/` for caption feedback before writing.
- Shape: hook line ≤ 8 words, one or two lines of body naming format +
  variant, no more than 3 relevant hashtags. No emoji unless
  `knowledge/decisions/` says Molly wants them.

## Product description (listing)

- Factual block: artist, title, format (e.g. 3xLP), packaging (gatefold,
  box), variant/color, condition (new), label if known.
- One collector-angle sentence (why this pressing matters), grounded in
  what the footage actually shows.
- Mark anything unverified as "confirm before posting: ..." rather than
  omitting silently.

## Close out

Update the release README + board in the same turn. The caption ships as
a DRAFT — Molly approves before posting; this skill never posts anything.
