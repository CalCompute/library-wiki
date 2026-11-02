---
title: UC Davis HPC clusters
type: source
created: 2026-10-28
updated: 2026-10-28
tags: [A, institutional, hpc, uc-davis, gpu-count]
elements: [A]
origin: shared
tier: institutional
citable: yes
url: https://hpc.ucdavis.edu/clusters
rehost: no
---

# UC Davis HPC clusters

## Citation

UC Davis High Performance Computing (HPC) Core Facility. "Clusters." HPC@UCD website, table "as of September 2024", page last updated Aug. 24, 2026. https://hpc.ucdavis.edu/clusters. Read 2026-10-28.

## Bottom line

- UC Davis HPC manages three clusters: Farm, Franklin and Hive. The table gives 21,776 CPU (central processing unit) cores and 139 GPUs (graphics processing units) in total, as of September 2024.
- The text on the same page says "over 48,000 CPU cores, over 200 GPUs". The text and the table do not agree.
- The page says "not all clusters are for general use; many are restricted". It does not say who may use each cluster.

## Background

This page supports that claim: its text and its table give different totals.

This page gives Farm 126 nodes, 13,784 CPU cores and 46 GPUs.

> This page gives Farm 126 nodes, 13,784 CPU cores and 46 GPUs, "as of September 2024" ([UC Davis HPC clusters](UC%20Davis%20HPC%20clusters.md), Clusters table). The inventory marks the row "[CONFLICT]" and may use another UC Davis page. The node count differs by more than a quarter.

## Key claims

- Scale (section "Cluster Resources managed by HPC"): "The current HPC environment consists of over 48,000 CPU cores, over 200 GPUs, and dozens of petabytes in user data storage."
- Access (same section): "Note that not all clusters are for general use; many are restricted."
- Cluster table, "as of September 2024" (same section):

| Cluster | CPU cores | GPUs | Total RAM | Max RAM per node | Nodes | Interconnect | Users (total/active) | Sponsor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Farm | 13,784 | 46 | 124 TB | 2 TB | 126 | 200 Gbps | 726/328 | CAES |
| Franklin | 3,448 | 72 | 13 TB | 1 TB | 16 | 10 Gbps | not given | CBS |
| Hive | 4,544 | 21 | 64 TB | 2 TB | 77 | 200 Gbps | not given | HPC |

- Totals from the table (wiki arithmetic): 21,776 CPU cores, 139 GPUs, 219 nodes.
- Farm has the most users the page reports: 726 in total, 328 active. The page gives no user counts for Franklin or Hive.
- The navigation lists other clusters, HPC2 among them, which the table does not show ("HPC2 Migration to Hive").

## Evidence and method

The facility's own web page. It reports its own hardware. It gives no method and no source for the figures. The table date is September 2024. The page footer says "Last update: August 24, 2026".

## Limits

- The page does not name GPU models. GPU counts alone do not show AI capacity.
- The page does not expand "CAES" or "CBS".
- The page does not say which clusters are restricted, or who may use them. The FAQ and the UCD ServiceHub have that.
- The 48,000-core and 200-GPU figures may count clusters that the table does not list. The page does not say.
