---
title: AWS EC2 P6 instances (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, gpu, blackwell, b200, gb200, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://aws.amazon.com/ec2/instance-types/p6/
rehost: no
---

# AWS EC2 P6 instances (web)

## Citation

Amazon Web Services (AWS). "Amazon EC2 P6e UltraServers and P6 instances." AWS website, no date. https://aws.amazon.com/ec2/instance-types/p6/. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 P6 instances.md`.

## Bottom line

- AWS describes its P6 instances and P6e UltraServers of Amazon Elastic Compute Cloud (EC2), with NVIDIA Blackwell and Blackwell Ultra GPUs.
- The p6-b200.48xlarge has 8 Blackwell GPUs with 1,432 GB of HBM3e. The p6-b300.48xlarge has 8 Blackwell Ultra GPUs with 2,144 GB.
- The largest UltraServer, u-p6e-gb200x72, has 72 Blackwell GPUs with 13,320 GB of GPU memory. AWS sells it for training and deploying "frontier models at the multi-trillion-parameter scale".

## Background

AWS sells cloud computing. This is its product page for its newest GPU instance family, for AI training and inference. An UltraServer joins several instances in one NVIDIA NVLink domain. The page gives the hardware of each instance and UltraServer type, the claimed benefits and the ways to start. It gives no prices.

## Key claims

- "These UltraServers are ideal for the most compute- and memory-intensive AI workloads, such as training and deploying frontier models at the multi-trillion-parameter scale." (Why Amazon EC2 P6e UltraServers and P6 instances?)
- "With P6e-GB200 UltraServers, customers can access up to 72 Blackwell GPUs within one NVLink domain to use 360 petaflops of FP8 compute (without sparsity) and 13.4 TB of total high- bandwidth memory (HBM3e)." (Benefits)
- "p6-b200.48xlarge | 8 | 1,432 HBM3e | 192 | 2,048 | 8 x 3.84 | 3.2 | 100 | No" (Instance types table: size, Blackwell GPUs, GPU memory in GB, vCPUs, system memory in GiB, storage in TB, network in Tbps, EBS bandwidth in Gbps, in UltraServers)
- "p6-b300.48xlarge | 8 Ultra | 2,144 HBM3e | 192 | 4,096 | 8 x 3.84 | 6.4 | 100 | No" (Instance types table)
- "u-p6e-gb200x72 | 72 | 13,320 | 2,592 | 17,280 | 405 | 28,800 | 1,080 | Yes" (UltraServer types table)
- "P6e UltraServers and P6 instances are deployed in Amazon EC2 UltraClusters, which enable scaling up to tens of thousands of GPUs within a petabit-scale nonblocking network." (Benefits)
- "P6e UltraServers will also be available through NVIDIA NVIDA DGX Cloud, a fully managed environment with NVIDIA’s complete AI software stack." (Using DGX Cloud in AWS)

## Evidence and method

A vendor product page. Its hardware tables are the vendor's specifications. Its comparisons with P5en instances ("over 20x the compute") give no method or test.

## Limits

- The page gives no prices and no list of the AWS Regions that offer each type.
- It gives no count of P6 instances, UltraServers or GPUs that AWS has.
- The page describes P6e-GB300 UltraServers, but its tables list no GB300 type.
- The page gives the total memory of the u-p6e-gb200x72 as "13.4 TB" in its text and as "13,320" GB in its table.
