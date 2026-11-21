---
title: Azure retail prices ND96isr H100 v5 (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, microsoft, azure, commercial-cloud, pricing, gpu, h100, california, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://prices.azure.com/api/retail/prices?$filter=armSkuName%20eq%20%27Standard_ND96isr_H100_v5%27%20and%20priceType%20eq%20%27Consumption%27
rehost: no
---

# Azure retail prices ND96isr H100 v5 (web)

## Citation

Microsoft. Azure Retail Prices API, query for `armSkuName eq 'Standard_ND96isr_H100_v5' and priceType eq 'Consumption'`. JavaScript Object Notation (JSON) response, no date. https://prices.azure.com/api/retail/prices?$filter=armSkuName%20eq%20%27Standard_ND96isr_H100_v5%27%20and%20priceType%20eq%20%27Consumption%27. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure retail prices ND96isr H100 v5.md`.

## Bottom line

- The response gives 138 hourly retail prices in U.S. dollars of the Standard_ND96isr_H100_v5 VM (8 H100 GPUs), in 24 Azure regions.
- In West US, the region in California, the Linux pay-as-you-go price is $127.816 an hour. The Spot price is $23.620397 and the Low Priority price is $25.563.
- In East US, West US 2 and West US 3, the Linux pay-as-you-go price is $98.32 an hour.

## Background

Microsoft publishes Azure list prices through a public Retail Prices API. This query asks for the consumption prices of one VM size. Each record gives the region, the meter (standard, Spot or Low Priority) and the product (Linux or Windows). It also gives the price, the unit and the start date of the price. The VM's hardware is on its size page ([Azure ND H100 v5 series sizes (web)](Azure%20ND%20H100%20v5%20series%20sizes%20%28web%29.md)). The Azure regions list places West US in California ([Azure regions list (web)](Azure%20regions%20list%20%28web%29.md)).

## Key claims

- `"BillingCurrency": "USD"`, `"CustomerEntityType": "Retail"`, `"Count": 138` (response header)
- `"retailPrice": 127.816`, `"armRegionName": "westus"`, `"location": "US West"`, `"meterName": "ND96isrH100v5"`, `"productName": "Virtual Machines NDsr H100 v5 Series"`, `"unitOfMeasure": "1 Hour"`, `"effectiveStartDate": "2023-12-01T00:00:00Z"` (West US, Linux)
- `"retailPrice": 23.620397`, `"armRegionName": "westus"`, `"meterName": "ND96isrH100v5 Spot"`, `"effectiveStartDate": "2025-10-01T00:00:00Z"` (West US, Linux Spot)
- `"retailPrice": 98.32`, `"armRegionName": "eastus"`, `"meterName": "ND96isrH100v5"` (East US, Linux)
- `"retailPrice": 98.32`, `"armRegionName": "westus2"`, `"effectiveStartDate": "2025-01-01T00:00:00Z"` (West US 2, Linux)
- `"retailPrice": 186.608`, `"armRegionName": "southafricawest"` (South Africa West, Linux: the highest Linux pay-as-you-go price in the response)

## Evidence and method

A machine-readable vendor price record. The prices are retail list prices, before discounts and taxes. $127.816 an hour for 8 GPUs is $15.98 for each H100 GPU-hour in West US. $98.32 is $12.29. These two figures are this page's division, not figures that Microsoft prints.

## Limits

- The response does not say what a Spot or Low Priority meter means or what terms apply to it.
- It gives no reserved or savings plan prices, because the query asks for consumption prices only.
- It gives no capacity or availability in a region.
