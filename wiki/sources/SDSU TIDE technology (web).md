---
title: SDSU TIDE technology (web)
type: source
created: 2026-11-11
updated: 2026-11-11
tags: [A, D, F, csu, sdsu, tide, nrp, nautilus, cenic]
elements: [A, D, F]
origin: web
tier: institutional
citable: yes
url: https://tide.sdsu.edu/technology/
rehost: no
---

# SDSU TIDE technology (web)

## Citation

San Diego State University (SDSU), TIDE project. "Technology." TIDE: Technology Infrastructure for Data Exploration, web page, no date. NSF Award #2346701. https://tide.sdsu.edu/technology/. Read 2026-11-11. Cached copy: `.cache/web/2026-11-11 SDSU TIDE technology.md`.

## Bottom line

- TIDE (Technology Infrastructure for Data Exploration) adds 18 GPU nodes, 6 CPU nodes and 3 storage nodes to Nautilus. Nautilus is the cluster of the National Research Platform (NRP). The GPU nodes hold 72 GPUs.
- California State University (CSU) users get preferential scheduling on TIDE nodes and sign in to a managed JupyterHub with campus credentials. CENIC gives the network to the 23 CSU campuses.

## Background

SDSU hosts the TIDE project site. The page describes the hardware, the software and the network. It cites National Science Foundation (NSF) award 2346701. The text uses the future tense ("TIDE will add").

## Key claims

Hardware (section "Hardware"):

- "TIDE will focus heavily on graphic processing units keeping the CSU science drivers in mind."
- "17 GPU nodes will contain 4x NVIDIA L40 48GB accelerators, and a single GPU node will host 4x NVIDIA A100 80GB accelerators to add a total of 72 GPUs to Nautilus."
- "The storage nodes will add approximately 240 TB of usable storage available for science driver usage."

Scheduling (section "Nautilus as a Control Plane for TIDE"):

- "CSU users and science drivers will receive preferential scheduling on TIDE nodes and will be able to burst/utilize other CPUs and GPUs as needed."
- "The TIDE nodes will be tainted with a PreferNoSchedule as a restriction for workloads not explicitly tolerated with a TIDE designation to ensure up to 20% of resources are available to other Nautilus users."

Access (section "Software"):

- "In order to facilitate easy access to TIDE resources, a managed JupyterHub instance will provide access to common software container images for many common use cases. CSU users will use their campus credentials to access JupyterHub."

Network (section "Network"):

- "Network connectivity to the 23 CSU campuses is provided by the Corporation for Education Network Initiatives in California (CENIC)."
- "SDSU has implemented an instructional and enterprise Science DMZ architecture to isolate research traffic using 2×10 Gb CENIC CalREN-HPR uplinks."

## Evidence and method

This is a project technology page. It gives the planned hardware, the scheduling rule and the network design. It gives no usage data.

## Limits

- The page uses the future tense. It does not say if the nodes are in service.
- It does not give the cost or the award amount.
- It does not say how a CSU user outside SDSU signs up.
