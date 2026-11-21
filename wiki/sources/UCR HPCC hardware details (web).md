---
title: UCR HPCC hardware details (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, uc-riverside, ucr-hpcc, campus-compute, hardware, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://hpcc.ucr.edu/about/hardware/details/
rehost: no
---

# UCR HPCC hardware details (web)

## Citation

UC Riverside High-Performance Computing Center (HPCC). "Hardware Details." HPCC website, last modified June 1, 2026. https://hpcc.ucr.edu/about/hardware/details/. Read 2026-11-20. Cached copy: `.cache/web/2026-11-20 UCR HPCC hardware details.md`.

## Bottom line

- The UC Riverside (UCR) HPCC cluster has four storage systems, with about 3 PB of production storage and 3 PB of backup storage on GPFS.
- It connects to the campus research network with two redundant 40 Gb/s links, and to the public internet with one 10 Gb/s link. Its InfiniBand interconnect runs at 56, 200 and 400 Gb/s.
- The page lists the two head nodes. It points to an online spreadsheet for the worker nodes.

## Background

The HPCC runs the shared research cluster of UC Riverside. This page gives short lists for storage, network, head nodes and worker nodes. A footer dates its last change to June 1, 2026, with the note "Fix documentation inconsistencies in hardware and job specs".

## Key claims

- "Four enterprise class HPC storage systems" and "Approximately 3 PB production and 3 PB backup storage (total 6 PB or 6,144 TB)". (Storage)
- "2 x 40 Gb/s redundant connections to the campus high performance research network" and "1 x 10 Gb/s connection to the public internet". (Network, Ethernet)
- "56/200/400 Gb/s InfiniBand (FDR/HDR/NDR)". (Network, Interconnect)
- Head nodes "bluejay, skylark" with "256 cores, 512 GB memory", for "submitting jobs to the queuing system". (Head Nodes)
- "For a full list of nodes, please see our Node List sheet. This contains info on all nodes (public and private) that we have." (Worker Nodes)

## Evidence and method

A short facility page of about 400 words, with site navigation. It gives no node or GPU counts of its own. The node list is a Google Sheets document that this library does not hold.

## Limits

The page gives no count of worker nodes, cores or GPUs. It does not give the age or cost of the hardware.

> ⚠️ Contradiction: this page gives "3 PB production and 3 PB backup storage (total 6 PB". The hardware overview gives "6PB GPFS storage" for the parallel data storage system and another "6PB GPFS storage" for the backup system ([UCR HPCC hardware overview (web)](UCR%20HPCC%20hardware%20overview%20%28web%29.md)). The access page gives "~6PB parallel GPFS-based disk space" ([UCR HPCC access and rates (web)](UCR%20HPCC%20access%20and%20rates%20%28web%29.md)).
