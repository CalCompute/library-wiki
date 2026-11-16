---
title: LLNL El Capitan (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, D, hardware, supercomputer, national-laboratory, doe, california]
elements: [A, D]
origin: web
tier: institutional
citable: yes
url: https://hpc.llnl.gov/hardware/compute-platforms/el-capitan
rehost: yes
---

# LLNL El Capitan (web)

## Citation

Lawrence Livermore National Laboratory (LLNL), Livermore Computing. "El Capitan." Compute platform page, date not stated. https://hpc.llnl.gov/hardware/compute-platforms/el-capitan. Copy: [`raw/web/2026-11-11 LLNL El Capitan.md`](../../raw/web/2026-11-11%20LLNL%20El%20Capitan.md) (original: `.html` beside it). Read 2026-11-11.

## Bottom line

- El Capitan is "the CORAL2 flagship system" at LLNL in Livermore, California. It has 11,520 total nodes, 46,080 AMD MI300A graphics processing units (GPUs) and a peak of 2,889.2 petaflops.
- LLNL commissioned it in 2024. It is in the SCF zone and serves the ASC program. The page says it "currently has limited availability."

## Background

Livermore Computing, the computing center of LLNL, publishes this page. It gives the job limits, queues and hardware of El Capitan. Lawrence Livermore National Security, LLC operates LLNL for the Department of Energy's National Nuclear Security Administration (NNSA). The system vendor is HPE Cray.

## Key claims

- "NOTE This system currently has limited availability." (top of page)
- "El Capitan is the CORAL2 flagship system. There are 16 login nodes, 56 debug nodes, and 11,424 batch nodes." (Web Version of El Capitan Job Limits)
- "The compute nodes have 96 AMD EPYC cores/node, 4 AMD MI300A gpus/node, and 512 GB memory/node." (Web Version of El Capitan Job Limits)
- "Each LC platform is a shared resource." (Job Limits)
- "For batch jobs using more than 4150 nodes, please request an ASC dat via ASC DAT Request form." (plarge and DATs)
- Hardware table: "Zone SCF", "Vendor HPE Cray", "Total Nodes 11,520", "Total GPUs 46,080", "Peak PFLOPS (CPUs+GPUs) 2889.200", "Program ASC", "Year Commissioned 2024". (hardware table)

## Evidence and method

A technical page for users of the system. It gives node counts, processors, memory, peak performance, the scheduler (Flux), queues and job limits. It is a page of facts about one machine. It gives no cost, no power use and no count of users.

## Limits

The page does not say who can get an account. It does not explain "SCF", "ASC" or "DAT". The text and the table differ. The text gives "16 login nodes" and "56 debug nodes". The table gives 32 login nodes and "Debug Nodes 64".

> ⚠️ Contradiction: this page gives a peak of "2889.200" petaflops. [TOP500 El Capitan system (web)](TOP500%20El%20Capitan%20system%20%28web%29.md) gives a "Theoretical Peak (Rpeak)" of "2,821.10 PFlop/s".
