# Log

Append only. Each entry starts with `## [YYYY-MM-DD] <type> | <title>`.

## [2026-11-01] setup | Library set up
- Summary: 164 source pages about public documents, the seven element reading lists, 101 other entity pages, 25 team pages, 8 concept pages and 1 analyses.
- Pages created: all.
- Pages updated: none.
- Notable: every page reports only what public sources say; the consortium's communications appear only as dated markers.

## [2026-11-02] fetch | Six legislative originals
- Summary: downloaded the original PDFs of six legislative records from their official URLs, named after their excerpt files: the California Report on Frontier AI Policy (2025-06-17), and the SB-53 analyses of the Senate Governmental Organization Committee (2025-03-25), the Senate Judiciary Committee (2025-04-08), the Assembly Privacy Committee (2025-07-08, 2025-09-05) and the Assembly Floor (2025-09-08).
- Pages created: none.
- Pages updated: none.

## [2026-11-02] schema | Renamed to the CalCompute Research Library
- Summary: the library's name is now the CalCompute Research Library (user, Nov. 2, 2026). The Drive's top folder keeps its name, "CalCompute Library".
- Pages created: none.
- Pages updated: AGENTS.md, README.md, the ingest and lint skills.

## [2026-11-02] schema | Bottom line first; one writing standard
- Summary: source and entity pages now open with a Bottom line, and entity pages carry Why they matter (user, Nov. 2, 2026). The writing standard is now the full Simplified Technical English standard with Bottom line up front.
- Pages created: none.
- Pages updated: AGENTS.md (Writing standard, Page formats), every source page and 29 entity pages.

## [2026-11-02] schema | The library stands alone
- Summary: AGENTS.md, the README, the skills and the Drive guide describe only this library. The markers in the graph are the consortium's calls, email threads and chat topics, with a kind and a date (user, Nov. 2, 2026).
- Pages created: none.
- Pages updated: AGENTS.md, README.md, the ingest and suggestions skills.

## [2026-11-02] schema | The Drive is the public Drive
- Summary: in the graph, a square marks a document with a copy in the public Google Drive "CalCompute Library", and opens it there. The markers are the consortium's calls, email threads and chat topics only (user, Nov. 2, 2026).
- Pages created: none.
- Pages updated: AGENTS.md.

## [2026-11-02] lint | One page for the UC Office of the President
- Summary: removed the publisher page "University of California, Office of the President", a duplicate of "University of California Office of the President" that already lists the same source.
- Pages created: none.
- Pages updated: wiki/index.md; removed wiki/entities/University of California, Office of the President.md.

## [2026-11-05] schema | Consortium research sources arrive on the Suggestions page
- Summary: the consortium's wiki now queues its public sources on the Suggestions page, status approved. A row has title, address, publisher, date, folder and licence only. Ingest takes each row from the public address as soon as it arrives.
- Pages created: none.
- Pages updated: AGENTS.md, README.md, .agents/skills/ingest/SKILL.md, .agents/skills/suggestions/SKILL.md, analyses/Suggestions.md.
- Notable: a document the library already has under another address gets status duplicate.

