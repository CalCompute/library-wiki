---
title: NRP Getting started (web)
type: source
created: 2026-10-15
updated: 2026-10-15
tags: [A, D, F, nrp, onboarding, identity]
elements: [A, D, F]
origin: web
tier: institutional
citable: yes
url: https://nrp.ai/documentation/userdocs/start/getting-started/
rehost: no
---

# NRP Getting started (web)

## Citation

National Research Platform (NRP). "Getting access." NRP Documentation, User Guide, web page, "Last updated: Oct 8, 2026". https://nrp.ai/documentation/userdocs/start/getting-started/. Read 2026-10-15.

## Bottom line

- NRP has no proposal review. A user logs in through CILogon, the federated login service of research institutions. A faculty member, staff member or postdoc then requests a "namespace" with a form.
- Students cannot request a namespace. Their "research supervisor" adds them. The namespace admin is "responsible for all activity happening in your namespaces".

## Background

NRP runs the Nautilus Kubernetes cluster. The page gives the steps to log in, get a namespace and connect with the `kubectl` tool.

## Key claims

Login (section "Get access and log in"):

- "You will be redirected to CILogon — the federated login service shared by research institutions — where you have to Select an Identity Provider."
- If the institution is not listed and Microsoft does not work, "you can select Google or Github."
- "After a successful authentication, you will log in to the portal and your account will be created if it was not created before."

Who gets access (section "Get access and log in"):

- "If you are a student, please contact your research supervisor and ask them to add you to their namespace. Once you are added to a namespace, your status will change to a cluster user and you will get access to all namespace resources."
- "If you are a faculty member, university staff member, or postdoc starting a new project and need your own namespace — either for yourself or your research group — request one by filling out the namespace request form."
- "As a namespace admin, you will be the one responsible for all activity happening in your namespaces, keeping the user list up-to-date."
- "We're handling the namespaces management as a hierarchical model where we delegate the management of certain parts to the admins who can then further delegate the responsibilities.."

Rules before use (section "Get access and log in"):

- "Make sure you read the cluster policies before starting to use it." The page links the AUP and the Cluster Policies.
- "All Nautilus and NRP users are expected to join for user support and real-time updates."

Warnings (section "Updating namespace membership"):

- "Users running a Job with sleep command or equivalent (any command that never ends by itself) will be banned from using the cluster."

## Evidence and method

This is a how-to page. It has no data on how many namespaces NRP approves or refuses.

## Limits

- The page does not say who approves a namespace request or on what criteria.
- The page does not say if users from outside universities can get a namespace. Google and GitHub logins suggest that some can.
- The page does not say if NRP checks a user against federal research security lists. ACCESS does.
