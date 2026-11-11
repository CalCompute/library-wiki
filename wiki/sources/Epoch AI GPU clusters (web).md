---
title: Epoch AI GPU clusters (web)
type: source
created: 2026-11-09
updated: 2026-11-09
tags: [A, B, dataset, gpu-count, epoch-ai]
elements: [A, B]
origin: web
tier: institutional
citable: yes
url: https://epoch.ai/data/gpu_clusters.csv
rehost: no
---

# Epoch AI GPU clusters (web)

## Citation

Epoch AI. "Data on GPU clusters." CSV file, refreshed daily, downloaded 2026-11-09. https://epoch.ai/data/gpu_clusters.csv. Read 2026-11-09.

## Bottom line

- The CSV download of Epoch AI's GPU clusters dataset. On 2026-11-09 it has 482 clusters and 57 columns, with performance in H100 equivalents, chip type, power, cost, owner and sector.
- 119 clusters are in the United States. Eleven rows have a California location. The largest, El Capitan Phase 2 at Lawrence Livermore, has about 44,143 H100 equivalents.

## Background

Epoch AI publishes data and research on AI. This file is the data behind the [Epoch AI GPU clusters](Epoch%20AI%20GPU%20clusters.md) explorer. The [documentation overview](Epoch%20AI%20GPU%20clusters%20documentation%20%28web%29.md) says Epoch AI refreshes the file daily and that it is free to use under the Creative Commons Attribution license.

## Key claims

The quotes are column names and cell values from the file.

- Columns include "H100 equivalents", "Chip type (primary)", "Chip quantity (primary)", "Owner", "Sector", "Power Capacity (MW)", "Hardware Cost", "First Operational Date" and "Location" (header row).
- Largest row: "xAI Colossus Memphis Phase 3", owner "xAI", chip "NVIDIA H100 SXM5 80GB", quantity "200000", H100 equivalents "275795.85649723833", power "352.352" MW, first operational "2025-07-22" (row 1).
- Largest California row: "Lawrence Livermore NL El Capitan Phase 2", owner "US Department of Energy", chip "AMD Instinct MI300A", quantity "44544", H100 equivalents "44143.351592362786", power "35" MW, hardware cost "607324736.6965789", sector "Public" (row 8).
- "Lawrence Berkeley NL NERSC Perlmutter", chip "NVIDIA A100 SXM4 40 GB", quantity "6144", H100 equivalents "2260.147549300599", power "6.9" MW, first operational "2021-05-17" (row 77).
- Sector counts in the file: "Private" 274 rows, "Public" 149 rows, "Public/Private" 50 rows (Sector column).
- Certainty counts: "Confirmed" 401 rows, "Likely" 81 rows (Certainty column).

## Evidence and method

A research dataset. Each row cites up to five sources. Epoch AI estimates some performance, cost and power values from chip counts, as the explorer page says. Every row in this download has status "Existing".

## Limits

- The file changes daily. The counts here are for the download of 2026-11-09.
- Eleven California rows are national laboratory, NVIDIA and Cerebras systems. No University of California or San Diego Supercomputer Center cluster has a row.
- The explorer page says coverage is 10 to 20 percent of world GPU cluster performance.
