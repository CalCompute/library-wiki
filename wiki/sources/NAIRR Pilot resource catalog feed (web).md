---
title: NAIRR Pilot resource catalog feed (web)
type: source
created: 2026-11-10
updated: 2026-11-10
source_count: 1
tags: [A, D, F, nairr, nsf, resource-catalog, data-feed, industry-partners]
elements: [A, D, F]
origin: web
tier: institutional
citable: yes
url: https://submit-nairr.xras.org/resources.json
rehost: no
---

# NAIRR Pilot resource catalog feed (web)

## Citation

U.S. National Science Foundation (NSF), National Artificial Intelligence Research Resource (NAIRR) Pilot. "resources.json." JSON data feed of the NAIRR Pilot submission system (XRAS), date not stated. https://submit-nairr.xras.org/resources.json. Read 2026-11-10.

## Bottom line

- The feed lists 49 resources that NAIRR Pilot users can request: 25 compute, 13 cloud platform, 10 program and 1 observing facility.
- They come from federal and university centers and from companies, Anthropic, NVIDIA, OpenAI, Groq and SambaNova among them. Five company resources say they are "currently unable to accept additional NAIRR Pilot awards".

## Background

The NAIRR Pilot gives researchers and educators access to compute, models and data from its partners ([NAIRR Pilot resource allocations (web)](NAIRR%20Pilot%20resource%20allocations%20%28web%29.md)). This feed is the machine-readable list of resources in its request system. Each record gives the resource's name, type, organization, units, start and end dates, and a description. The counts on this page are the library's counts of the records.

## Key claims

- "The Anthropic Model API is currently unable to accept additional NAIRR Pilot awards. We are currently working to increase the donated allocation, but in the meantime researchers should consider other resources for their projects." (Anthropic Model API, description)
- "For up to 10 research teams, Anthropic is providing training resources and Claude API credits for Anthropic model access for natural sciences or life sciences research." (Anthropic Model API, description)
- "OpenAI API credits will be allocated in $5K, $25K, $50K, and $100K units." (OpenAI API, description)
- "The Expanse AI resource features 34 Dell XE9640 servers, each containing four NVIDIA H100 GPUs, two 36-core Intel Sapphire Road processors, 1 TB of RAM and 6.4 TB of local NVMe storage." (SDSC Expanse AI Resource, description)
- "Credits will cover GPU hours utilized; VAST storage, Managed Kubernetes and SLURM are offered at no additional cost." (Voltage Park, description)
- "PNRP Classroom offers GPU resources for your students and a Jupyter platform for teaching a class that makes heavy use of AI/ML and." (Prototype National Research Platform (PNRP) Classroom, description)

## Evidence and method

A structured data feed from the program's own request system. The feed measures resources in different units: "GPU Hours", "Core-hours", "SUs", "Node Hours", "Dollars", "Number of Students" and "Yes / No", among others.

The five resources that cannot accept new awards: Groq LPU Inference Engine, Anthropic Model API, NVIDIA DGX Cloud, OpenAI API and SambaCloud. The San Diego Supercomputer Center (SDSC) gives four resources: Expanse CPU, Expanse GPU, Expanse AI Resource and Voyager. CloudBank gives six: Voltage Park, CloudBank Classroom, CloudBank Research, Amazon Web Services, Google Cloud Platform and Microsoft Azure.

## Limits

The feed has no date of issue, so it shows the catalog on the day it was read. It gives no amount of each resource that the pilot holds, and no usage numbers. Some dates are not valid (the Cerebras record starts in "0024-07-01"). Several records end in 2027; for example, the NCSA Delta records end on "2027-08-31".
