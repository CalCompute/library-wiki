---
name: ingest
description: 'Add an approved source to the CalCompute Research Library: the handed file or a download, source page, reading lists, entities, index, log. Use when a person says "ingest", "add this source", or approves a suggestion.'
---

# Ingest

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

Ingest a row of `wiki/analyses/Suggestions.md` with status `approved` whose Notes start with "from the consortium's research", as soon as it is queued. Only those rows: an approved visitor suggestion goes to the consortium's wiki first and comes back as such a row. Then set the visitor's row to `ingested` too. Never read any folder outside this repo.

The consortium's wiki fetches each source from the web once (Nov. 20, 2026). A row whose Notes end with `file: <filename>` enters from that file in `.cache/handoff/`. Only a row with no `file:` note enters from its public URL.

1. If the row has a `file:` note, read that file in `.cache/handoff/` first. It is the publisher's document as served at the row's URL. Its fetch date is the date at the start of its file name.
   - If it is thin (a redirect page, an empty page shell, or not the document the row names), stop. Do not download the source again. Leave the row approved, record why in the log entry, and tell the person.
   - Do not change or delete the file.
2. Run `python3 bin/grab.py <URL> "<short title>" --publisher "<publisher>" --published <date>`, with the row's URL. Add `--file "<filename>"` for a row with a `file:` note: the script then copies that file and does not download. Add `--folder legislative` for a legislative record, `--license "<license>"` for an open-licensed file. A consortium row's Notes give these values. The rehost rule does not change: the row's URL and licence decide `raw/` or `.cache/`. If the library already has the document under another address, set the row's status to `duplicate` and stop.
3. Read the Markdown copy, in `raw/` or `.cache/`.
4. Write the source page in the format above. Tag its elements. Cite the row's URL, and give the date at the start of the file name as its fetch date.
5. Add it to each tagged element's reading list, under its tier.
6. If the publisher's entity page has no `mirror: yes`, add the source to it. A page with `mirror: yes`, or a publisher with no page, is the consortium wiki's: leave it.
7. If a concept page covers the topic, add what the source says there.
   Never edit a page with `mirror: yes`: the directory pages and their institution pages come from the consortium's wiki.
8. Update `wiki/index.md`, set the suggestion's status to `ingested`, and add a log entry: `## [YYYY-MM-DD] ingest | <title>`.
9. Run `python3 bin/drive_push.py --check`. Do not run the push itself: the maintainer runs it with the GitHub push (user, Nov. 20, 2026). Then it uploads each rehosted PDF or office file and adds every new source to the guide's table of contents.
