---
title: Azure ND H100 v5 series sizes (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, microsoft, azure, commercial-cloud, gpu, h100, vendor]
elements: [A]
origin: web
tier: trade
citable: yes
url: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series
rehost: no
---

# Azure ND H100 v5 series sizes (web)

## Citation

Microsoft. "ND-H100-v5 sizes series." Microsoft Learn, Azure documentation, last updated 2026-09-25. https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure ND H100 v5 series sizes.md`.

## Bottom line

- The Azure ND H100 v5 series has one virtual machine (VM) size, Standard_ND96isr_H100_v5. It has 8 NVIDIA H100 GPUs with 80 GB each, 96 vCPUs and 1,900 GiB of memory.
- Each GPU has its own 400 Gbps InfiniBand connection, so each VM has 3.2 Tbps of interconnect bandwidth.
- Microsoft says that deployments can scale to thousands of GPUs.

## Background

Microsoft sells the Azure cloud. This page gives the hardware of the ND H100 v5 VM series. The series is for deep learning training, generative AI and high performance computing (HPC). It gives the host, storage, network and GPU specifications, and the features that the series supports. It gives no price. The prices are in the Azure retail prices record ([Azure retail prices ND96isr H100 v5 (web)](Azure%20retail%20prices%20ND96isr%20H100%20v5%20%28web%29.md)).

## Key claims

- "The ND H100 v5 series starts with a single VM and eight NVIDIA H100 Tensor Core GPUs. ND H100 v5-based deployments can scale up to thousands of GPUs with 3.2 Tbps of interconnect bandwidth per VM." (In this article)
- "Each GPU within the VM is provided with its own dedicated, topology-agnostic 400 Gbps NVIDIA Quantum-2 CX7 InfiniBand connection." (In this article)
- "Accelerators | 8 GPUs | Nvidia H100 GPU (80GB)" (Host specifications)
- "Standard\_ND96isr\_H100\_v5 | 96 | 1,900" (Sizes in series, vCPUs and memory in GiB)
- "Standard\_ND96isr\_H100\_v5 | 1 | 1,024 | 8 | 28" (local storage: temp disks, temp disk GiB, NVMe disks, NVMe TiB)
- "Live Migration | Not Supported" (Feature support)

## Evidence and method

Vendor technical documentation. It gives specifications in tables, with notes on how to read the storage and network figures. It states that network upper limits "aren't guaranteed".

## Limits

- The page gives no price, no list of the regions that offer the size, and no capacity.
- The text gives "96 physical fourth Gen Intel Xeon Scalable processor cores". The host table gives "96 vCPUs".
