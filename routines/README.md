# Routines — runnable prompts for scheduled/remote runs

One markdown file per recurring workflow; the doctor reads this index
for its schedule-armed check. To arm a routine, wire a scheduler (Claude
scheduled tasks / cron / GitHub Actions) to run the prompt in its file,
then flip its `armed` flag here.

| Routine | Drives | Cadence | Armed |
|---|---|---|---|
| `janitor.md` | fatbeats-content-janitor | weekly | armed: no |
| `reflect.md` | fatbeats-content-reflect | monthly | armed: no |
| `compound-learn.md` | fatbeats-content-learn | after each work session | armed: no |

Until a schedule is armed, run them on demand — the doctor keeps a
standing low finding as a reminder that unattended self-maintenance
isn't live yet.
