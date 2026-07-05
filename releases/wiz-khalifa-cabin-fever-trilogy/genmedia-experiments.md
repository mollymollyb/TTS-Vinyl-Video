# Genmedia experiments — Wiz Khalifa Cabin Fever Trilogy

Goal: gen-z scroll-stopping hooks and treatments for the vinyl release,
generated with `genmedia` (fal.ai CLI). Sidney reviews; winners become
skills. Every experiment below is fully reproducible: model + exact
inputs + prompt live here, outputs land in the media plane at
`work/wiz-khalifa-cabin-fever-trilogy/genmedia/` (never in git).

**Spend tracking:** this file is the human-readable narrative (prompt
gists, reactions). The machine-readable twin — model, settings, cost,
and which generations combine into each finished composite — lives in
`genmedia.json` next to this file. Query it with
`.venv/bin/python -m library.genmedia_ledger summary --release
wiz-khalifa-cabin-fever-trilogy`. This batch's per-item costs weren't
itemized (only the ~$8 aggregate below), so `cost_usd` is `null` for
every 2026-07-03 record — itemize cost going forward.

## Seed assets (extracted from the raw MOV, uploaded to fal CDN)

| Seed | Source time | What it is |
|---|---|---|
| seed_cover | 3.0s | black Trilogy box cover, both hands |
| seed_backcover | 15.0s | tracklist back panel |
| seed_fan1 | 36.5s | three sleeves fanned, CF1 front |
| seed_cf2_white | 44.5s | CF2 white sleeve centered |
| seed_claw | 47.5s | CF3 claw artwork, two hands |
| seed_red_peak | 59.8s | red vinyl held at peak reveal |
| seed_red_fan | 67.0s | red vinyl large + sleeve fan |
| seed_closer | 80.3s | final comp: CF2 white + red slide-out |
| refclip_pull | 53.2–60.6s | 720p clip: the red vinyl pull |
| refclip_fan | 34.0–40.8s | 720p clip: fan arrange + hold |
| refclip_closer | 75.6–80.6s | 720p clip: slide-out closer |

CDN URLs: `media/derived/wiz-khalifa-cabin-fever-trilogy/gen-seeds/urls.txt`
(machine-local; re-upload with `genmedia upload` if expired).

## Experiment ledger — 2026-07-03 (24 artifacts, ~$8 est. spend)

All outputs: `media/work/wiz-khalifa-cabin-fever-trilogy/genmedia/`
(`preview/` holds stills for quick triage). Verdict column is Sidney's —
fill in cool / meh / kill; winners become skills.

### Batch A — animate the money stills (image-to-video)

| ID | Model | Seed | Prompt gist | My read | Verdict |
|---|---|---|---|---|---|
| A1 | seedance-2.0/fast/i2v | red_peak | red disc starts spinning in hand, dolly-in, lens flare | clean, subtle, usable as-is | |
| A2 | kling-v2.5-turbo/pro/i2v | red_peak | push-in, disc spins, red light glow on sleeve | close to A1; kling slightly smoother hand | |
| A3 | seedance-2.0/fast/i2v | claw | claw marks ignite from within, embers drift, menacing zoom | ember glow looks REAL against real street | |
| A4 | seedance-2.0/fast/i2v | cover | red title text pulses like neon, smoke curls, dusk mood | full relight to dusk — moodiest asset of the day | |
| A5 | hailuo-02/standard/i2v | fan1 | three sleeves levitate + fan apart mid-air like card trick | sleeves drift off-model (lose artwork) — weakest | |
| A6 | seedance-2.0/fast/i2v | closer | red vinyl slides out, floats up, spins to fill frame | ends INSIDE the red disc w/ sun flare — ending asset | |
| A7 | veo3.1/fast/i2v (8s, audio) | red_fan | orbital camera around red disc + fan, bass hum + crackle | premium trailer energy, native audio decent | |

### Batch B — restyle the cover (nano-banana-2/edit, stills)

