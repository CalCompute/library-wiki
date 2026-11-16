---
name: ingest
description: 'Add an approved source to the CalCompute Research Library: download, source page, reading lists, entities, index, log. Use when a person says "ingest", "add this source", or approves a suggestion.'
---

# Ingest

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

Ingest a row of `wiki/analyses/Suggestions.md` with status `approved` whose Notes start with "from the consortium's research", as soon as it is queued. Only those rows: an approved visitor suggestion goes to the consortium's wiki first and comes back as such a row. Then set the visitor's row to `ingested` too. Never read any folder outside this repo: a source enters only from its public URL.

1. Run `python3 bin/grab.py <URL> "<short title>" --publisher "<publisher>" --published <date>`. Add `--folder legislative` for a legislative record, `--license "<license>"` for an open-licensed file. A consortium row's Notes give these values. If the library already has the document under another address, set the row's status to `duplicate` and stop.
2. Read the Markdown copy, in `raw/` or `.cache/`.
3. Write the source page in the format above. Tag its elements.
4. Add it to each tagged element's reading list, under its tier.
5. If the publisher's entity page has no `mirror: yes`, add the source to it. A page with `mirror: yes`, or a publisher with no page, is the consortium wiki's: leave it.
6. If a concept page covers the topic, add what the source says there.
   Never edit a page with `mirror: yes`: the directory pages and their institution pages come from the consortium's wiki.
7. Update `wiki/index.md`, set the suggestion's status to `ingested`, and add a log entry: `## [YYYY-MM-DD] ingest | <title>`.
8. Run `python3 bin/drive_push.py`. It uploads a rehosted PDF or office file and adds every new source to the guide's table of contents.
