---
title: Berkeley Lab Einsteinium GPU cluster (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, D, lbnl, berkeley-lab, lawrencium, einsteinium, gpu, h100, h200, condo-model, recharge, california]
elements: [A, B, D]
origin: web
tier: institutional
citable: yes
url: https://scienceit-docs.lbl.gov/hpc/systems/einsteinium/
rehost: yes
---

# Berkeley Lab Einsteinium GPU cluster (web)

## Citation

Lawrence Berkeley National Laboratory (LBNL), Science IT. "Einsteinium GPU Cluster." Science IT documentation, last changed October 13, 2026. https://scienceit-docs.lbl.gov/hpc/systems/einsteinium/. Copy: [`raw/web/2026-11-20 Berkeley Lab Einsteinium GPU cluster.md`](../../raw/web/2026-11-20%20Berkeley%20Lab%20Einsteinium%20GPU%20cluster.md) (original: `.html` beside it). Fetched 2026-11-20. Read 2026-11-20.

## Bottom line

- Einsteinium is Berkeley Lab's institutional GPU cluster, part of the Lawrencium system. It has four partitions, `es0` to `es3`.
- `es2` has 3 nodes of 8 NVIDIA H200 GPUs and 4 nodes of 8 H100 GPUs, added in 2024 and 2025.
- `es3` has 12 nodes of 4 RTX PRO 6000 Blackwell GPUs, added in 2026. Five of them are condo nodes.
- One GPU-hour costs at least 56 Service Units (SUs) on `es2` and 32 SUs on `es3`. The `es0` partition has no SU charge.

## Background

LBNL is a national laboratory in Berkeley, California, managed by the University of California for the U.S. Department of Energy (DOE) ([NERSC Doudna announcement 2025-05-29 (web)](NERSC%20Doudna%20announcement%202025-05-29%20%28web%29.md)). Its Science IT group runs Lawrencium, the laboratory's condo cluster for midrange computing ([Berkeley Lab Lawrencium recharge rates (web)](Berkeley%20Lab%20Lawrencium%20recharge%20rates%20%28web%29.md)). This page is the user documentation of the GPU part of Lawrencium. It gives the hardware of each partition, the quality of service (QoS) options and sample job scripts.

## Key claims

- "Einsteinium is an institutional GPU cluster that was deployed to meet the growing computational demand for researchers doing machine learning and deep learning." (Einsteinium GPU Cluster)
- "`es3` partition nodes were introduced in 2026 to support growing AI/ML workflow needs. Five of the `es3` nodes are condo nodes." (`es3` Partition)
- "| NVIDIA H200 | 3 | 8x 141 GB | Intel Xeon Platinum 8570 | 112 | 2 TB | NDR |" and "| NVIDIA H100 | 4 | 8x 80 GB | Intel Xeon Platinum 8480+ | 112 | 1 TB | NDR |" (`es2` Partition table: accelerator, nodes, GPUs per node and memory, CPU, cores, RAM, InfiniBand)
- "Together with the [charging factor](../../#gpu-partitions-recharge-rates) of 4.0 for the `es2` partition, this means that each `GPU-hour` on the `es2` partition incurs at least 56 Service Units (SUs)." (`es2` Partition)
- "| `es3_lowprio` | Low priority (available to condo and `ac_` accounts) | Free of charge; jobs can be preempted and requeued when condo owners need their nodes. Not available `pc_` accounts |" (`es3` Partition, QoS table)
- "`es0` is a partition with NVIDIA 2080 TI GPUs that do not incur [Service Unit (SU) charges](../../#gpu-partitions-recharge-rates)." (`es0` Partition)

## Evidence and method

Institutional user documentation. The hardware tables are the operator's own list of its nodes. The charge rules refer to the recharge table on the Lawrencium page.

## Limits

- The page does not give the dollar value of a Service Unit. The Lawrencium page gives it: $0.01 ([Berkeley Lab Lawrencium recharge rates (web)](Berkeley%20Lab%20Lawrencium%20recharge%20rates%20%28web%29.md)).
- It does not say who can get an account, or who paid for the condo nodes.
- The `es1` table lists 1 A100 node, 30 A40 nodes, 1 RTX 8000 node and 15 V100 nodes. The page gives no year for them.
