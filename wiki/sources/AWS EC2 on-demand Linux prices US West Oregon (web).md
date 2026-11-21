---
title: AWS EC2 on-demand Linux prices US West Oregon (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, pricing, gpu, h100, h200, b200, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20West%20%28Oregon%29/Linux/index.json
rehost: no
---

# AWS EC2 on-demand Linux prices US West Oregon (web)

## Citation

Amazon Web Services (AWS). Amazon EC2 on-demand Linux price file for the US West (Oregon) Region. JavaScript Object Notation (JSON) file, publication date 2026-11-20T21:09:08Z in its manifest. https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20West%20%28Oregon%29/Linux/index.json. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 on-demand Linux prices US West Oregon.md`.

## Bottom line

- The file gives the on-demand price in U.S. dollars an hour of 1,333 Linux instance types in the AWS US West (Oregon) Region.
- A p5.48xlarge instance with 8 H100 GPUs is $55.04 an hour, and a p5.4xlarge instance with 1 H100 GPU is $6.88 an hour.
- The file also gives p5e and p5en (H200) at $63.296, p6-b200.48xlarge at $113.9328 and p6-b300.48xlarge at $142.416 an hour.

## Background

AWS publishes its prices as JSON files, which its pricing pages load ([AWS EC2 on-demand pricing (web)](AWS%20EC2%20on-demand%20pricing%20%28web%29.md)). This file is for one Region and one operating system. Each record gives the instance type, the price, the vCPUs, the memory, the storage, the network performance and the instance family. The GPU count of each instance type is not in the file. The P5 product page gives it for P5, P5e and P5en ([AWS EC2 P5 instances (web)](AWS%20EC2%20P5%20instances%20%28web%29.md)).

## Key claims

- `"hawkFilePublicationDate":"2026-11-20T21:09:08Z"`, `"currencyCode":"USD"` (manifest)
- `"price":"55.0400000000"`, `"Location":"US West (Oregon)"`, `"Instance Type":"p5.48xlarge"` (record "p5 48xlarge US West Oregon Linux")
- `"price":"6.8800000000"`, `"Instance Type":"p5.4xlarge"` (record "p5 4xlarge US West Oregon Linux")
- `"price":"63.2960000000"`, `"Instance Type":"p5en.48xlarge"` (record "p5en 48xlarge US West Oregon Linux")
- `"price":"113.9328000000"`, `"Instance Type":"p6-b200.48xlarge"` (record "p6-b200 48xlarge US West Oregon Linux")
- `"price":"21.9576400000"`, `"Instance Type":"p4d.24xlarge"` (record "p4d 24xlarge US West Oregon Linux")

## Evidence and method

A machine-readable vendor price file. The prices are list prices for on-demand use, before discounts and taxes. The p5.48xlarge price divided by its 8 GPUs is $6.88 for each H100 GPU-hour, the same as the one-GPU p5.4xlarge. This division is this page's, not a figure that AWS prints.

## Limits

- The Oregon Region is not in California. This library holds the California Region file too ([AWS EC2 on-demand Linux prices US West N California (web)](AWS%20EC2%20on-demand%20Linux%20prices%20US%20West%20N%20California%20%28web%29.md)). There, p5.48xlarge is $68.80 an hour.
- The file gives no GPU count or GPU model for p6 instances.
- It gives on-demand prices only, with no Savings Plans, Reserved Instance or Spot prices, and no capacity.
