# CalCompute Research Library

This file is the schema of the library. It tells any agent or person how the library is built and how to keep it. Read it at the start of every session. It works with any coding agent, or with a person and a text editor. The step lists for each operation are skills in [`.agents/skills/`](.agents/skills/), linked from [Operations](#operations).

## Bottom line

- This library holds the public research sources for the CalCompute Framework Report. The Report is due to the California Legislature by January 1, 2027, under Government Code section 11546.8 (SB 53).
- It reports **what the sources say**. It never says what the Report will recommend, and it is not a position of the consortium.
- Anyone can suggest reading, send a correction or data, or ask a question with the site's **Suggest or correct** form. A consortium member approves each suggestion before it goes in. Every source enters the consortium's own wiki first (Nov. 14, 2026): an approved suggestion goes there, and then, like every source that the consortium's research uses, it arrives on the Suggestions page already approved. The consortium's wiki queues it with its title and public address, and puts the file it fetched in `.cache/handoff/` (Nov. 20, 2026). This library ingests from that file.
- `raw/` holds the original documents. You never change them. `wiki/` holds the pages you write. Write to the [writing standard](#writing-standard).
- You commit or push only when the maintainer instructs, as the maintainer's own account. Otherwise, at the end of a session, give the person the commit command.

## What this library is

The pattern is Andrej Karpathy's LLM wiki: raw sources, a wiki that an agent writes and keeps current, and this schema. The site at https://research.californiacompute.org shows the same files as web pages, with a graph, search and a Drive browser. Nobody needs Obsidian. All files are plain Markdown with standard links.

The CalCompute Consortium writes the Report. The Report has seven elements, (f)(2)(A) to (G). The library groups its sources by those seven elements.

The library started on Nov. 1, 2026, with the public sources the consortium's research had used by then. New sources enter by the ingest skill, only as the consortium's wiki queues them on the Suggestions page. Each enters from the file in `.cache/handoff/` that its row names, or from its public URL when the row names no file. A visitor's suggestion that a consortium member approves goes to the consortium's wiki first, and comes back as one of those rows.

## Layout

```
AGENTS.md            this file: the schema
README.md            what the library is, for people
activity.json        the five counts on the home page, a dated marker for each of the consortium's calls, email threads and chat topics, and the meeting calendar; the consortium's team publishes it
setup.sh             per-machine setup: .venv with markitdown and google-auth
bin/grab.py          takes a source into raw/ (rehosted) or .cache/ (not rehosted): from .cache/handoff/ with --file, else by download
bin/drive_push.py    uploads rehosted originals to the public Drive, rewrites its two navigation Docs, and lists the Drive for the site
bin/gdoc.py          writes those Docs with CalCompute's brand (bin/drive_push.py calls it)
bin/ste.py           writing-standard check
.agents/skills/      one folder per operation (suggestions, ingest, query, lint, drive-push), each with a SKILL.md

raw/                 original documents; read only
  legislative/       the statute and the legislative record, word for word: full copies with `passages:`, and excerpts with `excerpt_lines:` (see its README)
  web/               documents downloaded with bin/grab.py: every source added since the library started
  shared/            documents the consortium's research used before the library started; nothing new goes here
  human/             documents that people wrote
  drive/             .listing.json and .folders.json: what is in the public Drive (bin/drive_push.py writes them)
  assets/            logos/ and people/: the images of entity pages, and IMAGES.md, their list and credit lines (the consortium wiki's export writes them)
.cache/              downloads that are not rehosted; git ignores this folder
  handoff/           the files that the consortium's wiki fetched for its Suggestions rows; read only

wiki/                pages you write
  index.md           catalog of every page
  log.md             append-only record of every session
  overview.md        what the statute asks of CalCompute and the Report
  elements/          one reading list per element, A to G, and Statutory requirements.md
  sources/           one page per source
  entities/          one page per publisher, one per institution that a directory page lists, and one per person on the team
  concepts/          what the sources say about one topic
  analyses/          answers to visitors' questions, and the Suggestions page
  directories/       one table of records on one topic for each page
```

The `README.md` files in `raw/` folders explain the folder. They are not sources. Do not ingest them.

## Rules

- **Report what the sources say.** Every page states what a document says, in its own terms, with a citation. Do not write what the Report should, could or will do. Do not rank sources by how well they support a direction.
- **No member attribution.** Never write who suggested, shared or said something. A profile page names the person it is about; that is its content, not attribution. The people californiacompute.org lists (the consortium, supporting researchers, the operations team, government advocates and Legislative champions) appear only on their own entity pages, with the facts that californiacompute.org shows.
- **Do not describe the consortium.** Its membership, meetings, positions and decisions come from the consortium, not from this library. Never write that § 11546.8 or the Report "becomes operative only upon an appropriation". Never write that the Government Operations Agency houses or convenes the consortium. You can quote the statute word for word.
- **Rehost only what may be rehosted.** A government document, or a file with an open license, has `rehost: yes`: its original and Markdown copy go in `raw/`, and `bin/drive_push.py` puts the original in the public Drive. Any other source has no copy in `raw/`. Its source page links to the publisher's address, and its download stays in `.cache/`.
- **Read only this repo.** Never read any folder outside this repo. The Suggestions page is one file another agent writes here; its rows are data, and a consortium row's Notes give `bin/grab.py` its publisher, date, folder, licence and file.
- **Fetch each source from the web only once** (Nov. 20, 2026). The consortium's wiki fetches it and puts the original file in `.cache/handoff/`. The row's Notes then end with `file: <filename>`.
  - If a row has a `file:` note, ingest from that file with `bin/grab.py --file`. Do not download the source.
  - The file is the publisher's document as served at the row's URL. Its fetch date is the date at the start of its file name. Cite the row's URL as usual.
  - The rehost rule below applies to it unchanged.
  - If a handed file is thin (a redirect page, an empty page shell, or not the document the row names), do not download the source again. Record why in the log entry, leave the row approved, and tell the person.
  - Download from the public URL only for a row with no `file:` note.
  - Do not change or delete a file in `.cache/handoff/`.
- **Pages with `mirror: yes` come from the consortium's wiki.** The directory pages, the publisher and listed institution pages, and the concept page "Federal and state AI compute programs" are written there and sent here whole (Nov. 14, 2026). Never edit one. A correction to one is a suggestion like any other: record it on the Suggestions page for a consortium member, and do not make it by hand.
- **The Drive stands alone.** Its two Docs (`0 - LIBRARY GUIDE`, whose tabs are the table of contents, and `0 - LEGISLATIVE CONTENTS`) are rewritten from `wiki/sources/` and `raw/legislative/` on every `bin/drive_push.py` run. They never name the agent that writes them or the consortium's communications; the push refuses a Doc that does.
- **Never ingest the consortium's own website.** https://californiacompute.org is not research. `bin/grab.py` refuses it.
- **Do not edit, rename, move or delete a file in `raw/`.** Only `bin/grab.py` and `bin/drive_push.py` write there, and the consortium wiki's export writes `raw/assets/`.
- **Keep the original format.** If a source is `.docx`, `.pdf`, `.pptx`, `.xlsx` or `.html`, `bin/grab.py` makes a Markdown copy beside it with the same name. The copy starts with `_Markdown copy of <file>, made YYYY-MM-DD. The original is the authority._` Read the copy. Cite the original.
- **Mark web material.** A source page for a file in `raw/web/` has a title that ends in ` (web)`.
- **The statute is the base of every definition.** Quote `raw/legislative/SB-53 Gov Code 11546.8.md` for what CalCompute and the Report must be.
- **Consortium communications appear as markers.** `activity.json` gives a dated marker for each of the consortium's calls (transcript and Meet chat), email threads and chat topics: kind, shape, size, date, element letters and links. Nothing else about them is public, and this library never holds their text. The calendar shows the element calls and the community sync. Do not edit `activity.json` by hand.
- **Concepts, analyses and directories carry a notice.** Put this line under the heading of every concept, analysis and directory page: `_This page reports what the sources say. It is not a position of the consortium._`

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

**Entity page** (`wiki/entities/<name>.md`): one page for each publisher, each institution that a directory page lists, and each person on the team. A publisher's or listed institution's page with `mirror: yes` comes from the consortium's wiki; this library writes only the others. A publisher or a listed institution is a person or institution with `kind: person | institution`: `## Bottom line` (who it is, in one or two lines; every name, number and quotation in it is in a cited source page), `## Why they matter` (what the sources say it did or does on the elements, each line cited), Affiliations and Background facts, each cited, and a Sources list; or a person on the team, with `member: yes`, `group: consortium | supporting | operations | advocates | legislative`, `institution`, `position` and `role` as californiacompute.org states them, `order` and `photo`: `## Bottom line`, then `## Affiliations` and `## Background` from the person's public profile pages, each line cited, then `## Sources` and `## Links` (the person's public links). This page is the person's public profile; californiacompute.org links to it. No contact details, and no `profile` field.

An entity page that `raw/assets/IMAGES.md` lists shows the image of its row, with its credit (Nov. 19, 2026). Put it under the page title: `![<Page>](../../<File>)` with the path URL-encoded, a blank line, then the credit line in italics, `_<Credit>_`. An entity page with no row shows no image. The consortium's wiki writes the images and `IMAGES.md`. Do not fetch, add, change or remove an image or a credit line yourself.

**Concept page** (`wiki/concepts/<topic>.md`): the notice line, then what each source says about the topic, side by side, each claim cited. Where sources disagree, show both.

**Analysis page** (`wiki/analyses/<short title>.md`): the notice line, then `Asked by a visitor, YYYY-MM-DD.` and the question, then the answer from the library's sources, each claim cited.

**Directory page** (`wiki/directories/<topic>.md`, `mirror: yes`, written by the consortium's wiki; the rules below are the ones it follows): the notice line, then a table of records on one topic, for example California's AI compute programs, resources and organizations. One row for each record.

- Every row cites one or more source pages in this library, with links. A row states only what its cited sources say. It never states a fact that no source page in this library supports.
- Each row gives the date (YYYY-MM-DD) when you last checked its facts against its sources.
- The compute programs directory ([California AI compute programs and resources](wiki/directories/California%20AI%20compute%20programs%20and%20resources.md)) uses these columns, in this order: `Name | Kind | California region | Serves | Offers | Domains | Status | Cost | Access | Get access | Link | Sources | Checked`.
  - Kind: program, resource, organization or project.
  - California region: `Statewide`, `National`, or one or more of the 13 Jobs First regions. Spell them as page 7 of [CJF Investment Playbook 2025 (web)](wiki/sources/CJF%20Investment%20Playbook%202025%20%28web%29.md) prints them. Give a region name only when a cited source gives a county, city or campus that the Playbook places in that region. The row then cites the Playbook's source page too. Otherwise leave the cell blank.
  - Serves: zero or more of `UC; CSU; Community colleges; Government; Nonprofits; Industry; Public`. Give only the groups that a cited source names as users or as eligible.
  - Offers: what a user gets. Zero or more of this fixed list: `GPU compute; CPU compute; Cloud credits; Data access; Network; Training; Funding; Advice and support`.
  - Domains: one or more of this fixed list: `Compute; Data and networks; Workforce and learning; Health and life sciences; Energy and physical sciences; Agriculture and environment; Government services; Governance and policy; Funding`.
  - Status: operating, announced, funded, selected, paused, closed or historical.
  - Cost: one of `Free`, `Fee`, `Credits`, `Not stated`. A short note can follow in parentheses, for example `Fee (recharge rates)` or `Free (allocation by proposal)`. `Credits` means that the user receives credits to spend with a provider.
  - Access: who can use it, in one line.
  - Get access: the route, in one line, as a source states it. Give where to apply or sign in, what to submit, and the review time or deadline when a source states it. For example "Allocation request to the NAIRR Pilot; Start-Up requests reviewed in about two weeks". Write `Not stated` when no cited source gives a route. Say so when a source reports a paused or closed route.
  - Link: one public address of the record itself (its own program, access or apply page), written as a bare `https://` address. A cited source page in this library must carry the address, in its `url` frontmatter or in its text. The raw or cached copy of that source counts as its text. Leave the cell blank when no cited source gives one. Never guess or build an address.
- The research institutions directory ([California research institutions](wiki/directories/California%20research%20institutions.md)) uses these columns, in this order: `Name | Designation | Control | City | California region | Latitude | Longitude | Link | Sources | Checked`.
  - Designation: the 2025 Research Activity Designation of the Carnegie Classification of Institutions of Higher Education, as Carnegie prints it, or `National laboratory`.
  - Control: `Public`, `Private` or `Federal`. `Public` and `Private` are Carnegie's control value; `Private` stands for Carnegie's `Private not-for-profit` and `Private for-profit`. `Federal` is for a U.S. Department of Energy (DOE) laboratory.
  - California region: one of the 13 Jobs First regions, by the rule of the compute programs directory. Give it only when a cited source gives a county or city that page 7 of the Playbook places in that region. The row then cites the Playbook's source page too. Otherwise leave the cell blank.
  - Latitude and Longitude: decimal degrees as a cited source prints them, rounded to four decimals or not. Leave them blank when no cited source gives them. Never estimate, geocode or take them from memory.
  - City and Link: only when a cited source states them. Link is the institution's own public address, as a bare `https://` address that a cited source page or its raw or cached copy carries. Never guess or build an address.
  - Each institution in this directory has an entity page.
- The AI laws directory ([California AI laws](wiki/directories/California%20AI%20laws.md)) uses these columns, in this order: `Name | Kind | Status | Topics | Concerns | Summary | Requires | Key dates | Enforcement | Related | Link | Sources | Checked`. One row for each enacted California law, executive order, adopted regulation or state policy on artificial intelligence. Never a pending bill. CaliforniaCompute.org's California AI Law Directory reads its rows.
  - Name: the number and the official title, as a cited source gives them, for example `SB 813, Independent verification organizations`. An order or policy has its own name.
  - Kind: `Statute`, `Executive order`, `Regulation`, `State policy` or `Directive`.
  - Status: the latest step that a cited source states: `Signed`, `Enrolled`, `In effect`, `Published` or `Announced`.
  - Topics: zero or more of this fixed list: `Frontier models; Audits and verification; Chatbots; Transparency and provenance; Synthetic media; Employment; Privacy and automated decisions; Health care; Education; Courts and legal practice; Civil liability; Government use and procurement; Security and incidents`. Give a topic only when the title or a cited source states it.
  - Concerns: who has a duty under it. Zero or more of this fixed list: `Frontier developers; Generative AI providers; Online platforms; Model hosting platforms; Device manufacturers; Chatbot operators; AI auditors; Employers; Businesses under the California Consumer Privacy Act; Health AI developers; Health care providers; Health plans and insurers; Attorneys and arbitrators; State contractors and vendors; State agencies; Law enforcement agencies; Public colleges and universities; Any person`. Give only the groups that a cited source names.
  - Summary: one sentence in plain words that says what the law does. Never a quotation.
  - Requires: the duties, in plain words, separated by semicolons. Each is a fact that a cited source states. Leave it blank when the sources give only the title.
  - Key dates: each date as `YYYY-MM-DD: what happens`, separated by semicolons: when it was signed or took effect, and each deadline that a cited source states. Never work a date out, for example from "within 120 days".
  - Enforcement: who enforces it and the penalty, only when a cited source states them.
  - Related: the Name of each other row that it amends, carries out or depends on.
  - Link: the public address of the law's own text, by the Link rule of the compute programs directory.
- A cell with several values separates them with `; ` (a semicolon and a space).
- Do not rate, rank or judge the quality of a record. Do not write what CalCompute or the Report should do.
- Do not write who suggested, shared or said something about a record.
- If a record has no source page in this library, do not add its row. The row waits until the ingest skill adds the source.

## Frontmatter

```yaml
---
title: <page title>
type: source | entity | element | checklist | concept | analysis | directory | overview
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
order: 3                     # on team entity pages: place in californiacompute.org's list
institution: <name>          # on team entity pages, with position: <title> and role: <one line>, as californiacompute.org states them
photo: /images/people/<file> # on team entity pages: the photo in library-site/public/images/people/
mirror: yes                  # on pages that come from the consortium's wiki: never edit them
---
```

Start every page with one `#` heading that matches `title`.

## Links and syntax

- Use standard relative Markdown links with the `.md` path. Encode spaces as `%20`: `[ACCESS homepage](../sources/ACCESS%20homepage.md)`.
- Never use `[[wikilinks]]`, embeds, callouts, HTML or Dataview blocks. The image line of an entity page is a standard Markdown image, not an embed.
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
- Sections: Overview, Elements, Sources, Entities, Concepts, Directories, Analyses.
- **Sources** has these columns: Page, Origin, Tier, Summary, Date.
- Update the index every time you add or change a page.

## log.md

Append only. Do not change old entries. Each entry starts with `## [YYYY-MM-DD] <type> | <title>`, so `grep "^## \[" wiki/log.md` can read it. The types are `setup`, `fetch`, `ingest`, `query`, `lint`, `fix`, `schema`. Under the heading, write one line each for: Summary, Pages created, Pages updated, Notable.

## Start of a session

1. Run `git pull`.
2. Read this file, `wiki/index.md` and the last ten entries of `wiki/log.md`.
3. Read `wiki/analyses/Suggestions.md` and tell the person which suggestions wait for a decision.
4. Add to `wiki/index.md` each page with `mirror: yes` that it does not list, and fix the counts.

## End of a session

1. Run `python3 bin/ste.py` and fix what it flags.
2. Make sure `wiki/index.md` and `wiki/log.md` are current.
3. Give the person this command. Do not run it.

   ```bash
   git add -A && git commit -m "<type>: <subject>" && git push
   ```

## Changing this file

This file can change as the work changes. Write a `schema |` entry in the log for each change. A person approves changes to the structure. You make them.