| ID | Prompt gist | My read | Verdict |
|---|---|---|---|
| B1 | 1998 VHS camcorder freeze-frame, REC + timestamp | flawless VHS, funny contrast w/ pristine product | |
| B2 | Y2K sticker-bomb zine collage around the 3 sleeves | loud thumbnail/carousel energy; some text gibberish (SRLING) | |
| B3 | red vinyl on turntable in smoky neon bodega | scene transplant is perfect, label readable | |
| B4 | cover on Times Square billboard, rain, crowds | epic scale flex (16:9) | |
| B5 | claw marks ripping open FOR REAL, red vinyl glowing inside | best single image of the day | |

### Batch C — pure text-to-video b-roll (no source needed)

| ID | Model | Prompt gist | My read | Verdict |
|---|---|---|---|---|
| C1 | seedance-2.0/fast/t2v | macro needle-drop on red vinyl, smoke, dust, audio | gorgeous cinematic b-roll, loopable | |
| C2 | seedance-2.0/fast/t2v | claymation: 3 sleeves with legs strut down a stoop | unhinged in the right way — most gen-z thing here | |
| C3 | veo3.1/fast (8s) | flythrough INSIDE the grooves, red canyon walls | surreal epic; abstract (no product ID until end) | |

### Batch D — reference-to-video (seedance-2.0)

| ID | Refs | Prompt gist | My read | Verdict |
|---|---|---|---|---|
| D1 | refclip_pull (@Video1) | recreate the pull as 90s anime cel | style IGNORED — but it faithfully re-staged the real shot (interesting for reshoots, not restyle) | |
| D2 | red_peak + claw (@Image1/2) | red disc spins in void, claw etched in embers behind | moody album-trailer beat, on-brand | |

### Batch E — first+last frame morph (seedance i2v + end_image_url)

| ID | Frames | Prompt gist | My read | Verdict |
|---|---|---|---|---|
| E1 | cover → red_peak | box dissolves into red smoke that condenses into the disc | red smoke vortex mid-morph; slightly literal but works as transition | |

### Batch F — the two-step pipeline (nano-banana still → seedance animates it)

| ID | Source | Prompt gist | My read | Verdict |
|---|---|---|---|---|
| F1 | B3 bodega | turntable spins, tonearm drops, smoke drifts, dolly-in | pipeline WORKS — styled still becomes living scene | |
| F2 | B5 torn cover | rips pulse red, embers flake, disc rotates inside | strongest hook of the day, period | |
| F3 | B4 billboard | rain, flicker, taxis, aerial push | great, but came out 16:9 (billboard seed is landscape) | |

### Batch X — finished composites (ffmpeg: AI hook + real edit + Impact captions)

| ID | Recipe | My read | Verdict |
|---|---|---|---|
| X1 | F2 torn-cover hook (2.6s, "the pressing on this goes CRAZY") → real v3 | 18.8s, ready to post | |
| X2 | F1 bodega hook (3s, "POV your bodega got the wiz trilogy on wax") → real v2 | 24.2s, POV-format native | |
| X3 | real cover ("wait for it") → E1 smoke morph → real red showcase → real closer | 16.2s, AI as invisible transition | |

## Round 2 — 2026-07-05: FULL videos, not shots

Sidney's note: "you're not really making full videos, just shots… be a
gen-z editor, go crazy, use seedance 2.0 4K 15 sec." Response: two new
formats — (1) beat-scripted 15s one-shot generations where the prompt is
a full timestamped edit script, (2) a 15-cut ffmpeg supercut mixing AI
+ real footage with a caption on every beat.

### Batch V — seedance-2.0 full 4K 15s videos (prompt = shot-by-shot script)

| ID | Model | Concept | My read | Verdict |
|---|---|---|---|---|
| V1 | ref-to-video (cover+claw+red_peak) | "red takeover": product opens, disc spins B&W-world, street floods red, sleeves rain from sky, turntable + OUT NOW end card | followed the ENTIRE script incl. text end card — best single generation so far | |
| V2 | text-to-video | claymation heist: sleeves steal the red disc from a record store, cat chase, milk-crate escape, GOT THE TRILOGY card | Aardman-quality, complete story w/ end card | |
| V3 | ref-to-video (refclip_pull video ref) | reality breaks: faithful re-stage of the real pull → datamosh → zero-g → ride INTO the groove → snap back | video ref anchors it to our real shot then goes surreal | |
| V4 | text-to-video | 90s VHS infomercial parody: BUT WAIT card, watermelon slice, astronaut DJ, NOT $19.99 PRICELESS, thumbs-up freeze | meme-dense, every beat rendered | |
| V5 | ref-to-video, generate_audio FALSE | listening-party ritual → party flip, graffiti end cards THE TRILOGY ON WAX / HITS DIFFERENT | v1+v2 attempts REJECTED (audio moderation); silent render passed, then mmaudio-v2 added the beat → `V5_mmaudio.mp4` | |

