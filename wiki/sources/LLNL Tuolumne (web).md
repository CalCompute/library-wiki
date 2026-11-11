---
title: LLNL Tuolumne (web)
type: source
created: 2026-11-09
updated: 2026-11-09
source_count: 1
tags: [A, D, hardware, supercomputer, national-laboratory, doe, california]
elements: [A, D]
origin: web
tier: institutional
citable: yes
url: https://hpc.llnl.gov/hardware/compute-platforms/tuolumne
rehost: yes
---

# LLNL Tuolumne (web)

## Citation

Lawrence Livermore National Laboratory (LLNL), Livermore Computing. "Tuolumne." Compute platform page, date not stated. https://hpc.llnl.gov/hardware/compute-platforms/tuolumne. Copy: [`raw/web/2026-11-09 LLNL Tuolumne.md`](../../raw/web/2026-11-09%20LLNL%20Tuolumne.md) (original: `.html` beside it). Read 2026-11-09.

## Bottom line

- Tuolumne is an unclassified supercomputer at LLNL in Livermore, California. It has the same architecture as El Capitan.
- It has 1,152 nodes, 4,608 AMD MI300A graphics processing units (GPUs) and a peak of 288.9 petaflops. LLNL commissioned it in 2024.

## Background

Livermore Computing, the computing center of LLNL, publishes this page. It gives the job limits and the hardware of Tuolumne. Lawrence Livermore National Security, LLC operates LLNL for the Department of Energy's National Nuclear Security Administration (NNSA). The page lists the programs that use the system as "ASC, M&IC, Bio".

## Key claims

- "Tuolumne is an unclassified sibling system of El Capitan, sharing the same architecture." (introduction)
- "At greater than 288 petaflops, it not only outstrips its unclassified predecessor Lassen, it also exceeds the speed of LLNL's previous flagship petascale machine, Sierra." (introduction)
- "Tuolumne debuted at #10 on the November 2024 Top500 list of most powerful supercomputers in the world." (introduction)
- "The compute nodes have 96 AMD EPYC cores/node, 4 AMD MI300A gpus/node, and 512 GB memory per node." (Web Version of Tuolumne Job Limits)
- "Each LC platform is a shared resource." (Job Limits)
- Hardware table: "Total Nodes 1,152", "Total GPUs 4,608", "Peak PFLOPS (CPUs+GPUs) 288.900", "Year Commissioned 2024". (hardware table)
- Job limits: pbatch "256/job" nodes and "24 hours"; pdebug "16/user" nodes and "1 hour". (Web Version of Tuolumne Job Limits)

## Evidence and method

A technical page for users of the system. It gives the node counts, the processors, the memory, the peak performance, the scheduler (Flux) and the job limits. It is a page of facts about one machine. It gives no cost, no power use and no count of users.

## Limits

The page does not say who can get an account or how to get an allocation. It names the programs "ASC, M&IC, Bio" but does not explain them. It does not give the cost or the power use of the system. The job-limit text gives 1,144 compute nodes in two partitions. The hardware table gives 1,152 total nodes, a figure that includes the 8 login nodes. [Epoch AI GPU clusters (web)](Epoch%20AI%20GPU%20clusters%20%28web%29.md) lists El Capitan Phase 2 at LLNL, the classified sibling system, but this page gives no figures for El Capitan.
