---
title: Azure NDm A100 v4 series sizes (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, microsoft, azure, commercial-cloud, gpu, a100, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndma100v4-series
rehost: no
---

# Azure NDm A100 v4 series sizes (web)

## Citation

Microsoft. "NDm_A100_v4 sizes series." Microsoft Learn, Azure Virtual Machines documentation, last updated 2026-07-28. https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndma100v4-series. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure NDm A100 v4 series sizes.md`.

## Bottom line

- Microsoft describes the NDm A100 v4 series of Azure virtual machines (VMs). It has one size, Standard_ND96amsr_A100_v4.
- That VM has 8 NVIDIA A100 GPUs with 80 GB each, 96 AMD EPYC vCPUs and 1,900 GiB of memory.
- It is the same design as the ND A100 v4 series, with GPUs of twice the memory ([Azure ND A100 v4 series sizes (web)](Azure%20ND%20A100%20v4%20series%20sizes%20%28web%29.md)).

## Background

Microsoft sells the Azure cloud. This is its documentation page for one GPU VM series, for deep learning training and HPC. It gives the host hardware, the storage and network limits, and the supported features. It gives no prices. The Azure Retail Prices API gives them ([Azure retail prices ND A100 v4 (web)](Azure%20retail%20prices%20ND%20A100%20v4%20%28web%29.md)).

## Key claims

- "The NDm A100 v4 series starts with a single VM and eight NVIDIA Ampere A100 80GB Tensor Core GPUs." (In this article)
- "NDm A100 v4-based deployments can scale up to thousands of GPUs with an 1.6 TB/s of interconnect bandwidth per VM." (In this article)
- "| Memory | 1,900 GiB |" and "| Local Storage | 1 Disk | 6,400 GiB |" (Host specifications)
- "| Accelerators | 8 GPUs | Nvidia A100 GPU (80GB) |" (Host specifications)
- "| Standard\_ND96amsr\_A100\_v4 | 8 | 80 |" (Accelerators table: size, accelerators, accelerator memory in GB)

## Evidence and method

Vendor technical documentation. Its tables are the vendor's specifications. Its claims of scale ("thousands of GPUs") give no count of the GPUs that Azure has.

## Limits

- The page gives no prices and no list of the Azure regions that offer the VM.
- It gives no count of these VMs or GPUs that Azure has.
- The accelerators table gives "80" GB of accelerator memory for the VM. The host table gives 8 GPUs of 80 GB each. For the ND A100 v4 size, the same table gives the total, "320" GB ([Azure ND A100 v4 series sizes (web)](Azure%20ND%20A100%20v4%20series%20sizes%20%28web%29.md)).
