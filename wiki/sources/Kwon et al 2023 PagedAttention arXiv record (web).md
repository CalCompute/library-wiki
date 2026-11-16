---
title: Kwon et al 2023 PagedAttention arXiv record (web)
type: source
created: 2026-11-11
updated: 2026-11-11
source_count: 1
tags: [A, inference, open-source, vllm]
elements: [A]
origin: web
tier: peer-reviewed
citable: yes
url: https://arxiv.org/abs/2309.06180
rehost: no
---

# Kwon et al 2023 PagedAttention arXiv record (web)

## Citation

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang and Ion Stoica. "Efficient Memory Management for Large Language Model Serving with PagedAttention." arXiv:2309.06180 [cs.LG], submitted Sept. 12, 2023. Comments: "SOSP 2023". https://doi.org/10.48550/arXiv.2309.06180. https://arxiv.org/abs/2309.06180. Read 2026-11-11.

## Bottom line

- The paper presents PagedAttention, an attention algorithm based on virtual memory and paging in operating systems, and vLLM, a serving system built on it.
- The authors say that vLLM gives 2 to 4 times the throughput of FasterTransformer and Orca at the same latency.
- The tests use popular large language models (LLMs). The source code of vLLM is public on GitHub.

## Background

This is the arXiv abstract page of the paper. arXiv lists it under Machine Learning (cs.LG) and Distributed, Parallel, and Cluster Computing (cs.DC). The comments field gives "SOSP 2023", the ACM Symposium on Operating Systems Principles. The record shows a Creative Commons Attribution 4.0 licence for the paper.

## Key claims

- Problem: "existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically." (Abstract)
- Method: "we propose PagedAttention, an attention algorithm inspired by the classical virtual memory and paging techniques in operating systems." (Abstract)
- System: "we build vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests to further reduce memory usage." (Abstract)
- Result: "vLLM improves the throughput of popular LLMs by 2-4$\times$ with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca." (Abstract)
- Scope: "The improvement is more pronounced with longer sequences, larger models, and more complex decoding algorithms." (Abstract)

## Evidence and method

The record gives the abstract only. The abstract reports an evaluation against other serving systems. This page did not read the full paper.

## Limits

- Only the abstract was read. The test set-up, hardware and models are in the full paper.
- The arXiv version is a preprint. The record's comments say "SOSP 2023" but give no page numbers or DOI for the conference version.
- The abstract does not name the authors' institutions. [PyTorch Foundation welcomes vLLM (web)](PyTorch%20Foundation%20welcomes%20vLLM%20%28web%29.md) says that vLLM was "Contributed by the University of California – Berkeley".
