---
title: Berkeley Savio system overview (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, uc-berkeley, savio, campus-compute, hardware, cenic, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://docs-research-it.berkeley.edu/services/high-performance-computing/overview/system-overview/
rehost: no
---

# Berkeley Savio system overview (web)

## Citation

UC Berkeley Research IT. "System Overview." Research IT documentation, Berkeley Research Computing (BRC), date not stated. https://docs-research-it.berkeley.edu/services/high-performance-computing/overview/system-overview/. Read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Berkeley Savio system overview.md`.

## Bottom line

- Savio is the institutional and condo cluster of Berkeley Research Computing at UC Berkeley. It launched in May 2014.
- As of April 2020, it had 600 compute nodes and over 15,300 cores. Its peak was 540 teraFLOPS on CPUs and 1 petaFLOPS on graphics processing units (GPUs).
- The fourth generation, Savio4, began at the end of 2022. A data transfer node connects directly to CENIC through the campus Science DMZ network.

## Background

Berkeley Research Computing runs Savio, the shared high performance computing (HPC) cluster of UC Berkeley. This page describes each generation of compute, the login nodes, storage, the interconnect, data transfer and the system software. It points to a facilities statement for grant proposals, which this library does not hold.

## Key claims

- "As of April 2020, the system consists of 600 compute nodes in various configurations to support a wide diversity of research applications, with a total of over 15,300 cores and a peak performance of 540 teraFLOPS (CPU) and 1 petaFLOPS (GPU), and offers approximately 3.0 Petabytes of high-speed parallel storage." (Summary)
- "Savio4 is the fourth (and current) generation of compute that began at the end of 2022. All Savio4 nodes are scheduled on a per-core basis rather than Savio's traditional per-node scheduling." (Compute)
- "savio4_gpu: nodes with eight nVIDIA A5000 GPUs or eight nVIDIA L40S GPUs." (Compute)
- "Each user is allotted 50 GB of backed up home directory storage on a VAST storage device." (Storage)
- Global Scratch is "a high performance 12 PB Lustre parallel filesystem" that "is NOT backed up". (Storage)
- "High speed data transfers are facilitated by a direct connection to CENIC via UC Berkeley's new Science DMZ network architecture." (Data Transfer)
- "The interconnect for the cluster is a 56Gb/s Mellanox FDR infiniband fabric configured as a two-level fat tree." (Interconnect)

## Evidence and method

A system documentation page of about 2,500 words, most of it site navigation. Its totals are of April 2020. Its notes on each generation give some later dates, for example savio2_1080ti "Retired in summer 2026". It gives no use figures and no costs.

## Limits

The totals of April 2020 come before Savio4. The page gives no current total of nodes, cores or GPUs. It does not give the funding source of the cluster.

> ⚠️ Contradiction: the Summary gives "approximately 3.0 Petabytes of high-speed parallel storage" (as of April 2020). The Storage section of the same page gives "a high performance 12 PB Lustre parallel filesystem".

> ⚠️ Contradiction: this page gives savio4_gpu as A5000 or "L40S" nodes, and savio3_gpu with "A100 GPUs". The hardware table lists "8x L40", a "4x H200" node and no A100 ([Berkeley Savio hardware configuration (web)](Berkeley%20Savio%20hardware%20configuration%20%28web%29.md)).
