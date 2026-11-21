---
title: AWS EC2 P4 instances (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, gpu, a100, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://aws.amazon.com/ec2/instance-types/p4/
rehost: no
---

# AWS EC2 P4 instances (web)

## Citation

Amazon Web Services (AWS). "Amazon EC2 P4 Instances." AWS website, no date. https://aws.amazon.com/ec2/instance-types/p4/. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 P4 instances.md`.

## Bottom line

- AWS describes its P4 family of Amazon Elastic Compute Cloud (EC2) GPU instances, with NVIDIA A100 GPUs. It has two sizes.
- The p4d.24xlarge has 8 A100 GPUs with 320 GB of HBM2 memory. The p4de.24xlarge has 8 A100 GPUs with 640 GB of HBM2e memory. Both have 96 vCPUs, 1,152 GiB of memory and 400 Gbps of networking.
- AWS says that P4d instances are also sold as Spot Instances, at "up to a 90% discount from On-Demand prices".

## Background

AWS sells cloud computing. This is its product page for the P4 instance family, for machine learning (ML) training and high performance computing (HPC). It gives the hardware of each size, the claimed benefits and customer statements. It gives no prices. The blog posts that it links have the date Nov. 2, 2020.

## Key claims

- "P4d instances are powered by NVIDIA A100 Tensor Core GPUs and deliver industry-leading high throughput and low-latency networking." (Why Amazon EC2 P4 Instances?)
- "p4d.24xlarge | 96 | 1152 | 8 | 320 GB  HBM2 | 400 ENA and EFA | Yes | 600 GB/s NVSwitch | 8 x 1000 NVMe SSD | 19" (Product details table: size, vCPUs, memory in GiB, A100 GPUs, GPU memory, network, GPUDirect RDMA, GPU peer to peer, storage, EBS bandwidth)
- "p4de.24xlarge | 96 | 1152 | 8 | 640 GB  HBM2e | 400 ENA and EFA | Yes | 600 GB/s NVSwitch | 8 x 1000 NVMe SSD | 19" (Product details table)
- "Unlike on-premises systems, you can access virtually unlimited compute and storage capacity, scale your infrastructure based on business needs, and spin up a multinode ML training job or a tightly coupled distributed HPC application in minutes, without any setup or maintenance costs." (Why Amazon EC2 P4 Instances?)
- "Spot Instances take advantage of unused EC2 instance capacity and can lower your EC2 costs significantly with up to a 90% discount from On-Demand prices." (Benefits, Lower the infrastructure costs for ML training and HPC)
- "P4d instances provide up to 60% lower cost to train ML models, including an average of 2.5x better performance for deep learning models compared to previous-generation P3 and P3dn instances." (Why Amazon EC2 P4 Instances?)

## Evidence and method

A vendor product page. Its hardware table is the vendor's specification. Its performance and cost claims give no method or test. The customer statements come from the vendor's customers, for example Toyota Research Institute, GE Healthcare and Rad AI.

## Limits

- The page gives no prices and no list of the AWS Regions that offer each size.
- It gives no count of P4 instances or GPUs that AWS has.
- The claim of "virtually unlimited compute" is the vendor's. The page gives no capacity figure that supports it.
- The page has no date. Its links and its comparison with P3 instances are from the 2020 launch.
