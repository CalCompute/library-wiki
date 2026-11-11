---
title: EPA FRS facility record LBNL (web)
type: source
created: 2026-11-10
updated: 2026-11-10
source_count: 1
tags: [A, location, national-laboratory, california]
elements: [A]
origin: web
tier: primary
citable: yes
url: https://frs-public.epa.gov/ords/frs_public2/frs_rest_services.get_facilities?output=JSON&registry_id=110055718709
rehost: yes
---

# EPA FRS facility record LBNL (web)

## Citation

U.S. Environmental Protection Agency (EPA), Facility Registry Service (FRS). Facility record, registry ID 110055718709, "LAWRENCE BERKELEY NATIONAL LABORATORY". JSON, from the FRS public web service. https://frs-public.epa.gov/ords/frs_public2/frs_rest_services.get_facilities?output=JSON&registry_id=110055718709. Read 2026-11-10. Copy: [`raw/web/2026-11-10 EPA FRS facility record LBNL.md`](../../raw/web/2026-11-10%20EPA%20FRS%20facility%20record%20LBNL.md) (original: `.json` beside it).

## Bottom line

- The record places the facility "LAWRENCE BERKELEY NATIONAL LABORATORY" at "1 CYCLOTRON RD", "BERKELEY", in the county "ALAMEDA", California.
- It gives the latitude "37.877117" and the longitude "-122.249379".

## Background

EPA publishes facility records in the FRS. Its public web service returns one record in JSON for one registry ID. The record is a work of the U.S. Government, so the library rehosts it. The library uses this record for the place of Lawrence Berkeley National Laboratory.

## Key claims

- "FacilityName":"LAWRENCE BERKELEY NATIONAL LABORATORY" (FRSFacility)
- "LocationAddress":"1 CYCLOTRON RD", "CityName":"BERKELEY", "CountyName":"ALAMEDA", "StateAbbr":"CA", "ZipCode":"94720" (FRSFacility)
- "FIPSCode":"1" (FRSFacility)
- "Latitude83":"37.877117", "Longitude83":"-122.249379" (FRSFacility)

## Evidence and method

A federal registry record with 11 fields: registry ID, facility name, address, supplemental location, city, county, state, ZIP code, FIPS code, latitude and longitude. The latitude and longitude are decimal degrees. The field names end in "83".

## Limits

- The record gives one point for the facility. It does not give the edge of the site.
- The record does not say how EPA got the point, and it does not describe the work of the laboratory.
- The FRS has other records under the same laboratory name or address, with other points. The record gives the FIPS code "1", not a five-digit county code.
