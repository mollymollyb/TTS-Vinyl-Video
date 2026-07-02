---
name: vinyl-janitor
description: Reconcile and de-stale the workspace, then prune ephemeral media. Use on the weekly routine, when the user says "clean up", "run the janitor", "prune old drafts", or after a burst of work left boards stale. Runs the doctor first and fixes only what is safe.
---

# Vinyl janitor (doctor first, then fix what's safe)

1. Run `vinyl-doctor`. Its punch list is your work order.
2. Fix the SAFE items: regenerate `releases/_board.md` and
   `artifacts/dashboard.html` from the release.json files; sync release
   READMEs with their release.json; fill missing folder README stubs;
   update `project-overview.md` for files that exist but aren't logged.
3. Prune media (the only deletion you're allowed):
   - `work/{slug}/{date}/` folders older than 14 days — delete, UNLESS the
     release status is `review` (Molly may still be choosing).
   - `derived/{slug}/` for releases at status `final` — delete proxies and
     frames (regenerable); keep `analysis.json` (it's in git).
   - NEVER touch `raw/` or `finals/`. Never delete git-tracked files.
4. Anything unsafe (contradictory statuses, a release.json that disagrees
   with reality, missing raw files) — DON'T guess. List it in the report
   for a human.
5. Re-run `operations/doctor.py`; report score before → after and what
   was pruned (file counts + MB freed).