### Batch X round 2 — supercut composite

| ID | Recipe | My read | Verdict |
|---|---|---|---|
| X4 | 15 beats × ~1.1s: alternating AI shot / real footage, caption per beat, punch-in jump cuts, one 0.85x slow-mo | 17.3s "gen-z editor" cut — rhythm carried by cuts not content; captions carry a running joke | |

## Round 3 — 2026-07-05: context-loaded generations

Sidney's verdicts so far: **V1 and V3 are the favorites.** His idea:
research the artist's RECENT arc + the actual product and keep it in a
folder the agent can sometimes pull from. Built
`knowledge/artists/wiz-khalifa.md` (product facts, recent arc,
iconography, moderation guardrails) and generated two videos that each
pull exactly one context thread:

| ID | Model | Context thread used | Concept | My read | Verdict |
|---|---|---|---|---|---|
| V6 | seedance-2.0 ref2v, 4K 15s | blog-era nostalgia (2026 "blog era boyz" w/ mgk = same Sledgren/ID Labs producers as Cabin Fever; mixtape-download era) | time machine: street 2026 → VHS rewind → 2011 dorm, download bar hits 100% → pixels shatter into the red vinyl → back to 2026, end cards YOU USED TO DOWNLOAD THIS / NOW ITS ON WAX / FIRST TIME EVER ON VINYL | concept exists only because of research; end cards flawless; flashback sleeves drifted off-model | |
| V7 | seedance-2.0 ref2v, 4K 15s | real tracklist + box facts (34 tracks; Taylor Gang / M.I.A. / GangBang / No Worries; red-foil treatment) | kinetic typography: track titles peel off the real back cover as red-foil 3D letters, tornado around the spinning disc, slam back down; end cards 34 TRACKS / ONE BOX / ALL RED WAX | peel/tornado spectacular; short cards clean, long floating titles typo (BIIG) | |

## Round 4 — 2026-07-05: chain + cut the favorites (V1, V3)

Sidney: "do it" on the two proposals — continuation chaining for
longer arcs, and X4-style trim/caption passes so 15s generations
become finished posts.

### Batch V-chain — continuation chaining

| ID | Model | Technique | Concept | My read | Verdict |
|---|---|---|---|---|---|
| V1B | seedance-2.0 ref2v, 4K 15s | V1's LAST frame extracted (`-sseof -0.15`) → uploaded → sole @Image1 ref; prompt opens "This is PART 2 of a video that ended on this exact frame" | end card burns to embers → dive INTO the groove canyon → POV flight → red glass shatter → slow-mo reassembly at golden hour → 3 CLASSICS / ONE BOX / LINK IN BIO | seam lands — the burn reads as a beat, not a stall; end cards clean. Two blemishes: the "12.2" timestamp cue leaked as tiny literal text, and fanned sleeves drift off-model (the chain's only ref is the last frame — product refs don't survive into part 2) | |

### Batch X round 4 — select cuts + the two-parter

| ID | Recipe | My read | Verdict |
|---|---|---|---|
| X5 | V1 (trimmed: dropped the 5.2–7.6s empty-street wander) + V1B (trimmed at the burn seam) = 24.5s two-part arc; captions only on beats without generated text ("the red took OVER", "POV. you fell in.") | the 30s-arc format works — part 1 hook + payoff, part 2 escalation + CTA | |
| X6 | V3 15s → 11.9s select cut: dropped the slow pull intro + mid-wander, captioned every beat (dont stare at the wax too long / told you. / gravity just LEFT / OH NO / INSIDE THE GROOVE RN), kept the generated IT GOES THAT DEEP end card | tighter than V3 raw; the stare-warning caption reframes the whole video as a dare | |

