---
title: Meta Building GenAI infrastructure 2024-03-12 (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, meta, gpu-clusters, private-compute, data-center]
elements: [A]
origin: web
tier: trade
citable: yes
url: https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/
rehost: no
---

# Meta Building GenAI infrastructure 2024-03-12 (web)

## Citation

Kevin Lee, Adi Gangidi and Mathew Oldham. "Building Meta's GenAI Infrastructure." Engineering at Meta (blog), Meta, March 12, 2024. https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/. Read 2026-11-11.

## Bottom line

- Meta describes two clusters of 24,576 NVIDIA H100 GPUs each, which it uses to train Llama 3. One uses a RoCE Ethernet network and one uses NVIDIA InfiniBand.
- Meta says that by the end of 2024 its infrastructure will include 350,000 NVIDIA H100 GPUs, in a portfolio equal to nearly 600,000 H100s.

## Background

Engineering at Meta is the company's engineering blog. Three Meta engineers wrote this post. It describes the network, compute, storage and software of the two clusters. Meta built them on its Grand Teton GPU platform, which it gave to the Open Compute Project (OCP), and on PyTorch. Its earlier AI Research SuperCluster (RSC) had 16,000 NVIDIA A100 GPUs.

## Key claims

- "Marking a major investment in Meta's AI future, we are announcing two 24k GPU clusters." (Summary)
- "By the end of 2024, we're aiming to continue to grow our infrastructure build-out that will include 350,000 NVIDIA H100 GPUs as part of a portfolio that will feature compute power equivalent to nearly 600,000 H100s." (Summary)
- "At Meta, we handle hundreds of trillions of AI model executions per day." (Under the hood)
- "Both of these solutions interconnect 400 Gbps endpoints." (Network)
- "In the figure we see that small cluster performance (overall communication bandwidth and utilization) reaches 90%+ out of the box, but an unoptimized large cluster performance has very poor utilization, ranging from 10% to 90%." (Performance)
- "We have identified multiple bottlenecks for process group initialization, and reduced the startup time from sometimes hours down to minutes." (Performance)

## Evidence and method

A company engineering blog post. It gives hardware counts, network and storage designs, and one performance chart. It gives no costs, no power figures and no locations for the clusters.

## Limits

The post is Meta's own account of its systems; no outside party checks it. It gives no dollar figures. The GPU target for 2024 is a plan, not a count. The clusters are for Meta's internal use; the post does not describe access for outside researchers, except the Open Innovation AI Research Community partnership program.
