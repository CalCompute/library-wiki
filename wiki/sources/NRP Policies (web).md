---
title: NRP Policies (web)
type: source
created: 2026-10-15
updated: 2026-10-15
tags: [C, D, F, nrp, gpu, fair-use]
elements: [C, D, F]
origin: web
tier: institutional
citable: yes
url: https://nrp.ai/documentation/userdocs/start/policies/
rehost: no
---

# NRP Policies (web)

## Citation

National Research Platform (NRP). "Cluster Policies." NRP Documentation, User Guide, web page, "Last updated: Oct 4, 2026". https://nrp.ai/documentation/userdocs/start/policies/. Read 2026-10-15.

## Bottom line

- NRP enforces efficient use with numbers. A user "can't submit more than 4 pods" that use less than 40 percent of their graphics processing units (GPUs). Admins "will ban namespaces with under-utilized resources requests."
- Time limits free idle resources: interactive pods stop after 6 hours, deployments after 2 weeks. Storage "not accessed for 6 months can be purged without notification".

## Background

NRP runs the Nautilus cluster on Kubernetes. Users work in a "namespace" that a faculty or staff admin owns. See [NRP Getting started (web)](NRP%20Getting%20started%20%28web%29.md).

## Key claims

Summary (section "TL;DR"):

- "Avoid wasting resources: if you've requested something, use it, and free it up once computation is done. Admins monitor resource utilization and will ban namespaces with under-utilized resources requests."
- "Users running a Job with sleep command or equivalent (script ending with "sleep") will be banned from using the cluster."
- "Any storage volume that was not accessed for 6 months can be purged without notification."

AUP: "You need to accept the AUP before using the cluster" (section "Acceptable Use Policy").

Resource allocation (section "Resource allocation"):

- "Your resource limits must be within 20% of the resource requests."
- "Do not waste resources. Namespaces with consistently underutilized requests risk being banned."

Violations (section "Resource usage violations"):

- "A user can not submit more than 4 pods, violating the following conditions: GPU utilization is more than 40% of the requested GPUs. CPU usage is within 20-200% of the requested CPUs. Memory (RAM) usage is within 20-150% of the requested memory."
- "These restrictions do not apply to pods requesting 1 CPU core and 2GB memory."
- "Keep checking the Violations page on the Nautilus portal to see if your pods are violating the usage policies."

Time limits:

- Interactive pods "will be destroyed in 6 hours unless you request an exception". They "are limited to 2 GPUs, 32 GB RAM, and 16 CPU cores." (section "Interactive use (6 hours max runtime)")
- A long-running idle deployment "can not request a GPU." "Deployments are automatically deleted after 2 weeks (unless the namespace is added to the exceptions list and runs a permanent service)." (section "Long-running idle pods")
- "You will receive 3 notifications if your workload is not on the exception list. After that, your workload will be deleted. Any data in persistent volumes will remain." (section "Workloads purging (2 weeks max runtime)")

GPUs (section "Requesting GPUs"):

- "When you request GPUs for your pod, nobody else can use those until you stop your pod. You should only schedule GPUs that you can actually use."
- "The only reason to request more than a single GPU is when your GPU utilization is close to 100% and you can leverage using more GPUs."
- "If you plan on deploying large jobs (>50 GPUs) please present a plan in Nautilus Support."
- "To prevent misuse, the default quota for A100 GPUs is set to zero for all namespaces." Users request access with a form "with the details of your workflow."

Data (section "Data purging"): "NRP resources should not be used as archival storage. You can only store the data actively used for computations."

## Evidence and method

This is an operations rule page. It gives thresholds. It gives no data on how many users NRP bans or warns.

## Limits

- The 40 percent GPU rule reads two ways. The text says a violation is GPU use "more than 40%". The "TL;DR" lists "GPU > 40%" among the "limits". The section "Requesting GPUs" says use must be "above 40%". The intent is that use under 40 percent is a violation, but the words say the opposite.
- The page does not say who decides a ban, how long it lasts, or how to appeal it.
- The page is a live document. It can change ("Last updated: Oct 4, 2026").

> ⚠️ Contradiction: the section "Resource usage violations" lists "GPU utilization is more than 40%" as a violation condition. The section "Requesting GPUs" asks users to "make sure the utilization is above 40%".
