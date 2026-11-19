---
title: OpenRouter State of AI 100 Trillion Token Study (web)
type: source
created: 2026-11-19
updated: 2026-11-19
source_count: 1
tags: [A, B, D, inference, open-weight, usage, pricing]
elements: [A, B, D]
origin: web
tier: trade
citable: yes
url: https://arxiv.org/pdf/2601.10088
rehost: no
---

# OpenRouter State of AI 100 Trillion Token Study (web)

## Citation

Malika Aubakirova, Alex Atallah, Chris Clark, Justin Summerville and Anjney Midha. "State of AI: An Empirical 100 Trillion Token Study with OpenRouter." OpenRouter Inc. and a16z (Andreessen Horowitz). arXiv:2601.10088 [cs.AI], submitted Jan. 15, 2026; the PDF gives December 2025. https://arxiv.org/abs/2601.10088. PDF: https://arxiv.org/pdf/2601.10088. Read 2026-11-19.

## Bottom line

- The paper analyses metadata for more than 100 trillion tokens of large language model (LLM) requests on OpenRouter.
- OpenRouter is a commercial service that sends each request to the model that the user selects.
- By late 2025, open-weight models served about one-third of tokens, and reasoning models served more than half.
- Programming grew from about 11 percent to more than 50 percent of tokens in 2025.
- It finds that demand is "relatively price-inelastic". Its data come from one platform only.

## Background

OpenRouter Inc. runs an inference platform that connects users to "hundreds of large language models". The lead author is at a16z (Andreessen Horowitz), a venture capital firm, and the other authors are at OpenRouter. The paper is a preprint on arXiv under arXiv's non-exclusive distribution licence. It is not peer reviewed. The library records it with tier "trade" because a company reports data from its own platform.

## Key claims

- Data: "The dataset used in this study consists of anonymized request-level metadata for billions of prompt–completion pairs from a global user base, spanning approximately two years up to the time of writing." (Section 2.1, p. 2)
- No text: "Crucially, we did not have access to the underlying text of prompts or completions." (Section 2.1, p. 2)
- Platform: "As of 2025, OpenRouter supports more than 300+ active models from over 60 providers and serves millions of developers and end-users, with over 50% of usage originating outside the United States." (Section 2.1, p. 3)
- Task labels: "OpenRouter performs internal categorization on a random sample comprising approximately 0.25% of all prompts and responses through a non-proprietary module GoogleTagClassifier." (Section 2.2, p. 3)
- Open-weight share: "While proprietary models, especially those from major North American providers, still serve the majority of tokens, OSS models have grown steadily, reaching approximately one-third of usage by late 2025." (Section 3, p. 5)
- Chinese open-weight models: "Over the one-year window, they averaged approximately 13.0% of weekly token volume, with strong growth concentrated in the second half of 2025." (Section 3, p. 5)
- Self-hosted models: "Small models are precisely the ones most commonly self-hosted, which means a meaningful portion of their real usage is invisible to any centralized API provider." (Section 3.2, p. 10)
- Reasoning models: "What was effectively a negligible slice of usage in early Q1 now exceeds fifty percent." (Section 4.1, p. 13)
- Request size: "Average prompt tokens per request have increased roughly fourfold from around 1.5K to over 6K while completions have nearly tripled from about 150 to 400 tokens." (Section 4.3, p. 15)
- Programming: "programming queries accounted for roughly 11% of total token volume in early 2025 and exceeded 50% in recent weeks." (Section 5.1, p. 18)
- Regions: "In the earliest weeks of the dataset, Asia represented roughly thirteen percent of global spend. Over time, this share more than doubled, reaching approximately 31% in the most recent period." (Section 6.1, p. 25)
- Cost: "The chart is bisected by a vertical line at the median cost of $0.73 per 1M tokens" (Section 8.1, p. 28)
- Price and demand: "The trendline is nearly flat, indicating that demand is relatively price-inelastic; a 10% decrease in price corresponds to only about a 0.5–0.7% increase in usage." (Section 8.2, p. 30)
- Scope: "This study reflects patterns observed on a single platform, namely OpenRouter, and over a finite time window, offering only a partial view of the broader ecosystem." (Section 10, p. 34)

## Evidence and method

The paper is an observational study of request metadata on one platform. Most model and price analyses cover Nov. 3, 2024, to Nov. 30, 2025. The task categories start in May 2025. A classifier labels a sample of about 0.25 percent of prompts, from users who opt in. The paper places users in regions by the billing location of each account.

The paper gives figures and tables of token shares, costs per million tokens and user retention by monthly cohort.

## Limits

- The data come from one commercial platform. The paper says that enterprise use, "locally hosted deployments, or closed internal systems" are outside its data (Section 10, p. 34).
- The authors work for OpenRouter and for a venture capital firm. The paper does not state the funding of the study or the authors' interests in the companies whose models it ranks.
- The paper is not peer reviewed. The PDF text gives December 2025, and arXiv gives Jan. 15, 2026.
- The costs are effective costs on OpenRouter after caching, not list prices. They exclude requests where users bring their own provider keys (Section 8.1, p. 28).
- The paper does not discuss public or research computing, California, or government use.
