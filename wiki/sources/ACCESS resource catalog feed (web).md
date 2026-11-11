---
title: ACCESS resource catalog feed (web)
type: source
created: 2026-11-10
updated: 2026-11-10
source_count: 1
tags: [A, D, access, nsf, resource-catalog, data-feed]
elements: [A, D]
origin: web
tier: institutional
citable: yes
url: https://operations-api.access-ci.org/wh2/cider/v1/access-active-groups/type/resource-catalog.access-ci.org/
rehost: no
---

# ACCESS resource catalog feed (web)

## Citation

ACCESS (Advanced Cyberinfrastructure Coordination Ecosystem: Services and Support), a program of the U.S. National Science Foundation (NSF). "access-active-groups, type resource-catalog.access-ci.org." JSON data feed of the ACCESS Operations API (CiDeR), date not stated. https://operations-api.access-ci.org/wh2/cider/v1/access-active-groups/type/resource-catalog.access-ci.org/. Read 2026-11-10.

## Bottom line

- The feed lists 26 active resource groups in the ACCESS resource catalog, with 45 resources (34 compute, 7 storage, 4 other) from 21 organizations.
- 12 groups carry the feature "NAIRR Pilot". Three groups are in California: Expanse and Voyager at the San Diego Supercomputer Center (SDSC), and CloudBank in La Jolla.

## Background

ACCESS is the NSF program that allocates national research computing resources. This feed is a machine-readable list from its Operations API. Each group has a name, a description, its resources, its feature tags and its operating organizations. The counts on this page are the library's counts of the records in the feed.

## Key claims

- "Expanse is a dedicated ACCESS cluster designed by Dell and SDSC delivering 5.16 peak petaflops, and will offer Composable Systems and Cloud Bursting." (group "Expanse")
- "Voyager is an innovative AI system designed specifically for science and engineering research at scale." (group "Voyager")
- "CloudBank is a service-based platform that facilitates access to commercial cloud resources through a flexible, multi-cloud infrastructure. It currently provides access to the following commercial cloud platforms Amazon Web Services, Google Cloud, IBM Cloud, and Microsoft Azure." (group "CloudBank")
- "The Prototype National Research Platform (PNRP) is a Category II NSF-funded system integrated into the Nautilus cluster operated jointly by the San Diego Supercomputer Center at UC San Diego, the Massachusetts Green High Performance Computing Center (MGHPCC) and the University of Nebraska–Lincoln (UNL)." (group "PNRP - COMING SOON")
- "Accelerating Computing for Emerging Sciences (ACES) is a NSF-Category II-funded test bed (award number 2112356) that offers state of the art GPUs and other novel accelerators in a composable environment." (group "ACES")
- Feature names in the category "NAIRR Pilot Opportunity": "NAIRR Pilot", "NAIRR Classroom" and "NAIRR Pilot Start-Up". (features list)

## Evidence and method

A structured data feed from the program's own catalog. It gives names, short descriptions, feature tags and the city and state of some organizations. It gives no allocation amounts, no prices and no usage numbers.

Groups with the "NAIRR Pilot" feature: ACES, Voyager, Bridges-2, CloudBank, Jetstream2, Anvil, Expanse, Neocortex, Delta, DeltaAI, FABRIC and Sage. The names of three groups end in "COMING SOON" (PNRP, Kitsune and Nexus). The name of one group ends in "NO NEW ALLOCATIONS" (Derecho).

## Limits

The feed has no date of issue, so it shows the catalog on the day it was read. The organization record for the National Research Platform ("NRP") has no city or state. The feed does not say how ACCESS allocates each resource; the rules are in [ACCESS Allocations policy](ACCESS%20Allocations%20policy.md).
