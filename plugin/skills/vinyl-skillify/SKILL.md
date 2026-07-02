---
name: vinyl-skillify
description: Promote proven, repeated work into a new skill. Use when the same manual process has been done twice, when the user says "make this a skill", "we keep doing this", or when the janitor finds recurring one-off work. One-off work stays in work/; only repetition earns a skill.
---

# Vinyl skillify

1. **Prove provenance.** Point at the 2+ real occurrences (releases,
   dates, files). If it happened once, stop — it lives in `work/` and
   does not become a skill.
2. **Extract the repeatable process** from what was actually done (not
   what should theoretically work): steps, inputs, the checks that caught
   mistakes.
3. **Stage a draft** at `work/YYYY-MM-DD-skillify-{name}/SKILL.md`,
   frontmatter matching the house style (name + description with real
   trigger phrases, no angle brackets in the description).
4. **Verify with the strongest available check** — run the drafted steps
   against a real release end to end and show the output.
5. **Ask for approval**, then move it to `plugin/skills/{name}/SKILL.md`,
   delete the staging folder, and log the addition in
   `project-overview.md` + `operations/improvements.md`.
