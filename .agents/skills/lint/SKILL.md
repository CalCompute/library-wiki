---
name: lint
description: 'Health check for the CalCompute Research Library: links, reading lists, rehost flags, attribution and direction-setting text. Use when a person says "lint" or "health check".'
---

# Lint

The rules in [AGENTS.md](../../../AGENTS.md) apply to every step.

When a person asks for a health check, find and report:

- broken links, and pages that no other page links to;
- source pages with no element tag, or missing from their reading lists;
- `rehost: yes` on a file that is not a government document and has no license, or a file in `raw/` with `rehost: no`;
- any name of a person as the one who suggested or said something, outside a quotation;
- a directory row with no link to a source page, or with no Checked date (an error);
- a directory row with a Serves, Offers, Domains, Cost or California region value outside its fixed list in AGENTS.md (an error; a Cost value can have a note in parentheses);
- a directory row with a Link that no cited source page carries in its `url`, its text or its raw or cached copy (an error);
- a directory row with a Checked date more than 90 days old (a warning);
- any sentence that says what the Report should, could or will do.

Write the report in `wiki/analyses/Lint YYYY-MM-DD.md` and add a `lint |` log entry.
