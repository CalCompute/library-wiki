---
title: Azure retail prices ND A100 v4 (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, microsoft, azure, commercial-cloud, pricing, gpu, a100, california, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://prices.azure.com/api/retail/prices?$filter=(armSkuName%20eq%20%27Standard_ND96asr_v4%27%20or%20armSkuName%20eq%20%27Standard_ND96amsr_A100_v4%27)%20and%20priceType%20eq%20%27Consumption%27
rehost: no
---

# Azure retail prices ND A100 v4 (web)

## Citation

Microsoft. Azure Retail Prices API, query for `(armSkuName eq 'Standard_ND96asr_v4' or armSkuName eq 'Standard_ND96amsr_A100_v4') and priceType eq 'Consumption'`. JavaScript Object Notation (JSON) response, no date. https://prices.azure.com/api/retail/prices?$filter=(armSkuName%20eq%20%27Standard_ND96asr_v4%27%20or%20armSkuName%20eq%20%27Standard_ND96amsr_A100_v4%27)%20and%20priceType%20eq%20%27Consumption%27. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 Azure retail prices ND A100 v4.md`.

## Bottom line

- The response gives 206 hourly retail prices in U.S. dollars of two Azure VMs with 8 A100 GPUs each, in 30 Azure regions.
- In West US, the region in California, the Standard_ND96amsr_A100_v4 (8 A100 GPUs of 80 GB) is $42.601 an hour, Linux pay-as-you-go. In East US, West US 2 and West US 3 it is $32.77.
- The Standard_ND96asr_v4 (8 A100 GPUs of 40 GB) has prices in six regions, and West US is not one of them. In East US and West US 2 it is $27.197 an hour.

## Background

Microsoft publishes Azure list prices through a public Retail Prices API. This query asks for the consumption prices of two VM sizes. Each record gives the region, the meter (standard, Spot or Low Priority) and the product (Linux or Windows). It also gives the price, the unit and the start date of the price. The hardware of the two VMs is on their size pages ([Azure ND A100 v4 series sizes (web)](Azure%20ND%20A100%20v4%20series%20sizes%20%28web%29.md); [Azure NDm A100 v4 series sizes (web)](Azure%20NDm%20A100%20v4%20series%20sizes%20%28web%29.md)). The Azure regions list places West US in California ([Azure regions list (web)](Azure%20regions%20list%20%28web%29.md)).

## Key claims

- `"BillingCurrency": "USD"`, `"CustomerEntityType": "Retail"`, `"Count": 206` (response header)
- `"retailPrice": 42.601`, `"armRegionName": "westus"`, `"location": "US West"`, `"meterName": "ND96amsr A100 v4"`, `"productName": "Virtual Machines NDamsr A100 v4 Series Linux"`, `"unitOfMeasure": "1 Hour"`, `"effectiveStartDate": "2023-09-01T00:00:00Z"` (West US, Linux)
- `"retailPrice": 10.974018`, `"armRegionName": "westus"`, `"meterName": "ND96amsr A100 v4 Spot"`, `"effectiveStartDate": "2026-09-01T00:00:00Z"` (West US, Linux Spot)
- `"retailPrice": 8.52`, `"armRegionName": "westus"`, `"meterName": "ND96amsr A100 v4 Low Priority"` (West US, Linux Low Priority)
- `"retailPrice": 32.77`, `"armRegionName": "eastus"`, `"meterName": "ND96amsr A100 v4"`, `"productName": "Virtual Machines NDamsr A100 v4 Series Linux"` (East US, Linux)
- `"retailPrice": 27.197`, `"armRegionName": "eastus"`, `"meterName": "ND96asr_A100_v4"`, `"productName": "Virtual Machines NDasr A100 v4 Series"`, `"effectiveStartDate": "2021-03-01T00:00:00Z"` (East US, ND96asr_v4)
- `"retailPrice": 65.54`, `"armRegionName": "brazilsouth"`, `"meterName": "ND96amsr A100 v4"` (Brazil South, Linux: the highest Linux pay-as-you-go price of this VM in the response)

## Evidence and method

A machine-readable vendor price record. The prices are retail list prices, before discounts and taxes. Of the 206 records, 174 are for the Standard_ND96amsr_A100_v4, in 29 regions. The other 32 are for the Standard_ND96asr_v4, in 6 regions. In West US, the price of $42.601 an hour for 8 GPUs is $5.33 for each A100 GPU-hour. $32.77 is $4.10, and $27.197 is $3.40. These figures and counts are this page's work, not figures that Microsoft prints.

## Limits

- The response does not say what a Spot or Low Priority meter means or what terms apply to it.
- It gives no reserved or savings plan prices, because the query asks for consumption prices only.
- It gives no capacity or availability in a region.
- For the Standard_ND96asr_v4, the Linux records have a product name with no "Linux" in it. This page reads them as Linux because the Windows records name Windows.
