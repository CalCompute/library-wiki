---
title: Azure regions list (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, microsoft, azure, commercial-cloud, regions, california, vendor]
elements: [A]
origin: web
tier: trade
citable: yes
url: https://learn.microsoft.com/en-us/azure/reliability/regions-list
rehost: no
---

# Azure regions list (web)

## Citation

Microsoft. "Azure regions list." Microsoft Learn, Azure reliability documentation, last updated 2026-10-13. https://learn.microsoft.com/en-us/azure/reliability/regions-list. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure regions list.md`.

## Bottom line

- Microsoft lists 60 regions of the Azure public cloud, with each region's paired region, physical location, geography, availability zones and programmatic name.
- West US (`westus`) is the only listed region with its physical location in California. It has no availability zones, and its paired region is East US in Virginia.
- The other United States regions are in Iowa, Virginia, Illinois, Texas, Wyoming, Washington and Phoenix.

## Background

Microsoft sells the Azure cloud. This page of its reliability documentation lists the regions of the Azure public cloud. Microsoft limits access to some regions to customer cases such as disaster recovery. The page points elsewhere for the sovereign cloud regions, Azure Government and Azure in China.

## Key claims

- "This article contains a list of all regions in the Azure public cloud, their paired region status, physical location, geography, and availability zone support." (In this article)
- "West US | N/A | East US | California | United States | westus" (Azure regions list table)
- "West US 2 | 3 | West Central US | Washington | United States | westus2" (Azure regions list table)
- "West US 3 | 3 | East US | Phoenix | United States | westus3" (Azure regions list table)
- "Access to this region is restricted to support specific customer scenarios, such as disaster recovery within a specific geographic area." (Legend)
- "Even when a region provides availability zones, some services might not support them in that region." (Note)

## Evidence and method

Vendor documentation in one table, with tabs by world area. The count of 60 regions is this page's count of the distinct programmatic names in the table. The page also says that Azure "provides the most extensive global footprint of any cloud provider", with no evidence for the claim.

## Limits

- The page gives no data center address, size or power.
- It does not say which VM sizes or services each region offers. The ND H100 v5 prices give one view of that for one size ([Azure retail prices ND96isr H100 v5 (web)](Azure%20retail%20prices%20ND96isr%20H100%20v5%20%28web%29.md)).
- It does not list the Azure Government regions ([Azure Government overview (web)](Azure%20Government%20overview%20%28web%29.md)).
