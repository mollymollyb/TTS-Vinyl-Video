# Release types — what the editor must know about vinyl formats

Every vinyl product LOOKS, FEELS, and OPERATES differently (Molly,
2026-06-29). The original skill was implicitly trained on one product
type and broke on the others. This playbook is the fix: identify the
type first, then edit to its structure.

Status: **draft — confirm each release's type with Molly** (ingest only
guesses from filenames; `release_type_confirmed: false` until she does).

## Formats

### 1xLP (single vinyl)
- Structure: sleeve front → open → pull vinyl → (variant reveal if
  colored) → back/tracklist pan.
- Edit shape: linear, one climax = the pull or the variant reveal.

### 2xLP (double)
- Two discs; often a gatefold. Both discs must appear; the pull of each
  disc is its own sequence.
- Longer raw (~2.5 min) still lands ~20s — compress dead space and
  transitions.

### 3xLP (triple — e.g. Wiz Khalifa Cabin Fever Trilogy)
- The hardest case and the one that broke the old system: showing discs
  1 → 2 → 3 is ONE narrative arc. Cutting after disc 2 reads as broken.
- Either show all three pulls (compressed each), or restructure around a
  different arc entirely — never truncate the count mid-arc.

### Gatefold
- The gatefold OPENING is the money shot and a strict sequence: closed →
  opening motion → fully open reveal. The old edits teased the open then
  snapped to the front cover — that is a hard-rule violation.

### Variant pressings (colored / splatter / etched)
- The variant is often WHY the product sells. Reveal it prominently —
  frequently as the opener (see editing-rules preferences).

### Box sets / live albums
- Extra inserts, booklets, multiple sleeves: each insert showcase is its
  own sequence; don't interleave them mid-motion.

## Target lengths (draft — confirm with Molly)

| Raw length | Format | Target cut |
|---|---|---|
| ~1.5 min | 1xLP | 12-20s |
| ~2.5 min | 2xLP / gatefold | ~20s |
| ~3 min | 3xLP / box set | 25-45s |

## Identification checklist (vinyl-ingest / vinyl-analyze)

1. Filename hints (e.g. "Trilogy" → 3xLP) — weak signal, mark draft.
2. Count distinct vinyl-pull sequences in the analysis — strong signal.
3. Gatefold-open sequence present → gatefold packaging.
4. Distinct disc colors across pulls → variant set; plan reveals.
5. Write the confirmed type back to `release.json`
   (`release_type_confirmed: true`) once Molly signs off.
