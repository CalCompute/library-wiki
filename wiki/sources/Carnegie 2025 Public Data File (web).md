---
title: Carnegie 2025 Public Data File (web)
type: source
created: 2026-11-10
updated: 2026-11-10
source_count: 1
tags: [A, carnegie-classification, research-activity, higher-education, data-file, california]
elements: [A]
origin: web
tier: institutional
citable: yes
url: https://carnegieclassifications.acenet.edu/wp-content/uploads/2025/04/2025-Public-Data-File.xlsx
rehost: no
---

# Carnegie 2025 Public Data File (web)

## Citation

American Council on Education (ACE), Carnegie Classification of Institutions of Higher Education. "2025 Public Data File." Spreadsheet (.xlsx), dated October 10, 2025 on the resources page of the Carnegie Classification website. https://carnegieclassifications.acenet.edu/wp-content/uploads/2025/04/2025-Public-Data-File.xlsx. Read 2026-11-10.

## Bottom line

- The file gives the 2025 Carnegie Classifications for 3,927 United States institutions of higher education. It gives the state, the city and the control of each one.
- It gives each institution's 2025 Research Activity Designation. In California, 54 institutions have one.
- 14 are "Research 1: Very High Spending and Doctorate Production". 16 are "Research 2: High Spending and Doctorate Production". 24 are "Research Colleges and Universities".

## Background

The American Council on Education publishes the Carnegie Classification of Institutions of Higher Education. The 2025 edition has an Institutional Classification, a Student Access and Earnings Classification and a separate Research Activity Designation. This file holds all three for each institution, with the data that each one uses. The site gives the licence of the Carnegie Classification as the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. That licence does not permit commercial use, so the library does not rehost the file. The counts on this page are the library's counts of the rows.

## Key claims

- The variable `research2025` is the "2025 Research Activity Designation", and its source is "CCIHE". (labels sheet)
- `research2025` has four values. (values sheet)
  - "Research 1: Very High Spending and Doctorate Production"
  - "Research 2: High Spending and Doctorate Production"
  - "Research Colleges and Universities"
  - "No research designation"
- The variable `control` is the "Control of institution", and its source is "IPEDS". Its values are "Public", "Private not-for-profit" and "Private for-profit". (labels and values sheets)
- The variable `herd_avg` is the "Average total R&D expenditures reported for FY21, FY22, FY23", and its source is "HERD". (labels sheet)
- The variable `rdoc_avg` is the "Average number of doctoral degrees-research/scholarship awarded in 2020-21, 2021-22, and 2022-23 academic years". (labels sheet)
- Row 110671: "University of California-Riverside | Riverside | California", with the 2025 Research Activity Designation "Research 1: Very High Spending and Doctorate Production". (data sheet)

## Evidence and method

- A data file with four sheets: README (empty), data, labels and values.
- The data sheet has 3,927 rows and 94 columns. Each row is one institution, by its Integrated Postsecondary Education Data System (IPEDS) unit ID.
- The columns give the name, the city, the state, the three 2025 classifications and the control.
- Other columns give minority-serving and other flags, enrollment and degrees awarded.
- Other columns give the research and development (R&D) expenditures that the Higher Education Research and Development (HERD) Survey reports.
- The labels sheet gives the source of each variable: IPEDS, HERD, College Scorecard or the Carnegie Classification itself (CCIHE).
- National counts of the 2025 Research Activity Designation in this file: 187 Research 1 and 139 Research 2.
- 216 are Research Colleges and Universities, and 3,385 have no research designation.
- California has 424 rows. 370 have no research designation.

## Limits

- The file gives no web address for any institution.
- The control value comes from IPEDS. It has no value for a federal institution: the Naval Postgraduate School has the value "Public".
- The data covers fiscal years 2021 to 2023 and degrees from 2020-21 to 2022-23. A designation does not show later change.
- The file does not list the national laboratories, because they are not institutions of higher education.
- The file does not describe the research computing of any institution.
