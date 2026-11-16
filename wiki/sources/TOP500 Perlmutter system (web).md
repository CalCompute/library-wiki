---
title: TOP500 Perlmutter system (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, hardware, supercomputer, benchmark, top500, nersc, perlmutter, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://top500.org/system/179972/
rehost: no
---

# TOP500 Perlmutter system (web)

## Citation

TOP500. "Perlmutter - HPE Cray EX 235n, AMD EPYC 7763 64C 2.45GHz, NVIDIA A100 SXM4 40 GB, Slingshot-11." System record, date not stated (lists to June 2026). https://top500.org/system/179972/. Read 2026-11-11.

## Bottom line

- TOP500 lists Perlmutter at "DOE/SC/LBNL/NERSC" with a Linpack performance (Rmax) of 79.23 petaflops and a power use of 2,945.00 kilowatts.
- Its rank fell from 5 in 2021 to 34 on the June 2026 list. Its benchmark result has not changed since November 2023.

## Background

TOP500 publishes a list of the most powerful supercomputers twice a year, ranked by the Linpack benchmark. This record gives the system's site, maker, cores, benchmark results, power and its rank on each list. It gives the system address as https://www.nersc.gov/systems/perlmutter/.

## Key claims

- "Site: DOE/SC/LBNL/NERSC", "System URL: https://www.nersc.gov/systems/perlmutter/", "Manufacturer: HPE", "Cores: 888,832", "Installation Year: 2021". (system table)
- "Linpack Performance (Rmax) 79.23 PFlop/s" and "Theoretical Peak (Rpeak) 113.00 PFlop/s". (Performance)
- "Power: 2,945.00 kW". (Power Consumption)
- Rank by list: "06/2026" rank "34"; "11/2025" rank "30"; "11/2023" rank "12"; "06/2021" rank "5". (list history)
- The June 2021 entry gives "706,304" cores and an Rmax of "64.59" petaflops. (list history)

## Evidence and method

A benchmark record. TOP500 reports the results of the Linpack (HPL) and HPCG benchmarks and the measured power. The power figure has "Power Measurement Level: 3". The record gives no cost and no GPU count.

## Limits

The record does not give the number of GPUs or say who can use the system. It does not explain the rise in cores and Rmax between 2021 and 2023.

> ⚠️ Contradiction: this record gives a "Theoretical Peak (Rpeak)" of "113.00 PFlop/s". The partition peaks on [NERSC Perlmutter architecture (web)](NERSC%20Perlmutter%20architecture%20%28web%29.md) add to 89.4 petaflops FP64.
