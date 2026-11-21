---
title: Berkeley Lab Lawrencium recharge rates (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, D, lbnl, berkeley-lab, lawrencium, condo-model, recharge, campus-compute, gpu, california]
elements: [A, B, D]
origin: web
tier: institutional
citable: yes
url: https://scienceit-docs.lbl.gov/hpc/
rehost: yes
---

# Berkeley Lab Lawrencium recharge rates (web)

## Citation

Lawrence Berkeley National Laboratory (LBNL), Science IT. "High Performance Computing." Science IT documentation, last changed October 28, 2026. https://scienceit-docs.lbl.gov/hpc/. Copy: [`raw/web/2026-11-20 Berkeley Lab Lawrencium recharge rates.md`](../../raw/web/2026-11-20%20Berkeley%20Lab%20Lawrencium%20recharge%20rates.md) (original: `.html` beside it). Fetched 2026-11-20. Read 2026-11-20.

## Bottom line

- Lawrencium is the platform of the LBNL Condo Cluster Computing (LC3) program, for Berkeley Lab's "midrange computing requirement".
- Condo users run free within their condo contributions. Other users pay the LBNL recharge rate of $0.01 for each Service Unit (SU), and every user account pays $25 a month.
- One GPU-hour costs 56 SUs ($0.56) on the `es2` partition (H100 and H200) and 32 SUs ($0.32) on `es3`.

## Background

LBNL is a national laboratory in Berkeley, California, managed by the University of California for the U.S. Department of Energy (DOE) ([NERSC Doudna announcement 2025-05-29 (web)](NERSC%20Doudna%20announcement%202025-05-29%20%28web%29.md)). Its Science IT group runs Lawrencium in the Berkeley Data Center. This is the main page of its HPC documentation. It gives the storage systems, the recharge model, the rate of each partition and the scheduler rules. The hardware of the GPU partitions is on the Einsteinium page ([Berkeley Lab Einsteinium GPU cluster (web)](Berkeley%20Lab%20Einsteinium%20GPU%20cluster%20%28web%29.md)).

## Key claims

- "**Lawrencium** is the platform for the [LBNL Condo Cluster Computing (LC3)](https://it.lbl.gov/service/scienceit/high-performance-computing/lrc/computing-on-lawrencium/condo-cluster-service/) program, which provides a sustainable way to meet the midrange computing requirement for Berkeley Lab." (High Performance Computing)
- "To achieve this goal, condo users are allowed to run within their condo contributions for free. However normal users who would like to use the Lawrencium cluster are subject to the LBNL recharge rate." (Recharge Model)
- "The current recharge rate is $0.01 per Service Unit (1 cent per service unit, SU). Due to the hardware architecture difference we discount effective recharge rate for older generations of hardware." (Recharge Model)
- "Separately, every user account is charged a $25/month account fee (LRCACT), whether or not jobs are run." (Recharge Model, Compute charges vs. the account fee)
- "One GPU-hour therefore costs 56 SU ($0.56) on `es2` and 32 SU ($0.32) on `es3`." (GPU Partitions Recharge Rates)
- "The usage calculation is based on the resource that is allocated to the job instead of the actual usage of the job." (Usage Calculation)
- "A standard fair-share policy with a decay half life value of 14 days (2 weeks) is enforced. All accounts are given equal shares value of 1." (Scheduler Configuration)

## Evidence and method

Institutional user documentation. The rates are the operator's published recharge rates. The page gives one worked example of a charge: an exclusive `lr5` node for 24 hours costs "$2.88".

## Limits

- The page does not say who can open an account, or what a condo contribution costs.
- It does not say how LBNL set the $0.01 rate, or what costs the rate recovers.
- The PI Computing Allowance (`pc_*`) accounts appear in the scheduler rules, but the page does not say what they give.
