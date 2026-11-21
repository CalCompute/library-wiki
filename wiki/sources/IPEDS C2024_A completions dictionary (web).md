---
title: IPEDS C2024_A completions dictionary (web)
type: source
created: 2026-11-19
updated: 2026-11-19
source_count: 1
tags: [E, ipeds, higher-education, data-file, completions, federal]
elements: [E]
origin: web
tier: primary
citable: yes
url: https://nces.ed.gov/ipeds/datacenter/data/C2024_A_Dict.zip
rehost: yes
---

# IPEDS C2024_A completions dictionary (web)

## Citation

U.S. Department of Education, National Center for Education Statistics (NCES). Integrated Postsecondary Education Data System (IPEDS), "File Documentation for the Completions Data File, 2023-24" (C2024_A), provisional release, September 2025. Zipped Excel file `C2024_a_dict.xlsx`. https://nces.ed.gov/ipeds/datacenter/data/C2024_A_Dict.zip. Read 2026-11-19. Copy: [`raw/web/2026-11-19 IPEDS C2024_A completions dictionary.md`](../../raw/web/2026-11-19%20IPEDS%20C2024_A%20completions%20dictionary.md) (original: `.zip` beside it).

## Bottom line

- The file is the data dictionary of the IPEDS completions file for 2023-24. It defines the 34 variables of the C2024_A data file and lists the code values of each.
- The data file counts the awards of each institution from July 1, 2023 to June 30, 2024. It gives them by program code, award level, race and ethnicity, and gender.
- Program codes include Artificial Intelligence (11.0102), Computer Science (11.0701), Cloud Computing (11.0902) and Data Science, General (30.7001).

## Background

NCES, in the U.S. Department of Education, runs IPEDS, the federal data collection for postsecondary institutions. The completions survey counts degrees and certificates. The dictionary comes with the data file and does not hold the award counts for one institution. It is a work of the U.S. Government, so the library rehosts it.

## Key claims

- "This file contains the number of awards by type of program, level of award (certificate or degree), first or second major and by race/ethnicity and gender. Data covers all awards granted between July 1, 2023 and June 30, 2024." (Introduction, Overview)
- "Type of program is categorized according to the 2020 Classification of Instructional Programs (CIP), a detailed coding system for postsecondary instructional programs." (Introduction, Overview)
- "Each record is uniquely defined by the variables IPEDS ID (UNITID), classification of instructional program (CIPCODE), first or second major (MAJORNUM) and award level (AWLEVEL)." (Introduction, Overview)
- "Data are imputed for nonresponding institutions." (Introduction, Note)
- The variable `CTOTALT` is "Awards/degrees conferred between July 1, 2023 and June 30, 2024 to all recipients, across all race/ethnicities and both genders". (Description)

## Evidence and method

- Federal data documentation. The workbook has six sheets: Introduction, Varlist, Description, Frequencies, Statistics and Imputation values.
- The Frequencies sheet gives the number of records for each code value, not the number of awards. For example, 493 records have the code 11.0102 Artificial Intelligence, and 4,668 have 11.0701 Computer Science.
- Award levels go from "Certificates of less than 12 weeks" (code 20) to "Doctor's degree - research/scholarship" (code 17). Some codes are totals, such as 12 "Degrees total".
- The file has 1,688,471 records (Statistics sheet).

## Limits

- The dictionary does not give award counts by institution or by state. Those are in the C2024_A data file, which this library does not have.
- The data are a provisional release. NCES says the final release can change values.
- The sums on the Statistics sheet add the total rows (such as CIP code 99 "Grand total") to the detail rows. They are not counts of awards.
