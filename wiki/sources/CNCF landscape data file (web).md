---
title: CNCF landscape data file (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, open-source, cloud-native, dataset]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml
rehost: no
---

# CNCF landscape data file (web)

## Citation

Cloud Native Computing Foundation (CNCF). "landscape.yml." Data file in the cncf/landscape repository on GitHub, master branch, date not stated. https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml. Read 2026-11-11.

## Bottom line

- The file is the data behind the CNCF landscape: a YAML (YAML Ain't Markup Language) list of cloud-native and AI projects, products and members.
- The copy read on 2026-11-11 has 15 categories and 2,444 items. 41 items are CNCF graduated projects, 37 incubating and 156 sandbox.
- Five of the categories are on AI: AI Agent, Inference, Data, Training and AI Native Infra.

## Background

The CNCF keeps this file in its public landscape repository on GitHub. Each item gives a name, a homepage, a repository address and a logo. Some items give a description and a CNCF project level. The first line points to a schema in the CNCF landscape2 tool, which builds the landscape web site from this file ([cncf landscape2 on GitHub](cncf%20landscape2%20on%20GitHub.md)).

## Key claims

- Structure: the file begins "landscape:" and then "- category: name: Provisioning". Each category holds subcategories, and each subcategory holds items. (lines 3 to 10)
- Categories: the 15 categories are Provisioning, Runtime, Orchestration & Management, App Definition and Development, Platform, Serverless, Observability and Analysis, Special, CNCF Members, Wasm, AI Agent, Inference, Data, Training and AI Native Infra. (category entries)
- Project level: items carry a field such as "project: sandbox". In this copy, 41 items have "project: graduated", 37 have "project: incubating" and 156 have "project: sandbox". (item fields; counted)
- vLLM item: "name: vLLM", "description: vLLM is a fast and easy-to-use library for LLM inference and serving.", "repo_url: https://github.com/vllm-project/vllm" (Inference category)
- llm-d item: "llm-d is a Kubernetes-native, high-performance distributed LLM inference framework built on vLLM and the Kubernetes Gateway API Inference Extension" (Inference category)
- Members: the CNCF Members category holds 720 items, the largest of the 15 categories. (counted)

## Evidence and method

This is a structured data file, not a report. The counts on this page come from a count of the "- item:" and "project:" lines in the copy read on 2026-11-11. The file changes often, so the counts change too.

## Limits

- The file lists projects and companies. It does not rate them and gives no data on use or cost.
- Most items have no CNCF project level. A listing does not mean that the CNCF hosts the item.
- The file has no date. The counts are true only for the copy read on 2026-11-11.
- The older page [CNCF landscape](CNCF%20landscape.md) is a saved copy of the landscape web site with no content.
