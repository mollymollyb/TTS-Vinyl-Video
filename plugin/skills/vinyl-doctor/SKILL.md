---
name: vinyl-doctor
description: Read-only health check of the whole workspace — the verification surface. Use when the user says "health check", "run the doctor", "is everything consistent", before packaging or pushing, and at the start of any janitor run. Never fixes anything; only reports.
---

# Vinyl doctor (read-only — a doctor that edits is a cage)

1. Run `.venv/bin/python operations/doctor.py` from the repo root. It
   mechanically checks: media config resolves; venv + ffmpeg present; no
   media files tracked by git; every release folder has release.json;
   statuses match artifacts on disk (analyzed → analysis.json with
   sequences; editing/review → at least one EDL; final → a file in the
   media finals folder); board/dashboard mention every release; routines
   index lists cadence + armed status.
2. Add judgment checks the script can't make: does `knowledge/` content
   contradict itself; are there stale "draft — confirm" items Molly
   answered long ago; any skill unreachable (description would never
   trigger); anything in `work/` (git) that should have been skillified.
3. Write the combined report to `operations/health.md`: score /100, one
   line per finding with severity (high/med/low) and the file it points
   at. Overwrite the previous report; git history keeps the old ones.
4. Report the score and the top findings. FIX NOTHING — remediation is
   `vinyl-janitor`'s job.
