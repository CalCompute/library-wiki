---
title: NVIDIA DGX B200 specifications (web)
type: source
created: 2026-11-09
updated: 2026-11-09
tags: [A, B, gpu, hardware, nvidia, specifications, power]
elements: [A, B]
origin: web
tier: trade
citable: yes
url: https://www.nvidia.com/en-us/data-center/dgx-b200/
rehost: no
---

# NVIDIA DGX B200 specifications (web)

## Citation

NVIDIA. "NVIDIA DGX B200." Product web page with specifications, date not stated. https://www.nvidia.com/en-us/data-center/dgx-b200/. Read 2026-11-09.

## Bottom line

- The DGX B200 is an NVIDIA server with eight Blackwell GPUs, 1,440 GB of GPU memory and a maximum power use of about 14.3 kW. It takes 10 rack units.
- NVIDIA claims 3X the training and 15X the inference performance of the DGX H100.

## Background

NVIDIA makes GPUs and complete AI systems. The DGX B200 is a complete system, not a single GPU. It is the building block of NVIDIA's DGX BasePOD and DGX SuperPOD designs. The page has a specifications table and an FAQ on inference cost per token. It gives no system price.

## Key claims

- "Equipped with eight NVIDIA Blackwell GPUs interconnected with fifth-generation NVIDIA® NVLink™, NVIDIA DGX B200 delivers 3X the training performance and 15X the inference performance of previous-generation systems." (Revolutionary Performance Backed by Evolutionary Innovation)
- "| GPU Memory | 1,440 GB total, 64 TB/s HBM3e bandwidth |" (NVIDIA DGX B200 Specifications).
- "| System Power Usage | ~14.3 kW max |" (NVIDIA DGX B200 Specifications).
- "| Rack Units (RU) | 10 RU |" and "| Enterprise Support | Three-year Enterprise Business-Standard Support |" (NVIDIA DGX B200 Specifications).
- "| Performance | FP4 Tensor Core: 144 PFLOPS | 72 PFLOPS\* FP8 Tensor Core: 72 PFLOPS\*\* |" (NVIDIA DGX B200 Specifications).
- "NVIDIA Blackwell-powered systems deliver AI inference at $0.02 per million tokens on GPT-OSS-120B using NVIDIA TensorRT™-LLM, as verified by SemiAnalysis InferenceX benchmarks (Q1 2026)." (NVIDIA Blackwell FAQs)

## Evidence and method

A vendor's product page. Performance claims are NVIDIA's projections. The page says "Projected performance subject to change." The cost-per-token figure cites a third-party benchmark that the library has not read.

## Limits

- No system price, so no cost per server.
- The power figure is the maximum for one server. It does not include cooling or the rest of the data center.
- The token cost is for one model and one software stack.
