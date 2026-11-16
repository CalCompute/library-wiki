---
title: ABCI computing resource (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, japan, aist, abci, national-compute, international, hardware]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://abci.ai/en/about_abci/computing_resource.html
rehost: no
---

# ABCI computing resource (web)

## Citation

National Institute of Advanced Industrial Science and Technology (AIST). "Computing Resource." AI Bridging Cloud Infrastructure (ABCI) website. No date on the page. https://abci.ai/en/about_abci/computing_resource.html. Read 2026-11-11.

## Bottom line

- ABCI 3.0 has 766 compute nodes with a total of 6,128 NVIDIA H200 GPUs, and 75 PB of storage.
- The total theoretical performance is 6.2 AI-EFLOPS at half precision and 425 PFLOPS at double precision.
- ABCI connects to the SINET6 network at 400 Gbps, so users can reach it through the internet.

## Background

This page of the ABCI website describes the hardware of ABCI 3.0, which started in January 2025 ([ABCI about (web)](ABCI%20about%20%28web%29.md)). AIST built ABCI. A separate page describes ABCI 2.0.

## Key claims

- System: "ABCI consists of; 766 Compute Nodes (H) that form in total 6,128 NVIDIA H200 GPU accelerators, the shared file system and object storage that provide in total 75PB capacity, high-speed InfiniBand network connecting the compute nodes and the storage systems, firewall equipments, and etc." (Computing Resource)
- Node: "Compute Node (H) has eight NVIDIA H200 GPU accelerators, two 5th-Generation Intel Xeon Scalable Processors (namely Emerald Rapids), two NVMe SSDs, eight InfiniBand NDR200 (200Gbps each), and one InfiniBand HDR for storage access." (Compute Node (H))
- Performance: "The total theoretical performance of Compute Nodes (H) is 6.2 AI-EFLOPS (half precision) and 425 PFLOPS (double precision)." (Compute Node (H))
- Server: the node table names "HPE Cray XD670 (1 server in 5U)" with "2TB DDR5-4800/5600" memory. (Compute Node (H))
- Storage: the shared file system "has an effective capacity of approximately 73PB". The object storage has "an Amazon Simple Storage Service (Amazon S3) compatible interface and has 1PB of physical capacity available." (Storage Systems)
- Network: "Since ABCI is connected to SINET6 (400Gbps), ABCI users may access ABCI through the internet. The connection is secured by firewalls and two-stage authentication is adopted." (Interconnection Network)

## Evidence and method

This is a technical specification page from the operator. It gives node counts, GPU counts, theoretical performance and storage figures. It gives no measured benchmark results.

## Limits

- The figures are theoretical peak values, not measured results.
- The page gives no cost, power use or usage figures.
- It does not say who can use the system or how. See [ABCI about (web)](ABCI%20about%20%28web%29.md).
