---
title: NERSC Perlmutter architecture (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, hardware, supercomputer, nersc, perlmutter, doe, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://docs.nersc.gov/systems/perlmutter/architecture/
rehost: yes
---

# NERSC Perlmutter architecture (web)

## Citation

National Energy Research Scientific Computing Center (NERSC). "Perlmutter Architecture." NERSC Documentation, date not stated. https://docs.nersc.gov/systems/perlmutter/architecture/. Copy: [`raw/web/2026-11-11 NERSC Perlmutter architecture.md`](../../raw/web/2026-11-11%20NERSC%20Perlmutter%20architecture.md) (original: `.html` beside it). Read 2026-11-11.

## Bottom line

- Perlmutter is an HPE Cray EX supercomputer at NERSC. It "is a heterogeneous system comprised of 3,072 CPU-only and 1,792 GPU-accelerated nodes."
- Each GPU node has four NVIDIA A100 GPUs, which gives 7,168 GPUs in all. The GPU partition has an aggregate peak of 69.5 petaflops FP64 on the GPUs.

## Background

NERSC is a U.S. Department of Energy (DOE) Office of Science user facility at Lawrence Berkeley National Laboratory. This page in the NERSC documentation gives the hardware of Perlmutter: partitions, nodes, interconnect, performance and storage. The name of the system honors the astrophysicist Saul Perlmutter.

## Key claims

- "Perlmutter, based on the HPE Cray Shasta platform, is a heterogeneous system comprised of 3,072 CPU-only and 1,792 GPU-accelerated nodes." (introduction)
- GPU partition: "1536" nodes with "4x NVIDIA A100 (40GB)" and "256" nodes with "4x NVIDIA A100 (80GB)". (System Specifications)
- Aggregate peak FP64: GPU partition CPUs "4.5", GPU partition GPUs "69.5 tensor: 140", CPU partition "15.4" petaflops. (System Performance)
- "The network has a 3-hop dragonfly topology." (Interconnect)
- GPU nodes have "256 GB of DDR4 DRAM". CPU nodes have "512 GB of DDR4 memory total". (Node Specifications)
- "The Perlmutter Scratch File System is an all-flash file system. It has 44 PB of disk space". (Storage)

## Evidence and method

A technical page for users of the system. It gives node counts, processors, GPUs, memory, network and storage. The count of 7,168 GPUs is 1,792 GPU nodes times four GPUs per node, from the page's own table. It is a page of facts about one machine.

## Limits

The page gives no cost, no power use and no date of installation. It does not say who can use the system; [NERSC ERCAP allocation form (web)](NERSC%20ERCAP%20allocation%20form%20%28web%29.md) gives the route.

> ⚠️ Contradiction: the partition peaks on this page add to 89.4 petaflops FP64. [TOP500 Perlmutter system (web)](TOP500%20Perlmutter%20system%20%28web%29.md) gives a "Theoretical Peak (Rpeak)" of "113.00 PFlop/s" and an Rmax of "79.23 PFlop/s".
