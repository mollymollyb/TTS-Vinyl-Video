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
