---
title: Azure ND A100 v4 series sizes (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, microsoft, azure, commercial-cloud, gpu, a100, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndasra100v4-series
rehost: no
---

# Azure ND A100 v4 series sizes (web)

## Citation

Microsoft. "NDasrA100_v4 sizes series." Microsoft Learn, Azure Virtual Machines documentation, last updated 2026-07-28. https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndasra100v4-series. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure ND A100 v4 series sizes.md`.

## Bottom line

- Microsoft describes the ND A100 v4 series of Azure virtual machines (VMs). It has one size, Standard_ND96asr_v4.
- That VM has 8 NVIDIA A100 GPUs with 40 GB each, 96 AMD EPYC vCPUs and 900 GiB of memory.
- Each GPU has its own 200 GB/s InfiniBand connection. Microsoft says deployments "can scale up to thousands of GPUs".

## Background

Microsoft sells the Azure cloud. This is its documentation page for one GPU VM series, for deep learning training and HPC. It gives the host hardware, the storage and network limits, and the supported features. It gives no prices. The Azure Retail Prices API gives them ([Azure retail prices ND A100 v4 (web)](Azure%20retail%20prices%20ND%20A100%20v4%20%28web%29.md)).

## Key claims

- "The ND A100 v4 series starts with a single VM and eight NVIDIA Ampere A100 40GB Tensor Core GPUs." (In this article)
- "ND A100 v4-based deployments can scale up to thousands of GPUs with an 1.6 TB/s of interconnect bandwidth per VM." (In this article)
- "Each GPU within the VM is provided with its own dedicated, topology-agnostic 200 GB/s NVIDIA Mellanox HDR InfiniBand connection." (In this article)
- "| Memory | 900 GiB |" and "| Accelerators | 8 GPUs | Nvidia A100 GPU (40GB) |" (Host specifications)
- "| Standard\_ND96asr\_v4 | 8 | 320 |" (Accelerators table: size, accelerators, accelerator memory in GB)
- "| [Live Migration](../../maintenance-and-updates#live-migration) | Not Supported |" (Feature support)

## Evidence and method

Vendor technical documentation. Its tables are the vendor's specifications. Its claims of scale ("thousands of GPUs") give no count of the GPUs that Azure has.

## Limits

- The page gives no prices and no list of the Azure regions that offer the VM.
- It gives no count of these VMs or GPUs that Azure has.
- It says that network limits "aren't guaranteed".
