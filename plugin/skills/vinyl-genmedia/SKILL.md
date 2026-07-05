---
name: vinyl-genmedia
description: Core mechanics for AI media generation with the fal.ai genmedia CLI - seeds, uploads, async runs, polling, cost checks, and mandatory ledger logging. Use when the user says "generate AI video", "run genmedia", "make gen content for this release", or before any other vinyl-gen-* skill runs. Every fal call gets logged or it didn't happen.
---

# Vinyl genmedia (core mechanics)

The foundation under `vinyl-gen-video` and `vinyl-gen-composite`. Those
skills decide WHAT to make; this one is HOW to run it without losing
money, work, or reproducibility.

## 0. Preflight (every session)

- `genmedia` on PATH? If not: install per
  github.com/fal-ai-community/genmedia-cli#setup — the installer's PATH
  check can fail on a malformed shell PATH even when the binary landed;
  check `~/.local/bin/genmedia` before reinstalling.
- `FAL_API_KEY` comes from `.env` (`set -a && source .env && set +a`).
- Price the model BEFORE running: `genmedia pricing {model}` — 4K/15s
  video is ~10x the 720p/5s workhorse. Confirm spend with the user if a
  batch will exceed ~$10.

## 1. Seed assets (give the model our product, not its imagination)

Extract stills/clips from the release's RAW footage at money moments
(cover, back cover, each sleeve, variant reveal peak, closer):

```bash
ffmpeg -ss {t} -i {raw} -frames:v 1 -q:v 2 media/derived/{slug}/gen-seeds/seed_{name}.jpg
# reference clips for reference-to-video: <=720p, 2-15s, no audio
ffmpeg -ss {a} -to {b} -i {raw} -vf scale=-2:1104 -c:v libx264 -crf 23 -an .../refclip_{name}.mp4
```

Rules: pre-crop seeds to 9:16 if the output must be vertical (landscape
seeds → landscape videos). Upload with `genmedia upload {file} --json`
and read the **`cdn_url`** key (not `url`); append every URL to
`media/derived/{slug}/gen-seeds/urls.txt` so reruns don't re-upload.

## 2. Running models

- Array params are JSON literals: `--image_urls '["url1","url2"]'` —
  a bare string 422s.
- Anything ≥30s of render time (all video models): `--async --json`,
  capture `request_id`, submit the WHOLE batch, then poll:
  `genmedia status {endpoint} {request_id} --download -o {out}`.
  4K/15s seedance runs take 8-15 min; never block on one.
- Unsure about a model's inputs? `genmedia schema {model}` first.

## 3. Verify before claiming done

Download, then extract 3-4 preview stills per output
(`ffmpeg -ss {t} -i out.mp4 -frames:v 1 preview/{id}_t{t}.jpg`) and
actually Read them. Judge: product on-model? text legible? beats
followed? Log the honest read — "sleeves drifted off-model" is more
useful than "done".

## 4. Ledger (non-negotiable, same turn as the run)

Two twins, both updated every time:

- `releases/{slug}/genmedia-experiments.md` — human narrative: batch
  tables (ID, model, prompt gist, my read, Verdict column left empty
  for the user), technique notes.
- `releases/{slug}/genmedia.json` — machine twin via
  `.venv/bin/python -m library.genmedia_ledger add-generation --release {slug} --json '{...}'`
  (and `add-final` when a composite ships). Itemize `cost_usd` per
  record from the CLI's own cost output; `validate` before committing.

Outputs land in the media plane at `media/work/{slug}/genmedia/` —
NEVER in git. IDs are `{batch-letter}{n}` (A1, V3) and match across
both ledgers, prompts, and filenames.

## Known failure modes

- `content_policy_violation` AFTER full inference (still billed): the
  generated AUDIO tripped it. Resubmit with `--generate_audio false`,
  then add foley via `fal-ai/mmaudio-v2` (negative_prompt: "speech,
  vocals, singing"). Details + artist-specific triggers:
  `knowledge/artists/{artist}.md` guardrails section.
- Model drift on product artwork grows with distance from the seed —
  keep the product anchored to reference images (see vinyl-gen-video).
