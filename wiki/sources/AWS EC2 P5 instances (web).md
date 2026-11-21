---
title: AWS EC2 P5 instances (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, gpu, h100, h200, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://aws.amazon.com/ec2/instance-types/p5/
rehost: no
---

# AWS EC2 P5 instances (web)

## Citation

Amazon Web Services (AWS). "Amazon EC2 P5 instances." AWS website, no date. https://aws.amazon.com/ec2/instance-types/p5/. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 P5 instances.md`.

## Bottom line

- AWS describes its P5 family of Amazon Elastic Compute Cloud (EC2) GPU instances. P5 instances have NVIDIA H100 GPUs, and P5e and P5en instances have NVIDIA H200 GPUs.
- The p5.48xlarge size has 8 H100 GPUs with 640 GB of GPU memory. It has 192 vCPUs, 2 TiB of memory and 3,200 Gbps of network bandwidth.
- AWS says that EC2 UltraClusters connect up to 20,000 H100 or H200 GPUs.

## Background

AWS sells cloud computing. This is its product page for the P5 instance family, for deep learning and high performance computing (HPC). It gives the hardware of each instance size, the claimed benefits, and customer statements. It gives no prices. The AWS price files give them ([AWS EC2 on-demand Linux prices US West N California (web)](AWS%20EC2%20on-demand%20Linux%20prices%20US%20West%20N%20California%20%28web%29.md); [AWS EC2 on-demand Linux prices US West Oregon (web)](AWS%20EC2%20on-demand%20Linux%20prices%20US%20West%20Oregon%20%28web%29.md)).

## Key claims

- "P5 instances provide up to 8 NVIDIA H100 GPUs with a total of up to 640 GB HBM3 GPU memory per instance. P5e and P5en instances provide up to 8 NVIDIA H200 GPUs with a total of up to 1128 GB HBM3e GPU memory per instance." (Features)
- "p5.4xlarge | 16 | 256 GiB | 1 H100 | 80 GB HBM3 | 100 Gbps EFA" (Product details table)
- "p5.48xlarge | 192 | 2 TiB | 8 H100 | 640 GB HBM3 | 3200 Gbps EFA" (Product details table)
- "these instances are deployed in Amazon EC2 UltraClusters that enable scaling up to 20,000 H100 or H200 GPUs interconnected with a petabit-scale nonblocking network." (Why Amazon EC2 P5 instances?)
- "P5, P5e, and P5en instances deliver up to 40% savings on DL training and HPC infrastructure costs compared to previous-generation GPU-based EC2 instances." (Benefits)
- "Each instance also supports up to 30 TB of local NVMe SSD storage for fast access to large datasets." (Features)

## Evidence and method

A vendor product page. Its hardware tables are the vendor's specifications. Its performance and cost claims ("up to 4x", "up to 40%") give no method or test. The customer statements come from the vendor's customers and partners.

## Limits

- The page gives no prices and no list of the AWS Regions that offer each size.
- It gives no count of P5 instances or GPUs that AWS has.
- The customer section says that it gives examples "with Amazon EC2 P4 instances", but some statements are about P5.
