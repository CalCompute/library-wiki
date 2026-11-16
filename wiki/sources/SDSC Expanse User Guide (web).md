---
title: SDSC Expanse User Guide (web)
type: source
created: 2026-11-12
updated: 2026-11-12
source_count: 1
tags: [A, D, sdsc, access, nairr, california, hardware]
elements: [A, D]
origin: web
tier: institutional
citable: yes
url: https://www.sdsc.edu/support/user_guides/expanse.html
rehost: no
---

# SDSC Expanse User Guide (web)

## Citation

San Diego Supercomputer Center (SDSC), UC San Diego. "Expanse User Guide." Web page, date not stated. https://www.sdsc.edu/support/user_guides/expanse.html. Read 2026-11-12. The library read the Technical Summary, System Access, Job Charging, Expanse AI Resource, Composable Systems and Citations sections. It read the other sections in part.

## Bottom line

- Expanse is a National Science Foundation (NSF) funded cluster at SDSC, UC San Diego, with a peak of 5.16 petaflops. Users get time through ACCESS.
- The guide caps a principal investigator (PI) at "15M core-hours and 75K GPU hours", and a job at 4,096 cores.
- The Expanse AI resource adds 34 servers with four NVIDIA H100 GPUs each. Its time comes through the National Artificial Intelligence Research Resource (NAIRR) Pilot.

## Background

SDSC operates Expanse, which Dell and SDSC designed. This user guide covers hardware, access, charging, job scripts, storage and software. Expanse is on the ACCESS resource list ([ACCESS resource catalog feed (web)](ACCESS%20resource%20catalog%20feed%20%28web%29.md)).

## Key claims

- System: "Expanse is a dedicated Advanced Cyberinfrastructure Coordination Ecosystem: Services and Support (ACCESS) cluster designed by Dell and SDSC delivering 5.16 peak petaflops, and will offer Composable Systems and Cloud Bursting." (Technical Summary)
- Funding and access: "Expanse is an NSF-funded system operated by the San Diego Supercomputer Center at UC San Diego, and is available through the ACCESS program." (Technical Summary)
- Size: "Expanse is organized into 13 SDSC Scalable Compute Units (SSCUs), comprising 728 standard nodes, 54 GPU nodes and 4 large-memory nodes." (Technical Summary)
- Allocation cap: "The maximum allocation for a Principle Investigator on Expanse is 15M core-hours and 75K GPU hours. Limiting the allocation size means that Expanse can support more projects, since the average size of each is smaller." (Resource Allocation Policies)
- Job cap: "The maximum allowable job size on Expanse is 4,096 cores". (Job Scheduling Policies)
- Account route: "To obtain an account, users may submit a proposal through the ACCESS Allocation Request System or request a Trial Account." (System Access)
- Charge unit: "The charge unit for all SDSC machines, including Expanse, is the Service Unit (SU)." One SU is one core for one hour with 2G or less, "or 1 GPU using less than 92G of data for 1 hour". (Job Charging)
- AI resource: "The Expanse AI resource features 34 Dell XE9640 servers, each containing four NVIDIA H100 GPUs, two 36-core Intel Sapphire Road processors, 1 TB of RAM and 6.4 TB of local NVMe storage." (Expanse AI Resource)
- AI allocation: "Time on the nodes is allocated via the NAIRR Pilot Program". (Expanse AI Resource)
- Composable Systems: "All Composable System requests must include a brief justification, specifically describing why a Composable System is required for the project." (Composable Systems)

## Evidence and method

This is technical user documentation. It gives hardware figures, allocation caps and charge rules. It gives no usage data and no cost to users.

## Limits

- The guide does not give a cost in dollars. It does not say if an ACCESS user pays for time.
- It does not give a start date or an end date for Expanse.

> ⚠️ Contradiction: the Technical Summary of this guide gives "54 GPU nodes". The Technical Details table of the same guide gives "Nodes | 52" for GPU nodes, "Total GPU nodes | 52" and "Total V100 GPUs | 208".
