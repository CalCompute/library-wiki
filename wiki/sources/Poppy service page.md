---
title: Poppy service page
type: source
created: 2026-10-15
updated: 2026-10-15
tags: [A, B, D, F, G, state-platform, cdt, pricing]
elements: [A, B, D, F, G]
origin: shared
tier: primary
citable: yes
url: https://www.cdt.ca.gov/services/poppy/
rehost: yes
---

# Poppy service page

## Citation

California Department of Technology (CDT). "Poppy: California's Digital Assistant." Service page with rates, request process and terms, publication date unknown. https://www.cdt.ca.gov/services/poppy/. Copy: [`raw/shared/2026-10-14 Poppy service page.md`](../../raw/shared/2026-10-14%20Poppy%20service%20page.md) (original: `.html` beside it), fetched 2026-10-14. Read 2026-10-15.

## Bottom line

- CDT charges state departments for Poppy. Usage above a threshold adds a "2.79% pass through applied to compute costs".
- This is a real state price list for a shared AI service.
- Poppy runs on "State infrastructure (CDT-managed cloud)" but calls commercial models by API. That split matters for (d)(1).

## Background

The page is the CDT service catalog entry for Poppy. It covers features, rates, how to request service, limits and a FAQ. (page sections)

## Key claims

- "Poppy is CDT's secure, GenAI platform, built by state staff for state staff." Inputs "stay in the State's hands". (section "Meet Poppy")
- Trust and security list: "SIMM 140 compliant", "Single Sign On (SSO)", "No model training", "State infrastructure (CDT-managed cloud)", "Encrypted in transit (HTTPS) and at rest", "Cal-Secure aligned". (section "Benefits at a glance")
- Integration uses "familiar standards (including an OpenAI compatible API)". (section "What you can do with Poppy")
- Rates (section "Rates"):
  - Tiers P101 to P107: $7,500, $10,000, $15,000, $20,000, $25,000, $35,000 and $50,000 "Per Department".
  - Pay per user: $8.00 (P108).
  - "Exceeded Capacity - LLM Pass through Fee": "2.79% of excess usage" (P109).
  - A limited free trial (P110).
- "Departments pay a flat monthly rate per authorized user ($8 per user per month)." The committed tier gives "a shared usage pool available to all authorized users within the department". (section "Rates")
- Billing is monthly with no partial-month credits. (section "Subscription Terms")
- A request must be submitted by "the state entity's AIO or department CIO", with a user list they approve. A "dedicated Poppy environment" needs a discovery meeting and a design session. (section "Request service")
- Prohibited data: CJIS, PCI, PHI, PII and FTI. (section "Limitations and responsible use"; FAQ 9)
- "The minimal data required for a query is sent to the LLM via API, but the API provider is contracted not to retain or use this data for model training." (FAQ 3)
- A sample prompt reads: "Show me how to create and save custom prompts in LiteLLM." (FAQ 8)
- References: Executive Order N-12-23 and SIMM 140 (the Statewide Information Management Manual section 140). (section "References")

## Evidence and method

A service catalog page. The rates are CDT's published prices. There is no usage or cost data behind them.

## Limits

- The rate table gives the tiers "Per Department". The text says billing is monthly. The capacity in each tier is not stated.
- The page does not say which model providers are under contract or what CDT pays them.
- The LiteLLM mention suggests the platform uses that open-source gateway. The page does not say so directly.

> ⚠️ Contradiction: FAQ 3 says query data "is sent to the LLM via API". The [Poppy overview](Poppy%20overview.md) says information "never leaves California's trusted environment".
