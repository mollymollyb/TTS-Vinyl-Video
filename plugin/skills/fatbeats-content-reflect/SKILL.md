---
name: fatbeats-content-reflect
description: Improve the system itself — skills, checks, templates, routing — based on observed friction. Use after repeated friction, when the user says "make the system better", "why does this keep happening", or on the monthly routine. Changes the machinery, not the content.
---

# Fatbeats-content reflect — the 50/50 budget

Spend roughly half the improvement effort on the machinery, not just the
work. Only act on OBSERVED repetition (real sessions, real friction) —
never generic best-practice noise.

1. Gather evidence: `operations/health.md` history (git log),
   `knowledge/decisions/` for repeated feedback themes, recent session
   friction the user names.
2. Pick the highest-leverage fix, usually one of: a skill's instructions
   were ambiguous (edit the SKILL.md); a mechanical check is missing
   (add it to `operations/doctor.py`); a library function keeps being
   hand-patched (fix the module); the editing rules have a gap (send to
   `fatbeats-content-learn` instead — that's content, not machinery).
3. Make the change, and log one dated entry in
   `operations/improvements.md`: friction observed → change made → how
   we'll know it worked.
4. If a skill changed, sanity-check its description still routes
   correctly against the others (no overlaps, no dead skills).
