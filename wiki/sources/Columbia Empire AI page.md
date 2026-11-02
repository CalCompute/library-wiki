---
title: Columbia Empire AI page
type: source
created: 2026-10-28
updated: 2026-10-28
tags: [B, C, D, A, empire-ai, new-york, allocation, service-units, pricing]
elements: [A, B, C, D]
origin: shared
tier: institutional
citable: yes
url: https://www.cuit.columbia.edu/empire-ai
rehost: no
---

# Columbia Empire AI page

## Citation

Columbia University Information Technology (CUIT). "Empire AI." Research services page, publication date unknown (it reports events to September 2026). https://www.cuit.columbia.edu/empire-ai. Read 2026-10-28.

## Bottom line

- Empire AI gives each member institution 700,000 Service Units (SUs) a year, out of 6.3 million SUs from Alpha and Beta. One Alpha GPU hour is 1 SU (Institutional Allocation & Service Units).
- One SU costs $0.50.
- Users who go over an allocation pay nothing more. They drop to free, low-priority, preemptible queues (FAQ).

## Background

Columbia is a founding member of Empire AI, New York's state AI computing consortium. This page is Columbia's guide for its own researchers. It updates the 2025 paper on hardware and dates ([PEARC 2025 Empire AI model for provisioning AI and HPC](PEARC%202025%20Empire%20AI%20model%20for%20provisioning%20AI%20and%20HPC.md)). Cornell's call gives the same SU price ([Empire AI access (web)](Empire%20AI%20access%20%28web%29.md)).

## Key claims

Allocation and cost:

- "Alpha and Beta will deliver 6.3M SUs per year with each institutional allocation at 700,000 SUs per year. Each approved project is allowed to request an initial allocation of up to 2,000 SUs." (Institutional Allocation & Service Units)
- Rates: "1 Alpha GPU hour = 1 SU", "1 Beta GPU hour = 2 SU", "1 Grace-Grace node hour = 0.5 SU", "1 TB.month = 8.333 SU up to 100 TB". Priority queues cost 2x. Shared resources cost 0.5x. (Institutional Allocation & Service Units)
- "For Empire AI, 1 SU will equate to $0.50. For Columbia users, the University will be subsidizing 50% of the cost, therefore $0.25/SU." Schools and departments can add subsidies.
- "Institutions and projects will not be charged for more than their allocation." Over-allocation users get "free, low-priority, preemptible queues". (FAQ, If I go over)
- Users buy more SUs through Columbia's iLab system with a university chartstring. (FAQ, iLab request)

Access rules:

- "Only those who hold a full-time appointment in a PI-eligible position at Columbia University may submit project proposals for Empire AI." (Eligibility)
- "Empire AI is not currently certified to hold/process sensitive data (RHI, PII, PHI-related clinical data)." (Data Compliance)
- HIPAA: there are "plans to handle sensitive data and anticipate compliance by late 2026/early 2027 for a subset of the system". (FAQ)
- Columbia runs monthly user sessions from September 2026. (page notice)

Hardware and use:

- Alpha "was recently upgraded to Alpha++ over Fall 2025, with now 24 HGX nodes": 18 nodes of 8 H100 GPUs and 6 nodes of 8 H200 GPUs. (Alpha Hardware Specifications)
- Beta: "4 racks NVL72 with 288 B200 GPUs for AI Applications" and "60 Grace-Grace Superchip nodes", with about 10 PB DDN and 20 PB VAST storage. (Beta Hardware Specifications)
- "There are currently over 120 active projects and 320 users across all the institutions on Empire AI." (Alpha Hardware Specifications)

Timeline and policy:

- "The Beta system is scheduled to come online end of May 2026". The Gamma facility "is expected to open in Mid-late 2027, with the full Gamma system becoming operational in the first half of 2028". (Timeline)
- Executive Order No. 62 of July 14, 2026 pauses state permits for new hyperscale data centers. "Empire AI is exempt from this Order". (Executive Order 62 notice)

## Evidence and method

A member university's own service page for its researchers. The SU rates and the $0.50 price are Empire AI figures, as Columbia reports them. The subsidy is Columbia's own policy.

## Limits

- The page does not say who set the 700,000 SU share, or whether all members pay the same.
- Some text is out of date.
- It does not say how Columbia ranks proposals within its share.
- 6.3M divided by 700,000 is nine shares. The page does not name the nine institutions.

> ⚠️ Contradiction: this page gives each institution an equal "700,000 SUs per year" (Institutional Allocation & Service Units).

> ⚠️ Contradiction: this page says Alpha++ has 24 HGX nodes, with 18 H100 nodes (Alpha Hardware Specifications). The 2025 paper gives 13 H100 nodes plus 6 planned H200 nodes, 19 in all ([PEARC 2025 Empire AI model for provisioning AI and HPC](PEARC%202025%20Empire%20AI%20model%20for%20provisioning%20AI%20and%20HPC.md), §2, §5). Five more H100 nodes appear here. The upgrade likely added them, but neither source says so.

> ⚠️ Contradiction: this page gives Beta online at "end of May 2026" and Gamma operational "in the first half of 2028" (Timeline). The 2025 paper gives Beta in "early fall 2025" and Gamma "by spring 2027" ([PEARC 2025 Empire AI model for provisioning AI and HPC](PEARC%202025%20Empire%20AI%20model%20for%20provisioning%20AI%20and%20HPC.md), §5, §6).
