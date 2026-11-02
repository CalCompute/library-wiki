# CalCompute Research Library

A public library of research sources for the CalCompute Framework Report. California's Government Code section 11546.8 (SB 53) asks a consortium to send the Legislature a framework for CalCompute, a public cloud computing cluster, by January 1, 2027. The Report has seven elements, A to G. This library collects public documents about each one.

The library reports what the sources say. It does not say what the Report will recommend, and it is not a position of the consortium.

This library is a tool to navigate and explore the research. An AI agent keeps its pages and links current. The consortium does not use AI to write the CalCompute Framework Report.

## Read it

- On the web: https://research.californiacompute.org, with a graph, search, the Drive and this repository.
- In this repository: start at [wiki/index.md](wiki/index.md). The seven reading lists are in [wiki/elements/](wiki/elements/).
- The calendar of element calls, and a dated marker in the graph for each of the consortium's calls, email threads and chat topics. Their content is not public.
- Original documents: government documents and open-licensed files are in [raw/](raw/) and in the public Google Drive "CalCompute Library". Other sources link to their publisher.

## Suggest reading or ask a question

Write to team@californiacompute.org with the subject "Suggested reading". Give the link, what it is, and the element it is about. A consortium member reads every suggestion. The [Suggestions](wiki/analyses/Suggestions.md) page shows what came in and what happened to it, without names.

## How it is built

The library follows Andrej Karpathy's LLM-wiki pattern: original documents in `raw/`, pages that an agent writes in `wiki/`, and one schema, [AGENTS.md](AGENTS.md), with every rule and operation. Any coding agent, or a person, can follow it. The site ([CalCompute/library-site](https://github.com/CalCompute/library-site)) turns these files into web pages on every push.
