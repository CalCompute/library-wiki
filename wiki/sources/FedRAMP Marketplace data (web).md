---
title: FedRAMP Marketplace data (web)
type: source
created: 2026-11-11
updated: 2026-11-20
source_count: 1
tags: [A, D, fedramp, cloud-security, dataset]
elements: [A, D]
origin: web
tier: primary
citable: yes
url: https://raw.githubusercontent.com/FedRAMP/marketplace-fedramp-gov-data/main/data.json
rehost: no
---

# FedRAMP Marketplace data (web)

## Citation

Federal Risk and Authorization Management Program (FedRAMP), U.S. General Services Administration (GSA). "data.json," the data file of the FedRAMP Marketplace, in the GitHub repository FedRAMP/marketplace-fedramp-gov-data. File last changed 2026-11-11 (`"last_change":"2026-11-11T02:27:33.644Z"`). https://raw.githubusercontent.com/FedRAMP/marketplace-fedramp-gov-data/main/data.json. Not rehosted: the library reads it at the publisher's address. Read 2026-11-11.

## Bottom line

- The file is the machine-readable data of the FedRAMP Marketplace, the federal list of cloud services and their FedRAMP status. GSA produces it.
- Its metrics block gives 533 authorized services, 63 "FedRAMP Ready" and 12 "in process". It also has records for 248 agencies and 49 assessors.

## Background

The FedRAMP Marketplace is the public list of cloud services that have a FedRAMP authorization or are on the way to one. This JSON file holds the same data for download. It has seven sections: Metrics, Filters, Products, Agencies, Assessors, AtoMapping and ReuseMapping.

## Key claims

- `"produced_by":"General Services Administration"` (meta)
- `"ready":63,"in_process":12,"total":533` (data.Metrics)
- `"impact_level":"20x Low"` is one of the impact levels in the product records (data.Products). Fourteen records carry it, by the library's count.
- The cloud.gov record: `"name":"18F - 18F Cloud.gov"`, `"status":"FedRAMP Authorized"`, `"auth_date":"2017-02-02T20:00:00.000Z"`, `"auth_type":"JAB"` (data.Products, id F1607067912)
- The same record: `"service_model":["PaaS"],"deployment_model":"Government Community Cloud","impact_level":"Moderate"` (data.Products, id F1607067912)

## Evidence and method

A government dataset. The library counted the product records with a short script. There are 656 product records: 533 "FedRAMP Authorized", 63 "FedRAMP Ready", 48 "Agency In Process" and 12 "FedRAMP In Process". By impact level, 448 records are Moderate, 125 High, 44 LI-SaaS, 14 "20x Low", 14 "20x Moderate" and 11 Low. By deployment model, 370 are Government Community Cloud, 237 Public Cloud and 49 Hybrid Cloud. Software as a service (SaaS) alone is the service model of 559 records.

## Limits

The file is a snapshot. Its counts change when GSA updates it. It has no record for the Sherlock Secure Cloud of the San Diego Supercomputer Center. Sherlock has "FedRAMP Moderate equivalency" ([SDSC Sherlock FedRAMP release 2026-09-21 (web)](SDSC%20Sherlock%20FedRAMP%20release%202026-09-21%20%28web%29.md)). The file gives no prices. Its assessor and product records hold contact names and email addresses; this page does not repeat them.

The Marketplace page of Nov. 19, 2026 uses new terms, "FedRAMP Certified" and Classes A to D, and gives 795 results ([FedRAMP Marketplace products page (web)](FedRAMP%20Marketplace%20products%20page%20%28web%29.md)). For the program rules, see [FedRAMP 20x (web)](FedRAMP%2020x%20%28web%29.md).