### Round 4 technique notes

15. **Continuation chaining works** (V1→V1B): extract the final frame
    (`ffmpeg -sseof -0.15 -i part1.mp4 -frames:v 1`), upload, make it
    @Image1, open the prompt "This is PART 2 of a video that ended on
    this exact frame, so start exactly there and continue", and script
    part 2 to immediately TRANSFORM the inherited frame (burn/dive) so
    the seam is a beat. Stitch + trim to 22–28s, not the raw 30.
16. **Chain limitation**: part 2's only product ref is the inherited
    frame — anything else it shows (sleeves) drifts off-model. Either
    keep part 2 abstract (canyon/shatter) or re-attach product seeds
    as extra refs.
17. **Never write timestamps as bare numbers in text-adjacent beats**
    ("at 12.2s 'CARD'" leaked "12.2" on screen next to the card).
    Phrase end-card timing as "in three quick beats" instead.
18. **Select-cut discipline**: a 15s generation keeps its best 10–12s.
    Probe frames every ~1.5s, drop the slowest stretch (usually the
    intro or a mid-video wander), never caption over generated cards.

### Round 3 technique notes

12. **Context threads work at two levels**: concept (V6's whole
    premise = the blog-era research find) and copy (real track titles,
    "first time ever on vinyl" as end cards). Product VISUALS still
    need reference images — V6's flashback scenes (far from any ref)
    invented a gold sleeve. Keep the product on-screen anchored to
    refs; let context drive the story and the text.
13. **AI-rendered text limit**: ≤3-word end cards render clean at 4K;
    longer floating text (track titles) gets typos. Long copy →
    ffmpeg drawtext overlays instead.
14. Context files live at `knowledge/artists/{artist}.md` — CLAUDE.md
    routes any prompt/caption work through them ("1–2 details max,
    note which in the ledger"). Same pattern scales to the Mac
    Miller / Jeezy / Jean Dawson releases on the board.

### Round 2 technique notes

8. **The 15s prompt-script format works**: write the prompt as literal
   timestamped beats ("0-2s: … 2-5s: …") with camera moves, sound cues,
   and on-screen text — seedance-2.0 (non-fast) executes it nearly
   beat-for-beat, including legible end-card text at 4K.
9. **Audio moderation gotcha**: seedance's generated audio can trip
   `content_policy_violation` AFTER a full 7-min inference (still
   billed). Anything implying chant/ritual/vocals is risky. Fix:
   `--generate_audio false` then `fal-ai/mmaudio-v2` ($0.001/s) for
   instrumental foley — negative_prompt "speech, vocals, singing".
10. **4K 15s seedance runs take 8–15 min** — always `--async`, always
    batch-submit before polling.
11. **Supercut recipe**: normalize every beat to 1080x1920@30 (zoom
    factor per beat = punch-in jump cut), caption each beat, concat.
    Cutting real+AI every ~1.1s hides AI imperfections and reads as
    intentional style.

### Technique notes (for future skills)

1. **Two-step pipeline (B→F) is the unlock**: nano-banana-2/edit restyles
   a real frame (product stays identical), then seedance i2v animates the
   styled still. Full art direction control vs one-shot i2v.
2. **seedance-2.0/fast/i2v at 720p** is the workhorse: ~fast, cheap,
   native audio, obeys "keep hands still" style constraints well.
3. **Array params need JSON literals** in genmedia CLI:
   `--image_urls '["url"]'` — plain strings 422.
4. **reference-to-video ignores style asks** (D1) but nails product
   consistency from multi-image refs (D2). Use it for "same product, new
   scene", not restyles.
5. **Landscape seeds produce landscape videos** (F3) — pre-crop seeds to
   9:16 before animating if the post needs vertical.
6. **Composites**: normalize every piece to 1080x1920@30 + aac 48k
   stereo before concat, then `-c copy` — mixed gen resolutions concat
   clean. Captions: Impact, borderw=7, y=h*0.14.
7. Async submit + poll loop (`--async` → `status --download`) runs the
   whole batch in parallel; 16 videos landed in ~12 min wall time.
