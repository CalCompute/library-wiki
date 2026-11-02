---
title: PEARC 2025 Empire AI model for provisioning AI and HPC
type: source
created: 2026-10-28
updated: 2026-10-28
tags: [A, B, C, D, F, paper, empire-ai, new-york, governance, allocation]
elements: [A, B, C, D, F]
origin: shared
tier: peer-reviewed
citable: yes
url: https://dl.acm.org/doi/10.1145/3708035.3736070
rehost: yes
license: CC BY 4.0
---

# PEARC 2025 Empire AI model for provisioning AI and HPC

## Citation

Stacie Bloom, Joshua Brumberg, Ian Fisk, Robert Harrison, Robert Hull, Melur Ramasubramanian, Krystyn Van Vliet and Jeannette Wing. "Empire AI: A new model for provisioning AI and HPC for academic research in the public good." In *Practice and Experience in Advanced Research Computing (PEARC '25)*, July 20-24, 2025, Columbus, OH. ACM, 4 pages. https://doi.org/10.1145/3708035.3736070. Copy: [`raw/shared/2026-10-28 PEARC 2025 Empire AI model for provisioning AI and HPC.md`](../../raw/shared/2026-10-28%20PEARC%202025%20Empire%20AI%20model%20for%20provisioning%20AI%20and%20HPC.md) (original: `.pdf` beside it). Read 2026-10-28.

## Bottom line

- Empire AI's own leaders describe its model. It is a New York nonprofit with $250M in state capital and $150M from members for ten years of operations (§1). The state required a site at the University at Buffalo (§6).
- Access is for US-resident members only. Empire AI collects proposals centrally, and each member screens and ranks its own (§3.1). Its scheduling moved from a weekly priority rotation to fair-share (§3.1).

## Background

The authors are leaders at the member institutions, Empire AI and the Flatiron Institute. Robert Harrison writes from Empire AI. Jeannette Wing writes from Columbia University. The paper dates from mid-2025, before Beta came online. Later pages update its member list, user counts and schedule.

## Key claims

Governance and legal form:

- "Empire AI Consortium, Inc., is a not-for-profit company incorporated in New York State in July 2024" (§1).
- Members in 2025: CUNY, Columbia, Cornell, NYU, Rensselaer Polytechnic Institute (RPI) and SUNY, "with the Simons Foundation as a close partner" (§1).
- "Empire AI's board of directors includes a member from each institution, and 3 independent and 2 advisory members. The chair is Tom Secunda" (§1).
- Purpose: Empire AI "seeks to address the dominance by large technology companies of the AI ecosystem" (§1).

Funding:

- "In April 2024, the state committed $250M in capital funds that is complemented by $150M of contributions through these academic institutions for operations over the first decade." (§1)
- "Pending approval in the State budget is an additional $90M to bring in 3 new members and provide an additional allocation to SUNY." The authors expect "the final budget being well over $0.5B" (§1).
- The facility "location on the SUNY UB campus was required in the state funding commitment" (§6).
- Three generations of computer over ten years, "each at circa $100M" (§6).
- Alpha "is on loan to Empire AI as a philanthropic gift from the Simons' Foundation" and Flatiron Institute staff operate it (§2).

Hardware:

- Alpha: "13 HGX nodes each with 8 H100 80GB GPUs". It has 2.8 PB DDN flash and 2 PB effective VAST flash, at the UB Center for Computational Research (§2).
- Beta: "An NVIDIA DGX GB200 NVL72 SuperPOD with 288 B200 GPUs". It adds 60 Grace-Grace nodes, 20+ PB VAST, 10+ PB DDN and a 100 Gbit/s link to NYSERNet (§5).
- Alpha "will also be expanded with 6 HGX H200 nodes (48 H200 GPUs)" (§5).
- Facility: "5MW for the first phase of operations, with cost-efficient incremental upgrade to 15MW", on Niagara Falls hydroelectric power (§6).

Access and allocation:

- "Only faculty, staff, postdocs, and students of member institutions who live in the US are allowed to use Empire AI resources, and consortium members approve all projects and teams." (§3.1)
- "Project proposals are centrally collected by Empire AI using a uniform format and process, and then member institutions perform their own screening and prioritization." (§3.1)
- Empire AI supports "only ... unclassified, fundamental research as defined in NSDD-189" (§3.1).
- Demand: "Over 300 proposals were submitted to use Alpha but, due to the limited resource, only 90 projects were started." (§3)
- Scheduling: each institution has its own Slurm partition. At first, each week one institution "would have high priority on 12 of the 13 nodes". Now "we now allocate just six of the nodes in a priority week, with the remaining nodes open to all" (§3.1).
- For Beta, the aim is "equity between institutions through finite project allocations, fair-share and, hopefully minimal, manual priority adjustments" (§3.1).

Operations and support:

- Alpha served "about 250 users and growing" (§4).
- Each member names a technical point of contact and several support "agents". They "meet virtually every two weeks" (§4).

Economic impact:

- HR&A Advisors studied about $196 million in initial investment. It projects "750 job-years, $67 million in labor income, and $155 million in economic output in New York State between 2024 and 2026" (§7).

## Evidence and method

A four-page practice paper in ACM proceedings, written by the program's own leaders. The economic figures come from a preliminary input-output study by a consultant (§7). The authors used Gemini to draft the project categories in §3 and state it was "the only use of generative AI in this paper".

## Limits

- The paper is by Empire AI's own leaders. It gives no independent evaluation.
- Its member list, user counts and dates are mid-2025. Later pages report more members and a later schedule.
- The economic impact is preliminary and counts construction and purchase only (§7).

> ⚠️ Contradiction: the paper says Beta "will start operations in early fall 2025" and Gamma "is expected to start operations by spring 2027" (§5, §6). Columbia says Beta "is scheduled to come online end of May 2026" and the full Gamma system will be operational "in the first half of 2028" ([Columbia Empire AI page](Columbia%20Empire%20AI%20page.md), Timeline). Empire AI says Gamma is "expected to be completed by the end of 2027" ([Empire AI access (web)](Empire%20AI%20access%20%28web%29.md), Background). The schedule slipped. Use the latest date with its source.

> ⚠️ Contradiction: the paper gives the board as one member from each institution, "3 independent and 2 advisory members" (§1). With six members, that is 11 seats. New members joined after the paper. Neither source gives the current seat rule.

> ⚠️ Contradiction: the paper names state capital ($250M) and member contributions ($150M) as the funding base. Philanthropy appears as the loaned Alpha system and Tom Secunda's role (§1, §2). The paper gives no dollar figure for philanthropy.
