---
title: ABCI usage fees (web)
type: source
created: 2026-11-18
updated: 2026-11-18
source_count: 1
tags: [B, D, japan, aist, abci, national-compute, international, pricing, gpu]
elements: [B, D]
origin: web
tier: primary
citable: yes
url: https://abci.ai/en/how_to_use/tariffs.html
rehost: no
---

# ABCI usage fees (web)

## Citation

AIST Solutions Co. (AISol) and the National Institute of Advanced Industrial Science and Technology (AIST). "ABCI Usage Fees (FY2026)." AI Bridging Cloud Infrastructure (ABCI) website. No date on the page; its revision history gives "Initial Release for FY2026 (2026/04/21)". https://abci.ai/en/how_to_use/tariffs.html. Read 2026-11-18.

## Bottom line

- In fiscal year (FY) 2026, one ABCI point costs 220 yen, tax included. Users buy points in units of 1,000, so the smallest purchase is 220,000 yen.
- A full node with eight graphics processing units (GPUs) costs 16 points an hour in standard use. In Development Acceleration Use, it costs 7.5 points.
- Unused points expire at the end of the fiscal year, and the fee is not refunded. Use is free when AIST and AISol approve free use.

## Background

This page of the ABCI website gives the price list for FY2026. ABCI is the AI computing system that AIST owns and AISol operates ([ABCI about (web)](ABCI%20about%20%28web%29.md)). The Agreement of Use sets the points system and leaves the prices to the AISol website ([ABCI Agreement of Use 2026 Japanese (web)](ABCI%20Agreement%20of%20Use%202026%20Japanese%20%28web%29.md)). The page links to archived price lists for FY2024 and FY2025.

## Key claims

- Point price: "In FY2026, 1 ABCI Point costs 220 yen (tax included). There is no change from the previous fiscal year." (ABCI Point Unit Price)
- Purchase unit: "The point acquisition unit is 1,000 points (220,000 yen (tax included))." (ABCI Point Unit Price)
- Full node, standard use: "rt_HF | 8 GPUs, 96 cores, 1920 GB Memory | 16 points/hour | 576 Points/day （equivalent to 24 points/hour）". (Standard Use, Compute Node (H))
- Single GPU, standard use: "rt_HG | 1 GPU, 8 cores, 160 GB Memory | 3 points/hour". (Standard Use, Compute Node (H))
- Full node, Development Acceleration Use: "rt_HF | 8 GPUs, 96 cores, 1920 GB Memory | 7.5 points/hour | 270 Points/day （equivalent to 11.25 points/hour）". (Development Acceleration Use, Compute Node (H))
- Power cap: "The GPUs in the compute nodes (H) are provided with a power cap of 500 W applied." (Notes)
- Storage: "Home (shared disk) | free of charge（2TB）" and "Group area (shared disk) | 5 points/TB⋅month" in standard use. (Storage)
- Cap on holdings: the point balance of one group "will not exceed 19,000,000 points". (Important Notes)
- Expiry: "Points that are not fully used by **Mar 30 5:00pm (Japan Standard Time)** of the fiscal year in which the application is submitted will expire and cannot be carried over to the following fiscal year." (Important Notes)
- Free use: the fee is free "In cases where free use of ABCI is approved, such as the implementation of a proposal planned by the Institute and AIST Solutions." (Important Notes)

## Evidence and method

This is an official price list from the operator. It gives point costs for three node types in three service modes. "Spot" is for batch jobs, "On-demand" for interactive jobs and "Reserved" for booking by the day. It gives storage prices and the rules for buying, holding and losing points. At 220 yen a point, 16 points gives 3,520 yen for one full node hour. This is the library's arithmetic, not a figure on the page.

## Limits

- The page does not say who qualifies for Development Acceleration Use. It links to a separate page that the library has not read.
- It does not give the cost to AIST or AISol of one node hour, or the subsidy, if any, in the price.
- It does not say how often AIST and AISol approve free use, or for whom.
- After October 1, AISol can cap new points by the points that a group used by September 30. The page does not give the formula.
