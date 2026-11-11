---
name: ingest
description: 'Add an approved source to the CalCompute Research Library: download, source page, reading lists, entities, index, log. Use when a person says "ingest", "add this source", or approves a suggestion.'
---

# Ingest

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

Ingest a row of `wiki/analyses/Suggestions.md` with status `approved`: a visitor's suggestion when a person asks, and a consortium research row (its Notes start with "from the consortium's research") as soon as it is queued. Never read any folder outside this repo: a source enters only from its public URL.

1. Run `python3 bin/grab.py <URL> "<short title>" --publisher "<publisher>" --published <date>`. Add `--folder legislative` for a legislative record, `--license "<license>"` for an open-licensed file. A consortium row's Notes give these values. If the library already has the document under another address, set the row's status to `duplicate` and stop.
2. Read the Markdown copy, in `raw/` or `.cache/`.
3. Write the source page in the format above. Tag its elements.
4. Add it to each tagged element's reading list, under its tier.
5. Add or update the publisher's entity page.
6. If a concept page covers the topic, add what the source says there.
   If a directory page lists the record, update its row and its Checked date. If the source describes a new record, add a row. When a row names an institution, add or update its entity page.
7. Update `wiki/index.md`, set the suggestion's status to `ingested`, and add a log entry: `## [YYYY-MM-DD] ingest | <title>`.
8. Run `python3 bin/drive_push.py`. It uploads a rehosted PDF or office file and adds every new source to the guide's table of contents.
