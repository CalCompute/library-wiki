# CalCompute Research Library

This file is the schema of the library. It tells any agent or person how the library is built and how to keep it. Read it at the start of every session. It works with any coding agent, or with a person and a text editor. The step lists for each operation are skills in [`.agents/skills/`](.agents/skills/), linked from [Operations](#operations).

## Bottom line

- This library holds the public research sources for the CalCompute Framework Report. The Report is due to the California Legislature by January 1, 2027, under Government Code section 11546.8 (SB 53).
- It reports **what the sources say**. It never says what the Report will recommend, and it is not a position of the consortium.
- Anyone can suggest reading or ask a question by email. A consortium member approves each suggestion before it goes in.
- `raw/` holds the original documents. You never change them. `wiki/` holds the pages you write. Write to the [writing standard](#writing-standard).
- You never commit or push. At the end of a session, give the person the commit command.

## What this library is

The pattern is Andrej Karpathy's LLM wiki: raw sources, a wiki that an agent writes and keeps current, and this schema. The site at https://research.californiacompute.org shows the same files as web pages, with a graph, search and a Drive browser. Nobody needs Obsidian. All files are plain Markdown with standard links.

The CalCompute Consortium writes the Report. The Report has seven elements, (f)(2)(A) to (G). The library groups its sources by those seven elements.

The library started on Nov. 1, 2026, with the public sources the consortium's research had used by then. New sources enter by the ingest skill, from their public URLs, when a person approves them.

## Layout

```
AGENTS.md            this file: the schema
README.md            what the library is, for people
activity.json        the five counts on the home page, a dated marker for each of the consortium's calls, email threads and chat topics, and the meeting calendar; the consortium's team publishes it
setup.sh             per-machine setup: .venv with markitdown and google-auth
bin/grab.py          downloads a source into raw/ (rehosted) or .cache/ (not rehosted)
bin/drive_push.py    uploads rehosted originals to the public Drive, rewrites its two navigation Docs, and lists the Drive for the site
bin/gdoc.py          writes those Docs with CalCompute's brand (bin/drive_push.py calls it)
bin/ste.py           writing-standard check
.agents/skills/      one folder per operation (suggestions, ingest, query, lint, drive-push), each with a SKILL.md

raw/                 original documents; read only
  legislative/       the statute and the legislative record, word for word
  web/               documents downloaded with bin/grab.py: every source added since the library started
  shared/            documents the consortium's research used before the library started; nothing new goes here
  human/             documents that people wrote
  drive/             .listing.json and .folders.json: what is in the public Drive (bin/drive_push.py writes them)
.cache/              downloads that are not rehosted; git ignores this folder

wiki/                pages you write
  index.md           catalog of every page
  log.md             append-only record of every session
  overview.md        what the statute asks of CalCompute and the Report
  elements/          one reading list per element, A to G, and Statutory requirements.md
  sources/           one page per source
  entities/          one page per publisher, and one per person on the team
  concepts/          what the sources say about one topic
  analyses/          answers to visitors' questions, and the Suggestions page
```

The `README.md` files in `raw/` folders explain the folder. They are not sources. Do not ingest them.

## Rules

- **Report what the sources say.** Every page states what a document says, in its own terms, with a citation. Do not write what the Report should, could or will do. Do not rank sources by how well they support a direction.
- **No member attribution.** Never write who suggested, shared or said something. A profile page names the person it is about; that is its content, not attribution. The people californiacompute.org lists (the consortium, supporting researchers, the operations team, government advocates and Legislative champions) appear only on their own entity pages, with the facts that californiacompute.org shows.
- **Do not describe the consortium.** Its membership, meetings, positions and decisions come from the consortium, not from this library. Never write that § 11546.8 or the Report "becomes operative only upon an appropriation". Never write that the Government Operations Agency houses or convenes the consortium. You can quote the statute word for word.
- **Rehost only what may be rehosted.** A government document, or a file with an open license, has `rehost: yes`: its original and Markdown copy go in `raw/`, and `bin/drive_push.py` puts the original in the public Drive. Any other source has no copy in `raw/`. Its source page links to the publisher's address, and its download stays in `.cache/`.
- **Read only this repo.** Never read any folder outside this repo. A source enters only from its public URL.
- **The Drive stands alone.** Its two Docs (`0 - LIBRARY GUIDE`, whose tabs are the table of contents, and `0 - LEGISLATIVE CONTENTS`) are rewritten from `wiki/sources/` and `raw/legislative/` on every `bin/drive_push.py` run. They never name the agent that writes them or the consortium's communications; the push refuses a Doc that does.
- **Never ingest the consortium's own website.** https://californiacompute.org is not research. `bin/grab.py` refuses it.
- **Do not edit, rename, move or delete a file in `raw/`.** Only `bin/grab.py` and `bin/drive_push.py` write there.
- **Keep the original format.** If a source is `.docx`, `.pdf`, `.pptx`, `.xlsx` or `.html`, `bin/grab.py` makes a Markdown copy beside it with the same name. The copy starts with `_Markdown copy of <file>, made YYYY-MM-DD. The original is the authority._` Read the copy. Cite the original.
- **Mark web material.** A source page for a file in `raw/web/` has a title that ends in ` (web)`.
- **The statute is the base of every definition.** Quote `raw/legislative/SB-53 Gov Code 11546.8.md` for what CalCompute and the Report must be.
- **Consortium communications appear as markers.** `activity.json` gives a dated marker for each of the consortium's calls (transcript and Meet chat), email threads and chat topics: kind, shape, size, date, element letters and links. Nothing else about them is public, and this library never holds their text. The calendar shows the element calls and the community sync. Do not edit `activity.json` by hand.
- **Concepts and analyses carry a notice.** Put this line under the heading of every concept and analysis page: `_This page reports what the sources say. It is not a position of the consortium._`

## Page formats

**Source page** (`wiki/sources/<title>.md`):

1. `## Citation`: author or body, title, publisher or venue, date, the publisher's URL, and the date you read it. For a rehosted source, add the `raw/` path.
2. `## Bottom line`: what the document is and what it says, in two or three lines. No claim about where the Report is heading.
3. `## Background`: what the document is and who published it, in two to five sentences.
4. `## Key claims`: three or more word-for-word quotes, each with its page or section.
5. `## Evidence and method`: what kind of document it is and what evidence it gives.
6. `## Limits`: what it does not cover. A contradiction with another source is a flag: `> ⚠️ Contradiction: ...`, with both sources cited.

**Profile page**: a source page about one person or their organisation (a staff bio, ORCID record, award notice, personal site), tagged `people`. It is listed on that person's entity page, not on a reading list.

**Element reading list** (`wiki/elements/<L> - <Title>.md`): the statute text for the element, then `## Reading list` with every source tagged with that element, grouped by tier (primary, peer-reviewed, institutional, trade). One line per source: link and a one-line summary. No synthesis.

**Entity page** (`wiki/entities/<name>.md`): a person or institution with `kind: person | institution`: `## Bottom line` (who it is, in one or two lines; every name, number and quotation in it is in a cited source page), `## Why they matter` (what the sources say it did or does on the elements, each line cited), Affiliations and Background facts, each cited, and a Sources list; or a person on the team, with `member: yes`, `group: consortium | supporting | operations | advocates | legislative`, institution, role as californiacompute.org states it, and public links. No contact details.

**Concept page** (`wiki/concepts/<topic>.md`): the notice line, then what each source says about the topic, side by side, each claim cited. Where sources disagree, show both.

**Analysis page** (`wiki/analyses/<short title>.md`): the notice line, then `Asked by a visitor, YYYY-MM-DD.` and the question, then the answer from the library's sources, each claim cited.

## Frontmatter

```yaml
---
title: <page title>
type: source | entity | element | checklist | concept | analysis | overview
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: <number of sources the page uses>
tags: [A, C]                 # the element letters the page is about, and other tags
elements: [A, C]             # on source and element pages
origin: legislative | web | shared | human    # on source pages only
tier: primary | peer-reviewed | institutional | trade   # on source pages only
citable: yes | no            # on source pages: whether a public report could cite it
url: <publisher's address>   # on source pages
rehost: yes | no             # on source pages and raw Markdown copies
element: A                   # on element reading lists only
member: yes                  # on team entity pages only
group: consortium            # on team entity pages: consortium | supporting | operations | advocates | legislative
---
```

Start every page with one `#` heading that matches `title`.

## Links and syntax

- Use standard relative Markdown links with the `.md` path. Encode spaces as `%20`: `[ACCESS homepage](../sources/ACCESS%20homepage.md)`.
- Never use `[[wikilinks]]`, embeds, callouts, HTML or Dataview blocks.
- Flags are plain blockquotes: `> ⚠️ Contradiction: ...` and `> 🔍 Gap: ...`.
- Search with `wiki/index.md` first, then `grep -ril "<term>" wiki/`.

## Citations

- **Every source page starts with a full citation.**
- **Every claim on a wiki page cites its source page** with a link.
- **Quote word for word.** Do not put a paraphrase in quotation marks.
- **Cite only what you read.**
- **Prefer primary and peer-reviewed sources.** Use government or statutory primary sources, peer-reviewed work and reports from recognised research institutions. Record trade press and vendor material with tier "trade".

## Writing standard

Write every page to ASD-STE100 (Simplified Technical English) at about 80 percent. Apply the writing rules fully. Use the controlled dictionary as a direction, not a rule.

- **Bottom line up front (BLUF).** Every source page (after its Citation), entity page and analysis starts with `## Bottom line`: what the document says, or who the person or institution is. Detail comes after. A reader who stops after the first lines has the answer. A Bottom line never says where the Report is heading.
- **Sentences.** One topic in each sentence. Instructions have 20 words or fewer. Descriptions have 25 words or fewer.
- **Grammar.** Use the active voice. Use the present tense, unless the event is in the past. Every sentence has a verb.
- **Paragraphs.** Six sentences or fewer, about one topic. Use a list for items of the same type, one item on each line.
- **Terms.** Use one term for one thing in all of the library: CalCompute, the Report, the consortium, element A. Do not use synonyms for variety.
- **Words.** Do not use more than three nouns in a row. Keep "the" and "a". Do not use slang or idioms. Write an acronym in full the first time it appears on a page. Use short, common words.
- **Instructions** use the imperative: "Put the file in `raw/web/`." Put a warning or condition before the instruction.
- **Quotations are exempt.** Statute text and cited passages stay word for word.
- **No em dashes.** Use a period, a comma or a colon.
- **No AI-writing patterns.** Write the fact and its source, and stop. This applies to every page and every Doc the push writes. Do not use:
  - openers and fillers: `It is worth noting`, `Importantly`, `Notably`, `Furthermore`, `Moreover`, `In summary`;
  - inflated words: `delve`, `robust`, `leverage`, `streamline`, `foster`, `ensure`, `seamless`, `pivotal`, `crucial`, `underscore`, `showcase`;
  - a closing sentence that repeats the section, or a sentence that says what the next sentence will say;
  - three adjectives or three clauses only for rhythm;
  - hedges such as "may potentially" or "arguably";
  - rhetorical questions;
  - a chain of "<Name> noted that ..." and "<Name> highlighted ..." lines. Say what the source says.
  `bin/ste.py` flags the words in this list.
- **Check.** Run `python3 bin/ste.py` on the pages you changed. Fix what it flags, but not quotations or titles.

## Operations

Each operation is a skill: a step list in `.agents/skills/<name>/SKILL.md`. Any agent or person can follow it. Open the skill before you do the work.

- [Suggestions](.agents/skills/suggestions/SKILL.md): Record a visitor's suggested source or question on the Suggestions page and take it to a consortium member for a decision.
- [Ingest](.agents/skills/ingest/SKILL.md): Add an approved source to the CalCompute Research Library: download, source page, reading lists, entities, index, log.
- [Query](.agents/skills/query/SKILL.md): Answer a question from the library's sources with citations, and file approved visitor questions in wiki/analyses/.
- [Lint](.agents/skills/lint/SKILL.md): Health check for the CalCompute Research Library: links, reading lists, rehost flags, attribution and direction-setting text.
- [Drive push](.agents/skills/drive-push/SKILL.md): Upload new rehosted originals to the public "CalCompute Library" Drive, rewrite its contents Docs, and refresh the site's Drive listing.

## index.md

- Header: `_Last updated: YYYY-MM-DD, N pages_`.
- Sections: Overview, Elements, Sources, Entities, Concepts, Analyses.
- **Sources** has these columns: Page, Origin, Tier, Summary, Date.
- Update the index every time you add or change a page.

## log.md

Append only. Do not change old entries. Each entry starts with `## [YYYY-MM-DD] <type> | <title>`, so `grep "^## \[" wiki/log.md` can read it. The types are `setup`, `fetch`, `ingest`, `query`, `lint`, `fix`, `schema`. Under the heading, write one line each for: Summary, Pages created, Pages updated, Notable.

## Start of a session

1. Run `git pull`.
2. Read this file, `wiki/index.md` and the last ten entries of `wiki/log.md`.
3. Read `wiki/analyses/Suggestions.md` and tell the person which suggestions wait for a decision.

## End of a session

1. Run `python3 bin/ste.py` and fix what it flags.
2. Make sure `wiki/index.md` and `wiki/log.md` are current.
3. Give the person this command. Do not run it.

   ```bash
   git add -A && git commit -m "<type>: <subject>" && git push
   ```

## Changing this file

This file can change as the work changes. Write a `schema |` entry in the log for each change. A person approves changes to the structure. You make them.
