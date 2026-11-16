---
title: National Compute Grid paper (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, B, C, national-compute, compute-pooling, compute-market, utilization]
elements: [A, B, C]
origin: web
tier: trade
citable: no
url: https://console.nationalcompute.com/api/checkpoints/public/7e4c8aab-d1df-5b0b-ad97-0d0755a56dde/content
rehost: no
---

# National Compute Grid paper (web)

## Citation

[Authors anonymized]. "The National Compute Grid: Pooled Infrastructure for the Frontier Research Ecosystem." Draft for review, marked "EMBARGOED UNTIL OCTOBER 7, 2026" and anonymized "for Submission to the 2027 Proceedings of MLSys". PDF from National Compute Labs PBC, date not stated. https://console.nationalcompute.com/api/checkpoints/public/7e4c8aab-d1df-5b0b-ad97-0d0755a56dde/content. Read 2026-11-11.

## Bottom line

- The paper says that single-tenant clusters split up frontier AI compute and are idle most of the time. It describes the National Compute Grid, a private network that pools compute across laboratories, clouds and chip types and allocates it by market.
- Members pay in Grid Credits for completed work ("goodput"), not GPU-hours. The paper reports more than $1.1 billion in reservations and a target of 2 gigawatts (GW) of pooled capacity by 2030.

## Background

The paper comes from a coalition that it describes as "frontier laboratories, chip manufacturers, research universities, and investors". The nationalcompute.com home page links to it. It says that members of the founding team built Google's Borg and Quota Marketplace scheduling systems. Section 5 is a request for comment on security and governance rules, with a "Grid Constitution" to follow. Section 6 links the Grid to America's AI Action Plan and the Genesis Mission.

## Key claims

- "Single-tenant clusters in the independent ecosystem frequently exhibit node occupancy below 60%, MFU below 30% and average net FLOPs utilization below 15 percent, while individual teams struggle to forecast capacity needs accurately in advance." (Abstract)
- "We introduce the National Compute Grid, a shared infrastructure network that pools AI compute across laboratories, clouds, and chip architectures and clears it in real time, in the tradition of the interconnected power grid and the Interstate Highway System." (Abstract)
- Members "transact in Grid Credits and pay only for useful completed work (“goodput”) rather than GPU-hours" (Abstract)
- "New entrants, academic groups, and government laboratories are priced out not by the cost of compute but by the cost of committing to compute." (Section 2.2)
- "pooling ten independent laboratories cuts the waste per FLOP by a factor of roughly three, and pooling a hundred by a factor of ten." (Section 3.1)
- "The Grid is a private undertaking, financed and operated by its members, at no cost to the taxpayer." (Section 6)
- "the Grid's founding commitments include compute-credit grants to U.S. government laboratories" (Section 6)
- "The Grid entered invite-only early access in June 2026. In its first ninety days it accumulated more than $1.1B in reservations" (Section 7)

## Evidence and method

A draft systems paper. It gives a statistical model of pooling gains (Equation 1). As evidence, it cites Google's published Quota Marketplace results: a static pool at 75 percent occupancy and a market pool at 93 percent. The utilization figures for independent clusters come from "our members' experience" and are not shown in detail. Section 5 lists open design questions, not final rules.

## Limits

The paper is a draft from the operator of the Grid, with anonymized authors and no peer review yet. It names no member organisations. The Markdown copy mixes the PDF's two columns, so the quotes above follow the PDF's reading order.

> ⚠️ Contradiction: The abstract says "The Grid enters general availability on January 15, 2027". Section 7 says "The Grid Exchange enters general availability on September 15, 2026", and the Conclusion says "The National Compute Grid opens on September 15." The [National Compute home page (web)](National%20Compute%20home%20page%20%28web%29.md) says that the Grid is in "Public Sector Access" and "only available to public access partners during preview".