## [2026-11-05] ingest | 21 consortium research sources from the Suggestions page
- Summary: ingested the 21 approved consortium research rows whose documents the library did not have. Five rows were already in the library under another address and got status duplicate: Anthropic AI for Science program rules, the Empire AI Cornell call, NAIRR Pilot review and matching, LeMahieu 2017 and the Public AI Network 2024 white paper record. Four originals went to raw/web/ as rehosted copies: the NSF AI-Ready America Workshop Report, UC Regents Policy 5203, the Governor's Innovation Fellows program and the State Water Resources Control Board About page. The rest stay in .cache/.
- Pages created: 21 source pages (NSF AI-Ready America Workshop Report (web); Berkeley Data Science Discovery partner page (web); CENIC About (web); CENIC membership (web); CFPIC who we are (web); CITRIS About (web); CITRIS mission and history (web); Google Summer of Code how it works (web); UC Regents Policy 5203 campus foundations (web); Roy-Chowdhury UCR personal page (web); Becerra AI priorities (web); Campus Explorer university extension programs (web); Center for AI Safety About (web); Center for AI Safety Compute Cluster (web); Governor's Innovation Fellows program (web); RAISE at UCR homepage (web); RAISE at UCR people (web); SDSC Sherlock Cloud services (web); Skills Caravan training vs development (web); State Water Resources Control Board About (web); UCR receives 8 million federal grants 2026-10-19 (web)); entity pages for Amit Roy-Chowdhury, Campus Explorer, Center for AI Safety, Child and Family Policy Institute of California, CITRIS and the Banatao Institute, Regents of the University of California, Skills Caravan, State Water Resources Control Board, Xavier Becerra for Governor 2026.
- Pages updated: the seven element reading lists; entity pages for CENIC, California Office of Data and Innovation, Google, San Diego Supercomputer Center, U.S. National Science Foundation, UC Berkeley College of Computing, Data Science, and Society, UC Riverside, Kevin Michael Esterling; wiki/index.md; analyses/Suggestions.md.
- Notable: bin/drive_push.py has not run yet for the four rehosted originals. Roy-Chowdhury UCR personal page (web) is a profile page, listed on his entity page and not on a reading list.

## [2026-11-06] schema | Team pages carry cited bios
- Summary: a team entity page is now the person's public profile, and californiacompute.org links to it. It has a Bottom line, cited Affiliations and Background from the person's public profile pages, Sources and Links. The `profile` field is gone. The Frontmatter block now lists `order`, `institution`, `position`, `role` and `photo`, which team pages already used.
- Pages created: none.
- Pages updated: AGENTS.md.
- Notable: a person approved the change on 2026-11-06.

## [2026-11-06] ingest | Profile sources and cited bios for the 25 team pages
- Summary: ingested 36 profile pages for people on the team, from the public links californiacompute.org gives and from funder, university, government and journal records. Rewrote the 25 team entity pages to the new format. A claim with no public source was left out.
- Pages created: 36 source pages tagged people (5 NSF award records, 1 NSF PAR record, and government, university, journal and personal profile pages; see the Sources table).
- Pages updated: the 25 team entity pages; wiki/index.md; analyses/Suggestions.md.
- Notable: no public source describes Ariya Mohanty, Daniel Romo or Deeksha Vaidyanathan yet; their pages say so. Some profile links were not readable (HTTP 403, JavaScript pages, a failed DNS or TLS check), so their claims are out. The new pages are on no reading list. bin/drive_push.py uploaded the three rehosted PDFs (FCC notice DA 24-150, the SB 1047 veto message, the Assembly Daily Journal of 2023-06-30) and rewrote both Docs.

## [2026-11-06] fix | Two team roles and two restored originals
- Summary: the roles of Kevin Michael Esterling and Stephanie Lieggi said "UC" where californiacompute.org's original text says "researcher"; both now say "researcher", as the site does again. Downloaded the Governor's and Cal OES homepages again into raw/web/; they are rehosted originals with no source page.
- Pages created: none.
- Pages updated: Kevin Michael Esterling, Stephanie Lieggi.
- Notable: none.

## [2026-11-06] schema | Full legislative copies in raw/legislative
- Summary: raw/legislative/ now holds full copies, word for word, of the ten documents californiacompute.org used to host. A full copy has `passages:`, the file lines of its CalCompute passages; the Drive's "0 - LEGISLATIVE CONTENTS" quotes only those lines. An excerpt keeps `excerpt_lines:` and its `[...]` cuts. On the site, a full copy renders as a page with its Drive PDF linked; an excerpt still opens in the Drive.
- Pages created: none.
- Pages updated: AGENTS.md (Layout line), raw/legislative/README.md, bin/drive_push.py.
- Notable: the person's call on 2026-11-06. It breaks two rules once: nine files in raw/legislative/ were replaced, and their full text came from the transcriptions the excerpts were cut from, each with its official `sourceUrl`, not from a download. The rules stay.

## [2026-11-06] fix | Ten legislative documents as full copies
- Summary: nine raw/legislative excerpts are now full copies, and the full SB 53 bill is a new file, SB-53 chaptered 2025-09-29.md, beside the § 11546.8 excerpt. Each `passages:` range picks out the same text the old excerpt held. The source pages now say the copy is full, and their Limits lines describe the full text.
- Pages created: none (the chaptered bill is a raw file; the statute's source page links it).
- Pages updated: source pages for the frontier AI report, the working group release, the signing release, the two Assembly Privacy analyses, the Senate Judiciary analysis, the signing message (now with `url:` and `rehost: yes`), the SB 294 announcement, the expansion release and the statute; reading lists A to E; wiki/index.md.
- Notable: the frontier AI report names CalCompute nowhere in its text. bin/drive_push.py rewrote both Docs; "0 - LEGISLATIVE CONTENTS" quotes each full copy's `passages:` and lists the full bill in place of the § 11546.8 excerpt. No new uploads.

## [2026-11-06] fix | Two false descriptions removed
- Summary: deleted the `description:` of the frontier AI report, which said it informed "the CalCompute Consortium structure" (the report does not mention CalCompute), and of the SB 53 bill and its § 11546.8 excerpt, which said the statute establishes CalCompute (subd. (a) establishes a consortium to develop a framework for it). The descriptions were the site's text, not the documents'. The full copies' `passages:` moved up one line with their text.
- Pages created: none.
- Pages updated: source pages for the frontier AI report and the statute (their line numbers).
- Notable: the person's call on 2026-11-06; three files in raw/legislative/ changed again.

## [2026-11-09] ingest | 75 consortium research sources from the Suggestions page
- Summary: ingested 75 of the 77 approved consortium research rows. None was a duplicate. Two rows failed and stay approved: FedRAMP marketplace (the address is a script redirect with no content) and cloud.gov what is cloud.gov (the address now redirects to the cloud.gov homepage). Rehosted originals went to raw/web/ and raw/legislative/; the rest stay in .cache/.
- Pages created: 75 source pages (listed in wiki/index.md, created 2026-11-09); 32 entity pages (Arizona State University, California Community Colleges Board of Governors, California Department of General Services, California Department of Human Resources, California Department of Justice, California Division of Apprenticeship Standards, California Employment Development Department, California Employment Training Panel, California Faculty Association, California Policy Lab, California State University, Center for Security and Emerging Technology, Choose New Jersey, County of San Diego, Maryland General Assembly, Massachusetts Institute of Technology, Mississippi Department of Information Technology Services, National Institutes of Health, Office of the Federal Register, National Archives, QuantZero, SEIU Local 1000, Senate Committee on Budget and Fiscal Review, State of New Jersey, Office of the Governor, Texas A&M University, Texas A&M University System, U.S. Department of Education, Federal Student Aid, U.S. Energy Information Administration, UC San Diego, UCLA, UCLA Digital and Technology Solutions, University of Florida, University of Massachusetts Amherst, Public Interest Technology).
- Pages updated: the seven element reading lists (element A now has a Trade section); entity pages for Amazon Web Services, Anthropic, CENIC, Cal-ICOR, California Department of Technology, California Government Operations Agency, California Office of Data and Innovation, California State Assembly, Epoch AI, NVIDIA, Office of the Governor of California, SEIU Local 1000, San Diego Supercomputer Center, Stanford University, U.S. National Science Foundation, University of California Office of the President; concept pages Fully owned and hosted platform, Funding models, Hybrid compute and open-weight models, NAIRR and the National Research Platform, State AI compute clusters and the Empire AI model, Who can use CalCompute; wiki/index.md; analyses/Suggestions.md; bin/grab.py (accepts CSV and XLSX files).
- Notable: the two failed rows left redirect stubs in raw/web/ (2026-11-09 FedRAMP marketplace and 2026-11-09 cloud.gov what is cloud.gov, .html and .md) with no source page. The Markdown copy of Executive Order N-5-26 is empty because the PDF is a scan; its source page quotes the page images. The UF HiPerGator pages give two costs for the fourth generation ($33 million and $24 million); both pages flag the contradiction. Epoch AI and CSET state open licences that the rows did not give, so those files are not rehosted. bin/drive_push.py has not run yet for the new rehosted originals.

## [2026-11-09] ingest | 14 consortium research sources from the Suggestions page
- Summary: ingested the 14 new approved consortium research rows: eight World Economic Forum (WEF) reports and six Ohio Supercomputer Center (OSC) pages. None was a duplicate. None is rehosted: the WEF reports say "All rights reserved", and osc.edu is not a government host; the downloads stay in .cache/. The two rows that failed earlier stay approved: the FedRAMP marketplace address is still a script redirect to /marketplace/products/, and the cloud.gov address still redirects to the cloud.gov homepage.
- Pages created: 14 source pages (WEF AI Infrastructure in the Age of Sovereignty 2026 (web); WEF AI and the Future of Entry-Level Work 2026 (web); WEF Future of Jobs Report 2025 (web); WEF Making Agentic AI Work for Government 2026 (web); WEF Next-Generation Computing Framework 2026 (web); WEF Rethinking AI Sovereignty 2026 (web); WEF Global Cybersecurity Outlook 2026 (web); WEF Global Risks Report 2026 (web); Ohio Supercomputer Center homepage (web); OSC at a glance (web); OSC governance (web); OSC getting started and fees (web); OSC supercomputers (web); OSC 2025-2026 research report (web)); entity pages for World Economic Forum and Ohio Supercomputer Center.
- Pages updated: the seven element reading lists (Institutional sections); concept pages State AI compute clusters and the Empire AI model, Who can use CalCompute, Funding models, Hybrid compute and open-weight models, Fully owned and hosted platform; wiki/index.md; analyses/Suggestions.md.
- Notable: the Future of Jobs Report and the Global Risks Report pages draw on named parts only; their Limits sections list them. The OSC research report page draws on the web page, not the PDF of the full report. The OSC supercomputers address serves the page "Cluster Computing". The Next-Generation Computing Framework gives two figures for 2025 investment ($448 billion and $459 billion), and its page flags the contradiction. bin/drive_push.py --check passes. The push has not run yet. It would also upload the rehosted originals of the earlier 2026-11-09 ingest.

## [2026-11-09] ingest | 20 consortium research sources from the Suggestions page
- Summary: ingested 20 of the 21 new approved consortium research rows. None was a duplicate. One row failed and stays approved: the F3I portal address serves a script-only sign-in app with no readable text. The two rows that failed earlier stay approved: the FedRAMP marketplace address is still a script redirect, and the cloud.gov address still redirects to the cloud.gov homepage. The Governor's release and the five UC AI pages are rehosted in raw/web/; the rest stay in .cache/.
- Pages created: 20 source pages (Berkeley EECS colloquium Marin open lab (web); California Policy Lab AI-Unemployment Tracker (web); Chip supply chain homepage (web); Chips for Humanity homepage (web); Chips for Humanity sources (web); F3 Innovate about (web); F3I homepage (web); F3i Supercomputing Center (web); GovAI Coalition Summit event page (web); Governor partners with tech companies on AI education 2025-08-07 (web); Littler California 2026 AI employment laws (web); UC AI Council about (web); UC AI Council roster (web); UC AI Council subcommittees (web); UC AI applicable law and policy (web); UC AI governance and transparency (web); UC Noyce Initiative cybersecurity (web); UC Noyce Initiative homepage (web); UC Noyce Initiative power of five (web); UCI data infrastructure award 2026-08-27 (web)); 8 entity pages (Chips for Humanity, chipsupplychain.org, e.Republic, Government Technology, F3 Innovate, Littler Mendelson, UC Berkeley Department of Electrical Engineering and Computer Sciences, UC Irvine, UC Noyce Initiative).
- Pages updated: the seven element reading lists; entity pages for California Policy Lab, Office of the Governor of California, University of California Office of the President; concept pages CalCompute as coordinator vs operator, Funding models, Hybrid compute and open-weight models, Who can use CalCompute; wiki/index.md; analyses/Suggestions.md.
- Notable: the Governor's release of 2025-08-07 gives "33 of the top 50" AI companies where other Governor's releases give 32; its page flags the contradiction. The three UC AI pages give different names for the AI Council subcommittees, and their pages flag it. The chip supply chain site is one person's work, made "(with Claude)". Its page has tier trade and citable no. bin/drive_push.py --check passes. The push has not run yet.

## [2026-11-09] ingest | CCST about (web)
- Summary: ingested the one new approved consortium research row, CCST about. It was not a duplicate. It is not rehosted: ccst.us is not a government host and the page states no open licence; the download stays in .cache/. The three rows that failed earlier stay approved: the FedRAMP marketplace address is still a script redirect to /marketplace/products/, the cloud.gov address still serves a redirect stub, and the F3I portal still serves a script-only sign-in app.
- Pages created: CCST about (web).
- Pages updated: element reading lists C - Governance, E - Workforce and F - Partnerships (Institutional sections); entity page California Council on Science and Technology (Bottom line, Why they matter and Affiliations added); concept page Funding models; wiki/index.md; analyses/Suggestions.md.
- Notable: the page lists its partners as logos only; the source page names them from the logo titles. It gives no budget and no amount of partner support. bin/drive_push.py --check passes. The push has not run yet. It would also upload the three rehosted originals of the earlier 2026-11-09 ingests.

## [2026-11-09] ingest | 7 consortium research sources from the Suggestions page
- Summary: ingested the seven new approved consortium research rows: two Chronicle of Philanthropy stories, the Imagine Canada report, the NJIT and URI pages on NSF programs, the NSF news release on AI Infrastructure Hubs and the UC press release on the AI Steering Committee. None was a duplicate. raw/web/ holds the NSF and UC releases as rehosted copies. The other downloads stay in .cache/. The three rows that failed earlier stay approved: the FedRAMP marketplace address is still a script redirect, the cloud.gov address still serves a redirect stub, and the F3I portal still serves a script-only sign-in app.
- Pages created: 7 source pages (Chronicle of Philanthropy nonprofit AI gap (web); Chronicle of Philanthropy nonprofits embracing AI funding (web); Imagine Canada State of AI Adoption in Canadian Nonprofits (web); NJIT NSF 26-508 round dates (web); NSF news AI Infrastructure Hubs (web); UC press release systemwide AI expertise (web); URI IACR NSF 26-512 and 26-513 summary (web)); 4 entity pages (Imagine Canada, New Jersey Institute of Technology, The Chronicle of Philanthropy, University of Rhode Island).
- Pages updated: element reading lists A to F; entity pages U.S. National Science Foundation and University of California Office of the President; concept pages Funding models, State AI compute clusters and the Empire AI model, NAIRR and the National Research Platform, Hybrid compute and open-weight models; source pages NSF 26-508 TechAccess solicitation (web) and UC Regents B4 Update on AI 2026-09-16 (contradiction flags); wiki/index.md (the Sources count is now 338, the number of source pages); analyses/Suggestions.md.
- Notable: the NJIT page gives the round 2 letter of intent date as December 15, 2027; NSF gives Dec. 15, 2026. The UC press release says President Milliken formed the Steering Committee in May 2026; the Regents item says March 2026. Both pairs of pages flag the contradiction. The Imagine Canada report has a CC BY-NC-ND 4.0 licence that the row did not give, so it is not rehosted. The second Chronicle story carries the date October 2, 2025, but gives a 2026 figure. bin/drive_push.py --check passes. The push has not run yet. This ingest adds no Drive files, because both rehosted copies are web pages; the push would add the seven sources to the guide and upload the rehosted originals of the earlier 2026-11-09 ingests.

## [2026-11-09] schema | Directory pages
- Summary: a new page type, the directory page, in wiki/directories/: a table of records on one topic, one row for each record. Each row cites source pages in this library and gives the date of its last check (user, Nov. 9, 2026).
- Pages created: none.
- Pages updated: AGENTS.md (Layout, Rules, Page formats, Frontmatter, index.md); wiki/index.md (an empty Directories section).
- Notable: no directory page exists yet.

## [2026-11-09] ingest | 16 consortium research sources from the Suggestions page
- Summary: ingested 16 of the 20 approved consortium research rows. None was a duplicate. Four rows failed and stay approved: the FedRAMP marketplace address is still a script redirect, the cloud.gov address still serves a redirect stub, the F3I portal still serves a script-only sign-in app, and the City of Santa Ana address serves a Laserfiche WebLink viewer with 23 words and no document text. The CDT, GovOps, Governor, LLNL and ODI pages are rehosted in raw/web/; the rest stay in .cache/.
- Pages created: 16 source pages (ALERTCalifornia homepage (web); AWS Activate startup credits (web); CDT Anthropic partnership expansion 2026-07 (web); California Policy Lab hosted projects (web); GovOps generative AI executive order page (web); Governor California NVIDIA collaboration 2024-08-09 (web); LLNL Tuolumne (web); NAIRR Pilot Start-Up projects (web); NORC Cradle-to-Career data enclave (web); ODI Statewide Data Strategy 2026-2027 (web); SDSC F3i Supercomputing Center release 2026-07-16 (web); SDSC National Data Platform release 2026-08-10 (web); SDSC Sherlock FedRAMP release 2026-09-21 (web); SDSC data-driven agriculture 2026-01-13 (web); SDSU AI-Ready California launch 2026-07 (web); UCOP Research and Innovation VP (web)); 5 entity pages (ALERTCalifornia, UC San Diego; Lawrence Livermore National Laboratory; NORC at the University of Chicago; San Diego State University; Theresa A. Maldonado).
- Pages updated: the seven element reading lists; entity pages for Amazon Web Services, Anthropic, California Cradle-to-Career Data System, California Department of Technology, California Government Operations Agency, California Office of Data and Innovation, California Policy Lab, NVIDIA, Office of the Governor of California, San Diego Supercomputer Center, U.S. National Science Foundation, NAIRR Pilot, University of California Office of the President; concept pages CalCompute as coordinator vs operator, Funding models, NAIRR and the National Research Platform, Who can use CalCompute; wiki/index.md; analyses/Suggestions.md.
- Notable: the UCOP page is a profile page; it is listed on the Theresa A. Maldonado entity page, not on a reading list. The ALERTCalifornia homepage gives two camera counts ("more than 1,300" and "1,200 cameras deployed (as of February 2026)"), and the NAIRR Start-Up call gives two review times ("within 2 weeks" and "within 3 weeks"); each page records its own inconsistency. The SDSC agriculture story carries the date January 15, 2026; its address says 20260113. The ODI strategy is titled 2026-2027 but sets objectives for 2026-2028. No contradiction with another source page was found. bin/drive_push.py --check passes. The push has not run yet.

## [2026-11-09] query | California AI compute programs and resources (directory)
- Summary: wrote the first directory page from a sweep of all 354 source pages: 95 rows (39 programs, 28 resources, 21 organizations, 7 projects), each with its source pages and the check date 2026-11-09. No new source was added.
- Pages created: directories/California AI compute programs and resources.
- Pages updated: wiki/index.md (Directories is now 1; 562 pages).
- Notable: 40 rows are Statewide, 13 are National and 42 have no region. The source page California Jobs First regions names the 13 regions but lists no county or city for a region, so no row has a region name; the page flags the gap. Vendor credit programs whose source pages state no geographic eligibility have no row.

## [2026-11-09] query | Federal and state AI compute programs (concept)
- Summary: wrote a concept page with one table of 23 federal and California state programs and actions that fund or govern AI compute, with the amounts and dates that the source pages give.
- Pages created: concepts/Federal and state AI compute programs.
- Pages updated: wiki/index.md (Concepts is now 9).
- Notable: two contradiction flags. The NSF 26-508 round 2 letter of intent is Dec. 15, 2026 in the NSF solicitation and "December 15, 2027" in the NJIT listing. The UC AI Steering Committee was formed in March 2026 in the Regents item and "in May of 2026" in the UC press release.

## [2026-11-09] schema | Directory rows in the ingest and lint skills
- Summary: the ingest skill now updates a directory row and its Checked date, or adds a row for a new record. The lint skill now reports a directory row with no source link or no Checked date as an error.
- Pages created: none.
- Pages updated: .agents/skills/ingest/SKILL.md (step 6); .agents/skills/lint/SKILL.md.
- Notable: none.

## [2026-11-10] ingest | 10 consortium research sources from the Suggestions page
- Summary: ingested 10 of the 14 approved consortium research rows. None was a duplicate. The four rows that failed earlier stay approved: the FedRAMP marketplace address is still a script redirect, the cloud.gov address still serves a redirect stub, the F3I portal still serves a script-only sign-in app, and the City of Santa Ana address still serves a Laserfiche WebLink viewer with no document text. The CJF Playbook, the DOE awards list and the DOE user facilities page are rehosted in raw/web/; the rest stay in .cache/.
- Pages created: 10 source pages (ACCESS resource catalog feed (web); CASC member directory (web); CENIC research education and cultural community (web); CJF Investment Playbook 2025 (web); DOE Genesis Mission awards list 2026 (web); DOE Office of Science user facilities at a glance (web); NACo county AI use cases (web); NAIRR Pilot resource catalog feed (web); SLAC Genesis Mission phase II projects (web); UC MRPI current awards (web)); 4 entity pages (Coalition for Academic Scientific Computation; National Association of Counties; SLAC National Accelerator Laboratory; U.S. Department of Energy, Office of Science).
- Pages updated: element reading lists A, B, D, E, F and G; entity pages ACCESS, U.S. National Science Foundation; CENIC; California Jobs First; U.S. National Science Foundation, NAIRR Pilot; University of California Office of the President; concept pages Federal and state AI compute programs (new Genesis Mission row; NAIRR Pilot and CloudBank rows) and NAIRR and the National Research Platform; directory California AI compute programs and resources (8 rows updated, 16 rows added, now 111; the region gap note); wiki/index.md; analyses/Suggestions.md.
- Notable: the DOE list has 278 rows, which agrees with the "40 of the 278 projects" in the UC Regents item. The CJF Playbook lists the counties of each Jobs First region (p. 7), so the directory's region column can now be filled; that is not done yet. The Playbook names "North San Joaquin" where the regions page names "Northern San Joaquin"; the Playbook page flags it. The two JSON feeds have no date of issue. The DOE user facilities copy shows only the first 12 facilities. bin/drive_push.py --check passes. The push has not run yet. It would upload the CJF Playbook and the DOE awards list PDFs, with the rehosted originals of the earlier 2026-11-09 ingests.

## [2026-11-10] schema | directory columns
- Summary: the directory page format has new columns, in this order: Name, Kind, California region, Serves, Domains, Status, Access, Sources, Checked (user, Nov. 10, 2026). California region uses Statewide, National or the 13 Jobs First regions, spelled as on page 7 of the CJF Investment Playbook 2025. A row with a region name cites the Playbook. Serves and Domains use fixed lists. A cell with several values separates them with a semicolon and a space.
- Pages created: none.
- Pages updated: AGENTS.md (Page formats, Directory page); .agents/skills/lint/SKILL.md (a Serves, Domains or California region value outside its fixed list is an error).
- Notable: the ingest skill's directory rule names no columns, so it does not change.

## [2026-11-10] fix | California AI compute programs and resources (directory)
- Summary: rebuilt the directory in the new columns. All 111 rows have the new columns. It adds 60 rows: 56 Genesis Mission selections with a California address, 3 SLAC Genesis Mission Phase II projects and 1 UC MRPI award. The page now has 171 rows, all checked 2026-11-10.
- Pages created: none.
- Pages updated: directories/California AI compute programs and resources (table, Regions section, a new Serves and Domains section); wiki/index.md.
- Notable: 100 rows have a region name, 40 are Statewide, 13 are National and 18 are blank. The Playbook does not place UC San Diego, UC Davis or UC Merced, so their rows need a city from a cited source. The region gap note is gone. The directory now flags a contradiction: the Playbook spells "North San Joaquin", and the regions page spells "Northern San Joaquin". The NAIRR Pilot and ACCESS feeds, the CASC directory and the NACo use cases add no new rows: their California records already have rows. The CENIC community page lists members only, and the DOE user facilities copy gives no California computing facility, so they add no rows.

## [2026-11-10] schema | directory columns for action
- Summary: the directory page format now has 13 columns (user, Nov. 10, 2026). The order is Name, Kind, California region, Serves, Offers, Domains, Status, Cost, Access, Get access, Link, Sources, Checked. Offers uses a fixed list of eight values. Cost is Free, Fee, Credits or Not stated, with an optional note in parentheses. Get access gives the route as a source states it. Link is one public address of the record that a cited source page carries.
- Pages created: none.
- Pages updated: AGENTS.md (Page formats, Directory page); .agents/skills/lint/SKILL.md (three new checks for Offers and Cost values, Links and old Checked dates).
- Notable: the Link rule counts the raw or cached copy of a cited source as its text. Some source pages do not print the record's own address. The earlier rules stay: fixed lists for region, Serves and Domains, and no ratings or advice.

## [2026-11-10] fix | California AI compute programs and resources (directory refill)
- Summary: refilled all 171 rows in the 13 columns. The agent read the 69 resources and programs again against their source pages and raw or cached copies. Of these, 45 have a Link, 23 have a Cost, 39 have a Get access route, 52 have Offers and 55 have Serves. The 102 organizations and projects have 18 Links and 7 Offers cells. The row count, and every Name, Kind and California region, stay the same.
- Pages created: none.
- Pages updated: directories/California AI compute programs and resources (table, introduction, and the sections under the table); wiki/index.md.
- Notable: Serves has new groups in five rows: F3i Supercomputing Center (CSU), SDSC Expanse AI (Industry), ACCESS (Community colleges, Government, Industry), CloudBank (Community colleges) and Center for AI Safety Compute Cluster (UC). The ACCESS row now cites ACCESS homepage for "at no cost to you". Two routes are not open: the NVIDIA Academic Grant Program has a pause, and the Center for AI Safety cluster takes no new external applications. The NAIRR Pilot feed marks 8 resources as not able to take new awards. 13 Links are in a raw or cached copy only, not in the source page text. Offers has no value for compute with no stated type or for AI model access, so 17 resource and program rows have no Offers value.

## [2026-11-10] schema | entity pages for listed institutions and research institutions directory columns
- Summary: an institution that a directory page lists now gets an entity page, not only a publisher (maintainer, Nov. 10, 2026). The 13 columns stay for the compute programs directory. The research institutions directory has its own columns: Name, Designation, Control, City, Link, Sources, Checked. Designation is the Carnegie 2025 Research Activity Designation as Carnegie prints it, or National laboratory. Control is Public, Private or Federal.
- Pages created: none.
- Pages updated: AGENTS.md (Layout, entities/; Page formats, Entity page and Directory page); .agents/skills/ingest/SKILL.md (step 6: a directory row that names an institution adds or updates its entity page).
- Notable: Private stands for Carnegie's "Private not-for-profit" and "Private for-profit". City and Link appear only when a cited source states them.

## [2026-11-10] ingest | Carnegie 2025 Public Data File (web)
- Summary: ingested the 2025 Public Data File of the Carnegie Classification of Institutions of Higher Education (American Council on Education). It has 3,927 rows with the state, the city, the control and the 2025 Research Activity Designation of each institution. 54 California institutions have a designation: 14 Research 1, 16 Research 2 and 24 Research Colleges and Universities. The licence is CC BY-NC-SA 4.0, so the file is not rehosted (rehost: no) and bin/drive_push.py did not run.
- Pages created: sources/Carnegie 2025 Public Data File (web); entities/American Council on Education.
- Pages updated: elements/A - Landscape Analysis (Institutional); analyses/Suggestions (new row, ingested); wiki/index.md.
- Notable: the 2025 Research Activity Designation Public Data File (Feb. 13, 2025) lists the same 54 California institutions, but it has no control column, so the library uses the 2025 Public Data File only. The file gives no web addresses. It gives the Naval Postgraduate School the control value "Public".

## [2026-11-10] fix | California research institutions (new directory) and 57 institution entity pages
- Summary: new directory of 57 California research institutions: the 54 Carnegie institutions with a 2025 Research Activity Designation and the three DOE national laboratories. Each institution has an entity page.
- Pages created: directories/California research institutions; 46 entity pages (6 Research 1, 16 Research 2, 24 Research Colleges and Universities), each with a Bottom line from the Carnegie file and a gap line.
- Pages updated: entity pages UC Irvine, UCLA, UC Merced, UC Riverside, UC San Diego, UC Santa Cruz, Stanford University and San Diego State University (Carnegie lines in Bottom line and Sources); Lawrence Berkeley National Laboratory and Lawrence Livermore National Laboratory (new Bottom line); sources/LBNL 2024 US Data Center Energy Usage Report (Background gives the place and the Office of Science support, from the report's Citation and Acknowledgements); wiki/index.md.
- Notable: UC Santa Cruz had kind: person and tags [person, publisher]; it is now kind: institution with tags [institution, publisher]. Carnegie's membership and designations agree with the expected list. Carnegie prints "San Jose State University" and "Charles R Drew University of Medicine and Science"; the file names keep "San José" and "Charles R.". Link is blank in 56 rows: the Carnegie file has no addresses, the LBNL report carries none, and the LLNL page carries only http://www.llnl.gov/.

## [2026-11-10] schema | research institutions directory: region and coordinates
- Summary: the research institutions directory has three new columns, so a map can place each institution (maintainer, Nov. 10, 2026). The order is Name, Designation, Control, City, California region, Latitude, Longitude, Link, Sources, Checked. California region follows the rule of the compute programs directory. Latitude and Longitude are decimal degrees as a cited source prints them, or blank.
- Pages created: none.
- Pages updated: AGENTS.md (Page formats, Directory page).
- Notable: the rule forbids estimated, geocoded or remembered coordinates.

## [2026-11-10] fix | bin/grab.py takes zip files
- Summary: bin/grab.py now accepts a zip file (application/zip and application/x-zip-compressed). It keeps the zip as downloaded. The markitdown tool converts each file in the zip to the Markdown copy. bin/grab.py now runs markitdown on the file name in its own folder, so a zip copy does not print the local path.
- Pages created: none.
- Pages updated: bin/grab.py (the TYPES table and the markitdown call).
- Notable: the first download of the IPEDS file printed the local path in its Markdown copy. The agent removed that copy and its zip, which it had made a few minutes before, and downloaded the file again with the fix.

## [2026-11-10] ingest | IPEDS HD2025 Directory information (web) and three EPA FRS facility records (web)
- Summary: ingested the NCES IPEDS HD2025 directory file. It gives 5,985 institutions, with county, latitude and longitude by IPEDS unit ID. Also ingested the EPA Facility Registry Service (FRS) records of the three laboratories: LBNL, LLNL and SLAC. All four are U.S. Government works, so the library rehosts them in raw/web/ (rehost: yes).
- Pages created: sources/IPEDS HD2025 Directory information (web); sources/EPA FRS facility record LBNL (web); sources/EPA FRS facility record LLNL (web); sources/EPA FRS facility record SLAC (web); entities/U.S. Department of Education, National Center for Education Statistics; entities/U.S. Environmental Protection Agency.
- Pages updated: elements/A - Landscape Analysis (Primary); analyses/Suggestions (four new rows, ingested); wiki/index.md.
- Notable: NCES gives the HD file only as a zip with one CSV file. The full CSV file is in the Markdown copy, about 4.5 MB, not filtered. The FRS has many records for each laboratory. The library uses one main-site record for each. bin/drive_push.py did not run. It uploads only PDF and office files, so these files would add only guide entries.

## [2026-11-10] fix | California research institutions (region and coordinates)
- Summary: all 57 rows now have a California region, a latitude and a longitude. The 54 colleges and universities match the IPEDS file by unit ID, with the same name and city. The county from IPEDS or FRS gives the Jobs First region from page 7 of the Playbook.
- Pages created: none.
- Pages updated: directories/California research institutions (table, introduction bullets, notes, source_count); wiki/index.md.
- Notable: Los Angeles County has 20 rows, Bay Area 13, Central Coast 6 and Southern Border 5. Inland SoCal and Orange County have 3 each, and Capital has 2. Central San Joaquin, Kern County, North San Joaquin, North State and Redwood have 1 each. Sierra has none. The LLNL record is for the Livermore main site; FRS also has records for Site 300 in San Joaquin County. The institution entity pages do not have the new facts yet.
