---
title: IPEDS HD2025 Directory information (web)
type: source
created: 2026-11-10
updated: 2026-11-10
source_count: 1
tags: [A, ipeds, higher-education, data-file, location, california]
elements: [A]
origin: web
tier: primary
citable: yes
url: https://nces.ed.gov/ipeds/complete-data-files/HD2025.zip
rehost: yes
---

# IPEDS HD2025 Directory information (web)

## Citation

U.S. Department of Education, National Center for Education Statistics (NCES). Integrated Postsecondary Education Data System (IPEDS), "2025 Institutional Characteristics: Directory information" (HD2025). Zipped CSV file `hd2025.csv`, dated July 17, 2026 in the zip file, listed on the IPEDS Complete Data Files page (https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=2025&surveyNumber=1). https://nces.ed.gov/ipeds/complete-data-files/HD2025.zip. Read 2026-11-10. Copy: [`raw/web/2026-11-10 IPEDS HD2025 Directory information.md`](../../raw/web/2026-11-10%20IPEDS%20HD2025%20Directory%20information.md) (original: `.zip` beside it).

## Bottom line

- The file gives the directory information of each institution in the 2025 IPEDS Institutional Characteristics data: 5,985 rows, one for each IPEDS unit ID (`UNITID`).
- Each row gives the name, the address, the city, the state, the county name (`COUNTYNM`), the latitude (`LATITUDE`) and the longitude (`LONGITUD`).
- All 54 California institutions with a 2025 Carnegie Research Activity Designation have a row, with a county, a latitude and a longitude.

## Background

NCES, in the U.S. Department of Education, runs IPEDS, the federal data collection for postsecondary institutions. The HD file is the directory part of the Institutional Characteristics survey. NCES gives it as a zip file with one CSV file in it. It is a work of the U.S. Government, so the library rehosts it.

## Key claims

- The header row of `hd2025.csv` starts "UNITID,INSTNM,IALIAS,ADDR,CITY,STABBR,ZIP" and ends "COUNTYCD,COUNTYNM,CNGDSTCD,LONGITUD,LATITUDE". (hd2025.csv, header row)
- Row 110671: "110671,University of California-Riverside,UC Riverside,900 University Ave,Riverside,CA,92521", with `COUNTYNM` "Riverside County", `LONGITUD` "-117.327410" and `LATITUDE` "33.972460". (hd2025.csv)
- Row 243744: "Stanford University", city "Stanford", `COUNTYNM` "Santa Clara County", `LONGITUD` "-122.167359" and `LATITUDE` "37.429434". (hd2025.csv)
- Row 445188: "University of California-Merced", city "Merced", `COUNTYNM` "Merced County", `LONGITUD` "-120.424944" and `LATITUDE` "37.366237". (hd2025.csv)

## Evidence and method

- Federal administrative data that institutions report to IPEDS. The file has 70 columns.
- Other columns give the chief administrator, the web addresses, the sector, the control, the Carnegie codes and the core-based statistical area.
- `LATITUDE` and `LONGITUD` are decimal degrees with six decimal places.
- 664 rows have the state `CA`.
- The library's count: all 54 California unit IDs with a designation in the [Carnegie 2025 Public Data File (web)](Carnegie%202025%20Public%20Data%20File%20%28web%29.md) are in this file. For each of the 54, the name and the city are the same in the two files.
- The Markdown copy renders the whole CSV file as one table, about 4.5 MB.

## Limits

- The file gives one point for each institution. It does not give the location of other campuses, medical centers or field stations.
- The file does not say how NCES got the latitude and longitude.
- The file does not list the national laboratories, because they are not postsecondary institutions.
- The file is for the 2025 data year. A later file can change values.
