---
title: National Compute docs Public Research (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [D, B, national-compute, public-research, gpu-access, data-sharing]
elements: [D, B]
origin: web
tier: trade
citable: yes
url: https://docs.nationalcompute.com/public-research/
rehost: no
---

# National Compute docs Public Research (web)

## Citation

National Compute Labs PBC. "Public Research." National Compute Docs, date not stated. https://docs.nationalcompute.com/public-research/. Read 2026-11-11.

## Bottom line

- Public Research gives one whole 8-GPU node at a time to an individual researcher with a `.edu`, `.mil` or `.gov` address. The researcher asks the agent Marshall for a node and waits in a first-come, first-served queue.
- A lease is 4 hours and bills per GPU-hour. A public research organization starts with $100 of Promo credits. For a `.edu` organization, data sharing at tier 2 is a condition of the program: the platform collects the training artifacts of each run.

## Background

National Compute Labs PBC publishes the documentation for its compute platform. This page describes the Public Research pool: eligibility, the node, the request through Marshall, the queue, the lease and billing. The nodes are 8× AMD MI355X 288 GB or 8× NVIDIA B300 288 GB.

## Key claims

- "Public Research is one whole GPU node at a time for an individual researcher, requested from Marshall and used over `ssh`: no cluster to set up, no limit price to pick, no auction to wait on." (Public Research)
- "The organization an eligible `.edu`, `.mil` or `.gov` address receives at sign-in is one; National Compute sets the kind for any other organization by arrangement." (Public Research)
- "Public Research is open to commercial work" (Commercial work)
- "an organization created for a `.edu` address takes part at tier 2 as a condition of the program, so the training artifacts your runs write (checkpoints, logs, configs and datasets, including results copied from the node back to your workspace disk) are collected whatever the project." (Commercial work)
- "Nodes come in two shapes, 8 GPUs each: 8× AMD MI355X 288 GB or 8× NVIDIA B300 288 GB." (The node)
- "A public research organization starts with $100 of Promo credits (the `airdrop` deposit on its ledger), which expire 30 days after sign-up by default" (Asking Marshall)
- "A lease is 4 hours (currently) and is preempted only when someone is waiting." (The lease)
- "A lease bills per GPU-hour, for every GPU in the node, at the rate shown in your Marshall quote" (Billing)

## Evidence and method

Product documentation. It states the rules of the pool. It gives no rate per GPU-hour and no count of nodes or users.

## Limits

The page gives no prices; Marshall quotes them. A node has no multi-node fabric, so jobs larger than one node go to the market. The page does not say how many GPUs the pool holds. The page has no date, and several values carry the word "currently".
