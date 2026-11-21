---
title: Berkeley Savio hardware configuration (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, uc-berkeley, savio, campus-compute, hardware, gpu, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/hardware-config/
rehost: no
---

# Berkeley Savio hardware configuration (web)

## Citation

UC Berkeley Research IT. "Hardware Config." Research IT documentation, Berkeley Research Computing (BRC), date not stated. https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/hardware-config/. Read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Berkeley Savio hardware configuration.md`.

## Bottom line

- The page lists every partition of the Savio cluster at UC Berkeley. For each, it gives the node count, CPU model, cores, memory and graphics processing units (GPUs).
- The newest GPU partition has one node with four NVIDIA H200 GPUs. It also has 26 nodes with eight RTX A5000 GPUs and three nodes with eight L40 GPUs.
- The GPU table lists 372 GPUs on 67 nodes, by a count of its rows.

## Background

Berkeley Research Computing runs Savio, the shared high performance computing (HPC) cluster of UC Berkeley. This page is part of the Savio user guide. It has four tables: CPU hardware, GPU hardware, retired hardware, and the Rosalind condo of the Computational Genomics Resource Laboratory (CGRL).

## Key claims

- "Each partition corresponds to a combination of a generation and type of node. All nodes utilize an FDR Infiniband connection." (Savio Hardware Configuration)
- savio4_gpu, one node: "4x H200", "144 GB". 26 nodes: "8x RTX A5000", "24 GB". 3 nodes: "8x L40", "46 GB". (GPU Hardware)
- savio3_gpu: 37 nodes with Tesla V100, 2080Ti, TITAN RTX and A40 GPUs, from "2x Tesla V100" to "8x TITAN RTX" for each node. (GPU Hardware)
- savio4_htc: 224 nodes with Intel Xeon Gold 5520 or 6330 processors, "56" cores and "256 GB" or "512 GB" of memory. (CPU Hardware)
- Retired hardware includes the first-generation "savio" partition, "savio2_gpu" with "4x Nvidia K80" and "savio2_1080ti". (Retired hardware)
- "The CGRL hardware consists of the Rosalind condo within Savio." (CGRL Hardware Configuration)

## Evidence and method

A user guide page of about 1,800 words, most of it tables and site navigation. The tables give node ranges, models and sizes. They give no dates of purchase, no use figures and no costs. The counts of 372 GPUs and 67 GPU nodes are sums of the GPU table, not figures that the page prints.

## Limits

The page does not say which nodes are condo nodes and which are institutional nodes. It does not give peak performance. It does not date the tables.

> ⚠️ Contradiction: this page lists "8x L40" GPUs and a "4x H200" node in savio4_gpu. The system overview says savio4_gpu has "eight nVIDIA A5000 GPUs or eight nVIDIA L40S GPUs", and that savio3_gpu has "A100 GPUs", which this table does not list ([Berkeley Savio system overview (web)](Berkeley%20Savio%20system%20overview%20%28web%29.md)). The condo page gives the H200 node as "8 GPUs" ([Berkeley Savio condo cluster service (web)](Berkeley%20Savio%20condo%20cluster%20service%20%28web%29.md)).

> ⚠️ Contradiction: this page lists 28 savio2_knl nodes and 8 savio2_1080ti nodes. The system overview gives "32 nodes with Intel Knights Landing" and "7 nodes" with 1080Ti cards ([Berkeley Savio system overview (web)](Berkeley%20Savio%20system%20overview%20%28web%29.md)).
