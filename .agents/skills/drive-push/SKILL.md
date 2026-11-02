---
name: drive-push
description: 'Upload new rehosted originals to the public "CalCompute Library" Drive, rewrite its contents Docs, and refresh the site''s Drive listing. Use after every ingest.'
---

# Drive push

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

Run `python3 bin/drive_push.py --check`, then `python3 bin/drive_push.py`. It uploads new rehosted originals, rewrites the two Docs (the guide, whose tabs list every source with its web address, and the legislative contents), and rewrites `raw/drive/.listing.json` and `raw/drive/.folders.json`. Commit those two files. If it prints `NOT PUSHED`, fix the source page the line comes from and run it again.
