---
title: LBNL 2024 US Data Center Energy Usage Report
type: source
created: 2026-10-28
updated: 2026-10-28
tags: [A, B, energy, data-centers, water, federal]
elements: [B, A]
origin: shared
tier: institutional
citable: yes
url: https://escholarship.org/uc/item/32d6m0d1
rehost: yes
license: U.S. Government licence
---

# LBNL 2024 US Data Center Energy Usage Report

## Citation

Shehabi, Arman, Sarah Josephine Smith, Alex Hubbard, Alexander Newkirk, Nuoa Lei, Md AbuBakar Siddik, Billie Holecek, Jonathan G. Koomey, Eric R. Masanet, and Dale A. Sartor. "2024 United States Data Center Energy Usage Report." Lawrence Berkeley National Laboratory (LBNL), Energy Analysis and Environmental Impacts Division, LBNL-2001637, Dec. 19, 2024. DOI: 10.71468/P1WC7Q. https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report. Copy: [`raw/shared/2026-10-28 LBNL 2024 US Data Center Energy Usage Report.md`](../../raw/shared/2026-10-28%20LBNL%202024%20US%20Data%20Center%20Energy%20Usage%20Report.md) (original: `.pdf` beside it, from the eScholarship record https://escholarship.org/uc/item/32d6m0d1). Read 2026-10-28.

## Bottom line

- United States data centers used 176 terawatt-hours (TWh) in 2023, "4.4% of total U.S. electricity consumption" (p. 5). The report projects 325 to 580 TWh in 2028, "6.7% to 12.0%" of forecast United States electricity use (p. 6).
- Graphics processing unit (GPU) accelerated servers for artificial intelligence (AI) drive the growth. Their electricity use went from "less than 2 TWh in 2017 to more than 40 TWh in 2023" (p. 49).
- This is the source of the CSIS figure. CSIS says "energy" and "triple". The report says electricity, and a range of about 1.8 to 3.3 times the 2023 value. Cite this report, not CSIS.

## Background

The Energy Act of 2020 asks the U.S. Department of Energy to update the LBNL report of 2016. This report is "designed to meet that Congressional request" (p. 5). It is the third such report "released over nearly 20 years" (p. 67). The DOE Office of Energy Efficiency and Renewable Energy funded it (title page). Analyst firms Omdia, Dell'Oro Group, S&P Global and the International Data Corporation gave input data (Acknowledgements).

## Key claims

- **2023 use (p. 5, repeated p. 52).** "U.S. data center energy use has continued to grow at an increasing rate, reaching 176 TWh by 2023, representing 4.4% of total U.S. electricity consumption."
- **2018 use (p. 5).** About 76 TWh in 2018, "1.9% of total annual U.S. electricity consumption".
- **2028 range (p. 6).** "the low and high end of roughly 325 and 580 TWh in 2028". At 50 percent average use of capacity, this is "a total power demand for data centers between 74 and 132 GW". It "represents 6.7% to 12.0% of total U.S. electricity consumption forecasted for 2028".
- The range for 2023 to 2028 is "13% to 27%".
- **Cause (p. 6).** "the rapid growth in accelerated servers has caused current total data center energy demand to more than double between 2017 and 2023".
- **AI servers (p. 49).** GPU-accelerated AI servers "grew in energy usage from less than 2 TWh in 2017 to more than 40 TWh in 2023". All servers used "nearly 100 TWh in 2023". The 2028 server range is "about 240 and 380 TWh".
- **Training and inference (p. 50).** Inference servers "make up nearly 60% of the AI server energy usage in 2023". By 2028, training uses "between 50% and 53% of the total AI server energy".
- **Who uses it (p. 50).** By 2028, "hyperscale and colocation will account for over 90% of server energy consumption, primarily driven by AI workloads".
- **California (p. 37).** "Virginia hosts the highest electricity demand associated with data centers in the United States, serving as the primary hub for both colocation and hyperscale data centers, followed by California and Texas." The report gives no California figure in TWh.
- **Direct water (p. 55).** Data centers used 21.2 billion liters of water in 2014 and 66 billion liters in 2023. "Hyperscale data centers in 2028 are expected to consume between 60 and 124 billion liters" (pp. 55-56).
- **Indirect water and emissions (p. 57).** "The total indirect water footprint of U.S. data centers is nearly 800 billion liters". Emissions for the same electricity are "61 billion kilograms of CO2 equivalent".
- **Cooling (p. 6).** The 2028 range includes cooling scenarios, "such as shifting to liquid base cooling or moving away from evaporative cooling".
- **Data gap (p. 68).** "Very few companies report actual data center electricity use and virtually none report it in context of IT characteristics such as compute capacities, average system configurations, and workload types."

> ⚠️ Contradiction: [CSIS If Compute Is the New Oil](CSIS%20If%20Compute%20Is%20the%20New%20Oil.md) says "In 2023, data centers accounted for 4.4 percent of the United States' annual energy consumption, a figure projected to triple by 2028." This report says 4.4 percent of total U.S. **electricity** consumption, not energy (p. 5). The 2028 range is 325 to 580 TWh (p. 6). That is about 1.8 to 3.3 times 176 TWh. "Triple" is true only at the top of the range. As a share of electricity, the range is 6.7 to 12.0 percent, about 1.5 to 2.7 times 4.4 percent.

## Evidence and method

- A "bottom-up" model: it counts the installed base of servers, storage and network equipment and multiplies by power draw and cooling overhead (p. 6; Section 2).
- After 2023, results are scenarios. They vary GPU shipments, how hard and how long AI servers run, and cooling systems (p. 6; p. 49).
- Water and emissions use grid data by balancing authority from the U.S. Energy Information Administration (EIA) and the Environmental Protection Agency (EPA) (p. 57).
- About 50 organizations reviewed drafts (Acknowledgements). The eScholarship cover page marks the record "Peer reviewed".

## Limits

- The authors say "the lack of data availability significantly limits the analysis in this report" (p. 6).
- The model uses "proprietary market analyst data".
- Figures are national. The report ranks California second in data center demand but gives no state value (p. 37).
- The indirect water and emissions method ignores power purchase agreements and on-site generation (pp. 57-58).
- The data ends in 2023. Projections to 2028 rest on GPU shipment forecasts (p. 49).
- The copy is a pdftotext conversion. Page numbers in this page are the report's printed page numbers.
