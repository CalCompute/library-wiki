---
title: AWS EC2 on-demand Linux prices US West N California (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, pricing, gpu, h100, h200, california, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20West%20%28N.%20California%29/Linux/index.json
rehost: no
---

# AWS EC2 on-demand Linux prices US West N California (web)

## Citation

Amazon Web Services (AWS). Amazon EC2 on-demand Linux price file for the US West (N. California) Region. JavaScript Object Notation (JSON) file, publication date 2026-11-20T21:09:08Z in its manifest. https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20West%20%28N.%20California%29/Linux/index.json. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 on-demand Linux prices US West N California.md`.

## Bottom line

- The file gives the on-demand price in U.S. dollars an hour of 703 Linux instance types in the AWS US West (N. California) Region.
- A p5.48xlarge instance with 8 H100 GPUs is $68.80 an hour. A p5en.48xlarge instance with 8 H200 GPUs is $79.12 an hour.
- The only GPU instance families in the file are g3, g4dn, p5 and p5en.

## Background

AWS publishes its prices as JSON files, which its pricing pages load ([AWS EC2 on-demand pricing (web)](AWS%20EC2%20on-demand%20pricing%20%28web%29.md)). This file is for one Region and one operating system. Each record gives the instance type, the price, the vCPUs, the memory, the storage, the network performance and the instance family. The GPU count of each instance type is not in the file. The P5 product page gives it ([AWS EC2 P5 instances (web)](AWS%20EC2%20P5%20instances%20%28web%29.md)).

## Key claims

- `"hawkFilePublicationDate":"2026-11-20T21:09:08Z"`, `"currencyCode":"USD"`, `"source":"ec2-ondemand-without-sec-sel"` (manifest)
- `"price":"68.8000000000"`, `"Location":"US West (N. California)"`, `"Instance Family":"GPU instance"`, `"vCPU":"192"`, `"Instance Type":"p5.48xlarge"`, `"Memory":"2048 GiB"` (record "p5 48xlarge US West N. California Linux")
- `"price":"79.1200000000"`, `"Instance Type":"p5en.48xlarge"` (record "p5en 48xlarge US West N. California Linux")
- `"price":"9.3890000000"`, `"Instance Type":"g4dn.metal"` (record "g4dn metal US West N. California Linux")

## Evidence and method

A machine-readable vendor price file. The prices are list prices for on-demand use, before discounts and taxes. For 8 GPUs, $68.80 an hour is $8.60 for each H100 GPU-hour, and $79.12 is $9.89 for each H200 GPU-hour. These two figures are this page's division, not figures that AWS prints.

## Limits

- The file has no p4d, p5.4xlarge, p5e, p6, g5, g6 or g6e instance. It does not say whether AWS offers them in this Region in another way.
- It gives on-demand prices only, with no Savings Plans, Reserved Instance or Spot prices.
- It gives no capacity or availability.
- The same instance types cost less in the US West (Oregon) Region ([AWS EC2 on-demand Linux prices US West Oregon (web)](AWS%20EC2%20on-demand%20Linux%20prices%20US%20West%20Oregon%20%28web%29.md)).
