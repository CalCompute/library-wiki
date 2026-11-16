---
title: Google Sensitive Data Protection overview (web)
type: source
created: 2026-11-11
updated: 2026-11-11
tags: [C, D, google, cloud, data-protection, privacy]
elements: [C, D]
origin: web
tier: trade
citable: yes
url: https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
rehost: no
---

# Google Sensitive Data Protection overview (web)

## Citation

Google Cloud. "Sensitive Data Protection overview." Google Cloud documentation page, last updated Nov. 3, 2026. https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview. Read 2026-11-11.

## Bottom line

- Sensitive Data Protection is a Google Cloud service that finds, classifies and de-identifies sensitive data.
- It has four services: discovery, inspection, de-identification and risk analysis. The Cloud Data Loss Prevention API (DLP API) gives access to them in code.
- Google lists compliance with GDPR, HIPAA and PCI DSS (Payment Card Industry Data Security Standard) as a use case.

## Background

Google Cloud publishes this page in its product documentation. It describes the services of Sensitive Data Protection and when to use them.

## Key claims

- Purpose: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (introduction)
- De-identification for research: "Transform direct and indirect identifiers using pseudonymization, date shifting, or bucketing so research and business intelligence teams can analyze data without exposing plaintext PII." (When to use Sensitive Data Protection)
- Compliance: "Detect and monitor protected health information (PHI) and financial records to satisfy compliance obligations under GDPR, HIPAA, and PCI DSS." (When to use Sensitive Data Protection)
- Methods: "Various transformation methods are available, including masking, redaction, bucketing, date shifting, and tokenization." (Sensitive data de-identification)
- Risk analysis: "The risk analysis service lets you analyze structured BigQuery data to identify and visualize the risk that sensitive information will be revealed (re-identified)." (Risk analysis)
- Storage of results: "The results of content methods and the image.redact method aren't stored in Google Cloud." (Synchronous operations)

## Evidence and method

Vendor documentation. It describes the product. It gives no test results or accuracy figures.

## Limits

- The page does not state prices. It links to a pricing page.
- The page does not say how well de-identification prevents re-identification.
