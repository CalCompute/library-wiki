---
title: FedRAMP Marketplace products page (web)
type: source
created: 2026-11-20
updated: 2026-11-20
source_count: 1
tags: [A, D, fedramp, cloud-security, marketplace]
elements: [A, D]
origin: web
tier: primary
citable: yes
url: https://www.fedramp.gov/marketplace/
rehost: yes
---

# FedRAMP Marketplace products page (web)

## Citation

Federal Risk and Authorization Management Program (FedRAMP), U.S. General Services Administration (GSA). "FedRAMP Marketplace," the products page of FedRAMP.gov. Marketplace data last updated Nov. 19, 2026, 21:06:31 Pacific Standard Time. https://www.fedramp.gov/marketplace/. Fetched 2026-11-20; read 2026-11-20. Rehosted: `raw/web/2026-11-20 FedRAMP Marketplace products page.html`, with its Markdown copy `raw/web/2026-11-20 FedRAMP Marketplace products page.md`.

## Bottom line

- The page is the public list of cloud services in the FedRAMP Marketplace. It gives 795 results, with counts by certification status, business category, class, service model and deployment model.
- A notice on the page renames "FedRAMP Authorization" to "FedRAMP Certification". Classes A to D replace the Low, Moderate and High impact levels. The old levels go away in January 2027.

## Background

FedRAMP is the federal program for the security of cloud services that agencies use, and GSA runs it. The Marketplace page lists each service with its status and class. The list itself loads in the browser. The Markdown copy has the filter counts and the notice; the product records are in the page's script data in the original HTML file.

## Key claims

- "Effective immediately, "FedRAMP Authorization" is now called "FedRAMP Certification," and Impact Levels have been replaced with Classes A-D for package specifications." (FedRAMP Terminology Update notice)
- "FedRAMP will provide previous Impact Levels in parentheses after classes until December 31, 2026 to help stakeholders transition to the new terminology. Beginning in January 2027, "Low", "Moderate", and "High" Impact Levels will be removed and full transition to the class structure will take effect." (FedRAMP Terminology Update notice)
- "All Items (795 results)" (results header)
- Certification Status filter: "Legacy FedRAMP Ready (51)", "Initial Implementation (132)", "FedRAMP Certified (561)", "Agency Auth In Process (36)", "FedRAMP In Process (15)". (Filter & Sort)
- Cert Class filter: "Class A (Pilot) (12)", "Class B (LI-SaaS) (42)", "Class B (Low) (23)", "Class C (Moderate) (462)", "Class D (High) (128)". (Filter & Sort)
- Service Model filter: "SaaS (759)", "PaaS (83)", "IaaS (26)". Deployment Model filter: "Public Cloud (323)", "Government Community Cloud (384)", "Hybrid Cloud (53)". (Filter & Sort)
- Business Categories filter: "Artificial Intelligence (AI) (98)" and "Research (87)". (Filter & Sort)
- "Marketplace data last updated: Thu Nov 19 2026 21:06:31 GMT-0800 (Pacific Standard Time)" (below the results)

The script data in the original HTML file gives these records, among others. Each has the status "FedRAMP Certified" and the certification type "Rev5":

- `cso="AWS GovCloud"`: Amazon Web Services, Inc.; Class D; IaaS, PaaS and SaaS; Government Community Cloud; certified 2016-06-21.
- `cso="AWS US East/West"`: Amazon Web Services, Inc.; Class C; IaaS, PaaS and SaaS; Public Cloud; certified 2013-05-01.
- `cso="Azure Commercial Cloud"`: Microsoft; Class D; SaaS, PaaS and IaaS; Public Cloud; certified 2019-05-03.
- `cso="Azure Government (includes Dynamics 365)"`: Microsoft; Class D; SaaS, PaaS and IaaS; Government Community Cloud; certified 2020-04-29.
- `cso="Google Services (Google Cloud Platform Products and underlying Infrastructure)"`: Google; Class D; SaaS, PaaS and IaaS; Public Cloud; certified 2019-12-04.
- `cso="Oracle Cloud Infrastructure-Government Cloud"`: Oracle; Class D; PaaS and IaaS; Government Community Cloud; certified 2020-10-01.
- `cso="CG-TTS - Cloud.Gov"`: "18F - 18F Cloud.gov"; Class C; PaaS; Government Community Cloud; `cert_path="JAB"`; certified 2017-02-02.

The library converted the certification dates from the page's time stamps (UTC).

## Evidence and method

A government web page that lists records. The filter counts are the page's own counts. The seven records above are from the script data of the HTML file. The library did not count all the records in that data.

## Limits

The page is a snapshot of Nov. 19, 2026, and its counts change when GSA updates the Marketplace. It gives no prices. The Markdown copy does not show the product list, only the counts.

The library has the Marketplace data file of Nov. 11, 2026, which uses the earlier terms: 533 "FedRAMP Authorized" services among 656 product records, by impact level ([FedRAMP Marketplace data (web)](FedRAMP%20Marketplace%20data%20%28web%29.md)). This page gives 561 "FedRAMP Certified" among 795 results, by class. The two use different terms and dates. The library does not take the difference as a contradiction.

For the program rules, see [FedRAMP 20x (web)](FedRAMP%2020x%20%28web%29.md).
