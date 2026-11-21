---
title: AWS EC2 G6e instances (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, B, aws, commercial-cloud, gpu, l40s, inference, vendor]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://aws.amazon.com/ec2/instance-types/g6e/
rehost: no
---

# AWS EC2 G6e instances (web)

## Citation

Amazon Web Services (AWS). "Amazon EC2 G6e Instances." AWS website, no date. https://aws.amazon.com/ec2/instance-types/g6e/. Fetched 2026-11-20; read 2026-11-20. Cached copy: `.cache/web/2026-11-20 AWS EC2 G6e instances.md`.

## Bottom line

- AWS describes its G6e family of Amazon Elastic Compute Cloud (EC2) instances, with NVIDIA L40S GPUs. AWS sells them for AI inference and spatial computing.
- Each L40S GPU has 48 GB of memory. The largest size, g6e.48xlarge, has 8 GPUs with 384 GB of GPU memory, 192 vCPUs and 400 Gbps of network bandwidth.
- AWS says that G6e instances can deploy large language models (LLMs) "with up to 13B parameters".

## Background

AWS sells cloud computing. This is its product page for the G6e instance family. It gives the hardware of each of the eight sizes, the claimed benefits, one customer statement and the ways to start. It gives no prices.

## Key claims

- "Amazon EC2 G6e instances powered by NVIDIA L40S Tensor Core GPUs are the most cost-efficient GPU instances for deploying generative AI models and the highest performance GPU instances for spatial computing workloads." (Why Amazon EC2 G6e Instances?)
- "Customers can use G6e instances to deploy large language models (LLMs) with up to 13B parameters and diffusion models for generating images, video, and audio." (Why Amazon EC2 G6e Instances?)
- "This makes them well suited for cost-efficient single-node fine-tuning or training of smaller models." (Benefits, Cost-efficient training for moderately complex AI models)
- "g6e.xlarge | 1 | 48 | 4 | 32 | 250 | Up to 20 | Up to 5" (Product details table: size, GPUs, GPU memory in GB, vCPUs, memory in GiB, storage in GB, network and EBS bandwidth in Gbps)
- "g6e.48xlarge | 8 | 384 | 192 | 1536 | 7600 | 400 | 60" (Product details table)
- "G6e instances offer NVIDIA RTX Enterprise and gaming drivers to customers at no additional cost." (Features, NVIDIA drivers and libraries)

## Evidence and method

A vendor product page. Its hardware table is the vendor's specification. Its comparisons ("up to 2.5x better performance", "saving up to 20% in cost") give no method or test. The one customer statement comes from Leonardo.AI.

## Limits

- The page gives no prices and no list of the AWS Regions that offer each size.
- It gives no count of G6e instances or GPUs that AWS has.
- The page says that the L40S GPU is for inference and smaller models. It does not compare G6e with the P5 or P6 families ([AWS EC2 P5 instances (web)](AWS%20EC2%20P5%20instances%20%28web%29.md); [AWS EC2 P6 instances (web)](AWS%20EC2%20P6%20instances%20%28web%29.md)).
