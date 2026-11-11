---
name: suggestions
description: 'Record a visitor''s suggested source, correction, data or question on the Suggestions page and take it to a consortium member for a decision. Use when the site''s Suggest or correct form has new entries (npm run submissions in library-site).'
---

# Suggestions

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

1. A visitor sends the site's **Suggest or correct** form. It is stored, not published. In `library-site`, `npm run submissions` prints the entries not yet read, each with an id.
2. A person adds a row to `wiki/analyses/Suggestions.md`: date received, the source, correction or question, status `received`. Never the sender's name, address or institution. Then marks the entry read (the command is at the top of `library-site/scripts/submissions.mjs`).
3. A consortium member reads the suggestion and decides. The person sets the status to `approved` or `declined`, with a short reason.
4. Only an approved source goes to Ingest. Only an approved question goes to Query. An approved correction is made by hand on the page it names, and its log entry says so. Nothing a visitor sends is applied without that approval.
5. A row whose Notes start with "from the consortium's research" comes from the consortium's wiki, already approved, with the source's title and address only. It goes straight to Ingest.
