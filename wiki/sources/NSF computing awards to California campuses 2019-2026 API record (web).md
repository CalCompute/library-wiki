---
title: NSF computing awards to California campuses 2019-2026 API record (web)
type: source
created: 2026-11-19
updated: 2026-11-19
source_count: 1
tags: [A, B, nsf, award-record, campus-cyberinfrastructure, mri, hpc, gpu, uc, csu]
elements: [A, B]
origin: web
tier: primary
citable: yes
url: https://api.nsf.gov/services/v1/awards.json?id=2509729,2408259,2406524,2320846,2215705,2117956,2019144,1919771,2430291,2346744,2346701,2232917,2019220,2019194,1925717,1925558,2503029,2346636,2322420,2126319,2201592&rpp=25
rehost: yes
---

# NSF computing awards to California campuses 2019-2026 API record (web)

## Citation

U.S. National Science Foundation (NSF). Awards 2509729, 2408259, 2406524, 2320846, 2215705, 2117956, 2019144, 1919771, 2430291, 2346744, 2346701, 2232917, 2019220, 2019194, 1925717, 1925558, 2503029, 2346636, 2322420, 2126319 and 2201592. NSF awards application programming interface (API) records, one query, award dates July 15, 2019 to July 29, 2026. https://api.nsf.gov/services/v1/awards.json?id=2509729,2408259,2406524,2320846,2215705,2117956,2019144,1919771,2430291,2346744,2346701,2232917,2019220,2019194,1925717,1925558,2503029,2346636,2322420,2126319,2201592&rpp=25. Copy: [`raw/web/2026-11-19 NSF computing awards to California campuses 2019-2026 API record.md`](../../raw/web/2026-11-19%20NSF%20computing%20awards%20to%20California%20campuses%202019-2026%20API%20record.md) (original: `raw/web/2026-11-19 NSF computing awards to California campuses 2019-2026 API record.json`). Read 2026-11-19.

## Bottom line

- The query returns 21 NSF awards for computing, storage and network equipment at 12 California institutions. All 21 are standard grants, with award dates from July 15, 2019 to July 29, 2026.
- The obligations total $13,394,493. Each award is between $100,000 and $1,000,000. Thirteen are Campus Cyberinfrastructure (CC*) awards, and eight are Major Research Instrumentation (MRI) awards.

## Background

This is one NSF awards API query for 21 award numbers, in JavaScript Object Notation (JSON) format. The response metadata gives `"totalCount":21`. Each record gives the recipient, the principal investigator (PI), the program, the dates, the amounts and an abstract. The recipients are:

- University of California (UC) campuses, 9 awards, $5,352,804: Santa Barbara (3), Merced (2), Riverside (2), Los Angeles (1) and San Diego (1).
- California State University (CSU) campus corporations and foundations, 6 awards, $3,729,779: Northridge (3), San Diego State (2) and San José State (1).
- Private institutions, 6 awards, $4,311,910: University of Southern California (3), California Institute of Technology (1), Claremont McKenna College (1) and Occidental College (1).

Other library pages cover two of the awards: [Chadalapaka NSF award 2346744](Chadalapaka%20NSF%20award%202346744.md) (CENVAL-ARC at UC Merced) and [SDSU TIDE technology (web)](SDSU%20TIDE%20technology%20%28web%29.md) (award 2346701).

## Key claims

- UC Santa Barbara, award 2509729, $900,000, Aug. 1, 2026 to July 31, 2029: "Approximately 80% of the hundreds of users of the machines are students at the undergraduate, graduate or postdoctoral level" (abstract)
- San José State University, award 2430291, $628,773: "This award establishes the SJSU Enterprise HPC Cluster, which features high-end NVIDIA GPU nodes (8 H100 and 8 L40S GPUs) and 400TB of high-performance SSD storage." (abstract)
- San Diego State University, award 2346701, $991,749: "The Technology Infrastructure for Data Exploration (TIDE) creates a pioneering computational core facility within the California State University (CSU) system, focused on machine learning and AI research." (abstract)
- University of Southern California, award 2232917, $999,970: "Educational institutions in Southern California, particularly those focused on undergraduate studies, face challenges in accessing essential high-performance computing (HPC) resources and cyber-infrastructure." (abstract)
- The same award names a "collaboration between USC and the Los Nettos consortium, comprised of 6 member universities and 30 associate networks" and a hub called "the Southern California Research Computing Alliance". (abstract)
- UC San Diego, award 1925558, Triton Stratus, $399,514: "Triton Stratus permits exploration of the emerging hybrid model of on-premise cluster computing resources coupled with commercial cloud computing services" (abstract)
- Claremont McKenna College, award 2408259, $918,485: "This MRI award will enable Claremont McKenna College (CMC) and Harvey Mudd College (CMC) to acquire a high-performance computing (HPC) cluster." (abstract)
- Every abstract ends: "This award reflects NSF's statutory mission and has been deemed worthy of support through evaluation using the Foundation's intellectual merit and broader impacts review criteria." (abstracts)

## Evidence and method

Federal award records from the NSF awards API. They give amounts, dates, programs and the NSF unit that manages each award. The Office of Advanced Cyberinfrastructure (OAC) manages 15 of the awards. Other NSF units manage the other six: Cyber, Physical, and Intelligent Systems (4), the Materials Research Section (1) and the Division of Biological Infrastructure (1). The abstracts are the recipients' plans at the time of the award. They are not reports on results.

## Limits

- The query names its 21 award numbers in its address. The record does not say that these are all of the NSF computing awards to California institutions in the period.
- No award goes to a community college.
- For each award, the estimated total and the obligated amount are the same. The records give no usage data and no allocation rules.
- The Claremont McKenna abstract gives "(CMC)" for Harvey Mudd College, and then "HMC". The quote keeps the record's text.
- The records give the PI's and co-PIs' email addresses. This page does not repeat them.
