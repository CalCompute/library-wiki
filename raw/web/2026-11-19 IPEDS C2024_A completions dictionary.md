---
url: https://nces.ed.gov/ipeds/datacenter/data/C2024_A_Dict.zip
fetched: 2026-11-19
publisher: "U.S. Department of Education, National Center for Education Statistics (NCES), IPEDS"
published: unknown
original: 2026-11-19 IPEDS C2024_A completions dictionary.zip
rehost: yes
---

_Markdown copy of 2026-11-19 IPEDS C2024_A completions dictionary.zip, made 2026-11-19. The original is the authority._
Content from the zip file `2026-11-19 IPEDS C2024_A completions dictionary.zip`:

## File: C2024_a_dict.xlsx

## Introduction
| File Documentation for the Completions Data File, 2023-24 | Unnamed: 1 |
| --- | --- |
| (Provisional release) | NaN |
| NaN | NaN |
| Filename | C2024\_A |
| Provisional release: | September 2025 |
| NaN | NaN |
| Overview | This file contains the number of awards by type of program, level of award (certificate or degree), first or second major and by race/ethnicity and gender. Data covers all awards granted between July 1, 2023 and June 30, 2024.  Type of program is categorized according to the 2020 Classification of Instructional Programs (CIP), a detailed coding system for postsecondary instructional programs.  The 2010 CIP was used to categorize programs for Completions data collected from 2009-10 through 2018-19.  Information on the CIP classification taxonomy, including a crosswalk between CIP 2010 and 2020 is available at https://nces.ed.gov/ipeds/cipcode/resources.aspx?y=56 . Beginning in  2019-20, the less than 1 year certificate award level is divided into the following two award levels: certificates of less than 12 weeks and certificates of at least 12 weeks but less than 1 year.\n\nThis file contains multiple records per institution. Each record is uniquely defined by the variables IPEDS ID (UNITID), classification of instructional program (CIPCODE), first or second major (MAJORNUM) and award level (AWLEVEL).  Each record will contain the total awards,  awards for men and women, and the total awards and awards for men and women for all nine race/ethnicity categories. |
| Note: | Provisional release data have undergone all NCES data quality control procedures. Data are imputed for nonresponding institutions. These data are used for First Look (Provisional Data) Web Tables. Final release data include revisions to the provisional release data that have been made by institutions during the subsequent data collection year. The final release data can be used when the most up to date data are required; however, these data may not match First Look Web Tables based on provisional data. |
| NaN | NaN |
| Contents of spreadsheet | NaN |
| NaN | NaN |
| Varlist | Variable list: Lists all variables in the table. Includes the variable name, variable label and the Data type, format and maximum field width of each variable.  The data type describes a variable as either a numeric (N) or Alphanumeric (A) and the format of a variable defines a variable as either continuous (Cont) or categorical (Disc).  It all also lists the variable name of all imputation flag variables for each continuous variable. Imputation flag variable describes whether a value for the corresponding variable was reported, imputed or not applicable. |
| Description | Long description or glossary definition of a variable. |
| Frequencies | This worksheet contains the code values for of all categorical variables in the data file. It also lists the frequency and percent distribution for each code value by variable. |
| Statistics | This worksheet lists the sum, mean, minimum and maximum values of all continuous variables in the data file. |
| Imputation code values | This worksheet lists the code values for all imputation flag variables. |

## Varlist
| varNumber | varName | DataType | FieldWidth | format | imputationvar | varTitle |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | UNITID | N | 6 | Cont | NaN | Unique identification number of the institution |
| 35000 | CIPCODE | A | 7 | Disc | NaN | CIP Code -  2020 Classification |
| 31005 | MAJORNUM | N | 1 | Disc | NaN | First or Second Major |
| 35005 | AWLEVEL | N | 2 | Disc | NaN | Award Level code |
| 31130 | CTOTALT | N | 6 | Cont | XCTOTALT | Grand total |
| 31085 | CTOTALM | N | 6 | Cont | XCTOTALM | Grand total men |
| 31090 | CTOTALW | N | 6 | Cont | XCTOTALW | Grand total women |
| 31580 | CAIANT | N | 6 | Cont | XCAIANT | American Indian or Alaska Native total |
| 31515 | CAIANM | N | 6 | Cont | XCAIANM | American Indian or Alaska Native men |
| 31520 | CAIANW | N | 6 | Cont | XCAIANW | American Indian or Alaska Native women |
| 31585 | CASIAT | N | 6 | Cont | XCASIAT | Asian total |
| 31525 | CASIAM | N | 6 | Cont | XCASIAM | Asian men |
| 31530 | CASIAW | N | 6 | Cont | XCASIAW | Asian women |
| 31590 | CBKAAT | N | 6 | Cont | XCBKAAT | Black or African American total |
| 31535 | CBKAAM | N | 6 | Cont | XCBKAAM | Black or African American men |
| 31540 | CBKAAW | N | 6 | Cont | XCBKAAW | Black or African American women |
| 31575 | CHISPT | N | 6 | Cont | XCHISPT | Hispanic or Latino total |
| 31505 | CHISPM | N | 6 | Cont | XCHISPM | Hispanic or Latino men |
| 31510 | CHISPW | N | 6 | Cont | XCHISPW | Hispanic or Latino women |
| 31595 | CNHPIT | N | 6 | Cont | XCNHPIT | Native Hawaiian or Other Pacific Islander total |
| 31545 | CNHPIM | N | 6 | Cont | XCNHPIM | Native Hawaiian or Other Pacific Islander men |
| 31550 | CNHPIW | N | 6 | Cont | XCNHPIW | Native Hawaiian or Other Pacific Islander women |
| 31600 | CWHITT | N | 6 | Cont | XCWHITT | White total |
| 31555 | CWHITM | N | 6 | Cont | XCWHITM | White men |
| 31560 | CWHITW | N | 6 | Cont | XCWHITW | White women |
| 31605 | C2MORT | N | 6 | Cont | XC2MORT | Two or more races total |
| 31565 | C2MORM | N | 6 | Cont | XC2MORM | Two or more races men |
| 31570 | C2MORW | N | 6 | Cont | XC2MORW | Two or more races women |
| 31125 | CUNKNT | N | 6 | Cont | XCUNKNT | Race/ethnicity unknown total |
| 31075 | CUNKNM | N | 6 | Cont | XCUNKNM | Race/ethnicity unknown men |
| 31080 | CUNKNW | N | 6 | Cont | XCUNKNW | Race/ethnicity unknown women |
| 31095 | CNRALT | N | 6 | Cont | XCNRALT | U.S. Nonresident total |
| 31015 | CNRALM | N | 6 | Cont | XCNRALM | U.S. Nonresident men |
| 31020 | CNRALW | N | 6 | Cont | XCNRALW | U.S. Nonresident women |

## Description
| varNumber | varName | longDescription |
| --- | --- | --- |
| 1 | UNITID | NaN |
| 35000 | CIPCODE | Classification of instrucional Program (CIP) code. A six-digit code in the form xx.xxxx that identifies instructional  program specialties within educational institutions.    \n\nThe Classification of Instructional Programs (CIP) provides a taxonomic scheme that supports the accurate tracking and reporting of fields of study and program completions activity. CIP was originally developed by the U.S. Department of Education's National Center for Education Statistics (NCES) in 1980, with revisions occurring in 1985, 1990, 2000, 2010 and 2020.\n\nInformation on the CIP classification taxonomy, including a crosswalk between CIP 2010 and 2020 is available at https://nces.ed.gov/ipeds/cipcode/resources.aspx?y=56 |
| 31005 | MAJORNUM | First or Second Major |
| 35005 | AWLEVEL | Award level code\n\nThe twelve award levels under which completions can be reported are:\n\nCertificates of less than 12 weeks includes programs of less than 300 clock hours, or, Less than 9 SEMESTER or TRIMESTER credit hours, or Less than 13 QUARTER credit hours\nCertificates of at least 12 weeks but less than 1 year includes programs of 300-899 clock hours, or 9-29 SEMESTER or TRIMESTER credit hours, or 13-44 QUARTER credit hours\nCertificates of at least 1 year but less the 2 years includes programs of at least 900, but less than 1800 clock hours, or at least 30, but less than 60 SEMESTER OR TRIMESTER HOURS, or at least 45, but less than 90 QUARTER HOURS\nAssociate's degree\nCertificates of at least 2 years but less the 4 years includes programs of 1800 or more clock hours, or 60 or more SEMESTER OR TRIMESTER credit hours, or 90 or more QUARTER credit hours\nBachelor's degree\nPostbaccalaureate certificate\nMaster's degree\nPost-master's certificate\nDoctor's degree - research/scholarship\nDoctor's degree - professional practice\nDoctor's degree - other |
| 31130 | CTOTALT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to all recipients, across all race/ethnicities and both genders |
| 31085 | CTOTALM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Grand total men |
| 31090 | CTOTALW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Grand total women |
| 31580 | CAIANT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to American Indian or Alaska Native men and women.\n\nAmerican Indian or Alaska Native - A person having origins in any of the original peoples of North and South America (including Central America) who maintains cultural identification through tribal affiliation or community attachment. |
| 31515 | CAIANM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to American Indian or Alaska Native men.\n\nAmerican Indian or Alaska Native - A person having origins in any of the original peoples of North and South America (including Central America) who maintains cultural identification through tribal affiliation or community attachment. |
| 31520 | CAIANW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to American Indian or Alaska Native women.\n\nAmerican Indian or Alaska Native - A person having origins in any of the original peoples of North and South America (including Central America) who maintains cultural identification through tribal affiliation or community attachment. |
| 31585 | CASIAT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Asian men and women.\n\nAsian - A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian Subcontinent, including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. |
| 31525 | CASIAM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Asian men.\n\nAsian - A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian Subcontinent, including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. |
| 31530 | CASIAW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Asian women.\n\nAsian - A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian Subcontinent, including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. |
| 31590 | CBKAAT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Black or African American men and women.\n\nBlack or African American - A person having origins in any of the black racial groups of Africa |
| 31535 | CBKAAM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Black or African American men.\n\nBlack or African American - A person having origins in any of the black racial groups of Africa |
| 31540 | CBKAAW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Black or African American women.\n\nBlack or African American - A person having origins in any of the black racial groups of Africa |
| 31575 | CHISPT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Hispanic or Latino men and women.\n\nHispanic or Latino - A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. |
| 31505 | CHISPM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Hispanic or Latino men.\n\nHispanic or Latino - A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. |
| 31510 | CHISPW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Hispanic or Latino women.\n\nHispanic or Latino - A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. |
| 31595 | CNHPIT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Native Hawaiian or Other Pacific Islanders men and women.\n\nNative Hawaiian or Other Pacific Islanders - A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. |
| 31545 | CNHPIM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Native Hawaiian or Other Pacific Islanders men.\n\nNative Hawaiian or Other Pacific Islanders - A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. |
| 31550 | CNHPIW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Native Hawaiian or Other Pacific Islanders women.\n\nNative Hawaiian or Other Pacific Islanders - A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. |
| 31600 | CWHITT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to White men and women.\n\nWhite - A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. |
| 31555 | CWHITM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to White men.\n\nWhite - A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. |
| 31560 | CWHITW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to White women.\n\nWhite - A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. |
| 31605 | C2MORT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to two or more races men and women.\n\nTwo or more races - Category used by institutions to report persons who selected more than one race. |
| 31565 | C2MORM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to two or more races men.\n\nTwo or more races - Category used by institutions to report persons who selected more than one race. |
| 31570 | C2MORW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to two or more races women.\n\nTwo or more races - Category used by institutions to report persons who selected more than one race. |
| 31125 | CUNKNT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to race/ethnicity unknown men and women.                                                           \nRace/ethnicity unknown - Category used to classify students or employees whose race/ethnicity is not known, and institutions are unable to place them in one of the specified racial/ethnic categories. |
| 31075 | CUNKNM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Race/ethnicity unknown men                                               \n\nRace/ethnicity unknown - Category used to classify students or employees whose race/ethnicity is not known and institutions are unable to place them in one of the specified racial/ethnic categories. |
| 31080 | CUNKNW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to Race/ethnicity unknown women                                               \n\nRace/ethnicity unknown - Category used to classify students or employees whose race/ethnicity is not known and institutions are unable to place them in one of the specified racial/ethnic categories. |
| 31095 | CNRALT | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to U.S. Nonresident men and women.\n\nU.S. Nonresident  - A person who is not a citizen or national of the United States and who is in this country on a visa or temporary basis and does not have the right to remain indefinitely. |
| 31015 | CNRALM | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to U.S. Nonresident men.\n\nU.S. Nonresident - A person who is not a citizen or national of the United States and who is in this country on a visa or temporary basis and does not have the right to remain indefinitely. |
| 31020 | CNRALW | Awards/degrees conferred between July 1, 2023 and June 30, 2024 to U.S. Nonresident women.\n\nU.S. Nonresident - A person who is not a citizen or national of the United States and who is in this country on a visa or temporary basis and does not have the right to remain indefinitely. |

## Frequencies
| varNumber | VarName | CodeValue | ValueLabel | Frequency | Percent |
| --- | --- | --- | --- | --- | --- |
| 31005 | MAJORNUM | 1.0000 | First major | 1542031 | 91.33 |
| 31005 | MAJORNUM | 2.0000 | Second major | 146440 | 8.67 |
| 35000 | CIPCODE | 99.0000 | Grand total | 41867 | 2.48 |
| 35000 | CIPCODE | 1.0000 | Agriculture, General | 715 | 0.04 |
| 35000 | CIPCODE | 1.0101 | Agricultural Business and Management, General | 657 | 0.04 |
| 35000 | CIPCODE | 1.0102 | Agribusiness/Agricultural Business Operations | 879 | 0.05 |
| 35000 | CIPCODE | 1.0103 | Agricultural Economics | 251 | 0.01 |
| 35000 | CIPCODE | 1.0104 | Farm/Farm and Ranch Management | 262 | 0.02 |
| 35000 | CIPCODE | 1.0105 | Agricultural/Farm Supplies Retailing and Wholesaling | 73 | 0.00 |
| 35000 | CIPCODE | 1.0106 | Agricultural Business Technology/Technician | 43 | 0.00 |
| 35000 | CIPCODE | 1.0199 | Agricultural Business and Management, Other | 61 | 0.00 |
| 35000 | CIPCODE | 1.0201 | Agricultural Mechanization, General | 143 | 0.01 |
| 35000 | CIPCODE | 1.0204 | Agricultural Power Machinery Operation | 50 | 0.00 |
| 35000 | CIPCODE | 1.0205 | Agricultural Mechanics and Equipment/Machine Technology/Technician | 219 | 0.01 |
| 35000 | CIPCODE | 1.0207 | Irrigation Management Technology/Technician | 4 | 0.00 |
| 35000 | CIPCODE | 1.0299 | Agricultural Mechanization, Other | 16 | 0.00 |
| 35000 | CIPCODE | 1.0301 | Agricultural Production Operations, General | 377 | 0.02 |
| 35000 | CIPCODE | 1.0302 | Animal/Livestock Husbandry and Production | 290 | 0.02 |
| 35000 | CIPCODE | 1.0303 | Aquaculture | 99 | 0.01 |
| 35000 | CIPCODE | 1.0304 | Crop Production | 279 | 0.02 |
| 35000 | CIPCODE | 1.0306 | Dairy Husbandry and Production | 45 | 0.00 |
| 35000 | CIPCODE | 1.0307 | Horse Husbandry/Equine Science and Management | 218 | 0.01 |
| 35000 | CIPCODE | 1.0308 | Agroecology and Sustainable Agriculture | 436 | 0.03 |
| 35000 | CIPCODE | 1.0399 | Agricultural Production Operations, Other | 37 | 0.00 |
| 35000 | CIPCODE | 1.0401 | Agricultural and Food Products Processing | 116 | 0.01 |
| 35000 | CIPCODE | 1.0504 | Dog/Pet/Animal Grooming | 46 | 0.00 |
| 35000 | CIPCODE | 1.0505 | Animal Training | 25 | 0.00 |
| 35000 | CIPCODE | 1.0507 | Equestrian/Equine Studies | 266 | 0.02 |
| 35000 | CIPCODE | 1.0508 | Taxidermy/Taxidermist | 5 | 0.00 |
| 35000 | CIPCODE | 1.0599 | Agricultural and Domestic Animal Services, Other | 28 | 0.00 |
| 35000 | CIPCODE | 1.0601 | Applied Horticulture/Horticulture Operations, General | 922 | 0.05 |
| 35000 | CIPCODE | 1.0603 | Ornamental Horticulture | 90 | 0.01 |
| 35000 | CIPCODE | 1.0604 | Greenhouse Operations and Management | 97 | 0.01 |
| 35000 | CIPCODE | 1.0605 | Landscaping and Groundskeeping | 548 | 0.03 |
| 35000 | CIPCODE | 1.0606 | Plant Nursery Operations and Management | 178 | 0.01 |
| 35000 | CIPCODE | 1.0607 | Turf and Turfgrass Management | 247 | 0.01 |
| 35000 | CIPCODE | 1.0608 | Floriculture/Floristry Operations and Management | 163 | 0.01 |
| 35000 | CIPCODE | 1.0609 | Public Horticulture | 3 | 0.00 |
| 35000 | CIPCODE | 1.0610 | Urban and Community Horticulture | 17 | 0.00 |
| 35000 | CIPCODE | 1.0699 | Applied Horticulture/Horticultural Business Services, Other | 54 | 0.00 |
| 35000 | CIPCODE | 1.0701 | International Agriculture | 63 | 0.00 |
| 35000 | CIPCODE | 1.0801 | Agricultural and Extension Education Services | 121 | 0.01 |
| 35000 | CIPCODE | 1.0802 | Agricultural Communication/Journalism | 102 | 0.01 |
| 35000 | CIPCODE | 1.0899 | Agricultural Public Services, Other | 12 | 0.00 |
| 35000 | CIPCODE | 1.0901 | Animal Sciences, General | 646 | 0.04 |
| 35000 | CIPCODE | 1.0902 | Agricultural Animal Breeding | 12 | 0.00 |
| 35000 | CIPCODE | 1.0903 | Animal Health | 35 | 0.00 |
| 35000 | CIPCODE | 1.0904 | Animal Nutrition | 6 | 0.00 |
| 35000 | CIPCODE | 1.0905 | Dairy Science | 60 | 0.00 |
| 35000 | CIPCODE | 1.0906 | Livestock Management | 55 | 0.00 |
| 35000 | CIPCODE | 1.0907 | Poultry Science | 53 | 0.00 |
| 35000 | CIPCODE | 1.0999 | Animal Sciences, Other | 46 | 0.00 |
| 35000 | CIPCODE | 1.1001 | Food Science | 360 | 0.02 |
| 35000 | CIPCODE | 1.1002 | Food Technology and Processing | 119 | 0.01 |
| 35000 | CIPCODE | 1.1003 | Brewing Science | 103 | 0.01 |
| 35000 | CIPCODE | 1.1004 | Viticulture and Enology | 191 | 0.01 |
| 35000 | CIPCODE | 1.1005 | Zymology/Fermentation Science | 26 | 0.00 |
| 35000 | CIPCODE | 1.1099 | Food Science and Technology, Other | 77 | 0.00 |
| 35000 | CIPCODE | 1.1101 | Plant Sciences, General | 231 | 0.01 |
| 35000 | CIPCODE | 1.1102 | Agronomy and Crop Science | 355 | 0.02 |
| 35000 | CIPCODE | 1.1103 | Horticultural Science | 271 | 0.02 |
| 35000 | CIPCODE | 1.1104 | Agricultural and Horticultural Plant Breeding | 25 | 0.00 |
| 35000 | CIPCODE | 1.1105 | Plant Protection and Integrated Pest Management | 91 | 0.01 |
| 35000 | CIPCODE | 1.1106 | Range Science and Management | 104 | 0.01 |
| 35000 | CIPCODE | 1.1199 | Plant Sciences, Other | 34 | 0.00 |
| 35000 | CIPCODE | 1.1201 | Soil Science and Agronomy, General | 167 | 0.01 |
| 35000 | CIPCODE | 1.1202 | Soil Chemistry and Physics | 4 | 0.00 |
| 35000 | CIPCODE | 1.1299 | Soil Sciences, Other | 25 | 0.00 |
| 35000 | CIPCODE | 1.1302 | Pre-Veterinary Studies | 186 | 0.01 |
| 35000 | CIPCODE | 1.1399 | Agriculture/Veterinary Preparatory Programs, Other | 7 | 0.00 |
| 35000 | CIPCODE | 1.8001 | Veterinary Medicine | 108 | 0.01 |
| 35000 | CIPCODE | 1.8101 | Veterinary Sciences/Veterinary Clinical Sciences, General | 117 | 0.01 |
| 35000 | CIPCODE | 1.8102 | Comparative and Laboratory Animal Medicine | 26 | 0.00 |
| 35000 | CIPCODE | 1.8103 | Large Animal/Food Animal and Equine Surgery and Medicine | 7 | 0.00 |
| 35000 | CIPCODE | 1.8104 | Small/Companion Animal Surgery and Medicine | 8 | 0.00 |
| 35000 | CIPCODE | 1.8106 | Veterinary Infectious Diseases | 10 | 0.00 |
| 35000 | CIPCODE | 1.8107 | Veterinary Microbiology and Immunobiology | 17 | 0.00 |
| 35000 | CIPCODE | 1.8108 | Veterinary Pathology and Pathobiology | 35 | 0.00 |
| 35000 | CIPCODE | 1.8109 | Veterinary Physiology | 6 | 0.00 |
| 35000 | CIPCODE | 1.8110 | Veterinary Preventive Medicine, Epidemiology, and Public Health | 18 | 0.00 |
| 35000 | CIPCODE | 1.8199 | Veterinary Biomedical and Clinical Sciences, Other | 6 | 0.00 |
| 35000 | CIPCODE | 1.8201 | Veterinary Administrative Services, General | 3 | 0.00 |
| 35000 | CIPCODE | 1.8202 | Veterinary Office Management/Administration | 8 | 0.00 |
| 35000 | CIPCODE | 1.8203 | Veterinary Reception/Receptionist | 4 | 0.00 |
| 35000 | CIPCODE | 1.8204 | Veterinary Administrative/Executive Assistant and Veterinary Secretary | 4 | 0.00 |
| 35000 | CIPCODE | 1.8301 | Veterinary/Animal Health Technology/Technician and Veterinary Assistant | 1104 | 0.07 |
| 35000 | CIPCODE | 1.8399 | Veterinary/Animal Health Technologies/Technicians, Other | 15 | 0.00 |
| 35000 | CIPCODE | 1.9999 | Agricultural/Animal/Plant/Veterinary Science and Related Fields, Other | 155 | 0.01 |
| 35000 | CIPCODE | 3.0101 | Natural Resources/Conservation, General | 695 | 0.04 |
| 35000 | CIPCODE | 3.0103 | Environmental Studies | 2506 | 0.15 |
| 35000 | CIPCODE | 3.0104 | Environmental Science | 2825 | 0.17 |
| 35000 | CIPCODE | 3.0199 | Natural Resources Conservation and Research, Other | 113 | 0.01 |
| 35000 | CIPCODE | 3.0201 | Environmental/Natural Resources Management and Policy, General | 341 | 0.02 |
| 35000 | CIPCODE | 3.0204 | Environmental/Natural Resource Economics | 85 | 0.01 |
| 35000 | CIPCODE | 3.0205 | Water, Wetlands, and Marine Resources Management | 148 | 0.01 |
| 35000 | CIPCODE | 3.0206 | Land Use Planning and Management/Development | 60 | 0.00 |
| 35000 | CIPCODE | 3.0207 | Environmental/Natural Resource Recreation and Tourism | 74 | 0.00 |
| 35000 | CIPCODE | 3.0208 | Environmental/Natural Resources Law Enforcement and Protective Services | 102 | 0.01 |
| 35000 | CIPCODE | 3.0209 | Energy and Environmental Policy | 46 | 0.00 |
| 35000 | CIPCODE | 3.0299 | Environmental/Natural Resources Management and Policy, Other | 125 | 0.01 |
| 35000 | CIPCODE | 3.0301 | Fishing and Fisheries Sciences and Management | 119 | 0.01 |
| 35000 | CIPCODE | 3.0501 | Forestry, General | 240 | 0.01 |
| 35000 | CIPCODE | 3.0502 | Forest Sciences and Biology | 86 | 0.01 |
| 35000 | CIPCODE | 3.0506 | Forest Management/Forest Resources Management | 96 | 0.01 |
| 35000 | CIPCODE | 3.0508 | Urban Forestry | 82 | 0.00 |
| 35000 | CIPCODE | 3.0509 | Wood Science and Wood Products/Pulp and Paper Technology/Technician | 41 | 0.00 |
| 35000 | CIPCODE | 3.0510 | Forest Resources Production and Management | 30 | 0.00 |
| 35000 | CIPCODE | 3.0511 | Forest Technology/Technician | 160 | 0.01 |
| 35000 | CIPCODE | 3.0599 | Forestry, Other | 52 | 0.00 |
| 35000 | CIPCODE | 3.0601 | Wildlife, Fish and Wildlands Science and Management | 395 | 0.02 |
| 35000 | CIPCODE | 3.9999 | Natural Resources and Conservation, Other | 72 | 0.00 |
| 35000 | CIPCODE | 4.0200 | Pre-Architecture Studies | 27 | 0.00 |
| 35000 | CIPCODE | 4.0201 | Architecture | 521 | 0.03 |
| 35000 | CIPCODE | 4.0202 | Architectural Design | 18 | 0.00 |
| 35000 | CIPCODE | 4.0299 | Architecture, Other | 4 | 0.00 |
| 35000 | CIPCODE | 4.0301 | City/Urban, Community, and Regional Planning | 591 | 0.04 |
| 35000 | CIPCODE | 4.0401 | Environmental Design/Architecture | 190 | 0.01 |
| 35000 | CIPCODE | 4.0402 | Healthcare Environment Design/Architecture | 16 | 0.00 |
| 35000 | CIPCODE | 4.0403 | Sustainable Design/Architecture | 17 | 0.00 |
| 35000 | CIPCODE | 4.0499 | Environmental Design, Other | 3 | 0.00 |
| 35000 | CIPCODE | 4.0501 | Interior Architecture | 173 | 0.01 |
| 35000 | CIPCODE | 4.0601 | Landscape Architecture | 260 | 0.02 |
| 35000 | CIPCODE | 4.0801 | Architectural History and Criticism, General | 89 | 0.01 |
| 35000 | CIPCODE | 4.0802 | Architectural Conservation | 3 | 0.00 |
| 35000 | CIPCODE | 4.0803 | Architectural Studies | 30 | 0.00 |
| 35000 | CIPCODE | 4.0901 | Architectural Technology/Technician | 358 | 0.02 |
| 35000 | CIPCODE | 4.0902 | Architectural and Building Sciences/Technology | 514 | 0.03 |
| 35000 | CIPCODE | 4.0999 | Architectural Sciences and Technology, Other | 6 | 0.00 |
| 35000 | CIPCODE | 4.1001 | Real Estate Development | 79 | 0.00 |
| 35000 | CIPCODE | 4.9999 | Architecture and Related Services, Other | 93 | 0.01 |
| 35000 | CIPCODE | 5.0101 | African Studies | 334 | 0.02 |
| 35000 | CIPCODE | 5.0102 | American/United States Studies/Civilization | 869 | 0.05 |
| 35000 | CIPCODE | 5.0103 | Asian Studies/Civilization | 697 | 0.04 |
| 35000 | CIPCODE | 5.0104 | East Asian Studies | 390 | 0.02 |
| 35000 | CIPCODE | 5.0105 | Russian, Central European, East European and Eurasian Studies | 106 | 0.01 |
| 35000 | CIPCODE | 5.0106 | European Studies/Civilization | 249 | 0.01 |
| 35000 | CIPCODE | 5.0107 | Latin American Studies | 769 | 0.05 |
| 35000 | CIPCODE | 5.0108 | Near and Middle Eastern Studies | 368 | 0.02 |
| 35000 | CIPCODE | 5.0109 | Pacific Area/Pacific Rim Studies | 27 | 0.00 |
| 35000 | CIPCODE | 5.0110 | Russian Studies | 264 | 0.02 |
| 35000 | CIPCODE | 5.0111 | Scandinavian Studies | 40 | 0.00 |
| 35000 | CIPCODE | 5.0112 | South Asian Studies | 72 | 0.00 |
| 35000 | CIPCODE | 5.0113 | Southeast Asian Studies | 31 | 0.00 |
| 35000 | CIPCODE | 5.0114 | Western European Studies | 32 | 0.00 |
| 35000 | CIPCODE | 5.0115 | Canadian Studies | 14 | 0.00 |
| 35000 | CIPCODE | 5.0118 | Slavic Studies | 21 | 0.00 |
| 35000 | CIPCODE | 5.0119 | Caribbean Studies | 13 | 0.00 |
| 35000 | CIPCODE | 5.0120 | Ural-Altaic and Central Asian Studies | 12 | 0.00 |
| 35000 | CIPCODE | 5.0121 | Commonwealth Studies | 4 | 0.00 |
| 35000 | CIPCODE | 5.0122 | Regional Studies (U.S., Canadian, Foreign) | 89 | 0.01 |
| 35000 | CIPCODE | 5.0123 | Chinese Studies | 133 | 0.01 |
| 35000 | CIPCODE | 5.0124 | French Studies | 191 | 0.01 |
| 35000 | CIPCODE | 5.0125 | German Studies | 218 | 0.01 |
| 35000 | CIPCODE | 5.0126 | Italian Studies | 183 | 0.01 |
| 35000 | CIPCODE | 5.0127 | Japanese Studies | 88 | 0.01 |
| 35000 | CIPCODE | 5.0128 | Korean Studies | 15 | 0.00 |
| 35000 | CIPCODE | 5.0130 | Spanish and Iberian Studies | 60 | 0.00 |
| 35000 | CIPCODE | 5.0133 | Irish Studies | 7 | 0.00 |
| 35000 | CIPCODE | 5.0134 | Latin American and Caribbean Studies | 144 | 0.01 |
| 35000 | CIPCODE | 5.0135 | Appalachian Studies | 9 | 0.00 |
| 35000 | CIPCODE | 5.0199 | Area Studies, Other | 387 | 0.02 |
| 35000 | CIPCODE | 5.0200 | Ethnic Studies | 408 | 0.02 |
| 35000 | CIPCODE | 5.0201 | African-American/Black Studies | 1025 | 0.06 |
| 35000 | CIPCODE | 5.0202 | American Indian/Native American Studies | 511 | 0.03 |
| 35000 | CIPCODE | 5.0203 | Hispanic-American, Puerto Rican, and Mexican-American/Chicano Studies | 361 | 0.02 |
| 35000 | CIPCODE | 5.0206 | Asian-American Studies | 111 | 0.01 |
| 35000 | CIPCODE | 5.0207 | Women's Studies | 2041 | 0.12 |
| 35000 | CIPCODE | 5.0208 | Gay/Lesbian Studies | 80 | 0.00 |
| 35000 | CIPCODE | 5.0209 | Folklore Studies | 48 | 0.00 |
| 35000 | CIPCODE | 5.0210 | Disability Studies | 135 | 0.01 |
| 35000 | CIPCODE | 5.0211 | Deaf Studies | 130 | 0.01 |
| 35000 | CIPCODE | 5.0212 | Comparative Group Studies | 45 | 0.00 |
| 35000 | CIPCODE | 5.0299 | Ethnic, Cultural Minority, Gender, and Group Studies, Other | 760 | 0.05 |
| 35000 | CIPCODE | 5.9999 | Area, Ethnic, Cultural, Gender, and Group Studies, Other | 43 | 0.00 |
| 35000 | CIPCODE | 9.0100 | Communication, General | 1781 | 0.11 |
| 35000 | CIPCODE | 9.0101 | Speech Communication and Rhetoric | 3588 | 0.21 |
| 35000 | CIPCODE | 9.0102 | Mass Communication/Media Studies | 1611 | 0.10 |
| 35000 | CIPCODE | 9.0199 | Communication and Media Studies, Other | 593 | 0.04 |
| 35000 | CIPCODE | 9.0401 | Journalism | 1870 | 0.11 |
| 35000 | CIPCODE | 9.0402 | Broadcast Journalism | 304 | 0.02 |
| 35000 | CIPCODE | 9.0404 | Photojournalism | 79 | 0.00 |
| 35000 | CIPCODE | 9.0406 | Cultural Journalism | 4 | 0.00 |
| 35000 | CIPCODE | 9.0407 | Science/Health/Environmental Journalism | 9 | 0.00 |
| 35000 | CIPCODE | 9.0499 | Journalism, Other | 219 | 0.01 |
| 35000 | CIPCODE | 9.0701 | Radio and Television | 856 | 0.05 |
| 35000 | CIPCODE | 9.0702 | Digital Communication and Media/Multimedia | 1993 | 0.12 |
| 35000 | CIPCODE | 9.0799 | Radio, Television, and Digital Communication, Other | 179 | 0.01 |
| 35000 | CIPCODE | 9.0900 | Public Relations, Advertising, and Applied Communication | 796 | 0.05 |
| 35000 | CIPCODE | 9.0901 | Organizational Communication, General | 454 | 0.03 |
| 35000 | CIPCODE | 9.0902 | Public Relations/Image Management | 758 | 0.04 |
| 35000 | CIPCODE | 9.0903 | Advertising | 506 | 0.03 |
| 35000 | CIPCODE | 9.0904 | Political Communication | 77 | 0.00 |
| 35000 | CIPCODE | 9.0905 | Health Communication | 304 | 0.02 |
| 35000 | CIPCODE | 9.0906 | Sports Communication | 362 | 0.02 |
| 35000 | CIPCODE | 9.0907 | International and Intercultural Communication | 126 | 0.01 |
| 35000 | CIPCODE | 9.0908 | Technical and Scientific Communication | 129 | 0.01 |
| 35000 | CIPCODE | 9.0909 | Communication Management and Strategic Communications | 260 | 0.02 |
| 35000 | CIPCODE | 9.0999 | Public Relations, Advertising, and Applied Communication, Other | 246 | 0.01 |
| 35000 | CIPCODE | 9.1001 | Publishing | 131 | 0.01 |
| 35000 | CIPCODE | 9.9999 | Communication, Journalism, and Related Programs, Other | 364 | 0.02 |
| 35000 | CIPCODE | 10.0105 | Communications Technology/Technician | 231 | 0.01 |
| 35000 | CIPCODE | 10.0201 | Photographic and Film/Video Technology/Technician | 591 | 0.04 |
| 35000 | CIPCODE | 10.0202 | Radio and Television Broadcasting Technology/Technician | 438 | 0.03 |
| 35000 | CIPCODE | 10.0203 | Recording Arts Technology/Technician | 894 | 0.05 |
| 35000 | CIPCODE | 10.0204 | Voice Writing Technology/Technician | 10 | 0.00 |
| 35000 | CIPCODE | 10.0299 | Audiovisual Communications Technologies/Technicians, Other | 88 | 0.01 |
| 35000 | CIPCODE | 10.0301 | Graphic Communications, General | 179 | 0.01 |
| 35000 | CIPCODE | 10.0302 | Printing Management | 12 | 0.00 |
| 35000 | CIPCODE | 10.0303 | Prepress/Desktop Publishing and Digital Imaging Design | 525 | 0.03 |
| 35000 | CIPCODE | 10.0304 | Animation, Interactive Technology, Video Graphics, and Special Effects | 1259 | 0.07 |
| 35000 | CIPCODE | 10.0305 | Graphic and Printing Equipment Operator, General Production | 157 | 0.01 |
| 35000 | CIPCODE | 10.0306 | Platemaker/Imager | 19 | 0.00 |
| 35000 | CIPCODE | 10.0307 | Printing Press Operator | 10 | 0.00 |
| 35000 | CIPCODE | 10.0308 | Computer Typography and Composition Equipment Operator | 3 | 0.00 |
| 35000 | CIPCODE | 10.0399 | Graphic Communications, Other | 45 | 0.00 |
| 35000 | CIPCODE | 10.9999 | Communications Technologies/Technicians and Support Services, Other | 113 | 0.01 |
| 35000 | CIPCODE | 11.0101 | Computer and Information Sciences, General | 4667 | 0.28 |
| 35000 | CIPCODE | 11.0102 | Artificial Intelligence | 493 | 0.03 |
| 35000 | CIPCODE | 11.0103 | Information Technology | 3533 | 0.21 |
| 35000 | CIPCODE | 11.0104 | Informatics | 363 | 0.02 |
| 35000 | CIPCODE | 11.0105 | Human-Centered Technology Design | 120 | 0.01 |
| 35000 | CIPCODE | 11.0199 | Computer and Information Sciences,  Other | 417 | 0.02 |
| 35000 | CIPCODE | 11.0201 | Computer Programming/Programmer, General | 2292 | 0.14 |
| 35000 | CIPCODE | 11.0202 | Computer Programming, Specific Applications | 770 | 0.05 |
| 35000 | CIPCODE | 11.0203 | Computer Programming, Vendor/Product Certification | 133 | 0.01 |
| 35000 | CIPCODE | 11.0204 | Computer Game Programming | 155 | 0.01 |
| 35000 | CIPCODE | 11.0205 | Computer Programming, Specific Platforms | 53 | 0.00 |
| 35000 | CIPCODE | 11.0299 | Computer Programming, Other | 121 | 0.01 |
| 35000 | CIPCODE | 11.0301 | Data Processing and Data Processing Technology/Technician | 643 | 0.04 |
| 35000 | CIPCODE | 11.0401 | Information Science/Studies | 1991 | 0.12 |
| 35000 | CIPCODE | 11.0501 | Computer Systems Analysis/Analyst | 454 | 0.03 |
| 35000 | CIPCODE | 11.0601 | Data Entry/Microcomputer Applications, General | 507 | 0.03 |
| 35000 | CIPCODE | 11.0602 | Word Processing | 17 | 0.00 |
| 35000 | CIPCODE | 11.0699 | Data Entry/Microcomputer Applications, Other | 20 | 0.00 |
| 35000 | CIPCODE | 11.0701 | Computer Science | 4668 | 0.28 |
| 35000 | CIPCODE | 11.0801 | Web Page, Digital/Multimedia and Information Resources Design | 2262 | 0.13 |
| 35000 | CIPCODE | 11.0802 | Data Modeling/Warehousing and Database Administration | 690 | 0.04 |
| 35000 | CIPCODE | 11.0803 | Computer Graphics | 660 | 0.04 |
| 35000 | CIPCODE | 11.0804 | Modeling, Virtual Environments and Simulation | 204 | 0.01 |
| 35000 | CIPCODE | 11.0899 | Computer Software and Media Applications, Other | 396 | 0.02 |
| 35000 | CIPCODE | 11.0901 | Computer Systems Networking and Telecommunications | 2739 | 0.16 |
| 35000 | CIPCODE | 11.0902 | Cloud Computing | 290 | 0.02 |
| 35000 | CIPCODE | 11.0999 | Computer Systems Networking and Telecommunications, Other | 12 | 0.00 |
| 35000 | CIPCODE | 11.1001 | Network and System Administration/Administrator | 1295 | 0.08 |
| 35000 | CIPCODE | 11.1002 | System, Networking, and LAN/WAN Management/Manager | 464 | 0.03 |
| 35000 | CIPCODE | 11.1003 | Computer and Information Systems Security/Auditing/Information Assurance | 4668 | 0.28 |
| 35000 | CIPCODE | 11.1004 | Web/Multimedia Management and Webmaster | 619 | 0.04 |
| 35000 | CIPCODE | 11.1005 | Information Technology Project Management | 345 | 0.02 |
| 35000 | CIPCODE | 11.1006 | Computer Support Specialist | 1313 | 0.08 |
| 35000 | CIPCODE | 11.1099 | Computer/Information Technology Services Administration and Management, Other | 485 | 0.03 |
| 35000 | CIPCODE | 11.9999 | Computer and Information Sciences and Support Services, Other | 418 | 0.02 |
| 35000 | CIPCODE | 12.0301 | Funeral Service and Mortuary Science, General | 236 | 0.01 |
| 35000 | CIPCODE | 12.0302 | Funeral Direction/Service | 56 | 0.00 |
| 35000 | CIPCODE | 12.0303 | Mortuary Science and Embalming/Embalmer | 20 | 0.00 |
| 35000 | CIPCODE | 12.0399 | Funeral Service and Mortuary Science, Other | 13 | 0.00 |
| 35000 | CIPCODE | 12.0401 | Cosmetology/Cosmetologist, General | 4817 | 0.29 |
| 35000 | CIPCODE | 12.0402 | Barbering/Barber | 1939 | 0.11 |
| 35000 | CIPCODE | 12.0404 | Electrolysis/Electrology and Electrolysis Technician | 50 | 0.00 |
| 35000 | CIPCODE | 12.0406 | Make-Up Artist/Specialist | 124 | 0.01 |
| 35000 | CIPCODE | 12.0407 | Hair Styling/Stylist and Hair Design | 360 | 0.02 |
| 35000 | CIPCODE | 12.0408 | Facial Treatment Specialist/Facialist | 341 | 0.02 |
| 35000 | CIPCODE | 12.0409 | Aesthetician/Esthetician and Skin Care Specialist | 3028 | 0.18 |
| 35000 | CIPCODE | 12.0410 | Nail Technician/Specialist and Manicurist | 2396 | 0.14 |
| 35000 | CIPCODE | 12.0411 | Permanent Cosmetics/Makeup and Tattooing | 11 | 0.00 |
| 35000 | CIPCODE | 12.0412 | Salon/Beauty Salon Management/Manager | 118 | 0.01 |
| 35000 | CIPCODE | 12.0413 | Cosmetology, Barber/Styling, and Nail Instructor | 2266 | 0.13 |
| 35000 | CIPCODE | 12.0414 | Master Aesthetician/Esthetician | 214 | 0.01 |
| 35000 | CIPCODE | 12.0499 | Cosmetology and Related Personal Grooming Arts, Other | 462 | 0.03 |
| 35000 | CIPCODE | 12.0500 | Cooking and Related Culinary Arts, General | 825 | 0.05 |
| 35000 | CIPCODE | 12.0501 | Baking and Pastry Arts/Baker/Pastry Chef | 960 | 0.06 |
| 35000 | CIPCODE | 12.0502 | Bartending/Bartender | 31 | 0.00 |
| 35000 | CIPCODE | 12.0503 | Culinary Arts/Chef Training | 1883 | 0.11 |
| 35000 | CIPCODE | 12.0504 | Restaurant, Culinary, and Catering Management/Manager | 655 | 0.04 |
| 35000 | CIPCODE | 12.0505 | Food Preparation/Professional Cooking/Kitchen Assistant | 290 | 0.02 |
| 35000 | CIPCODE | 12.0506 | Meat Cutting/Meat Cutter | 59 | 0.00 |
| 35000 | CIPCODE | 12.0507 | Food Service, Waiter/Waitress, and Dining Room Management/Manager | 75 | 0.00 |
| 35000 | CIPCODE | 12.0508 | Institutional Food Workers | 109 | 0.01 |
| 35000 | CIPCODE | 12.0509 | Culinary Science/Culinology | 43 | 0.00 |
| 35000 | CIPCODE | 12.0510 | Wine Steward/Sommelier | 19 | 0.00 |
| 35000 | CIPCODE | 12.0599 | Culinary Arts and Related Services, Other | 128 | 0.01 |
| 35000 | CIPCODE | 12.0602 | Casino Dealing | 4 | 0.00 |
| 35000 | CIPCODE | 12.9999 | Culinary, Entertainment, and Personal Services, Other | 23 | 0.00 |
| 35000 | CIPCODE | 13.0101 | Education, General | 3619 | 0.21 |
| 35000 | CIPCODE | 13.0201 | Bilingual and Multilingual Education | 444 | 0.03 |
| 35000 | CIPCODE | 13.0202 | Multicultural Education | 193 | 0.01 |
| 35000 | CIPCODE | 13.0203 | Indian/Native American Education | 43 | 0.00 |
| 35000 | CIPCODE | 13.0299 | Bilingual, Multilingual, and Multicultural Education, Other | 40 | 0.00 |
| 35000 | CIPCODE | 13.0301 | Curriculum and Instruction | 1862 | 0.11 |
| 35000 | CIPCODE | 13.0401 | Educational Leadership and Administration, General | 3455 | 0.20 |
| 35000 | CIPCODE | 13.0402 | Administration of Special Education | 158 | 0.01 |
| 35000 | CIPCODE | 13.0403 | Adult and Continuing Education Administration | 95 | 0.01 |
| 35000 | CIPCODE | 13.0404 | Educational, Instructional, and Curriculum Supervision | 416 | 0.02 |
| 35000 | CIPCODE | 13.0406 | Higher Education/Higher Education Administration | 1114 | 0.07 |
| 35000 | CIPCODE | 13.0407 | Community College Administration | 129 | 0.01 |
| 35000 | CIPCODE | 13.0408 | Elementary and Middle School Administration/Principalship | 150 | 0.01 |
| 35000 | CIPCODE | 13.0409 | Secondary School Administration/Principalship | 135 | 0.01 |
| 35000 | CIPCODE | 13.0410 | Urban Education and Leadership | 178 | 0.01 |
| 35000 | CIPCODE | 13.0411 | Superintendency and Educational System Administration | 352 | 0.02 |
| 35000 | CIPCODE | 13.0412 | International School Administration/Leadership | 13 | 0.00 |
| 35000 | CIPCODE | 13.0413 | Education Entrepreneurship | 15 | 0.00 |
| 35000 | CIPCODE | 13.0414 | Early Childhood Program Administration | 39 | 0.00 |
| 35000 | CIPCODE | 13.0499 | Educational Administration and Supervision, Other | 466 | 0.03 |
| 35000 | CIPCODE | 13.0501 | Educational/Instructional Technology | 1563 | 0.09 |
| 35000 | CIPCODE | 13.0601 | Educational Evaluation and Research | 220 | 0.01 |
| 35000 | CIPCODE | 13.0603 | Educational Statistics and Research Methods | 207 | 0.01 |
| 35000 | CIPCODE | 13.0604 | Educational Assessment, Testing, and Measurement | 111 | 0.01 |
| 35000 | CIPCODE | 13.0607 | Learning Sciences | 165 | 0.01 |
| 35000 | CIPCODE | 13.0608 | Institutional Research | 6 | 0.00 |
| 35000 | CIPCODE | 13.0699 | Educational Assessment, Evaluation, and Research, Other | 101 | 0.01 |
| 35000 | CIPCODE | 13.0701 | International and Comparative Education | 110 | 0.01 |
| 35000 | CIPCODE | 13.0901 | Social and Philosophical Foundations of Education | 317 | 0.02 |
| 35000 | CIPCODE | 13.1001 | Special Education and Teaching, General | 3511 | 0.21 |
| 35000 | CIPCODE | 13.1003 | Education/Teaching of Individuals with Hearing Impairments Including Deafness | 194 | 0.01 |
| 35000 | CIPCODE | 13.1004 | Education/Teaching of the Gifted and Talented | 298 | 0.02 |
| 35000 | CIPCODE | 13.1005 | Education/Teaching of Individuals with Emotional Disturbances | 96 | 0.01 |
| 35000 | CIPCODE | 13.1006 | Education/Teaching of Individuals with Intellectual Disabilities | 89 | 0.01 |
| 35000 | CIPCODE | 13.1007 | Education/Teaching of Individuals with Multiple Disabilities | 155 | 0.01 |
| 35000 | CIPCODE | 13.1008 | Education/Teaching of Individuals with Orthopedic and Other Physical Health Impairments | 25 | 0.00 |
| 35000 | CIPCODE | 13.1009 | Education/Teaching of Individuals with Vision Impairments Including Blindness | 84 | 0.00 |
| 35000 | CIPCODE | 13.1011 | Education/Teaching of Individuals with Specific Learning Disabilities | 250 | 0.01 |
| 35000 | CIPCODE | 13.1012 | Education/Teaching of Individuals with Speech or Language Impairments | 88 | 0.01 |
| 35000 | CIPCODE | 13.1013 | Education/Teaching of Individuals with Autism | 384 | 0.02 |
| 35000 | CIPCODE | 13.1014 | Education/Teaching of Individuals Who are Developmentally Delayed | 36 | 0.00 |
| 35000 | CIPCODE | 13.1015 | Education/Teaching of Individuals in Early Childhood Special Education Programs | 753 | 0.04 |
| 35000 | CIPCODE | 13.1016 | Education/Teaching of Individuals with Traumatic Brain Injuries | 16 | 0.00 |
| 35000 | CIPCODE | 13.1017 | Education/Teaching of Individuals in Elementary Special Education Programs | 361 | 0.02 |
| 35000 | CIPCODE | 13.1018 | Education/Teaching of Individuals in Junior High/Middle School Special Education Programs | 56 | 0.00 |
| 35000 | CIPCODE | 13.1019 | Education/Teaching of Individuals in Secondary Special Education Programs | 222 | 0.01 |
| 35000 | CIPCODE | 13.1099 | Special Education and Teaching, Other | 448 | 0.03 |
| 35000 | CIPCODE | 13.1101 | Counselor Education/School Counseling and Guidance Services | 1834 | 0.11 |
| 35000 | CIPCODE | 13.1102 | College Student Counseling and Personnel Services | 308 | 0.02 |
| 35000 | CIPCODE | 13.1199 | Student Counseling and Personnel Services, Other | 102 | 0.01 |
| 35000 | CIPCODE | 13.1201 | Adult and Continuing Education and Teaching | 361 | 0.02 |
| 35000 | CIPCODE | 13.1202 | Elementary Education and Teaching | 4739 | 0.28 |
| 35000 | CIPCODE | 13.1203 | Junior High/Intermediate/Middle School Education and Teaching | 1301 | 0.08 |
| 35000 | CIPCODE | 13.1205 | Secondary Education and Teaching | 2652 | 0.16 |
| 35000 | CIPCODE | 13.1206 | Teacher Education, Multiple Levels | 1278 | 0.08 |
| 35000 | CIPCODE | 13.1207 | Montessori Teacher Education | 79 | 0.00 |
| 35000 | CIPCODE | 13.1208 | Waldorf/Steiner Teacher Education | 3 | 0.00 |
| 35000 | CIPCODE | 13.1209 | Kindergarten/Preschool Education and Teaching | 614 | 0.04 |
| 35000 | CIPCODE | 13.1210 | Early Childhood Education and Teaching | 4688 | 0.28 |
| 35000 | CIPCODE | 13.1211 | Online Educator/Online Teaching | 97 | 0.01 |
| 35000 | CIPCODE | 13.1212 | International Teaching and Learning | 9 | 0.00 |
| 35000 | CIPCODE | 13.1213 | Science, Technology, Engineering, and Mathematics (STEM) Educational Methods | 122 | 0.01 |
| 35000 | CIPCODE | 13.1214 | College/Postsecondary/University Teaching | 66 | 0.00 |
| 35000 | CIPCODE | 13.1299 | Teacher Education and Professional Development, Specific Levels and Methods, Other | 935 | 0.06 |
| 35000 | CIPCODE | 13.1301 | Agricultural Teacher Education | 341 | 0.02 |
| 35000 | CIPCODE | 13.1302 | Art Teacher Education | 1342 | 0.08 |
| 35000 | CIPCODE | 13.1303 | Business and Innovation/Entrepreneurship Teacher Education | 348 | 0.02 |
| 35000 | CIPCODE | 13.1304 | Driver and Safety Teacher Education | 20 | 0.00 |
| 35000 | CIPCODE | 13.1305 | English/Language Arts Teacher Education | 1829 | 0.11 |
| 35000 | CIPCODE | 13.1306 | Foreign Language Teacher  Education | 415 | 0.02 |
| 35000 | CIPCODE | 13.1307 | Health Teacher Education | 493 | 0.03 |
| 35000 | CIPCODE | 13.1308 | Family and Consumer Sciences/Home Economics Teacher Education | 187 | 0.01 |
| 35000 | CIPCODE | 13.1309 | Technology Teacher Education/Industrial Arts Teacher Education | 280 | 0.02 |
| 35000 | CIPCODE | 13.1310 | Sales and Marketing Operations/Marketing and Distribution   Teacher Education | 31 | 0.00 |
| 35000 | CIPCODE | 13.1311 | Mathematics Teacher Education | 2035 | 0.12 |
| 35000 | CIPCODE | 13.1312 | Music Teacher Education | 2128 | 0.13 |
| 35000 | CIPCODE | 13.1314 | Physical Education Teaching and Coaching | 2015 | 0.12 |
| 35000 | CIPCODE | 13.1315 | Reading Teacher Education | 1477 | 0.09 |
| 35000 | CIPCODE | 13.1316 | Science Teacher Education/General Science Teacher Education | 1172 | 0.07 |
| 35000 | CIPCODE | 13.1317 | Social Science Teacher Education | 415 | 0.02 |
| 35000 | CIPCODE | 13.1318 | Social Studies Teacher Education | 1091 | 0.06 |
| 35000 | CIPCODE | 13.1319 | Technical Teacher Education | 221 | 0.01 |
| 35000 | CIPCODE | 13.1320 | Trade and Industrial Teacher Education | 224 | 0.01 |
| 35000 | CIPCODE | 13.1321 | Computer Teacher Education | 202 | 0.01 |
| 35000 | CIPCODE | 13.1322 | Biology Teacher Education | 1113 | 0.07 |
| 35000 | CIPCODE | 13.1323 | Chemistry Teacher Education | 762 | 0.05 |
| 35000 | CIPCODE | 13.1324 | Drama and Dance Teacher Education | 295 | 0.02 |
| 35000 | CIPCODE | 13.1325 | French Language Teacher Education | 317 | 0.02 |
| 35000 | CIPCODE | 13.1326 | German Language Teacher Education | 146 | 0.01 |
| 35000 | CIPCODE | 13.1327 | Health Occupations Teacher Education | 62 | 0.00 |
| 35000 | CIPCODE | 13.1328 | History Teacher Education | 710 | 0.04 |
| 35000 | CIPCODE | 13.1329 | Physics Teacher Education | 465 | 0.03 |
| 35000 | CIPCODE | 13.1330 | Spanish Language Teacher Education | 745 | 0.04 |
| 35000 | CIPCODE | 13.1331 | Speech Teacher Education | 106 | 0.01 |
| 35000 | CIPCODE | 13.1332 | Geography Teacher Education | 30 | 0.00 |
| 35000 | CIPCODE | 13.1333 | Latin Teacher Education | 51 | 0.00 |
| 35000 | CIPCODE | 13.1334 | School Librarian/School Library Media Specialist | 153 | 0.01 |
| 35000 | CIPCODE | 13.1335 | Psychology Teacher Education | 66 | 0.00 |
| 35000 | CIPCODE | 13.1337 | Earth Science Teacher Education | 220 | 0.01 |
| 35000 | CIPCODE | 13.1338 | Environmental Education | 83 | 0.00 |
| 35000 | CIPCODE | 13.1339 | Communication Arts and Literature Teacher Education | 16 | 0.00 |
| 35000 | CIPCODE | 13.1399 | Teacher Education and Professional Development, Specific Subject Areas, Other | 700 | 0.04 |
| 35000 | CIPCODE | 13.1401 | Teaching English as a Second or Foreign Language/ESL Language Instructor | 1951 | 0.12 |
| 35000 | CIPCODE | 13.1499 | Teaching English or French as a Second or Foreign Language, Other | 44 | 0.00 |
| 35000 | CIPCODE | 13.1501 | Teacher Assistant/Aide | 865 | 0.05 |
| 35000 | CIPCODE | 13.1502 | Adult Literacy Tutor/Instructor | 33 | 0.00 |
| 35000 | CIPCODE | 13.1599 | Teaching Assistants/Aides, Other | 37 | 0.00 |
| 35000 | CIPCODE | 13.9999 | Education, Other | 1226 | 0.07 |
| 35000 | CIPCODE | 14.0101 | Engineering, General | 1892 | 0.11 |
| 35000 | CIPCODE | 14.0102 | Pre-Engineering | 840 | 0.05 |
| 35000 | CIPCODE | 14.0103 | Applied Engineering | 72 | 0.00 |
| 35000 | CIPCODE | 14.0201 | Aerospace, Aeronautical, and Astronautical/Space Engineering, General | 476 | 0.03 |
| 35000 | CIPCODE | 14.0202 | Astronautical Engineering | 9 | 0.00 |
| 35000 | CIPCODE | 14.0299 | Aerospace, Aeronautical, and Astronautical/Space Engineering, Other | 3 | 0.00 |
| 35000 | CIPCODE | 14.0301 | Agricultural Engineering | 202 | 0.01 |
| 35000 | CIPCODE | 14.0401 | Architectural Engineering | 118 | 0.01 |
| 35000 | CIPCODE | 14.0501 | Bioengineering and Biomedical Engineering | 1157 | 0.07 |
| 35000 | CIPCODE | 14.0601 | Ceramic Sciences and Engineering | 29 | 0.00 |
| 35000 | CIPCODE | 14.0701 | Chemical Engineering | 935 | 0.06 |
| 35000 | CIPCODE | 14.0702 | Chemical and Biomolecular Engineering | 87 | 0.01 |
| 35000 | CIPCODE | 14.0799 | Chemical Engineering, Other | 21 | 0.00 |
| 35000 | CIPCODE | 14.0801 | Civil Engineering, General | 1414 | 0.08 |
| 35000 | CIPCODE | 14.0802 | Geotechnical and Geoenvironmental Engineering | 35 | 0.00 |
| 35000 | CIPCODE | 14.0803 | Structural Engineering | 108 | 0.01 |
| 35000 | CIPCODE | 14.0804 | Transportation and Highway Engineering | 86 | 0.01 |
| 35000 | CIPCODE | 14.0805 | Water Resources Engineering | 65 | 0.00 |
| 35000 | CIPCODE | 14.0899 | Civil Engineering, Other | 68 | 0.00 |
| 35000 | CIPCODE | 14.0901 | Computer Engineering, General | 1338 | 0.08 |
| 35000 | CIPCODE | 14.0902 | Computer Hardware Engineering | 35 | 0.00 |
| 35000 | CIPCODE | 14.0903 | Computer Software Engineering | 640 | 0.04 |
| 35000 | CIPCODE | 14.0999 | Computer Engineering, Other | 96 | 0.01 |
| 35000 | CIPCODE | 14.1001 | Electrical and Electronics Engineering | 2020 | 0.12 |
| 35000 | CIPCODE | 14.1003 | Laser and Optical Engineering | 33 | 0.00 |
| 35000 | CIPCODE | 14.1004 | Telecommunications Engineering | 69 | 0.00 |
| 35000 | CIPCODE | 14.1099 | Electrical, Electronics, and Communications Engineering, Other | 106 | 0.01 |
| 35000 | CIPCODE | 14.1101 | Engineering Mechanics | 126 | 0.01 |
| 35000 | CIPCODE | 14.1201 | Engineering Physics/Applied Physics | 500 | 0.03 |
| 35000 | CIPCODE | 14.1301 | Engineering Science | 347 | 0.02 |
| 35000 | CIPCODE | 14.1401 | Environmental/Environmental Health Engineering | 675 | 0.04 |
| 35000 | CIPCODE | 14.1801 | Materials Engineering | 548 | 0.03 |
| 35000 | CIPCODE | 14.1901 | Mechanical Engineering | 1982 | 0.12 |
| 35000 | CIPCODE | 14.2001 | Metallurgical Engineering | 55 | 0.00 |
| 35000 | CIPCODE | 14.2101 | Mining and Mineral Engineering | 93 | 0.01 |
| 35000 | CIPCODE | 14.2201 | Naval Architecture and Marine Engineering | 62 | 0.00 |
| 35000 | CIPCODE | 14.2301 | Nuclear Engineering | 196 | 0.01 |
| 35000 | CIPCODE | 14.2401 | Ocean Engineering | 75 | 0.00 |
| 35000 | CIPCODE | 14.2501 | Petroleum Engineering | 157 | 0.01 |
| 35000 | CIPCODE | 14.2701 | Systems Engineering | 514 | 0.03 |
| 35000 | CIPCODE | 14.2801 | Textile Sciences and Engineering | 21 | 0.00 |
| 35000 | CIPCODE | 14.3201 | Polymer/Plastics Engineering | 79 | 0.00 |
| 35000 | CIPCODE | 14.3301 | Construction Engineering | 203 | 0.01 |
| 35000 | CIPCODE | 14.3401 | Forest Engineering | 11 | 0.00 |
| 35000 | CIPCODE | 14.3501 | Industrial Engineering | 724 | 0.04 |
| 35000 | CIPCODE | 14.3601 | Manufacturing Engineering | 338 | 0.02 |
| 35000 | CIPCODE | 14.3701 | Operations Research | 176 | 0.01 |
| 35000 | CIPCODE | 14.3801 | Surveying Engineering | 96 | 0.01 |
| 35000 | CIPCODE | 14.3901 | Geological/Geophysical Engineering | 97 | 0.01 |
| 35000 | CIPCODE | 14.4001 | Paper Science and Engineering | 19 | 0.00 |
| 35000 | CIPCODE | 14.4101 | Electromechanical Engineering | 32 | 0.00 |
| 35000 | CIPCODE | 14.4201 | Mechatronics, Robotics, and Automation Engineering | 464 | 0.03 |
| 35000 | CIPCODE | 14.4301 | Biochemical Engineering | 31 | 0.00 |
| 35000 | CIPCODE | 14.4401 | Engineering Chemistry | 9 | 0.00 |
| 35000 | CIPCODE | 14.4501 | Biological/Biosystems Engineering | 114 | 0.01 |
| 35000 | CIPCODE | 14.4701 | Electrical and Computer Engineering | 174 | 0.01 |
| 35000 | CIPCODE | 14.4801 | Energy Systems Engineering, General | 88 | 0.01 |
| 35000 | CIPCODE | 14.4802 | Power Plant Engineering | 4 | 0.00 |
| 35000 | CIPCODE | 14.4899 | Energy Systems Engineering, Other | 7 | 0.00 |
| 35000 | CIPCODE | 14.9999 | Engineering, Other | 615 | 0.04 |
| 35000 | CIPCODE | 15.0000 | Engineering Technologies/Technicians, General | 1049 | 0.06 |
| 35000 | CIPCODE | 15.0001 | Applied Engineering Technologies/Technicians | 96 | 0.01 |
| 35000 | CIPCODE | 15.0101 | Architectural Engineering Technologies/Technicians | 398 | 0.02 |
| 35000 | CIPCODE | 15.0201 | Civil Engineering Technologies/Technicians | 612 | 0.04 |
| 35000 | CIPCODE | 15.0303 | Electrical, Electronic, and Communications Engineering Technology/Technician | 2074 | 0.12 |
| 35000 | CIPCODE | 15.0304 | Laser and Optical Technology/Technician | 129 | 0.01 |
| 35000 | CIPCODE | 15.0305 | Telecommunications Technology/Technician | 225 | 0.01 |
| 35000 | CIPCODE | 15.0306 | Integrated Circuit Design Technology/Technician | 11 | 0.00 |
| 35000 | CIPCODE | 15.0307 | Audio Engineering Technology/Technician | 65 | 0.00 |
| 35000 | CIPCODE | 15.0399 | Electrical/Electronic Engineering Technologies/Technicians, Other | 358 | 0.02 |
| 35000 | CIPCODE | 15.0401 | Biomedical Technology/Technician | 482 | 0.03 |
| 35000 | CIPCODE | 15.0403 | Electromechanical/Electromechanical Engineering Technology/Technician | 687 | 0.04 |
| 35000 | CIPCODE | 15.0404 | Instrumentation Technology/Technician | 430 | 0.03 |
| 35000 | CIPCODE | 15.0405 | Robotics Technology/Technician | 368 | 0.02 |
| 35000 | CIPCODE | 15.0406 | Automation Engineer Technology/Technician | 519 | 0.03 |
| 35000 | CIPCODE | 15.0407 | Mechatronics, Robotics, and Automation Engineering Technology/Technician | 305 | 0.02 |
| 35000 | CIPCODE | 15.0499 | Electromechanical Technologies/Technicians, Other | 496 | 0.03 |
| 35000 | CIPCODE | 15.0501 | Heating, Ventilation, Air Conditioning and Refrigeration Engineering Technology/Technician | 883 | 0.05 |
| 35000 | CIPCODE | 15.0506 | Water Quality and Wastewater Treatment Management and Recycling Technology/Technician | 393 | 0.02 |
| 35000 | CIPCODE | 15.0507 | Environmental/Environmental Engineering Technology/Technician | 256 | 0.02 |
| 35000 | CIPCODE | 15.0508 | Hazardous Materials Management and Waste Technology/Technician | 145 | 0.01 |
| 35000 | CIPCODE | 15.0599 | Environmental Control Technologies/Technicians, Other | 113 | 0.01 |
| 35000 | CIPCODE | 15.0607 | Plastics and Polymer Engineering Technology/Technician | 178 | 0.01 |
| 35000 | CIPCODE | 15.0611 | Metallurgical Technology/Technician | 37 | 0.00 |
| 35000 | CIPCODE | 15.0612 | Industrial Technology/Technician | 828 | 0.05 |
| 35000 | CIPCODE | 15.0613 | Manufacturing Engineering Technology/Technician | 1864 | 0.11 |
| 35000 | CIPCODE | 15.0614 | Welding Engineering Technology/Technician | 136 | 0.01 |
| 35000 | CIPCODE | 15.0615 | Chemical Engineering Technology/Technician | 35 | 0.00 |
| 35000 | CIPCODE | 15.0616 | Semiconductor Manufacturing Technology/Technician | 44 | 0.00 |
| 35000 | CIPCODE | 15.0617 | Composite Materials Technology/Technician | 42 | 0.00 |
| 35000 | CIPCODE | 15.0699 | Industrial Production Technologies/Technicians, Other | 404 | 0.02 |
| 35000 | CIPCODE | 15.0701 | Occupational Safety and Health Technology/Technician | 369 | 0.02 |
| 35000 | CIPCODE | 15.0702 | Quality Control Technology/Technician | 275 | 0.02 |
| 35000 | CIPCODE | 15.0703 | Industrial Safety Technology/Technician | 108 | 0.01 |
| 35000 | CIPCODE | 15.0704 | Hazardous Materials Information Systems Technology/Technician | 9 | 0.00 |
| 35000 | CIPCODE | 15.0799 | Quality Control and Safety Technologies/Technicians, Other | 70 | 0.00 |
| 35000 | CIPCODE | 15.0801 | Aeronautical/Aerospace Engineering Technology/Technician | 160 | 0.01 |
| 35000 | CIPCODE | 15.0803 | Automotive Engineering Technology/Technician | 260 | 0.02 |
| 35000 | CIPCODE | 15.0805 | Mechanical/Mechanical Engineering Technology/Technician | 978 | 0.06 |
| 35000 | CIPCODE | 15.0806 | Marine Engineering Technology/Technician | 22 | 0.00 |
| 35000 | CIPCODE | 15.0807 | Motorsports Engineering Technology/Technician | 5 | 0.00 |
| 35000 | CIPCODE | 15.0899 | Mechanical Engineering Related Technologies/Technicians, Other | 97 | 0.01 |
| 35000 | CIPCODE | 15.0901 | Mining Technology/Technician | 29 | 0.00 |
| 35000 | CIPCODE | 15.0903 | Petroleum Technology/Technician | 174 | 0.01 |
| 35000 | CIPCODE | 15.0999 | Mining and Petroleum Technologies/Technicians, Other | 3 | 0.00 |
| 35000 | CIPCODE | 15.1001 | Construction Engineering Technology/Technician | 703 | 0.04 |
| 35000 | CIPCODE | 15.1102 | Surveying Technology/Surveying | 464 | 0.03 |
| 35000 | CIPCODE | 15.1103 | Hydraulics and Fluid Power Technology/Technician | 61 | 0.00 |
| 35000 | CIPCODE | 15.1199 | Engineering-Related Technologies/Technicians, Other | 49 | 0.00 |
| 35000 | CIPCODE | 15.1201 | Computer Engineering Technology/Technician | 471 | 0.03 |
| 35000 | CIPCODE | 15.1202 | Computer/Computer Systems Technology/Technician | 437 | 0.03 |
| 35000 | CIPCODE | 15.1203 | Computer Hardware Technology/Technician | 31 | 0.00 |
| 35000 | CIPCODE | 15.1204 | Computer Software Technology/Technician | 111 | 0.01 |
| 35000 | CIPCODE | 15.1299 | Computer Engineering Technologies/Technicians, Other | 37 | 0.00 |
| 35000 | CIPCODE | 15.1301 | Drafting and Design Technology/Technician, General | 1508 | 0.09 |
| 35000 | CIPCODE | 15.1302 | CAD/CADD Drafting and/or Design Technology/Technician | 1114 | 0.07 |
| 35000 | CIPCODE | 15.1303 | Architectural Drafting and Architectural CAD/CADD | 634 | 0.04 |
| 35000 | CIPCODE | 15.1304 | Civil Drafting and Civil Engineering CAD/CADD | 131 | 0.01 |
| 35000 | CIPCODE | 15.1305 | Electrical/Electronics Drafting and Electrical/Electronics CAD/CADD | 65 | 0.00 |
| 35000 | CIPCODE | 15.1306 | Mechanical Drafting and Mechanical Drafting CAD/CADD | 663 | 0.04 |
| 35000 | CIPCODE | 15.1307 | 3-D Modeling and Design Technology/Technician | 55 | 0.00 |
| 35000 | CIPCODE | 15.1399 | Drafting/Design Engineering Technologies/Technicians, Other | 53 | 0.00 |
| 35000 | CIPCODE | 15.1401 | Nuclear Engineering Technology/Technician | 54 | 0.00 |
| 35000 | CIPCODE | 15.1501 | Engineering/Industrial Management | 838 | 0.05 |
| 35000 | CIPCODE | 15.1502 | Engineering Design | 40 | 0.00 |
| 35000 | CIPCODE | 15.1503 | Packaging Science | 51 | 0.00 |
| 35000 | CIPCODE | 15.1599 | Engineering-Related Fields, Other | 63 | 0.00 |
| 35000 | CIPCODE | 15.1601 | Nanotechnology | 128 | 0.01 |
| 35000 | CIPCODE | 15.1701 | Energy Systems Technology/Technician | 705 | 0.04 |
| 35000 | CIPCODE | 15.1702 | Power Plant Technology/Technician | 26 | 0.00 |
| 35000 | CIPCODE | 15.1703 | Solar Energy Technology/Technician | 248 | 0.01 |
| 35000 | CIPCODE | 15.1704 | Wind Energy Technology/Technician | 51 | 0.00 |
| 35000 | CIPCODE | 15.1799 | Energy Systems Technologies/Technicians, Other | 10 | 0.00 |
| 35000 | CIPCODE | 15.9999 | Engineering/Engineering-Related Technologies/Technicians, Other | 472 | 0.03 |
| 35000 | CIPCODE | 16.0101 | Foreign Languages and Literatures, General | 1219 | 0.07 |
| 35000 | CIPCODE | 16.0102 | Linguistics | 971 | 0.06 |
| 35000 | CIPCODE | 16.0103 | Language Interpretation and Translation | 470 | 0.03 |
| 35000 | CIPCODE | 16.0104 | Comparative Literature | 499 | 0.03 |
| 35000 | CIPCODE | 16.0105 | Applied Linguistics | 154 | 0.01 |
| 35000 | CIPCODE | 16.0199 | Linguistic, Comparative, and Related Language Studies and Services, Other | 126 | 0.01 |
| 35000 | CIPCODE | 16.0201 | African Languages, Literatures, and Linguistics | 18 | 0.00 |
| 35000 | CIPCODE | 16.0300 | East Asian Languages, Literatures, and Linguistics, General | 152 | 0.01 |
| 35000 | CIPCODE | 16.0301 | Chinese Language and Literature | 599 | 0.04 |
| 35000 | CIPCODE | 16.0302 | Japanese Language and Literature | 664 | 0.04 |
| 35000 | CIPCODE | 16.0303 | Korean Language and Literature | 99 | 0.01 |
| 35000 | CIPCODE | 16.0399 | East Asian Languages, Literatures, and Linguistics, Other | 49 | 0.00 |
| 35000 | CIPCODE | 16.0400 | Slavic Languages, Literatures, and Linguistics, General | 132 | 0.01 |
| 35000 | CIPCODE | 16.0402 | Russian Language and Literature | 570 | 0.03 |
| 35000 | CIPCODE | 16.0407 | Polish Language and Literature | 18 | 0.00 |
| 35000 | CIPCODE | 16.0408 | Bosnian, Serbian, and Croatian Languages and Literatures | 3 | 0.00 |
| 35000 | CIPCODE | 16.0499 | Slavic, Baltic, and Albanian Languages, Literatures, and Linguistics, Other | 4 | 0.00 |
| 35000 | CIPCODE | 16.0500 | Germanic Languages, Literatures, and Linguistics, General | 110 | 0.01 |
| 35000 | CIPCODE | 16.0501 | German Language and Literature | 1514 | 0.09 |
| 35000 | CIPCODE | 16.0502 | Scandinavian Languages, Literatures, and Linguistics | 31 | 0.00 |
| 35000 | CIPCODE | 16.0503 | Danish Language and Literature | 3 | 0.00 |
| 35000 | CIPCODE | 16.0504 | Dutch/Flemish Language and Literature | 6 | 0.00 |
| 35000 | CIPCODE | 16.0505 | Norwegian Language and Literature | 18 | 0.00 |
| 35000 | CIPCODE | 16.0506 | Swedish Language and Literature | 9 | 0.00 |
| 35000 | CIPCODE | 16.0599 | Germanic Languages, Literatures, and Linguistics, Other | 24 | 0.00 |
| 35000 | CIPCODE | 16.0601 | Modern Greek Language and Literature | 22 | 0.00 |
| 35000 | CIPCODE | 16.0700 | South Asian Languages, Literatures, and Linguistics, General | 11 | 0.00 |
| 35000 | CIPCODE | 16.0701 | Hindi Language and Literature | 3 | 0.00 |
| 35000 | CIPCODE | 16.0702 | Sanskrit and Classical Indian Languages, Literatures, and Linguistics | 13 | 0.00 |
| 35000 | CIPCODE | 16.0799 | South Asian Languages, Literatures, and Linguistics, Other | 7 | 0.00 |
| 35000 | CIPCODE | 16.0801 | Iranian Languages, Literatures, and Linguistics | 17 | 0.00 |
| 35000 | CIPCODE | 16.0900 | Romance Languages, Literatures, and Linguistics, General | 201 | 0.01 |
| 35000 | CIPCODE | 16.0901 | French Language and Literature | 2587 | 0.15 |
| 35000 | CIPCODE | 16.0902 | Italian Language and Literature | 645 | 0.04 |
| 35000 | CIPCODE | 16.0904 | Portuguese Language and Literature | 149 | 0.01 |
| 35000 | CIPCODE | 16.0905 | Spanish Language and Literature | 4843 | 0.29 |
| 35000 | CIPCODE | 16.0908 | Hispanic and Latin American Languages, Literatures, and Linguistics, General | 181 | 0.01 |
| 35000 | CIPCODE | 16.0999 | Romance Languages, Literatures, and Linguistics, Other | 90 | 0.01 |
| 35000 | CIPCODE | 16.1001 | American Indian/Native American Languages, Literatures, and Linguistics | 109 | 0.01 |
| 35000 | CIPCODE | 16.1100 | Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics, General | 40 | 0.00 |
| 35000 | CIPCODE | 16.1101 | Arabic Language and Literature | 308 | 0.02 |
| 35000 | CIPCODE | 16.1102 | Hebrew Language and Literature | 82 | 0.00 |
| 35000 | CIPCODE | 16.1103 | Ancient Near Eastern and Biblical Languages, Literatures, and Linguistics | 91 | 0.01 |
| 35000 | CIPCODE | 16.1199 | Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics, Other | 70 | 0.00 |
| 35000 | CIPCODE | 16.1200 | Classics and Classical Languages, Literatures, and Linguistics, General | 1199 | 0.07 |
| 35000 | CIPCODE | 16.1202 | Ancient/Classical Greek Language and Literature | 207 | 0.01 |
| 35000 | CIPCODE | 16.1203 | Latin Language and Literature | 300 | 0.02 |
| 35000 | CIPCODE | 16.1299 | Classics and Classical Languages, Literatures, and Linguistics, Other | 123 | 0.01 |
| 35000 | CIPCODE | 16.1301 | Celtic Languages, Literatures, and Linguistics | 14 | 0.00 |
| 35000 | CIPCODE | 16.1401 | Australian/Oceanic/Pacific Languages, Literatures, and Linguistics | 3 | 0.00 |
| 35000 | CIPCODE | 16.1402 | Indonesian/Malay Languages and Literatures | 3 | 0.00 |
| 35000 | CIPCODE | 16.1404 | Filipino/Tagalog Language and Literature | 7 | 0.00 |
| 35000 | CIPCODE | 16.1407 | Thai Language and Literature | 3 | 0.00 |
| 35000 | CIPCODE | 16.1408 | Vietnamese Language and Literature | 3 | 0.00 |
| 35000 | CIPCODE | 16.1409 | Hawaiian Language and Literature | 8 | 0.00 |
| 35000 | CIPCODE | 16.1499 | Southeast Asian and Australasian/Pacific Languages, Literatures, and Linguistics, Other | 4 | 0.00 |
| 35000 | CIPCODE | 16.1501 | Turkish Language and Literature | 10 | 0.00 |
| 35000 | CIPCODE | 16.1502 | Uralic Languages, Literatures, and Linguistics | 3 | 0.00 |
| 35000 | CIPCODE | 16.1601 | American Sign Language (ASL) | 465 | 0.03 |
| 35000 | CIPCODE | 16.1602 | Linguistics of ASL and Other Sign Languages | 13 | 0.00 |
| 35000 | CIPCODE | 16.1603 | Sign Language Interpretation and Translation | 650 | 0.04 |
| 35000 | CIPCODE | 16.1699 | American Sign Language, Other | 12 | 0.00 |
| 35000 | CIPCODE | 16.1701 | English as a Second Language | 68 | 0.00 |
| 35000 | CIPCODE | 16.9999 | Foreign Languages, Literatures, and Linguistics, Other | 279 | 0.02 |
| 35000 | CIPCODE | 19.0101 | Family and Consumer Sciences/Human Sciences, General | 429 | 0.03 |
| 35000 | CIPCODE | 19.0201 | Business Family and Consumer Sciences/Human Sciences | 30 | 0.00 |
| 35000 | CIPCODE | 19.0202 | Family and Consumer Sciences/Human Sciences Communication | 4 | 0.00 |
| 35000 | CIPCODE | 19.0203 | Consumer Merchandising/Retailing Management | 68 | 0.00 |
| 35000 | CIPCODE | 19.0401 | Family Resource Management Studies, General | 78 | 0.00 |
| 35000 | CIPCODE | 19.0402 | Consumer Economics | 24 | 0.00 |
| 35000 | CIPCODE | 19.0403 | Consumer Services and Advocacy | 18 | 0.00 |
| 35000 | CIPCODE | 19.0499 | Family and Consumer Economics and Related Services, Other | 17 | 0.00 |
| 35000 | CIPCODE | 19.0501 | Foods, Nutrition, and Wellness Studies, General | 702 | 0.04 |
| 35000 | CIPCODE | 19.0504 | Human Nutrition | 248 | 0.01 |
| 35000 | CIPCODE | 19.0505 | Foodservice Systems Administration/Management | 214 | 0.01 |
| 35000 | CIPCODE | 19.0599 | Foods, Nutrition, and Related Services, Other | 54 | 0.00 |
| 35000 | CIPCODE | 19.0601 | Housing and Human Environments, General | 50 | 0.00 |
| 35000 | CIPCODE | 19.0604 | Facilities Planning and Management | 49 | 0.00 |
| 35000 | CIPCODE | 19.0699 | Housing and Human Environments, Other | 15 | 0.00 |
| 35000 | CIPCODE | 19.0701 | Human Development and Family Studies, General | 853 | 0.05 |
| 35000 | CIPCODE | 19.0702 | Adult Development and Aging | 305 | 0.02 |
| 35000 | CIPCODE | 19.0704 | Family Systems | 123 | 0.01 |
| 35000 | CIPCODE | 19.0706 | Child Development | 1190 | 0.07 |
| 35000 | CIPCODE | 19.0707 | Family and Community Services | 349 | 0.02 |
| 35000 | CIPCODE | 19.0708 | Child Care and Support Services Management | 1230 | 0.07 |
| 35000 | CIPCODE | 19.0709 | Child Care Provider/Assistant | 2379 | 0.14 |
| 35000 | CIPCODE | 19.0710 | Developmental Services Worker | 45 | 0.00 |
| 35000 | CIPCODE | 19.0711 | Early Childhood and Family Studies | 78 | 0.00 |
| 35000 | CIPCODE | 19.0712 | Parent Education Services | 14 | 0.00 |
| 35000 | CIPCODE | 19.0799 | Human Development, Family Studies, and Related Services, Other | 129 | 0.01 |
| 35000 | CIPCODE | 19.0901 | Apparel and Textiles, General | 345 | 0.02 |
| 35000 | CIPCODE | 19.0902 | Apparel and Textile Manufacture | 114 | 0.01 |
| 35000 | CIPCODE | 19.0904 | Textile Science | 9 | 0.00 |
| 35000 | CIPCODE | 19.0905 | Apparel and Textile Marketing Management | 235 | 0.01 |
| 35000 | CIPCODE | 19.0906 | Fashion and Fabric Consultant | 19 | 0.00 |
| 35000 | CIPCODE | 19.0999 | Apparel and Textiles, Other | 14 | 0.00 |
| 35000 | CIPCODE | 19.1001 | Work and Family Studies | 3 | 0.00 |
| 35000 | CIPCODE | 19.9999 | Family and Consumer Sciences/Human Sciences, Other | 31 | 0.00 |
| 35000 | CIPCODE | 22.0000 | Legal Studies | 824 | 0.05 |
| 35000 | CIPCODE | 22.0001 | Pre-Law Studies | 325 | 0.02 |
| 35000 | CIPCODE | 22.0099 | Non-Professional Legal Studies, Other | 10 | 0.00 |
| 35000 | CIPCODE | 22.0101 | Law | 658 | 0.04 |
| 35000 | CIPCODE | 22.0201 | Advanced Legal Research/Studies, General | 328 | 0.02 |
| 35000 | CIPCODE | 22.0202 | Programs for Foreign Lawyers | 161 | 0.01 |
| 35000 | CIPCODE | 22.0203 | American/U.S. Law/Legal Studies/Jurisprudence | 173 | 0.01 |
| 35000 | CIPCODE | 22.0205 | Banking, Corporate, Finance, and Securities Law | 103 | 0.01 |
| 35000 | CIPCODE | 22.0206 | Comparative Law | 27 | 0.00 |
| 35000 | CIPCODE | 22.0207 | Energy, Environment, and Natural Resources Law | 94 | 0.01 |
| 35000 | CIPCODE | 22.0208 | Health Law | 108 | 0.01 |
| 35000 | CIPCODE | 22.0209 | International Law and Legal Studies | 116 | 0.01 |
| 35000 | CIPCODE | 22.0210 | International Business, Trade, and Tax Law | 70 | 0.00 |
| 35000 | CIPCODE | 22.0211 | Tax Law/Taxation | 115 | 0.01 |
| 35000 | CIPCODE | 22.0212 | Intellectual Property Law | 65 | 0.00 |
| 35000 | CIPCODE | 22.0213 | Patent Law | 3 | 0.00 |
| 35000 | CIPCODE | 22.0214 | Agriculture Law | 4 | 0.00 |
| 35000 | CIPCODE | 22.0215 | Arts and Entertainment Law | 3 | 0.00 |
| 35000 | CIPCODE | 22.0216 | Compliance Law | 17 | 0.00 |
| 35000 | CIPCODE | 22.0217 | Criminal Law and Procedure | 11 | 0.00 |
| 35000 | CIPCODE | 22.0220 | Human Resources Law | 15 | 0.00 |
| 35000 | CIPCODE | 22.0222 | Real Estate and Land Development Law | 6 | 0.00 |
| 35000 | CIPCODE | 22.0224 | Tribal/Indigenous Law | 31 | 0.00 |
| 35000 | CIPCODE | 22.0299 | Legal Research and Advanced Professional Studies, Other | 205 | 0.01 |
| 35000 | CIPCODE | 22.0301 | Legal Administrative Assistant/Secretary | 457 | 0.03 |
| 35000 | CIPCODE | 22.0302 | Legal Assistant/Paralegal | 2502 | 0.15 |
| 35000 | CIPCODE | 22.0303 | Court Reporting and Captioning/Court Reporter | 217 | 0.01 |
| 35000 | CIPCODE | 22.0304 | Court Interpreter | 4 | 0.00 |
| 35000 | CIPCODE | 22.0305 | Scopist | 3 | 0.00 |
| 35000 | CIPCODE | 22.0399 | Legal Support Services, Other | 40 | 0.00 |
| 35000 | CIPCODE | 22.9999 | Legal Professions and Studies, Other | 350 | 0.02 |
| 35000 | CIPCODE | 23.0101 | English Language and Literature, General | 6837 | 0.40 |
| 35000 | CIPCODE | 23.1301 | Writing, General | 555 | 0.03 |
| 35000 | CIPCODE | 23.1302 | Creative Writing | 2091 | 0.12 |
| 35000 | CIPCODE | 23.1303 | Professional, Technical, Business, and Scientific Writing | 990 | 0.06 |
| 35000 | CIPCODE | 23.1304 | Rhetoric and Composition | 545 | 0.03 |
| 35000 | CIPCODE | 23.1399 | Rhetoric and Composition/Writing Studies, Other | 90 | 0.01 |
| 35000 | CIPCODE | 23.1401 | General Literature | 303 | 0.02 |
| 35000 | CIPCODE | 23.1402 | American Literature (United States) | 32 | 0.00 |
| 35000 | CIPCODE | 23.1404 | English Literature (British and Commonwealth) | 61 | 0.00 |
| 35000 | CIPCODE | 23.1405 | Children's and Adolescent Literature | 46 | 0.00 |
| 35000 | CIPCODE | 23.1499 | Literature, Other | 31 | 0.00 |
| 35000 | CIPCODE | 23.9999 | English Language and Literature/Letters, Other | 295 | 0.02 |
| 35000 | CIPCODE | 24.0101 | Liberal Arts and Sciences/Liberal Studies | 6075 | 0.36 |
| 35000 | CIPCODE | 24.0102 | General Studies | 3729 | 0.22 |
| 35000 | CIPCODE | 24.0103 | Humanities/Humanistic Studies | 1697 | 0.10 |
| 35000 | CIPCODE | 24.0199 | Liberal Arts and Sciences, General Studies and Humanities, Other | 1689 | 0.10 |
| 35000 | CIPCODE | 25.0101 | Library and Information Science | 340 | 0.02 |
| 35000 | CIPCODE | 25.0102 | Children and Youth Library Services | 20 | 0.00 |
| 35000 | CIPCODE | 25.0103 | Archives/Archival Administration | 61 | 0.00 |
| 35000 | CIPCODE | 25.0199 | Library Science and Administration, Other | 3 | 0.00 |
| 35000 | CIPCODE | 25.0301 | Library and Archives Assisting | 181 | 0.01 |
| 35000 | CIPCODE | 25.9999 | Library Science, Other | 60 | 0.00 |
| 35000 | CIPCODE | 26.0101 | Biology/Biological Sciences, General | 7079 | 0.42 |
| 35000 | CIPCODE | 26.0102 | Biomedical Sciences, General | 1232 | 0.07 |
| 35000 | CIPCODE | 26.0202 | Biochemistry | 2467 | 0.15 |
| 35000 | CIPCODE | 26.0203 | Biophysics | 311 | 0.02 |
| 35000 | CIPCODE | 26.0204 | Molecular Biology | 368 | 0.02 |
| 35000 | CIPCODE | 26.0205 | Molecular Biochemistry | 81 | 0.00 |
| 35000 | CIPCODE | 26.0206 | Molecular Biophysics | 23 | 0.00 |
| 35000 | CIPCODE | 26.0207 | Structural Biology | 18 | 0.00 |
| 35000 | CIPCODE | 26.0209 | Radiation Biology/Radiobiology | 26 | 0.00 |
| 35000 | CIPCODE | 26.0210 | Biochemistry and Molecular Biology | 440 | 0.03 |
| 35000 | CIPCODE | 26.0299 | Biochemistry, Biophysics and Molecular Biology, Other | 90 | 0.01 |
| 35000 | CIPCODE | 26.0301 | Botany/Plant Biology | 249 | 0.01 |
| 35000 | CIPCODE | 26.0305 | Plant Pathology/Phytopathology | 108 | 0.01 |
| 35000 | CIPCODE | 26.0307 | Plant Physiology | 14 | 0.00 |
| 35000 | CIPCODE | 26.0308 | Plant Molecular Biology | 20 | 0.00 |
| 35000 | CIPCODE | 26.0399 | Botany/Plant Biology, Other | 22 | 0.00 |
| 35000 | CIPCODE | 26.0401 | Cell/Cellular Biology and Histology | 121 | 0.01 |
| 35000 | CIPCODE | 26.0403 | Anatomy | 176 | 0.01 |
| 35000 | CIPCODE | 26.0404 | Developmental Biology and Embryology | 45 | 0.00 |
| 35000 | CIPCODE | 26.0406 | Cell/Cellular and Molecular Biology | 497 | 0.03 |
| 35000 | CIPCODE | 26.0407 | Cell Biology and Anatomy | 72 | 0.00 |
| 35000 | CIPCODE | 26.0499 | Cell/Cellular Biology and Anatomical Sciences, Other | 92 | 0.01 |
| 35000 | CIPCODE | 26.0502 | Microbiology, General | 525 | 0.03 |
| 35000 | CIPCODE | 26.0503 | Medical Microbiology and Bacteriology | 183 | 0.01 |
| 35000 | CIPCODE | 26.0504 | Virology | 12 | 0.00 |
| 35000 | CIPCODE | 26.0505 | Parasitology | 7 | 0.00 |
| 35000 | CIPCODE | 26.0506 | Mycology | 4 | 0.00 |
| 35000 | CIPCODE | 26.0507 | Immunology | 133 | 0.01 |
| 35000 | CIPCODE | 26.0508 | Microbiology and Immunology | 145 | 0.01 |
| 35000 | CIPCODE | 26.0509 | Infectious Disease and Global Health | 31 | 0.00 |
| 35000 | CIPCODE | 26.0599 | Microbiological Sciences and Immunology, Other | 72 | 0.00 |
| 35000 | CIPCODE | 26.0701 | Zoology/Animal Biology | 256 | 0.02 |
| 35000 | CIPCODE | 26.0702 | Entomology | 185 | 0.01 |
| 35000 | CIPCODE | 26.0707 | Animal Physiology | 62 | 0.00 |
| 35000 | CIPCODE | 26.0708 | Animal Behavior and Ethology | 52 | 0.00 |
| 35000 | CIPCODE | 26.0709 | Wildlife Biology | 129 | 0.01 |
| 35000 | CIPCODE | 26.0799 | Zoology/Animal Biology, Other | 15 | 0.00 |
| 35000 | CIPCODE | 26.0801 | Genetics, General | 172 | 0.01 |
| 35000 | CIPCODE | 26.0802 | Molecular Genetics | 75 | 0.00 |
| 35000 | CIPCODE | 26.0804 | Animal Genetics | 24 | 0.00 |
| 35000 | CIPCODE | 26.0805 | Plant Genetics | 11 | 0.00 |
| 35000 | CIPCODE | 26.0806 | Human/Medical Genetics | 146 | 0.01 |
| 35000 | CIPCODE | 26.0807 | Genome Sciences/Genomics | 113 | 0.01 |
| 35000 | CIPCODE | 26.0899 | Genetics, Other | 15 | 0.00 |
| 35000 | CIPCODE | 26.0901 | Physiology, General | 334 | 0.02 |
| 35000 | CIPCODE | 26.0902 | Molecular Physiology | 33 | 0.00 |
| 35000 | CIPCODE | 26.0903 | Cell Physiology | 31 | 0.00 |
| 35000 | CIPCODE | 26.0904 | Endocrinology | 8 | 0.00 |
| 35000 | CIPCODE | 26.0905 | Reproductive Biology | 13 | 0.00 |
| 35000 | CIPCODE | 26.0907 | Cardiovascular Science | 16 | 0.00 |
| 35000 | CIPCODE | 26.0908 | Exercise Physiology and Kinesiology | 645 | 0.04 |
| 35000 | CIPCODE | 26.0909 | Vision Science/Physiological Optics | 50 | 0.00 |
| 35000 | CIPCODE | 26.0910 | Pathology/Experimental Pathology | 198 | 0.01 |
| 35000 | CIPCODE | 26.0911 | Oncology and Cancer Biology | 115 | 0.01 |
| 35000 | CIPCODE | 26.0912 | Aerospace Physiology and Medicine | 9 | 0.00 |
| 35000 | CIPCODE | 26.0913 | Biomechanics | 24 | 0.00 |
| 35000 | CIPCODE | 26.0999 | Physiology, Pathology, and Related Sciences, Other | 63 | 0.00 |
| 35000 | CIPCODE | 26.1001 | Pharmacology | 274 | 0.02 |
| 35000 | CIPCODE | 26.1002 | Molecular Pharmacology | 64 | 0.00 |
| 35000 | CIPCODE | 26.1003 | Neuropharmacology | 13 | 0.00 |
| 35000 | CIPCODE | 26.1004 | Toxicology | 145 | 0.01 |
| 35000 | CIPCODE | 26.1005 | Molecular Toxicology | 3 | 0.00 |
| 35000 | CIPCODE | 26.1006 | Environmental Toxicology | 50 | 0.00 |
| 35000 | CIPCODE | 26.1007 | Pharmacology and Toxicology | 81 | 0.00 |
| 35000 | CIPCODE | 26.1099 | Pharmacology and Toxicology, Other | 27 | 0.00 |
| 35000 | CIPCODE | 26.1101 | Biometry/Biometrics | 78 | 0.00 |
| 35000 | CIPCODE | 26.1102 | Biostatistics | 380 | 0.02 |
| 35000 | CIPCODE | 26.1103 | Bioinformatics | 504 | 0.03 |
| 35000 | CIPCODE | 26.1104 | Computational Biology | 122 | 0.01 |
| 35000 | CIPCODE | 26.1199 | Biomathematics, Bioinformatics, and Computational Biology, Other | 100 | 0.01 |
| 35000 | CIPCODE | 26.1201 | Biotechnology | 952 | 0.06 |
| 35000 | CIPCODE | 26.1301 | Ecology | 328 | 0.02 |
| 35000 | CIPCODE | 26.1302 | Marine Biology and Biological Oceanography | 366 | 0.02 |
| 35000 | CIPCODE | 26.1303 | Evolutionary Biology | 84 | 0.00 |
| 35000 | CIPCODE | 26.1304 | Aquatic Biology/Limnology | 43 | 0.00 |
| 35000 | CIPCODE | 26.1305 | Environmental Biology | 229 | 0.01 |
| 35000 | CIPCODE | 26.1306 | Population Biology | 13 | 0.00 |
| 35000 | CIPCODE | 26.1307 | Conservation Biology | 166 | 0.01 |
| 35000 | CIPCODE | 26.1308 | Systematic Biology/Biological Systematics | 7 | 0.00 |
| 35000 | CIPCODE | 26.1309 | Epidemiology | 429 | 0.03 |
| 35000 | CIPCODE | 26.1310 | Ecology and Evolutionary Biology | 190 | 0.01 |
| 35000 | CIPCODE | 26.1311 | Epidemiology and Biostatistics | 50 | 0.00 |
| 35000 | CIPCODE | 26.1399 | Ecology, Evolution, Systematics and Population Biology, Other | 65 | 0.00 |
| 35000 | CIPCODE | 26.1401 | Molecular Medicine | 43 | 0.00 |
| 35000 | CIPCODE | 26.1501 | Neuroscience | 1681 | 0.10 |
| 35000 | CIPCODE | 26.1503 | Neurobiology and Anatomy | 102 | 0.01 |
| 35000 | CIPCODE | 26.1504 | Neurobiology and Behavior | 40 | 0.00 |
| 35000 | CIPCODE | 26.1599 | Neurobiology and Neurosciences, Other | 48 | 0.00 |
| 35000 | CIPCODE | 26.9999 | Biological and Biomedical Sciences, Other | 609 | 0.04 |
| 35000 | CIPCODE | 27.0101 | Mathematics, General | 6561 | 0.39 |
| 35000 | CIPCODE | 27.0102 | Algebra and Number Theory | 7 | 0.00 |
| 35000 | CIPCODE | 27.0103 | Analysis and Functional Analysis | 9 | 0.00 |
| 35000 | CIPCODE | 27.0105 | Topology and Foundations | 6 | 0.00 |
| 35000 | CIPCODE | 27.0199 | Mathematics, Other | 147 | 0.01 |
| 35000 | CIPCODE | 27.0301 | Applied Mathematics, General | 1121 | 0.07 |
| 35000 | CIPCODE | 27.0303 | Computational Mathematics | 153 | 0.01 |
| 35000 | CIPCODE | 27.0304 | Computational and Applied Mathematics | 231 | 0.01 |
| 35000 | CIPCODE | 27.0305 | Financial Mathematics | 506 | 0.03 |
| 35000 | CIPCODE | 27.0306 | Mathematical Biology | 18 | 0.00 |
| 35000 | CIPCODE | 27.0399 | Applied Mathematics, Other | 108 | 0.01 |
| 35000 | CIPCODE | 27.0501 | Statistics, General | 1214 | 0.07 |
| 35000 | CIPCODE | 27.0502 | Mathematical Statistics and Probability | 97 | 0.01 |
| 35000 | CIPCODE | 27.0503 | Mathematics and Statistics | 220 | 0.01 |
| 35000 | CIPCODE | 27.0599 | Statistics, Other | 140 | 0.01 |
| 35000 | CIPCODE | 27.0601 | Applied Statistics, General | 143 | 0.01 |
| 35000 | CIPCODE | 27.9999 | Mathematics and Statistics, Other | 198 | 0.01 |
| 35000 | CIPCODE | 29.0201 | Intelligence, General | 99 | 0.01 |
| 35000 | CIPCODE | 29.0202 | Strategic Intelligence | 65 | 0.00 |
| 35000 | CIPCODE | 29.0203 | Signal/Geospatial Intelligence | 40 | 0.00 |
| 35000 | CIPCODE | 29.0204 | Command & Control (C3, C4I) Systems and Operations | 6 | 0.00 |
| 35000 | CIPCODE | 29.0206 | Information/Psychological Warfare and Military Media Relations | 3 | 0.00 |
| 35000 | CIPCODE | 29.0207 | Cyber/Electronic Operations and Warfare | 200 | 0.01 |
| 35000 | CIPCODE | 29.0299 | Intelligence, Command Control and Information Operations, Other | 9 | 0.00 |
| 35000 | CIPCODE | 29.0301 | Combat Systems Engineering | 6 | 0.00 |
| 35000 | CIPCODE | 29.0303 | Engineering Acoustics | 6 | 0.00 |
| 35000 | CIPCODE | 29.0304 | Low-Observables and Stealth Technology | 3 | 0.00 |
| 35000 | CIPCODE | 29.0305 | Space Systems Operations | 26 | 0.00 |
| 35000 | CIPCODE | 29.0306 | Operational Oceanography | 7 | 0.00 |
| 35000 | CIPCODE | 29.0307 | Undersea Warfare | 5 | 0.00 |
| 35000 | CIPCODE | 29.0399 | Military Applied Sciences, Other | 32 | 0.00 |
| 35000 | CIPCODE | 29.0401 | Aerospace Ground Equipment Technology | 6 | 0.00 |
| 35000 | CIPCODE | 29.0402 | Air and Space Operations Technology | 17 | 0.00 |
| 35000 | CIPCODE | 29.0404 | Explosive Ordinance/Bomb Disposal | 6 | 0.00 |
| 35000 | CIPCODE | 29.0405 | Joint Command/Task Force (C3, C4I) Systems | 3 | 0.00 |
| 35000 | CIPCODE | 29.0601 | Military Technology and Applied Sciences Management | 3 | 0.00 |
| 35000 | CIPCODE | 29.9999 | Military Technologies and Applied Sciences, Other | 35 | 0.00 |
| 35000 | CIPCODE | 30.0000 | Multi-/Interdisciplinary Studies, General | 1589 | 0.09 |
| 35000 | CIPCODE | 30.0001 | Comprehensive Transition and Postsecondary (CTP) Program | 56 | 0.00 |
| 35000 | CIPCODE | 30.0101 | Biological and Physical Sciences | 1284 | 0.08 |
| 35000 | CIPCODE | 30.0501 | Peace Studies and Conflict Resolution | 489 | 0.03 |
| 35000 | CIPCODE | 30.0601 | Systems Science and Theory | 235 | 0.01 |
| 35000 | CIPCODE | 30.0801 | Mathematics and Computer Science | 359 | 0.02 |
| 35000 | CIPCODE | 30.1001 | Biopsychology | 94 | 0.01 |
| 35000 | CIPCODE | 30.1101 | Gerontology | 729 | 0.04 |
| 35000 | CIPCODE | 30.1201 | Historic Preservation and Conservation, General | 212 | 0.01 |
| 35000 | CIPCODE | 30.1202 | Cultural Resource Management and Policy Analysis | 91 | 0.01 |
| 35000 | CIPCODE | 30.1299 | Historic Preservation and Conservation, Other | 24 | 0.00 |
| 35000 | CIPCODE | 30.1301 | Medieval and Renaissance Studies | 242 | 0.01 |
| 35000 | CIPCODE | 30.1401 | Museology/Museum Studies | 362 | 0.02 |
| 35000 | CIPCODE | 30.1501 | Science, Technology and Society | 290 | 0.02 |
| 35000 | CIPCODE | 30.1601 | Accounting and Computer Science | 45 | 0.00 |
| 35000 | CIPCODE | 30.1701 | Behavioral Sciences | 562 | 0.03 |
| 35000 | CIPCODE | 30.1801 | Natural Sciences | 520 | 0.03 |
| 35000 | CIPCODE | 30.1901 | Nutrition Sciences | 752 | 0.04 |
| 35000 | CIPCODE | 30.2001 | International/Globalization Studies | 1881 | 0.11 |
| 35000 | CIPCODE | 30.2101 | Holocaust and Related Studies | 56 | 0.00 |
| 35000 | CIPCODE | 30.2201 | Ancient Studies/Civilization | 175 | 0.01 |
| 35000 | CIPCODE | 30.2202 | Classical, Ancient Mediterranean, and Near Eastern Studies and Archaeology | 208 | 0.01 |
| 35000 | CIPCODE | 30.2299 | Classical and Ancient Studies, Other | 3 | 0.00 |
| 35000 | CIPCODE | 30.2301 | Intercultural/Multicultural and Diversity Studies | 571 | 0.03 |
| 35000 | CIPCODE | 30.2501 | Cognitive Science, General | 400 | 0.02 |
| 35000 | CIPCODE | 30.2502 | Contemplative Studies/Inquiry | 9 | 0.00 |
| 35000 | CIPCODE | 30.2601 | Cultural Studies/Critical Theory and Analysis | 229 | 0.01 |
| 35000 | CIPCODE | 30.2701 | Human Biology | 169 | 0.01 |
| 35000 | CIPCODE | 30.2801 | Dispute Resolution | 179 | 0.01 |
| 35000 | CIPCODE | 30.2901 | Maritime Studies | 22 | 0.00 |
| 35000 | CIPCODE | 30.3001 | Computational Science | 433 | 0.03 |
| 35000 | CIPCODE | 30.3101 | Human Computer Interaction | 247 | 0.01 |
| 35000 | CIPCODE | 30.3201 | Marine Sciences | 152 | 0.01 |
| 35000 | CIPCODE | 30.3301 | Sustainability Studies | 1142 | 0.07 |
| 35000 | CIPCODE | 30.3401 | Anthrozoology | 17 | 0.00 |
| 35000 | CIPCODE | 30.3501 | Climate Science | 46 | 0.00 |
| 35000 | CIPCODE | 30.3601 | Cultural Studies and Comparative Literature | 20 | 0.00 |
| 35000 | CIPCODE | 30.3701 | Design for Human Health | 3 | 0.00 |
| 35000 | CIPCODE | 30.3801 | Earth Systems Science | 33 | 0.00 |
| 35000 | CIPCODE | 30.3901 | Economics and Computer Science | 38 | 0.00 |
| 35000 | CIPCODE | 30.4001 | Economics and Foreign Language/Literature | 3 | 0.00 |
| 35000 | CIPCODE | 30.4101 | Environmental Geosciences | 56 | 0.00 |
| 35000 | CIPCODE | 30.4201 | Geoarcheaology | 10 | 0.00 |
| 35000 | CIPCODE | 30.4301 | Geobiology | 3 | 0.00 |
| 35000 | CIPCODE | 30.4401 | Geography and Environmental Studies | 342 | 0.02 |
| 35000 | CIPCODE | 30.4501 | History and Language/Literature | 12 | 0.00 |
| 35000 | CIPCODE | 30.4601 | History and Political Science | 72 | 0.00 |
| 35000 | CIPCODE | 30.4701 | Linguistics and Anthropology | 14 | 0.00 |
| 35000 | CIPCODE | 30.4801 | Linguistics and Computer Science | 12 | 0.00 |
| 35000 | CIPCODE | 30.4901 | Mathematical Economics | 46 | 0.00 |
| 35000 | CIPCODE | 30.5101 | Philosophy, Politics, and Economics | 81 | 0.00 |
| 35000 | CIPCODE | 30.5201 | Digital Humanities and Textual Studies, General | 3 | 0.00 |
| 35000 | CIPCODE | 30.5202 | Digital Humanities | 79 | 0.00 |
| 35000 | CIPCODE | 30.5203 | Textual Studies | 4 | 0.00 |
| 35000 | CIPCODE | 30.5299 | Digital Humanities and Textual Studies, Other | 3 | 0.00 |
| 35000 | CIPCODE | 30.5301 | Thanatology | 19 | 0.00 |
| 35000 | CIPCODE | 30.7001 | Data Science, General | 1359 | 0.08 |
| 35000 | CIPCODE | 30.7099 | Data Science, Other | 50 | 0.00 |
| 35000 | CIPCODE | 30.7101 | Data Analytics, General | 610 | 0.04 |
| 35000 | CIPCODE | 30.7102 | Business Analytics | 895 | 0.05 |
| 35000 | CIPCODE | 30.7103 | Data Visualization | 30 | 0.00 |
| 35000 | CIPCODE | 30.7104 | Financial Analytics | 182 | 0.01 |
| 35000 | CIPCODE | 30.7199 | Data Analytics, Other | 73 | 0.00 |
| 35000 | CIPCODE | 30.9999 | Multi-/Interdisciplinary Studies, Other | 3339 | 0.20 |
| 35000 | CIPCODE | 31.0101 | Parks, Recreation, and Leisure Studies | 579 | 0.03 |
| 35000 | CIPCODE | 31.0301 | Parks, Recreation, and Leisure Facilities Management, General | 614 | 0.04 |
| 35000 | CIPCODE | 31.0302 | Golf Course Operation and Grounds Management | 52 | 0.00 |
| 35000 | CIPCODE | 31.0399 | Parks, Recreation, and Leisure Facilities Management, Other | 6 | 0.00 |
| 35000 | CIPCODE | 31.0501 | Sports, Kinesiology, and Physical Education/Fitness, General | 1860 | 0.11 |
| 35000 | CIPCODE | 31.0504 | Sport and Fitness Administration/Management | 2905 | 0.17 |
| 35000 | CIPCODE | 31.0505 | Exercise Science and Kinesiology | 3183 | 0.19 |
| 35000 | CIPCODE | 31.0507 | Physical Fitness Technician | 676 | 0.04 |
| 35000 | CIPCODE | 31.0508 | Sports Studies | 229 | 0.01 |
| 35000 | CIPCODE | 31.0599 | Sports, Kinesiology, and Physical Education/Fitness, Other | 362 | 0.02 |
| 35000 | CIPCODE | 31.0601 | Outdoor Education | 226 | 0.01 |
| 35000 | CIPCODE | 31.9999 | Parks, Recreation, Leisure, Fitness, and Kinesiology, Other | 107 | 0.01 |
| 35000 | CIPCODE | 38.0001 | Philosophy and Religious Studies, General | 272 | 0.02 |
| 35000 | CIPCODE | 38.0101 | Philosophy | 4255 | 0.25 |
| 35000 | CIPCODE | 38.0102 | Logic | 30 | 0.00 |
| 35000 | CIPCODE | 38.0103 | Ethics | 136 | 0.01 |
| 35000 | CIPCODE | 38.0104 | Applied and Professional Ethics | 175 | 0.01 |
| 35000 | CIPCODE | 38.0199 | Philosophy, Other | 131 | 0.01 |
| 35000 | CIPCODE | 38.0201 | Religion/Religious Studies | 2556 | 0.15 |
| 35000 | CIPCODE | 38.0202 | Buddhist Studies | 15 | 0.00 |
| 35000 | CIPCODE | 38.0203 | Christian Studies | 360 | 0.02 |
| 35000 | CIPCODE | 38.0205 | Islamic Studies | 78 | 0.00 |
| 35000 | CIPCODE | 38.0206 | Jewish/Judaic Studies | 391 | 0.02 |
| 35000 | CIPCODE | 38.0207 | Talmudic Studies | 326 | 0.02 |
| 35000 | CIPCODE | 38.0208 | Catholic Studies | 38 | 0.00 |
| 35000 | CIPCODE | 38.0299 | Religion/Religious Studies, Other | 113 | 0.01 |
| 35000 | CIPCODE | 38.9999 | Philosophy and Religious Studies, Other | 199 | 0.01 |
| 35000 | CIPCODE | 39.0201 | Bible/Biblical Studies | 1210 | 0.07 |
| 35000 | CIPCODE | 39.0301 | Missions/Missionary Studies | 533 | 0.03 |
| 35000 | CIPCODE | 39.0302 | Church Planting | 32 | 0.00 |
| 35000 | CIPCODE | 39.0399 | Missions/Missionary Studies and Missiology, Other | 17 | 0.00 |
| 35000 | CIPCODE | 39.0401 | Religious Education | 524 | 0.03 |
| 35000 | CIPCODE | 39.0501 | Religious/Sacred Music | 483 | 0.03 |
| 35000 | CIPCODE | 39.0502 | Worship Ministry | 107 | 0.01 |
| 35000 | CIPCODE | 39.0599 | Religious Music and Worship, Other | 13 | 0.00 |
| 35000 | CIPCODE | 39.0601 | Theology/Theological Studies | 1508 | 0.09 |
| 35000 | CIPCODE | 39.0602 | Divinity/Ministry | 1044 | 0.06 |
| 35000 | CIPCODE | 39.0604 | Pre-Theology/Pre-Ministerial Studies | 141 | 0.01 |
| 35000 | CIPCODE | 39.0605 | Rabbinical Studies | 50 | 0.00 |
| 35000 | CIPCODE | 39.0699 | Theological and Ministerial Studies, Other | 551 | 0.03 |
| 35000 | CIPCODE | 39.0701 | Pastoral Studies/Counseling | 575 | 0.03 |
| 35000 | CIPCODE | 39.0702 | Youth Ministry | 343 | 0.02 |
| 35000 | CIPCODE | 39.0703 | Urban Ministry | 61 | 0.00 |
| 35000 | CIPCODE | 39.0704 | Women's Ministry | 46 | 0.00 |
| 35000 | CIPCODE | 39.0705 | Lay Ministry | 276 | 0.02 |
| 35000 | CIPCODE | 39.0706 | Chaplain/Chaplaincy Studies | 66 | 0.00 |
| 35000 | CIPCODE | 39.0799 | Pastoral Counseling and Specialized Ministries, Other | 320 | 0.02 |
| 35000 | CIPCODE | 39.0801 | Religious Institution Administration and Management | 24 | 0.00 |
| 35000 | CIPCODE | 39.9999 | Theology and Religious Vocations, Other | 428 | 0.03 |
| 35000 | CIPCODE | 40.0101 | Physical Sciences, General | 668 | 0.04 |
| 35000 | CIPCODE | 40.0201 | Astronomy | 473 | 0.03 |
| 35000 | CIPCODE | 40.0202 | Astrophysics | 219 | 0.01 |
| 35000 | CIPCODE | 40.0203 | Planetary Astronomy and Science | 66 | 0.00 |
| 35000 | CIPCODE | 40.0299 | Astronomy and Astrophysics, Other | 64 | 0.00 |
| 35000 | CIPCODE | 40.0401 | Atmospheric Sciences and Meteorology, General | 323 | 0.02 |
| 35000 | CIPCODE | 40.0402 | Atmospheric Chemistry and Climatology | 21 | 0.00 |
| 35000 | CIPCODE | 40.0403 | Atmospheric Physics and Dynamics | 4 | 0.00 |
| 35000 | CIPCODE | 40.0404 | Meteorology | 140 | 0.01 |
| 35000 | CIPCODE | 40.0499 | Atmospheric Sciences and Meteorology, Other | 34 | 0.00 |
| 35000 | CIPCODE | 40.0501 | Chemistry, General | 5585 | 0.33 |
| 35000 | CIPCODE | 40.0502 | Analytical Chemistry | 50 | 0.00 |
| 35000 | CIPCODE | 40.0503 | Inorganic Chemistry | 4 | 0.00 |
| 35000 | CIPCODE | 40.0504 | Organic Chemistry | 14 | 0.00 |
| 35000 | CIPCODE | 40.0506 | Physical Chemistry | 13 | 0.00 |
| 35000 | CIPCODE | 40.0507 | Polymer Chemistry | 44 | 0.00 |
| 35000 | CIPCODE | 40.0508 | Chemical Physics | 97 | 0.01 |
| 35000 | CIPCODE | 40.0509 | Environmental Chemistry | 75 | 0.00 |
| 35000 | CIPCODE | 40.0510 | Forensic Chemistry | 155 | 0.01 |
| 35000 | CIPCODE | 40.0511 | Theoretical Chemistry | 9 | 0.00 |
| 35000 | CIPCODE | 40.0512 | Cheminformatics/Chemistry Informatics | 3 | 0.00 |
| 35000 | CIPCODE | 40.0599 | Chemistry, Other | 308 | 0.02 |
| 35000 | CIPCODE | 40.0601 | Geology/Earth Science, General | 2287 | 0.14 |
| 35000 | CIPCODE | 40.0602 | Geochemistry | 53 | 0.00 |
| 35000 | CIPCODE | 40.0603 | Geophysics and Seismology | 180 | 0.01 |
| 35000 | CIPCODE | 40.0604 | Paleontology | 17 | 0.00 |
| 35000 | CIPCODE | 40.0605 | Hydrology and Water Resources Science | 194 | 0.01 |
| 35000 | CIPCODE | 40.0607 | Oceanography, Chemical and Physical | 175 | 0.01 |
| 35000 | CIPCODE | 40.0699 | Geological and Earth Sciences/Geosciences, Other | 434 | 0.03 |
| 35000 | CIPCODE | 40.0801 | Physics, General | 3957 | 0.23 |
| 35000 | CIPCODE | 40.0802 | Atomic/Molecular Physics | 21 | 0.00 |
| 35000 | CIPCODE | 40.0804 | Elementary Particle Physics | 10 | 0.00 |
| 35000 | CIPCODE | 40.0806 | Nuclear Physics | 7 | 0.00 |
| 35000 | CIPCODE | 40.0807 | Optics/Optical Sciences | 78 | 0.00 |
| 35000 | CIPCODE | 40.0808 | Condensed Matter and Materials Physics | 7 | 0.00 |
| 35000 | CIPCODE | 40.0809 | Acoustics | 27 | 0.00 |
| 35000 | CIPCODE | 40.0810 | Theoretical and Mathematical Physics | 43 | 0.00 |
| 35000 | CIPCODE | 40.0899 | Physics, Other | 265 | 0.02 |
| 35000 | CIPCODE | 40.1001 | Materials Science | 235 | 0.01 |
| 35000 | CIPCODE | 40.1002 | Materials Chemistry | 18 | 0.00 |
| 35000 | CIPCODE | 40.1099 | Materials Sciences, Other | 23 | 0.00 |
| 35000 | CIPCODE | 40.1101 | Physics and Astronomy | 17 | 0.00 |
| 35000 | CIPCODE | 40.9999 | Physical Sciences, Other | 176 | 0.01 |
| 35000 | CIPCODE | 41.0000 | Science Technologies/Technicians, General | 80 | 0.00 |
| 35000 | CIPCODE | 41.0101 | Biology/Biotechnology Technology/Technician | 491 | 0.03 |
| 35000 | CIPCODE | 41.0204 | Industrial Radiologic Technology/Technician | 40 | 0.00 |
| 35000 | CIPCODE | 41.0205 | Nuclear/Nuclear Power Technology/Technician | 47 | 0.00 |
| 35000 | CIPCODE | 41.0299 | Nuclear and Industrial Radiologic Technologies/Technicians, Other | 8 | 0.00 |
| 35000 | CIPCODE | 41.0301 | Chemical Technology/Technician | 379 | 0.02 |
| 35000 | CIPCODE | 41.0303 | Chemical Process Technology | 56 | 0.00 |
| 35000 | CIPCODE | 41.0399 | Physical Science Technologies/Technicians, Other | 3 | 0.00 |
| 35000 | CIPCODE | 41.9999 | Science Technologies/Technicians, Other | 279 | 0.02 |
| 35000 | CIPCODE | 42.0101 | Psychology, General | 7594 | 0.45 |
| 35000 | CIPCODE | 42.2701 | Cognitive Psychology and Psycholinguistics | 128 | 0.01 |
| 35000 | CIPCODE | 42.2702 | Comparative Psychology | 6 | 0.00 |
| 35000 | CIPCODE | 42.2703 | Developmental and Child Psychology | 296 | 0.02 |
| 35000 | CIPCODE | 42.2704 | Experimental Psychology | 391 | 0.02 |
| 35000 | CIPCODE | 42.2705 | Personality Psychology | 13 | 0.00 |
| 35000 | CIPCODE | 42.2706 | Behavioral Neuroscience | 162 | 0.01 |
| 35000 | CIPCODE | 42.2707 | Social Psychology | 144 | 0.01 |
| 35000 | CIPCODE | 42.2708 | Psychometrics and Quantitative Psychology | 60 | 0.00 |
| 35000 | CIPCODE | 42.2709 | Psychopharmacology | 17 | 0.00 |
| 35000 | CIPCODE | 42.2799 | Research and Experimental Psychology, Other | 785 | 0.05 |
| 35000 | CIPCODE | 42.2801 | Clinical Psychology | 834 | 0.05 |
| 35000 | CIPCODE | 42.2802 | Community Psychology | 163 | 0.01 |
| 35000 | CIPCODE | 42.2803 | Counseling Psychology | 1166 | 0.07 |
| 35000 | CIPCODE | 42.2804 | Industrial and Organizational Psychology | 542 | 0.03 |
| 35000 | CIPCODE | 42.2805 | School Psychology | 898 | 0.05 |
| 35000 | CIPCODE | 42.2806 | Educational Psychology | 439 | 0.03 |
| 35000 | CIPCODE | 42.2807 | Clinical Child Psychology | 53 | 0.00 |
| 35000 | CIPCODE | 42.2808 | Environmental Psychology | 18 | 0.00 |
| 35000 | CIPCODE | 42.2809 | Geropsychology | 10 | 0.00 |
| 35000 | CIPCODE | 42.2810 | Health/Medical Psychology | 112 | 0.01 |
| 35000 | CIPCODE | 42.2811 | Family Psychology | 46 | 0.00 |
| 35000 | CIPCODE | 42.2812 | Forensic Psychology | 271 | 0.02 |
| 35000 | CIPCODE | 42.2813 | Applied Psychology | 390 | 0.02 |
| 35000 | CIPCODE | 42.2814 | Applied Behavior Analysis | 673 | 0.04 |
| 35000 | CIPCODE | 42.2815 | Performance and Sport Psychology | 64 | 0.00 |
| 35000 | CIPCODE | 42.2817 | Transpersonal/Spiritual Psychology | 12 | 0.00 |
| 35000 | CIPCODE | 42.2899 | Clinical, Counseling and Applied Psychology, Other | 193 | 0.01 |
| 35000 | CIPCODE | 42.9999 | Psychology, Other | 405 | 0.02 |
| 35000 | CIPCODE | 43.0100 | Criminal Justice and Corrections, General | 326 | 0.02 |
| 35000 | CIPCODE | 43.0102 | Corrections | 1015 | 0.06 |
| 35000 | CIPCODE | 43.0103 | Criminal Justice/Law Enforcement Administration | 3306 | 0.20 |
| 35000 | CIPCODE | 43.0104 | Criminal Justice/Safety Studies | 4084 | 0.24 |
| 35000 | CIPCODE | 43.0107 | Criminal Justice/Police Science | 3093 | 0.18 |
| 35000 | CIPCODE | 43.0109 | Security and Loss Prevention Services | 160 | 0.01 |
| 35000 | CIPCODE | 43.0110 | Juvenile Corrections | 82 | 0.00 |
| 35000 | CIPCODE | 43.0112 | Securities Services Administration/Management | 174 | 0.01 |
| 35000 | CIPCODE | 43.0113 | Corrections Administration | 65 | 0.00 |
| 35000 | CIPCODE | 43.0114 | Law Enforcement Investigation and Interviewing | 79 | 0.00 |
| 35000 | CIPCODE | 43.0119 | Critical Incident Response/Special Police Operations | 10 | 0.00 |
| 35000 | CIPCODE | 43.0120 | Protective Services Operations | 43 | 0.00 |
| 35000 | CIPCODE | 43.0199 | Corrections and Criminal Justice, Other | 532 | 0.03 |
| 35000 | CIPCODE | 43.0201 | Fire Prevention and Safety Technology/Technician | 900 | 0.05 |
| 35000 | CIPCODE | 43.0202 | Fire Services Administration | 371 | 0.02 |
| 35000 | CIPCODE | 43.0203 | Fire Science/Fire-fighting | 1592 | 0.09 |
| 35000 | CIPCODE | 43.0204 | Fire Systems Technology | 42 | 0.00 |
| 35000 | CIPCODE | 43.0205 | Fire/Arson Investigation and Prevention | 39 | 0.00 |
| 35000 | CIPCODE | 43.0206 | Wildland/Forest Firefighting and Investigation | 91 | 0.01 |
| 35000 | CIPCODE | 43.0299 | Fire Protection, Other | 45 | 0.00 |
| 35000 | CIPCODE | 43.0301 | Homeland Security | 576 | 0.03 |
| 35000 | CIPCODE | 43.0302 | Crisis/Emergency/Disaster Management | 860 | 0.05 |
| 35000 | CIPCODE | 43.0303 | Critical Infrastructure Protection | 167 | 0.01 |
| 35000 | CIPCODE | 43.0304 | Terrorism and Counterterrorism Operations | 72 | 0.00 |
| 35000 | CIPCODE | 43.0399 | Homeland Security, Other | 104 | 0.01 |
| 35000 | CIPCODE | 43.0401 | Security Science and Technology, General | 18 | 0.00 |
| 35000 | CIPCODE | 43.0402 | Criminalistics and Criminal Science | 152 | 0.01 |
| 35000 | CIPCODE | 43.0403 | Cyber/Computer Forensics and Counterterrorism | 606 | 0.04 |
| 35000 | CIPCODE | 43.0404 | Cybersecurity Defense Strategy/Policy | 302 | 0.02 |
| 35000 | CIPCODE | 43.0405 | Financial Forensics and Fraud Investigation | 198 | 0.01 |
| 35000 | CIPCODE | 43.0406 | Forensic Science and Technology | 1168 | 0.07 |
| 35000 | CIPCODE | 43.0407 | Geospatial Intelligence | 36 | 0.00 |
| 35000 | CIPCODE | 43.0408 | Law Enforcement Intelligence Analysis | 73 | 0.00 |
| 35000 | CIPCODE | 43.0499 | Security Science and Technology, Other | 3 | 0.00 |
| 35000 | CIPCODE | 43.9999 | Homeland Security, Law Enforcement, Firefighting and Related Protective Services, Other | 403 | 0.02 |
| 35000 | CIPCODE | 44.0000 | Human Services, General | 2066 | 0.12 |
| 35000 | CIPCODE | 44.0201 | Community Organization and Advocacy | 640 | 0.04 |
| 35000 | CIPCODE | 44.0401 | Public Administration | 2079 | 0.12 |
| 35000 | CIPCODE | 44.0402 | Public Works Management | 13 | 0.00 |
| 35000 | CIPCODE | 44.0403 | Transportation and Infrastructure Planning/Studies | 9 | 0.00 |
| 35000 | CIPCODE | 44.0499 | Public Administration, Other | 21 | 0.00 |
| 35000 | CIPCODE | 44.0501 | Public Policy Analysis, General | 883 | 0.05 |
| 35000 | CIPCODE | 44.0502 | Education Policy Analysis | 63 | 0.00 |
| 35000 | CIPCODE | 44.0503 | Health Policy Analysis | 122 | 0.01 |
| 35000 | CIPCODE | 44.0504 | International Policy Analysis | 107 | 0.01 |
| 35000 | CIPCODE | 44.0599 | Public Policy Analysis, Other | 45 | 0.00 |
| 35000 | CIPCODE | 44.0701 | Social Work | 3382 | 0.20 |
| 35000 | CIPCODE | 44.0702 | Youth Services/Administration | 140 | 0.01 |
| 35000 | CIPCODE | 44.0703 | Forensic Social Work | 13 | 0.00 |
| 35000 | CIPCODE | 44.0799 | Social Work, Other | 189 | 0.01 |
| 35000 | CIPCODE | 44.9999 | Public Administration and Social Service Professions, Other | 347 | 0.02 |
| 35000 | CIPCODE | 45.0101 | Social Sciences, General | 1702 | 0.10 |
| 35000 | CIPCODE | 45.0102 | Research Methodology and Quantitative Methods | 281 | 0.02 |
| 35000 | CIPCODE | 45.0103 | Survey Research/Methodology | 9 | 0.00 |
| 35000 | CIPCODE | 45.0199 | Social Sciences, Other | 9 | 0.00 |
| 35000 | CIPCODE | 45.0201 | Anthropology, General | 2747 | 0.16 |
| 35000 | CIPCODE | 45.0202 | Physical and Biological Anthropology | 48 | 0.00 |
| 35000 | CIPCODE | 45.0203 | Medical Anthropology | 89 | 0.01 |
| 35000 | CIPCODE | 45.0204 | Cultural Anthropology | 61 | 0.00 |
| 35000 | CIPCODE | 45.0205 | Forensic Anthropology | 17 | 0.00 |
| 35000 | CIPCODE | 45.0299 | Anthropology, Other | 129 | 0.01 |
| 35000 | CIPCODE | 45.0301 | Archeology | 362 | 0.02 |
| 35000 | CIPCODE | 45.0401 | Criminology | 1158 | 0.07 |
| 35000 | CIPCODE | 45.0501 | Demography and Population Studies | 76 | 0.00 |
| 35000 | CIPCODE | 45.0502 | Applied Demography | 4 | 0.00 |
| 35000 | CIPCODE | 45.0601 | Economics, General | 3644 | 0.22 |
| 35000 | CIPCODE | 45.0602 | Applied Economics | 188 | 0.01 |
| 35000 | CIPCODE | 45.0603 | Econometrics and Quantitative Economics | 1641 | 0.10 |
| 35000 | CIPCODE | 45.0604 | Development Economics and International Development | 230 | 0.01 |
| 35000 | CIPCODE | 45.0605 | International Economics | 140 | 0.01 |
| 35000 | CIPCODE | 45.0699 | Economics, Other | 159 | 0.01 |
| 35000 | CIPCODE | 45.0701 | Geography | 1646 | 0.10 |
| 35000 | CIPCODE | 45.0702 | Geographic Information Science and Cartography | 1587 | 0.09 |
| 35000 | CIPCODE | 45.0799 | Geography, Other | 143 | 0.01 |
| 35000 | CIPCODE | 45.0901 | International Relations and Affairs | 1869 | 0.11 |
| 35000 | CIPCODE | 45.0902 | National Security Policy Studies | 181 | 0.01 |
| 35000 | CIPCODE | 45.0999 | International Relations and National Security Studies, Other | 109 | 0.01 |
| 35000 | CIPCODE | 45.1001 | Political Science and Government, General | 5883 | 0.35 |
| 35000 | CIPCODE | 45.1002 | American Government and Politics (United States) | 154 | 0.01 |
| 35000 | CIPCODE | 45.1004 | Political Economy | 115 | 0.01 |
| 35000 | CIPCODE | 45.1099 | Political Science and Government, Other | 307 | 0.02 |
| 35000 | CIPCODE | 45.1101 | Sociology, General | 5448 | 0.32 |
| 35000 | CIPCODE | 45.1102 | Applied/Public Sociology | 46 | 0.00 |
| 35000 | CIPCODE | 45.1103 | Rural Sociology | 29 | 0.00 |
| 35000 | CIPCODE | 45.1199 | Sociology, Other | 17 | 0.00 |
| 35000 | CIPCODE | 45.1201 | Urban Studies/Affairs | 549 | 0.03 |
| 35000 | CIPCODE | 45.1301 | Sociology and Anthropology | 265 | 0.02 |
| 35000 | CIPCODE | 45.9999 | Social Sciences, Other | 597 | 0.04 |
| 35000 | CIPCODE | 46.0000 | Construction Trades, General | 526 | 0.03 |
| 35000 | CIPCODE | 46.0101 | Mason/Masonry | 214 | 0.01 |
| 35000 | CIPCODE | 46.0201 | Carpentry/Carpenter | 1187 | 0.07 |
| 35000 | CIPCODE | 46.0301 | Electrical and Power Transmission Installation/Installer, General | 407 | 0.02 |
| 35000 | CIPCODE | 46.0302 | Electrician | 2393 | 0.14 |
| 35000 | CIPCODE | 46.0303 | Lineworker | 360 | 0.02 |
| 35000 | CIPCODE | 46.0399 | Electrical and Power Transmission Installers, Other | 88 | 0.01 |
| 35000 | CIPCODE | 46.0401 | Building/Property Maintenance | 537 | 0.03 |
| 35000 | CIPCODE | 46.0402 | Concrete Finishing/Concrete Finisher | 36 | 0.00 |
| 35000 | CIPCODE | 46.0403 | Building/Home/Construction Inspection/Inspector | 219 | 0.01 |
| 35000 | CIPCODE | 46.0404 | Drywall Installation/Drywaller | 37 | 0.00 |
| 35000 | CIPCODE | 46.0406 | Glazier | 28 | 0.00 |
| 35000 | CIPCODE | 46.0408 | Painting/Painter and Wall Coverer | 43 | 0.00 |
| 35000 | CIPCODE | 46.0410 | Roofer | 12 | 0.00 |
| 35000 | CIPCODE | 46.0411 | Metal Building Assembly/Assembler | 4 | 0.00 |
| 35000 | CIPCODE | 46.0412 | Building/Construction Site Management/Manager | 376 | 0.02 |
| 35000 | CIPCODE | 46.0413 | Carpet, Floor, and Tile Worker | 14 | 0.00 |
| 35000 | CIPCODE | 46.0414 | Insulator | 13 | 0.00 |
| 35000 | CIPCODE | 46.0415 | Building Construction Technology/Technician | 719 | 0.04 |
| 35000 | CIPCODE | 46.0499 | Building/Construction Finishing, Management, and Inspection, Other | 240 | 0.01 |
| 35000 | CIPCODE | 46.0502 | Pipefitting/Pipefitter and Sprinkler Fitter | 204 | 0.01 |
| 35000 | CIPCODE | 46.0503 | Plumbing Technology/Plumber | 733 | 0.04 |
| 35000 | CIPCODE | 46.0504 | Well Drilling/Driller | 3 | 0.00 |
| 35000 | CIPCODE | 46.0505 | Blasting/Blaster | 5 | 0.00 |
| 35000 | CIPCODE | 46.0599 | Plumbing and Related Water Supply Services, Other | 34 | 0.00 |
| 35000 | CIPCODE | 46.9999 | Construction Trades, Other | 163 | 0.01 |
| 35000 | CIPCODE | 47.0000 | Mechanics and Repairers, General | 68 | 0.00 |
| 35000 | CIPCODE | 47.0101 | Electrical/Electronics Equipment Installation and Repair Technology/Technician, General | 655 | 0.04 |
| 35000 | CIPCODE | 47.0103 | Communications Systems Installation and Repair Technology/Technician | 148 | 0.01 |
| 35000 | CIPCODE | 47.0104 | Computer Installation and Repair Technology/Technician | 574 | 0.03 |
| 35000 | CIPCODE | 47.0105 | Industrial Electronics Technology/Technician | 623 | 0.04 |
| 35000 | CIPCODE | 47.0106 | Appliance Installation and Repair Technology/Technician | 52 | 0.00 |
| 35000 | CIPCODE | 47.0110 | Security System Installation, Repair, and Inspection Technology/Technician | 17 | 0.00 |
| 35000 | CIPCODE | 47.0199 | Electrical/Electronics Maintenance and Repair Technologies/Technicians, Other | 107 | 0.01 |
| 35000 | CIPCODE | 47.0201 | Heating, Air Conditioning, Ventilation and Refrigeration Maintenance Technology/Technician | 3034 | 0.18 |
| 35000 | CIPCODE | 47.0302 | Heavy Equipment Maintenance Technology/Technician | 322 | 0.02 |
| 35000 | CIPCODE | 47.0303 | Industrial Mechanics and Maintenance Technology/Technician | 1693 | 0.10 |
| 35000 | CIPCODE | 47.0399 | Heavy/Industrial Equipment Maintenance Technologies/Technicians, Other | 44 | 0.00 |
| 35000 | CIPCODE | 47.0402 | Gunsmithing/Gunsmith | 94 | 0.01 |
| 35000 | CIPCODE | 47.0403 | Locksmithing and Safe Repair | 8 | 0.00 |
| 35000 | CIPCODE | 47.0404 | Musical Instrument Fabrication and Repair | 48 | 0.00 |
| 35000 | CIPCODE | 47.0408 | Watchmaking and Jewelrymaking | 25 | 0.00 |
| 35000 | CIPCODE | 47.0409 | Parts and Warehousing Operations and Maintenance Technology/Technician | 3 | 0.00 |
| 35000 | CIPCODE | 47.0499 | Precision Systems Maintenance and Repair Technologies/Technicians, Other | 29 | 0.00 |
| 35000 | CIPCODE | 47.0600 | Vehicle Maintenance and Repair Technology/Technician, General | 133 | 0.01 |
| 35000 | CIPCODE | 47.0603 | Autobody/Collision and Repair Technology/Technician | 1569 | 0.09 |
| 35000 | CIPCODE | 47.0604 | Automobile/Automotive Mechanics Technology/Technician | 4264 | 0.25 |
| 35000 | CIPCODE | 47.0605 | Diesel Mechanics Technology/Technician | 1598 | 0.09 |
| 35000 | CIPCODE | 47.0606 | Small Engine Mechanics and Repair Technology/Technician | 158 | 0.01 |
| 35000 | CIPCODE | 47.0607 | Airframe Mechanics and Aircraft Maintenance Technology/Technician | 770 | 0.05 |
| 35000 | CIPCODE | 47.0608 | Aircraft Powerplant Technology/Technician | 517 | 0.03 |
| 35000 | CIPCODE | 47.0609 | Avionics Maintenance Technology/Technician | 218 | 0.01 |
| 35000 | CIPCODE | 47.0610 | Bicycle Mechanics and Repair Technology/Technician | 7 | 0.00 |
| 35000 | CIPCODE | 47.0611 | Motorcycle Maintenance and Repair Technology/Technician | 153 | 0.01 |
| 35000 | CIPCODE | 47.0613 | Medium/Heavy Vehicle and Truck Technology/Technician | 457 | 0.03 |
| 35000 | CIPCODE | 47.0614 | Alternative Fuel Vehicle Technology/Technician | 169 | 0.01 |
| 35000 | CIPCODE | 47.0615 | Engine Machinist | 9 | 0.00 |
| 35000 | CIPCODE | 47.0616 | Marine Maintenance/Fitter and Ship Repair Technology/Technician | 221 | 0.01 |
| 35000 | CIPCODE | 47.0617 | High Performance and Custom Engine Technician/Mechanic | 71 | 0.00 |
| 35000 | CIPCODE | 47.0618 | Recreation Vehicle (RV) Service Technician | 3 | 0.00 |
| 35000 | CIPCODE | 47.0699 | Vehicle Maintenance and Repair Technologies/Technicians, Other | 81 | 0.00 |
| 35000 | CIPCODE | 47.0701 | Energy Systems Installation and Repair Technology/Technician | 27 | 0.00 |
| 35000 | CIPCODE | 47.0703 | Solar Energy System Installation and Repair Technology/Technician | 32 | 0.00 |
| 35000 | CIPCODE | 47.0704 | Wind Energy System Installation and Repair Technology/Technician | 19 | 0.00 |
| 35000 | CIPCODE | 47.0799 | Energy Systems Maintenance and Repair Technologies/Technicians, Other | 4 | 0.00 |
| 35000 | CIPCODE | 47.9999 | Mechanic and Repair Technologies/Technicians, Other | 195 | 0.01 |
| 35000 | CIPCODE | 48.0000 | Precision Production Trades, General | 35 | 0.00 |
| 35000 | CIPCODE | 48.0303 | Upholstery/Upholsterer | 39 | 0.00 |
| 35000 | CIPCODE | 48.0501 | Machine Tool Technology/Machinist | 1486 | 0.09 |
| 35000 | CIPCODE | 48.0503 | Machine Shop Technology/Assistant | 653 | 0.04 |
| 35000 | CIPCODE | 48.0506 | Sheet Metal Technology/Sheetworking | 150 | 0.01 |
| 35000 | CIPCODE | 48.0507 | Tool and Die Technology/Technician | 238 | 0.01 |
| 35000 | CIPCODE | 48.0508 | Welding Technology/Welder | 4843 | 0.29 |
| 35000 | CIPCODE | 48.0509 | Ironworking/Ironworker | 40 | 0.00 |
| 35000 | CIPCODE | 48.0510 | Computer Numerically Controlled (CNC) Machinist Technology/CNC Machinist | 915 | 0.05 |
| 35000 | CIPCODE | 48.0511 | Metal Fabricator | 122 | 0.01 |
| 35000 | CIPCODE | 48.0599 | Precision Metal Working, Other | 114 | 0.01 |
| 35000 | CIPCODE | 48.0701 | Woodworking, General | 44 | 0.00 |
| 35000 | CIPCODE | 48.0702 | Furniture Design and Manufacturing | 40 | 0.00 |
| 35000 | CIPCODE | 48.0703 | Cabinetmaking and Millwork | 239 | 0.01 |
| 35000 | CIPCODE | 48.0704 | Wooden Boatbuilding Technology/Technician | 11 | 0.00 |
| 35000 | CIPCODE | 48.0799 | Woodworking, Other | 12 | 0.00 |
| 35000 | CIPCODE | 48.0801 | Boilermaking/Boilermaker | 17 | 0.00 |
| 35000 | CIPCODE | 48.9999 | Precision Production, Other | 64 | 0.00 |
| 35000 | CIPCODE | 49.0101 | Aeronautics/Aviation/Aerospace Science and Technology, General | 433 | 0.03 |
| 35000 | CIPCODE | 49.0102 | Airline/Commercial/Professional Pilot and Flight Crew | 559 | 0.03 |
| 35000 | CIPCODE | 49.0104 | Aviation/Airway Management and Operations | 392 | 0.02 |
| 35000 | CIPCODE | 49.0105 | Air Traffic Controller | 87 | 0.01 |
| 35000 | CIPCODE | 49.0106 | Airline Flight Attendant | 26 | 0.00 |
| 35000 | CIPCODE | 49.0108 | Flight Instructor | 35 | 0.00 |
| 35000 | CIPCODE | 49.0109 | Remote Aircraft Pilot | 109 | 0.01 |
| 35000 | CIPCODE | 49.0199 | Air Transportation, Other | 94 | 0.01 |
| 35000 | CIPCODE | 49.0202 | Construction/Heavy Equipment/Earthmoving Equipment Operation | 271 | 0.02 |
| 35000 | CIPCODE | 49.0205 | Truck and Bus Driver/Commercial Vehicle Operator and Instructor | 1047 | 0.06 |
| 35000 | CIPCODE | 49.0208 | Railroad and Railway Transportation | 19 | 0.00 |
| 35000 | CIPCODE | 49.0209 | Forklift Operation/Operator | 12 | 0.00 |
| 35000 | CIPCODE | 49.0299 | Ground Transportation, Other | 65 | 0.00 |
| 35000 | CIPCODE | 49.0304 | Diver, Professional and Instructor | 31 | 0.00 |
| 35000 | CIPCODE | 49.0309 | Marine Science/Merchant Marine Officer | 41 | 0.00 |
| 35000 | CIPCODE | 49.0399 | Marine Transportation, Other | 51 | 0.00 |
| 35000 | CIPCODE | 49.9999 | Transportation and Materials Moving, Other | 25 | 0.00 |
| 35000 | CIPCODE | 50.0101 | Visual and Performing Arts, General | 1282 | 0.08 |
| 35000 | CIPCODE | 50.0102 | Digital Arts | 898 | 0.05 |
| 35000 | CIPCODE | 50.0201 | Crafts/Craft Design, Folk Art and Artisanry | 95 | 0.01 |
| 35000 | CIPCODE | 50.0301 | Dance, General | 1466 | 0.09 |
| 35000 | CIPCODE | 50.0302 | Ballet | 22 | 0.00 |
| 35000 | CIPCODE | 50.0399 | Dance, Other | 119 | 0.01 |
| 35000 | CIPCODE | 50.0401 | Design and Visual Communications, General | 1302 | 0.08 |
| 35000 | CIPCODE | 50.0402 | Commercial and Advertising Art | 954 | 0.06 |
| 35000 | CIPCODE | 50.0404 | Industrial and Product Design | 285 | 0.02 |
| 35000 | CIPCODE | 50.0406 | Commercial Photography | 382 | 0.02 |
| 35000 | CIPCODE | 50.0407 | Fashion/Apparel Design | 599 | 0.04 |
| 35000 | CIPCODE | 50.0408 | Interior Design | 1112 | 0.07 |
| 35000 | CIPCODE | 50.0409 | Graphic Design | 2634 | 0.16 |
| 35000 | CIPCODE | 50.0410 | Illustration | 308 | 0.02 |
| 35000 | CIPCODE | 50.0411 | Game and Interactive Media Design | 806 | 0.05 |
| 35000 | CIPCODE | 50.0499 | Design and Applied Arts, Other | 370 | 0.02 |
| 35000 | CIPCODE | 50.0501 | Drama and Dramatics/Theatre Arts, General | 4044 | 0.24 |
| 35000 | CIPCODE | 50.0502 | Technical Theatre/Theatre Design and Technology | 873 | 0.05 |
| 35000 | CIPCODE | 50.0504 | Playwriting and Screenwriting | 267 | 0.02 |
| 35000 | CIPCODE | 50.0505 | Theatre Literature, History and Criticism | 63 | 0.00 |
| 35000 | CIPCODE | 50.0506 | Acting | 505 | 0.03 |
| 35000 | CIPCODE | 50.0507 | Directing and Theatrical Production | 220 | 0.01 |
| 35000 | CIPCODE | 50.0509 | Musical Theatre | 528 | 0.03 |
| 35000 | CIPCODE | 50.0510 | Costume Design | 76 | 0.00 |
| 35000 | CIPCODE | 50.0511 | Comedy Writing and Performance | 6 | 0.00 |
| 35000 | CIPCODE | 50.0512 | Theatre and Dance | 50 | 0.00 |
| 35000 | CIPCODE | 50.0599 | Dramatic/Theatre Arts and Stagecraft, Other | 227 | 0.01 |
| 35000 | CIPCODE | 50.0601 | Film/Cinema/Media Studies | 1159 | 0.07 |
| 35000 | CIPCODE | 50.0602 | Cinematography and Film/Video Production | 1433 | 0.08 |
| 35000 | CIPCODE | 50.0605 | Photography | 1000 | 0.06 |
| 35000 | CIPCODE | 50.0607 | Documentary Production | 101 | 0.01 |
| 35000 | CIPCODE | 50.0699 | Film/Video and Photographic Arts, Other | 204 | 0.01 |
| 35000 | CIPCODE | 50.0701 | Art/Art Studies, General | 3314 | 0.20 |
| 35000 | CIPCODE | 50.0702 | Fine/Studio Arts, General | 2944 | 0.17 |
| 35000 | CIPCODE | 50.0703 | Art History, Criticism and Conservation | 1947 | 0.12 |
| 35000 | CIPCODE | 50.0705 | Drawing | 191 | 0.01 |
| 35000 | CIPCODE | 50.0706 | Intermedia/Multimedia | 206 | 0.01 |
| 35000 | CIPCODE | 50.0708 | Painting | 257 | 0.02 |
| 35000 | CIPCODE | 50.0709 | Sculpture | 265 | 0.02 |
| 35000 | CIPCODE | 50.0710 | Printmaking | 170 | 0.01 |
| 35000 | CIPCODE | 50.0711 | Ceramic Arts and Ceramics | 270 | 0.02 |
| 35000 | CIPCODE | 50.0712 | Fiber, Textile and Weaving Arts | 73 | 0.00 |
| 35000 | CIPCODE | 50.0713 | Jewelry Arts | 136 | 0.01 |
| 35000 | CIPCODE | 50.0714 | Metal Arts | 16 | 0.00 |
| 35000 | CIPCODE | 50.0799 | Fine Arts and Art Studies, Other | 410 | 0.02 |
| 35000 | CIPCODE | 50.0901 | Music, General | 4661 | 0.28 |
| 35000 | CIPCODE | 50.0902 | Music History, Literature, and Theory | 267 | 0.02 |
| 35000 | CIPCODE | 50.0903 | Music Performance, General | 2111 | 0.13 |
| 35000 | CIPCODE | 50.0904 | Music Theory and Composition | 868 | 0.05 |
| 35000 | CIPCODE | 50.0905 | Musicology and Ethnomusicology | 201 | 0.01 |
| 35000 | CIPCODE | 50.0906 | Conducting | 258 | 0.02 |
| 35000 | CIPCODE | 50.0907 | Keyboard Instruments | 427 | 0.03 |
| 35000 | CIPCODE | 50.0908 | Voice and Opera | 463 | 0.03 |
| 35000 | CIPCODE | 50.0910 | Jazz/Jazz Studies | 332 | 0.02 |
| 35000 | CIPCODE | 50.0911 | Stringed Instruments | 195 | 0.01 |
| 35000 | CIPCODE | 50.0912 | Music Pedagogy | 283 | 0.02 |
| 35000 | CIPCODE | 50.0913 | Music Technology | 603 | 0.04 |
| 35000 | CIPCODE | 50.0914 | Brass Instruments | 111 | 0.01 |
| 35000 | CIPCODE | 50.0915 | Woodwind Instruments | 110 | 0.01 |
| 35000 | CIPCODE | 50.0916 | Percussion Instruments | 98 | 0.01 |
| 35000 | CIPCODE | 50.0917 | Sound Arts | 31 | 0.00 |
| 35000 | CIPCODE | 50.0999 | Music, Other | 521 | 0.03 |
| 35000 | CIPCODE | 50.1001 | Arts, Entertainment, and Media Management, General | 372 | 0.02 |
| 35000 | CIPCODE | 50.1002 | Fine and Studio Arts Management | 387 | 0.02 |
| 35000 | CIPCODE | 50.1003 | Music Management | 527 | 0.03 |
| 35000 | CIPCODE | 50.1004 | Theatre/Theatre Arts Management | 172 | 0.01 |
| 35000 | CIPCODE | 50.1099 | Arts, Entertainment, and Media Management, Other | 87 | 0.01 |
| 35000 | CIPCODE | 50.1101 | Community/Environmental/Socially-Engaged Art | 38 | 0.00 |
| 35000 | CIPCODE | 50.9999 | Visual and Performing Arts, Other | 354 | 0.02 |
| 35000 | CIPCODE | 51.0000 | Health Services/Allied Health/Health Sciences, General | 2722 | 0.16 |
| 35000 | CIPCODE | 51.0001 | Health and Wellness, General | 889 | 0.05 |
| 35000 | CIPCODE | 51.0101 | Chiropractic | 54 | 0.00 |
| 35000 | CIPCODE | 51.0201 | Communication Sciences and Disorders, General | 717 | 0.04 |
| 35000 | CIPCODE | 51.0202 | Audiology/Audiologist | 257 | 0.02 |
| 35000 | CIPCODE | 51.0203 | Speech-Language Pathology/Pathologist | 692 | 0.04 |
| 35000 | CIPCODE | 51.0204 | Audiology/Audiologist and Speech-Language Pathology/Pathologist | 687 | 0.04 |
| 35000 | CIPCODE | 51.0299 | Communication Disorders Sciences and Services, Other | 103 | 0.01 |
| 35000 | CIPCODE | 51.0401 | Dentistry | 211 | 0.01 |
| 35000 | CIPCODE | 51.0501 | Dental Clinical Sciences, General | 115 | 0.01 |
| 35000 | CIPCODE | 51.0502 | Advanced General Dentistry | 72 | 0.00 |
| 35000 | CIPCODE | 51.0503 | Oral Biology and Oral and Maxillofacial Pathology | 96 | 0.01 |
| 35000 | CIPCODE | 51.0504 | Dental Public Health and Education | 63 | 0.00 |
| 35000 | CIPCODE | 51.0505 | Dental Materials | 6 | 0.00 |
| 35000 | CIPCODE | 51.0506 | Endodontics/Endodontology | 117 | 0.01 |
| 35000 | CIPCODE | 51.0507 | Oral/Maxillofacial Surgery | 59 | 0.00 |
| 35000 | CIPCODE | 51.0508 | Orthodontics/Orthodontology | 157 | 0.01 |
| 35000 | CIPCODE | 51.0509 | Pediatric Dentistry/Pedodontics | 92 | 0.01 |
| 35000 | CIPCODE | 51.0510 | Periodontics/Periodontology | 111 | 0.01 |
| 35000 | CIPCODE | 51.0511 | Prosthodontics/Prosthodontology | 88 | 0.01 |
| 35000 | CIPCODE | 51.0512 | Digital Dentistry | 3 | 0.00 |
| 35000 | CIPCODE | 51.0514 | Implantology/Implant Dentistry | 7 | 0.00 |
| 35000 | CIPCODE | 51.0599 | Advanced/Graduate Dentistry and Oral Sciences, Other | 61 | 0.00 |
| 35000 | CIPCODE | 51.0601 | Dental Assisting/Assistant | 2235 | 0.13 |
| 35000 | CIPCODE | 51.0602 | Dental Hygiene/Hygienist | 1205 | 0.07 |
| 35000 | CIPCODE | 51.0603 | Dental Laboratory Technology/Technician | 143 | 0.01 |
| 35000 | CIPCODE | 51.0699 | Dental Services and Allied Professions, Other | 44 | 0.00 |
| 35000 | CIPCODE | 51.0701 | Health/Health Care Administration/Management | 3438 | 0.20 |
| 35000 | CIPCODE | 51.0702 | Hospital and Health Care Facilities Administration/Management | 373 | 0.02 |
| 35000 | CIPCODE | 51.0703 | Health Unit Coordinator/Ward Clerk | 70 | 0.00 |
| 35000 | CIPCODE | 51.0704 | Health Unit Manager/Ward Supervisor | 18 | 0.00 |
| 35000 | CIPCODE | 51.0705 | Medical Office Management/Administration | 727 | 0.04 |
| 35000 | CIPCODE | 51.0706 | Health Information/Medical Records Administration/Administrator | 657 | 0.04 |
| 35000 | CIPCODE | 51.0707 | Health Information/Medical Records Technology/Technician | 1786 | 0.11 |
| 35000 | CIPCODE | 51.0708 | Medical Transcription/Transcriptionist | 228 | 0.01 |
| 35000 | CIPCODE | 51.0709 | Medical Office Computer Specialist/Assistant | 45 | 0.00 |
| 35000 | CIPCODE | 51.0710 | Medical Office Assistant/Specialist | 991 | 0.06 |
| 35000 | CIPCODE | 51.0711 | Medical/Health Management and Clinical Assistant/Specialist | 116 | 0.01 |
| 35000 | CIPCODE | 51.0712 | Medical Reception/Receptionist | 202 | 0.01 |
| 35000 | CIPCODE | 51.0713 | Medical Insurance Coding Specialist/Coder | 1629 | 0.10 |
| 35000 | CIPCODE | 51.0714 | Medical Insurance Specialist/Medical Biller | 735 | 0.04 |
| 35000 | CIPCODE | 51.0715 | Health/Medical Claims Examiner | 3 | 0.00 |
| 35000 | CIPCODE | 51.0716 | Medical Administrative/Executive Assistant and Medical Secretary | 1406 | 0.08 |
| 35000 | CIPCODE | 51.0717 | Medical Staff Services Technology/Technician | 28 | 0.00 |
| 35000 | CIPCODE | 51.0718 | Long Term Care Administration/Management | 161 | 0.01 |
| 35000 | CIPCODE | 51.0719 | Clinical Research Coordinator | 120 | 0.01 |
| 35000 | CIPCODE | 51.0720 | Regulatory Science/Affairs | 34 | 0.00 |
| 35000 | CIPCODE | 51.0721 | Disease Registry Data Management | 16 | 0.00 |
| 35000 | CIPCODE | 51.0722 | Healthcare Innovation | 55 | 0.00 |
| 35000 | CIPCODE | 51.0723 | Healthcare Information Privacy Assurance and Security | 9 | 0.00 |
| 35000 | CIPCODE | 51.0799 | Health and Medical Administrative Services, Other | 461 | 0.03 |
| 35000 | CIPCODE | 51.0801 | Medical/Clinical Assistant | 4648 | 0.28 |
| 35000 | CIPCODE | 51.0802 | Clinical/Medical Laboratory Assistant | 179 | 0.01 |
| 35000 | CIPCODE | 51.0803 | Occupational Therapist Assistant | 756 | 0.04 |
| 35000 | CIPCODE | 51.0805 | Pharmacy Technician/Assistant | 1748 | 0.10 |
| 35000 | CIPCODE | 51.0806 | Physical Therapy Assistant | 1217 | 0.07 |
| 35000 | CIPCODE | 51.0809 | Anesthesiologist Assistant | 84 | 0.00 |
| 35000 | CIPCODE | 51.0810 | Emergency Care Attendant (EMT Ambulance) | 401 | 0.02 |
| 35000 | CIPCODE | 51.0811 | Pathology/Pathologist Assistant | 33 | 0.00 |
| 35000 | CIPCODE | 51.0812 | Respiratory Therapy Technician/Assistant | 97 | 0.01 |
| 35000 | CIPCODE | 51.0814 | Radiologist Assistant | 42 | 0.00 |
| 35000 | CIPCODE | 51.0815 | Lactation Consultant | 32 | 0.00 |
| 35000 | CIPCODE | 51.0816 | Speech-Language Pathology Assistant | 94 | 0.01 |
| 35000 | CIPCODE | 51.0899 | Allied Health and Medical Assisting Services, Other | 380 | 0.02 |
| 35000 | CIPCODE | 51.0901 | Cardiovascular Technology/Technologist | 406 | 0.02 |
| 35000 | CIPCODE | 51.0902 | Electrocardiograph Technology/Technician | 245 | 0.01 |
| 35000 | CIPCODE | 51.0903 | Electroneurodiagnostic/Electroencephalographic Technology/Technologist | 150 | 0.01 |
| 35000 | CIPCODE | 51.0904 | Emergency Medical Technology/Technician (EMT Paramedic) | 3930 | 0.23 |
| 35000 | CIPCODE | 51.0905 | Nuclear Medical Technology/Technologist | 318 | 0.02 |
| 35000 | CIPCODE | 51.0906 | Perfusion Technology/Perfusionist | 54 | 0.00 |
| 35000 | CIPCODE | 51.0907 | Medical Radiologic Technology/Science - Radiation Therapist | 961 | 0.06 |
| 35000 | CIPCODE | 51.0908 | Respiratory Care Therapy/Therapist | 1400 | 0.08 |
| 35000 | CIPCODE | 51.0909 | Surgical Technology/Technologist | 1868 | 0.11 |
| 35000 | CIPCODE | 51.0910 | Diagnostic Medical Sonography/Sonographer and Ultrasound Technician | 1313 | 0.08 |
| 35000 | CIPCODE | 51.0911 | Radiologic Technology/Science - Radiographer | 2061 | 0.12 |
| 35000 | CIPCODE | 51.0912 | Physician Assistant | 919 | 0.05 |
| 35000 | CIPCODE | 51.0913 | Athletic Training/Trainer | 1386 | 0.08 |
| 35000 | CIPCODE | 51.0914 | Gene/Genetic Therapy | 14 | 0.00 |
| 35000 | CIPCODE | 51.0915 | Cardiopulmonary Technology/Technologist | 28 | 0.00 |
| 35000 | CIPCODE | 51.0916 | Radiation Protection/Health Physics Technician | 34 | 0.00 |
| 35000 | CIPCODE | 51.0917 | Polysomnography | 110 | 0.01 |
| 35000 | CIPCODE | 51.0918 | Hearing Instrument Specialist | 8 | 0.00 |
| 35000 | CIPCODE | 51.0919 | Mammography Technology/Technician | 137 | 0.01 |
| 35000 | CIPCODE | 51.0920 | Magnetic Resonance Imaging (MRI) Technology/Technician | 322 | 0.02 |
| 35000 | CIPCODE | 51.0922 | Intraoperative Neuromonitoring Technology/Technician | 3 | 0.00 |
| 35000 | CIPCODE | 51.0923 | Orthopedic Technology/Technician | 15 | 0.00 |
| 35000 | CIPCODE | 51.0999 | Allied Health Diagnostic, Intervention, and Treatment Professions, Other | 388 | 0.02 |
| 35000 | CIPCODE | 51.1001 | Blood Bank Technology Specialist | 49 | 0.00 |
| 35000 | CIPCODE | 51.1002 | Cytotechnology/Cytotechnologist | 83 | 0.00 |
| 35000 | CIPCODE | 51.1003 | Hematology Technology/Technician | 7 | 0.00 |
| 35000 | CIPCODE | 51.1004 | Clinical/Medical Laboratory Technician | 1095 | 0.06 |
| 35000 | CIPCODE | 51.1005 | Clinical Laboratory Science/Medical Technology/Technologist | 1112 | 0.07 |
| 35000 | CIPCODE | 51.1006 | Ophthalmic Laboratory Technology/Technician | 11 | 0.00 |
| 35000 | CIPCODE | 51.1007 | Histologic Technology/Histotechnologist | 60 | 0.00 |
| 35000 | CIPCODE | 51.1008 | Histologic Technician | 85 | 0.01 |
| 35000 | CIPCODE | 51.1009 | Phlebotomy Technician/Phlebotomist | 1493 | 0.09 |
| 35000 | CIPCODE | 51.1010 | Cytogenetics/Genetics/Clinical Genetics Technology/Technologist | 10 | 0.00 |
| 35000 | CIPCODE | 51.1011 | Renal/Dialysis Technologist/Technician | 82 | 0.00 |
| 35000 | CIPCODE | 51.1012 | Sterile Processing Technology/Technician | 430 | 0.03 |
| 35000 | CIPCODE | 51.1099 | Clinical/Medical Laboratory Science and Allied Professions, Other | 195 | 0.01 |
| 35000 | CIPCODE | 51.1101 | Pre-Dentistry Studies | 129 | 0.01 |
| 35000 | CIPCODE | 51.1102 | Pre-Medicine/Pre-Medical Studies | 581 | 0.03 |
| 35000 | CIPCODE | 51.1103 | Pre-Pharmacy Studies | 222 | 0.01 |
| 35000 | CIPCODE | 51.1105 | Pre-Nursing Studies | 420 | 0.02 |
| 35000 | CIPCODE | 51.1106 | Pre-Chiropractic Studies | 15 | 0.00 |
| 35000 | CIPCODE | 51.1107 | Pre-Occupational Therapy Studies | 100 | 0.01 |
| 35000 | CIPCODE | 51.1108 | Pre-Optometry Studies | 27 | 0.00 |
| 35000 | CIPCODE | 51.1109 | Pre-Physical Therapy Studies | 158 | 0.01 |
| 35000 | CIPCODE | 51.1110 | Pre-Art Therapy | 21 | 0.00 |
| 35000 | CIPCODE | 51.1111 | Pre-Physician Assistant | 52 | 0.00 |
| 35000 | CIPCODE | 51.1199 | Health/Medical Preparatory Programs, Other | 618 | 0.04 |
| 35000 | CIPCODE | 51.1201 | Medicine | 471 | 0.03 |
| 35000 | CIPCODE | 51.1202 | Osteopathic Medicine/Osteopathy | 111 | 0.01 |
| 35000 | CIPCODE | 51.1203 | Podiatric Medicine/Podiatry | 27 | 0.00 |
| 35000 | CIPCODE | 51.1299 | Medicine, Other | 3 | 0.00 |
| 35000 | CIPCODE | 51.1401 | Medical Science/Scientist | 322 | 0.02 |
| 35000 | CIPCODE | 51.1402 | Clinical and Translational Science | 67 | 0.00 |
| 35000 | CIPCODE | 51.1404 | Temporomandibular Disorders and Orofacial Pain | 9 | 0.00 |
| 35000 | CIPCODE | 51.1499 | Medical Clinical Sciences/Graduate Medical Studies, Other | 12 | 0.00 |
| 35000 | CIPCODE | 51.1501 | Substance Abuse/Addiction Counseling | 1990 | 0.12 |
| 35000 | CIPCODE | 51.1502 | Psychiatric/Mental Health Services Technician | 393 | 0.02 |
| 35000 | CIPCODE | 51.1503 | Clinical/Medical Social Work | 206 | 0.01 |
| 35000 | CIPCODE | 51.1504 | Community Health Services/Liaison/Counseling | 601 | 0.04 |
| 35000 | CIPCODE | 51.1505 | Marriage and Family Therapy/Counseling | 578 | 0.03 |
| 35000 | CIPCODE | 51.1506 | Clinical Pastoral Counseling/Patient Counseling | 89 | 0.01 |
| 35000 | CIPCODE | 51.1507 | Psychoanalysis and Psychotherapy | 9 | 0.00 |
| 35000 | CIPCODE | 51.1508 | Mental Health Counseling/Counselor | 1156 | 0.07 |
| 35000 | CIPCODE | 51.1509 | Genetic Counseling/Counselor | 131 | 0.01 |
| 35000 | CIPCODE | 51.1511 | Medical Family Therapy/Therapist | 8 | 0.00 |
| 35000 | CIPCODE | 51.1512 | Hospice and Palliative Care | 7 | 0.00 |
| 35000 | CIPCODE | 51.1513 | Trauma Counseling | 56 | 0.00 |
| 35000 | CIPCODE | 51.1599 | Mental and Social Health Services and Allied Professions, Other | 678 | 0.04 |
| 35000 | CIPCODE | 51.1701 | Optometry | 77 | 0.00 |
| 35000 | CIPCODE | 51.1801 | Opticianry/Ophthalmic Dispensing Optician | 114 | 0.01 |
| 35000 | CIPCODE | 51.1802 | Optometric Technician/Assistant | 81 | 0.00 |
| 35000 | CIPCODE | 51.1803 | Ophthalmic Technician/Technologist | 119 | 0.01 |
| 35000 | CIPCODE | 51.1804 | Orthoptics/Orthoptist | 9 | 0.00 |
| 35000 | CIPCODE | 51.1899 | Ophthalmic and Optometric Support Services and Allied Professions, Other | 19 | 0.00 |
| 35000 | CIPCODE | 51.2001 | Pharmacy | 484 | 0.03 |
| 35000 | CIPCODE | 51.2002 | Pharmacy Administration and Pharmacy Policy and Regulatory Affairs | 75 | 0.00 |
| 35000 | CIPCODE | 51.2003 | Pharmaceutics and Drug Design | 163 | 0.01 |
| 35000 | CIPCODE | 51.2004 | Medicinal and Pharmaceutical Chemistry | 139 | 0.01 |
| 35000 | CIPCODE | 51.2005 | Natural Products Chemistry and Pharmacognosy | 31 | 0.00 |
| 35000 | CIPCODE | 51.2006 | Clinical and Industrial Drug Development | 51 | 0.00 |
| 35000 | CIPCODE | 51.2007 | Pharmacoeconomics/Pharmaceutical Economics | 68 | 0.00 |
| 35000 | CIPCODE | 51.2008 | Clinical, Hospital, and Managed Care Pharmacy | 24 | 0.00 |
| 35000 | CIPCODE | 51.2009 | Industrial and Physical Pharmacy and Cosmetic Sciences | 42 | 0.00 |
| 35000 | CIPCODE | 51.2010 | Pharmaceutical Sciences | 345 | 0.02 |
| 35000 | CIPCODE | 51.2011 | Pharmaceutical Marketing and Management | 31 | 0.00 |
| 35000 | CIPCODE | 51.2099 | Pharmacy, Pharmaceutical Sciences, and Administration, Other | 131 | 0.01 |
| 35000 | CIPCODE | 51.2201 | Public Health, General | 2281 | 0.14 |
| 35000 | CIPCODE | 51.2202 | Environmental Health | 415 | 0.02 |
| 35000 | CIPCODE | 51.2205 | Health/Medical  Physics | 186 | 0.01 |
| 35000 | CIPCODE | 51.2206 | Occupational Health and Industrial Hygiene | 144 | 0.01 |
| 35000 | CIPCODE | 51.2207 | Public Health Education and Promotion | 722 | 0.04 |
| 35000 | CIPCODE | 51.2208 | Community Health and Preventive Medicine | 620 | 0.04 |
| 35000 | CIPCODE | 51.2209 | Maternal and Child Health | 90 | 0.01 |
| 35000 | CIPCODE | 51.2210 | International Public Health/International Health | 371 | 0.02 |
| 35000 | CIPCODE | 51.2211 | Health Services Administration | 614 | 0.04 |
| 35000 | CIPCODE | 51.2212 | Behavioral Aspects of Health | 216 | 0.01 |
| 35000 | CIPCODE | 51.2213 | Patient Safety and Healthcare Quality | 43 | 0.00 |
| 35000 | CIPCODE | 51.2299 | Public Health, Other | 355 | 0.02 |
| 35000 | CIPCODE | 51.2300 | Rehabilitation and Therapeutic Professions, General | 26 | 0.00 |
| 35000 | CIPCODE | 51.2301 | Art Therapy/Therapist | 303 | 0.02 |
| 35000 | CIPCODE | 51.2302 | Dance Therapy/Therapist | 17 | 0.00 |
| 35000 | CIPCODE | 51.2305 | Music Therapy/Therapist | 310 | 0.02 |
| 35000 | CIPCODE | 51.2306 | Occupational Therapy/Therapist | 949 | 0.06 |
| 35000 | CIPCODE | 51.2307 | Orthotist/Prosthetist | 85 | 0.01 |
| 35000 | CIPCODE | 51.2308 | Physical Therapy/Therapist | 973 | 0.06 |
| 35000 | CIPCODE | 51.2309 | Therapeutic Recreation/Recreational Therapy | 260 | 0.02 |
| 35000 | CIPCODE | 51.2310 | Vocational Rehabilitation Counseling/Counselor | 281 | 0.02 |
| 35000 | CIPCODE | 51.2311 | Kinesiotherapy/Kinesiotherapist | 22 | 0.00 |
| 35000 | CIPCODE | 51.2312 | Assistive/Augmentative Technology and Rehabilitation Engineering | 42 | 0.00 |
| 35000 | CIPCODE | 51.2313 | Animal-Assisted Therapy | 66 | 0.00 |
| 35000 | CIPCODE | 51.2314 | Rehabilitation Science | 206 | 0.01 |
| 35000 | CIPCODE | 51.2315 | Drama Therapy/Therapist | 3 | 0.00 |
| 35000 | CIPCODE | 51.2316 | Horticulture Therapy/Therapist | 4 | 0.00 |
| 35000 | CIPCODE | 51.2317 | Play Therapy/Therapist | 26 | 0.00 |
| 35000 | CIPCODE | 51.2399 | Rehabilitation and Therapeutic Professions, Other | 267 | 0.02 |
| 35000 | CIPCODE | 51.2601 | Health Aide | 128 | 0.01 |
| 35000 | CIPCODE | 51.2602 | Home Health Aide/Home Attendant | 279 | 0.02 |
| 35000 | CIPCODE | 51.2603 | Medication Aide | 140 | 0.01 |
| 35000 | CIPCODE | 51.2604 | Rehabilitation Aide | 48 | 0.00 |
| 35000 | CIPCODE | 51.2605 | Physical Therapy Technician/Aide | 6 | 0.00 |
| 35000 | CIPCODE | 51.2699 | Health Aides/Attendants/Orderlies, Other | 22 | 0.00 |
| 35000 | CIPCODE | 51.2703 | Medical Illustration/Medical Illustrator | 34 | 0.00 |
| 35000 | CIPCODE | 51.2706 | Medical Informatics | 731 | 0.04 |
| 35000 | CIPCODE | 51.2799 | Medical Illustration and Informatics, Other | 13 | 0.00 |
| 35000 | CIPCODE | 51.3101 | Dietetics/Dietitian | 719 | 0.04 |
| 35000 | CIPCODE | 51.3102 | Clinical Nutrition/Nutritionist | 185 | 0.01 |
| 35000 | CIPCODE | 51.3103 | Dietetic Technician | 137 | 0.01 |
| 35000 | CIPCODE | 51.3104 | Dietitian Assistant | 56 | 0.00 |
| 35000 | CIPCODE | 51.3199 | Dietetics and Clinical Nutrition Services, Other | 122 | 0.01 |
| 35000 | CIPCODE | 51.3201 | Bioethics/Medical Ethics | 261 | 0.02 |
| 35000 | CIPCODE | 51.3202 | Health Professions Education | 82 | 0.00 |
| 35000 | CIPCODE | 51.3203 | Nursing Education | 988 | 0.06 |
| 35000 | CIPCODE | 51.3204 | Medical/Health Humanities | 135 | 0.01 |
| 35000 | CIPCODE | 51.3205 | History of Medicine | 3 | 0.00 |
| 35000 | CIPCODE | 51.3206 | Arts in Medicine/Health | 4 | 0.00 |
| 35000 | CIPCODE | 51.3299 | Health Professions Education, Ethics, and Humanities, Other | 14 | 0.00 |
| 35000 | CIPCODE | 51.3300 | Alternative and Complementary Medicine and Medical Systems, General | 41 | 0.00 |
| 35000 | CIPCODE | 51.3301 | Acupuncture and Oriental Medicine | 173 | 0.01 |
| 35000 | CIPCODE | 51.3302 | Traditional Chinese Medicine and Chinese Herbology | 53 | 0.00 |
| 35000 | CIPCODE | 51.3303 | Naturopathic Medicine/Naturopathy | 21 | 0.00 |
| 35000 | CIPCODE | 51.3305 | Ayurvedic Medicine/Ayurveda | 18 | 0.00 |
| 35000 | CIPCODE | 51.3306 | Holistic/Integrative Health | 125 | 0.01 |
| 35000 | CIPCODE | 51.3399 | Alternative and Complementary Medicine and Medical Systems, Other | 34 | 0.00 |
| 35000 | CIPCODE | 51.3401 | Direct Entry Midwifery | 18 | 0.00 |
| 35000 | CIPCODE | 51.3499 | Alternative and Complementary Medical Support Services, Other | 9 | 0.00 |
| 35000 | CIPCODE | 51.3501 | Massage Therapy/Therapeutic Massage | 1771 | 0.10 |
| 35000 | CIPCODE | 51.3502 | Asian Bodywork Therapy | 16 | 0.00 |
| 35000 | CIPCODE | 51.3503 | Somatic Bodywork | 11 | 0.00 |
| 35000 | CIPCODE | 51.3599 | Somatic Bodywork and Related Therapeutic Services, Other | 8 | 0.00 |
| 35000 | CIPCODE | 51.3601 | Movement Therapy and Movement Education | 29 | 0.00 |
| 35000 | CIPCODE | 51.3602 | Yoga Teacher Training/Yoga Therapy | 52 | 0.00 |
| 35000 | CIPCODE | 51.3603 | Hypnotherapy/Hypnotherapist | 17 | 0.00 |
| 35000 | CIPCODE | 51.3699 | Movement and Mind-Body Therapies and Education, Other | 13 | 0.00 |
| 35000 | CIPCODE | 51.3701 | Aromatherapy | 3 | 0.00 |
| 35000 | CIPCODE | 51.3702 | Herbalism/Herbalist | 23 | 0.00 |
| 35000 | CIPCODE | 51.3801 | Registered Nursing/Registered Nurse | 7569 | 0.45 |
| 35000 | CIPCODE | 51.3802 | Nursing Administration | 1030 | 0.06 |
| 35000 | CIPCODE | 51.3803 | Adult Health Nurse/Nursing | 468 | 0.03 |
| 35000 | CIPCODE | 51.3804 | Nurse Anesthetist | 320 | 0.02 |
| 35000 | CIPCODE | 51.3805 | Family Practice Nurse/Nursing | 1470 | 0.09 |
| 35000 | CIPCODE | 51.3806 | Maternal/Child Health and Neonatal Nurse/Nursing | 104 | 0.01 |
| 35000 | CIPCODE | 51.3807 | Nurse Midwife/Nursing Midwifery | 119 | 0.01 |
| 35000 | CIPCODE | 51.3808 | Nursing Science | 600 | 0.04 |
| 35000 | CIPCODE | 51.3809 | Pediatric Nurse/Nursing | 246 | 0.01 |
| 35000 | CIPCODE | 51.3810 | Psychiatric/Mental Health Nurse/Nursing | 778 | 0.05 |
| 35000 | CIPCODE | 51.3811 | Public Health/Community Nurse/Nursing | 126 | 0.01 |
| 35000 | CIPCODE | 51.3812 | Perioperative/Operating Room and Surgical Nurse/Nursing | 55 | 0.00 |
| 35000 | CIPCODE | 51.3813 | Clinical Nurse Specialist | 172 | 0.01 |
| 35000 | CIPCODE | 51.3814 | Critical Care Nursing | 232 | 0.01 |
| 35000 | CIPCODE | 51.3815 | Occupational and Environmental Health Nursing | 16 | 0.00 |
| 35000 | CIPCODE | 51.3816 | Emergency Room/Trauma Nursing | 58 | 0.00 |
| 35000 | CIPCODE | 51.3818 | Nursing Practice | 1242 | 0.07 |
| 35000 | CIPCODE | 51.3819 | Palliative Care Nursing | 35 | 0.00 |
| 35000 | CIPCODE | 51.3820 | Clinical Nurse Leader | 150 | 0.01 |
| 35000 | CIPCODE | 51.3821 | Geriatric Nurse/Nursing | 272 | 0.02 |
| 35000 | CIPCODE | 51.3822 | Women's Health Nurse/Nursing | 96 | 0.01 |
| 35000 | CIPCODE | 51.3824 | Forensic Nursing | 22 | 0.00 |
| 35000 | CIPCODE | 51.3899 | Registered Nursing, Nursing Administration, Nursing Research and Clinical Nursing, Other | 530 | 0.03 |
| 35000 | CIPCODE | 51.3901 | Licensed Practical/Vocational Nurse Training | 3496 | 0.21 |
| 35000 | CIPCODE | 51.3902 | Nursing Assistant/Aide and Patient Care Assistant/Aide | 2463 | 0.15 |
| 35000 | CIPCODE | 51.3999 | Practical Nursing, Vocational Nursing and Nursing Assistants, Other | 331 | 0.02 |
| 35000 | CIPCODE | 51.9999 | Health Professions and Related Clinical Sciences, Other | 1042 | 0.06 |
| 35000 | CIPCODE | 52.0101 | Business/Commerce, General | 4072 | 0.24 |
| 35000 | CIPCODE | 52.0201 | Business Administration and Management, General | 13005 | 0.77 |
| 35000 | CIPCODE | 52.0202 | Purchasing, Procurement/Acquisitions and Contracts Management | 257 | 0.02 |
| 35000 | CIPCODE | 52.0203 | Logistics, Materials, and Supply Chain Management | 2202 | 0.13 |
| 35000 | CIPCODE | 52.0204 | Office Management and Supervision | 1327 | 0.08 |
| 35000 | CIPCODE | 52.0205 | Operations Management and Supervision | 989 | 0.06 |
| 35000 | CIPCODE | 52.0206 | Non-Profit/Public/Organizational Management | 1048 | 0.06 |
| 35000 | CIPCODE | 52.0207 | Customer Service Management | 168 | 0.01 |
| 35000 | CIPCODE | 52.0208 | E-Commerce/Electronic Commerce | 273 | 0.02 |
| 35000 | CIPCODE | 52.0209 | Transportation/Mobility Management | 216 | 0.01 |
| 35000 | CIPCODE | 52.0210 | Research and Development Management | 122 | 0.01 |
| 35000 | CIPCODE | 52.0211 | Project Management | 954 | 0.06 |
| 35000 | CIPCODE | 52.0212 | Retail Management | 522 | 0.03 |
| 35000 | CIPCODE | 52.0213 | Organizational Leadership | 2581 | 0.15 |
| 35000 | CIPCODE | 52.0215 | Risk Management | 84 | 0.00 |
| 35000 | CIPCODE | 52.0216 | Science/Technology Management | 103 | 0.01 |
| 35000 | CIPCODE | 52.0299 | Business Administration, Management and Operations, Other | 1613 | 0.10 |
| 35000 | CIPCODE | 52.0301 | Accounting | 7015 | 0.42 |
| 35000 | CIPCODE | 52.0302 | Accounting Technology/Technician and Bookkeeping | 3669 | 0.22 |
| 35000 | CIPCODE | 52.0303 | Auditing | 103 | 0.01 |
| 35000 | CIPCODE | 52.0304 | Accounting and Finance | 722 | 0.04 |
| 35000 | CIPCODE | 52.0305 | Accounting and Business/Management | 467 | 0.03 |
| 35000 | CIPCODE | 52.0399 | Accounting and Related Services, Other | 267 | 0.02 |
| 35000 | CIPCODE | 52.0401 | Administrative Assistant and Secretarial Science, General | 3059 | 0.18 |
| 35000 | CIPCODE | 52.0402 | Executive Assistant/Executive Secretary | 494 | 0.03 |
| 35000 | CIPCODE | 52.0406 | Receptionist | 80 | 0.00 |
| 35000 | CIPCODE | 52.0407 | Business/Office Automation/Technology/Data Entry | 775 | 0.05 |
| 35000 | CIPCODE | 52.0408 | General Office Occupations and Clerical Services | 719 | 0.04 |
| 35000 | CIPCODE | 52.0409 | Parts, Warehousing, and Inventory Management Operations | 72 | 0.00 |
| 35000 | CIPCODE | 52.0410 | Traffic, Customs, and Transportation Clerk/Technician | 20 | 0.00 |
| 35000 | CIPCODE | 52.0411 | Customer Service Support/Call Center/Teleservice Operation | 242 | 0.01 |
| 35000 | CIPCODE | 52.0499 | Business Operations Support and Secretarial Services, Other | 181 | 0.01 |
| 35000 | CIPCODE | 52.0501 | Business/Corporate Communications, General | 287 | 0.02 |
| 35000 | CIPCODE | 52.0502 | Grantsmanship | 7 | 0.00 |
| 35000 | CIPCODE | 52.0599 | Business/Corporate Communications, Other | 10 | 0.00 |
| 35000 | CIPCODE | 52.0601 | Business/Managerial Economics | 1068 | 0.06 |
| 35000 | CIPCODE | 52.0701 | Entrepreneurship/Entrepreneurial Studies | 3048 | 0.18 |
| 35000 | CIPCODE | 52.0702 | Franchising and Franchise Operations | 15 | 0.00 |
| 35000 | CIPCODE | 52.0703 | Small Business Administration/Management | 1130 | 0.07 |
| 35000 | CIPCODE | 52.0704 | Social Entrepreneurship | 69 | 0.00 |
| 35000 | CIPCODE | 52.0799 | Entrepreneurial and Small Business Operations, Other | 254 | 0.02 |
| 35000 | CIPCODE | 52.0801 | Finance, General | 3993 | 0.24 |
| 35000 | CIPCODE | 52.0803 | Banking and Financial Support Services | 566 | 0.03 |
| 35000 | CIPCODE | 52.0804 | Financial Planning and Services | 485 | 0.03 |
| 35000 | CIPCODE | 52.0806 | International Finance | 36 | 0.00 |
| 35000 | CIPCODE | 52.0807 | Investments and Securities | 109 | 0.01 |
| 35000 | CIPCODE | 52.0808 | Public Finance | 22 | 0.00 |
| 35000 | CIPCODE | 52.0809 | Credit Management | 12 | 0.00 |
| 35000 | CIPCODE | 52.0810 | Financial Risk Management | 15 | 0.00 |
| 35000 | CIPCODE | 52.0899 | Finance and Financial Management Services, Other | 220 | 0.01 |
| 35000 | CIPCODE | 52.0901 | Hospitality Administration/Management, General | 2050 | 0.12 |
| 35000 | CIPCODE | 52.0903 | Tourism and Travel Services Management | 291 | 0.02 |
| 35000 | CIPCODE | 52.0904 | Hotel/Motel Administration/Management | 572 | 0.03 |
| 35000 | CIPCODE | 52.0905 | Restaurant/Food Services Management | 338 | 0.02 |
| 35000 | CIPCODE | 52.0906 | Resort Management | 76 | 0.00 |
| 35000 | CIPCODE | 52.0907 | Meeting and Event Planning | 301 | 0.02 |
| 35000 | CIPCODE | 52.0908 | Casino Management | 51 | 0.00 |
| 35000 | CIPCODE | 52.0909 | Hotel, Motel, and Restaurant Management | 258 | 0.02 |
| 35000 | CIPCODE | 52.0910 | Brewery/Brewpub Operations/Management | 17 | 0.00 |
| 35000 | CIPCODE | 52.0999 | Hospitality Administration/Management, Other | 187 | 0.01 |
| 35000 | CIPCODE | 52.1001 | Human Resources Management/Personnel Administration, General | 2768 | 0.16 |
| 35000 | CIPCODE | 52.1002 | Labor and Industrial Relations | 169 | 0.01 |
| 35000 | CIPCODE | 52.1003 | Organizational Behavior Studies | 591 | 0.04 |
| 35000 | CIPCODE | 52.1004 | Labor Studies | 84 | 0.00 |
| 35000 | CIPCODE | 52.1005 | Human Resources Development | 375 | 0.02 |
| 35000 | CIPCODE | 52.1006 | Executive/Career Coaching | 44 | 0.00 |
| 35000 | CIPCODE | 52.1099 | Human Resources Management and Services, Other | 205 | 0.01 |
| 35000 | CIPCODE | 52.1101 | International Business/Trade/Commerce | 2312 | 0.14 |
| 35000 | CIPCODE | 52.1201 | Management Information Systems, General | 1898 | 0.11 |
| 35000 | CIPCODE | 52.1206 | Information Resources Management | 227 | 0.01 |
| 35000 | CIPCODE | 52.1207 | Knowledge Management | 103 | 0.01 |
| 35000 | CIPCODE | 52.1299 | Management Information Systems and Services, Other | 239 | 0.01 |
| 35000 | CIPCODE | 52.1301 | Management Science | 1821 | 0.11 |
| 35000 | CIPCODE | 52.1302 | Business Statistics | 539 | 0.03 |
| 35000 | CIPCODE | 52.1304 | Actuarial Science | 609 | 0.04 |
| 35000 | CIPCODE | 52.1399 | Management Sciences and Quantitative Methods, Other | 936 | 0.06 |
| 35000 | CIPCODE | 52.1401 | Marketing/Marketing Management, General | 5177 | 0.31 |
| 35000 | CIPCODE | 52.1402 | Marketing Research | 167 | 0.01 |
| 35000 | CIPCODE | 52.1403 | International Marketing | 74 | 0.00 |
| 35000 | CIPCODE | 52.1404 | Digital Marketing | 484 | 0.03 |
| 35000 | CIPCODE | 52.1499 | Marketing, Other | 431 | 0.03 |
| 35000 | CIPCODE | 52.1501 | Real Estate | 1218 | 0.07 |
| 35000 | CIPCODE | 52.1601 | Taxation | 488 | 0.03 |
| 35000 | CIPCODE | 52.1701 | Insurance | 469 | 0.03 |
| 35000 | CIPCODE | 52.1801 | Sales, Distribution, and Marketing Operations, General | 857 | 0.05 |
| 35000 | CIPCODE | 52.1802 | Merchandising and Buying Operations | 15 | 0.00 |
| 35000 | CIPCODE | 52.1803 | Retailing and Retail Operations | 267 | 0.02 |
| 35000 | CIPCODE | 52.1804 | Selling Skills and Sales Operations | 489 | 0.03 |
| 35000 | CIPCODE | 52.1899 | General Merchandising, Sales, and Related Marketing Operations, Other | 97 | 0.01 |
| 35000 | CIPCODE | 52.1901 | Auctioneering | 4 | 0.00 |
| 35000 | CIPCODE | 52.1902 | Fashion Merchandising | 392 | 0.02 |
| 35000 | CIPCODE | 52.1904 | Apparel and Accessories Marketing Operations | 43 | 0.00 |
| 35000 | CIPCODE | 52.1905 | Tourism and Travel Services Marketing Operations | 133 | 0.01 |
| 35000 | CIPCODE | 52.1906 | Tourism Promotion Operations | 21 | 0.00 |
| 35000 | CIPCODE | 52.1907 | Vehicle and Vehicle Parts and Accessories Marketing Operations | 38 | 0.00 |
| 35000 | CIPCODE | 52.1908 | Business and Personal/Financial Services Marketing Operations | 40 | 0.00 |
| 35000 | CIPCODE | 52.1909 | Special Products Marketing Operations | 55 | 0.00 |
| 35000 | CIPCODE | 52.1910 | Hospitality and Recreation Marketing Operations | 47 | 0.00 |
| 35000 | CIPCODE | 52.1999 | Specialized Merchandising, Sales, and Marketing Operations, Other | 52 | 0.00 |
| 35000 | CIPCODE | 52.2001 | Construction Management, General | 698 | 0.04 |
| 35000 | CIPCODE | 52.2002 | Construction Project Management | 14 | 0.00 |
| 35000 | CIPCODE | 52.2101 | Telecommunications Management | 60 | 0.00 |
| 35000 | CIPCODE | 52.9999 | Business, Management, Marketing, and Related Support Services, Other | 789 | 0.05 |
| 35000 | CIPCODE | 54.0101 | History, General | 6673 | 0.40 |
| 35000 | CIPCODE | 54.0102 | American  History (United States) | 85 | 0.01 |
| 35000 | CIPCODE | 54.0103 | European History | 53 | 0.00 |
| 35000 | CIPCODE | 54.0104 | History and Philosophy of Science and Technology | 114 | 0.01 |
| 35000 | CIPCODE | 54.0105 | Public/Applied History | 298 | 0.02 |
| 35000 | CIPCODE | 54.0106 | Asian History | 11 | 0.00 |
| 35000 | CIPCODE | 54.0108 | Military History | 42 | 0.00 |
| 35000 | CIPCODE | 54.0199 | History, Other | 285 | 0.02 |
| 35005 | AWLEVEL | 15.0000 | Degrees/certificates total | 427834 | 25.34 |
| 35005 | AWLEVEL | 12.0000 | Degrees total | 363816 | 21.55 |
| 35005 | AWLEVEL | 3.0000 | Associate's degree | 107388 | 6.36 |
| 35005 | AWLEVEL | 5.0000 | Bachelor's degree | 226411 | 13.41 |
| 35005 | AWLEVEL | 7.0000 | Master's degree | 93582 | 5.54 |
| 35005 | AWLEVEL | 17.0000 | Doctor's degree - research/scholarship | 28788 | 1.70 |
| 35005 | AWLEVEL | 18.0000 | Doctor's degree - professional practice | 6339 | 0.38 |
| 35005 | AWLEVEL | 19.0000 | Doctor's degree - other | 742 | 0.04 |
| 35005 | AWLEVEL | 13.0000 | Certificates below the baccalaureate total | 117013 | 6.93 |
| 35005 | AWLEVEL | 1.0000 | Certificates of less than 1 year | 80143 | 4.75 |
| 35005 | AWLEVEL | 20.0000 | Certificates of less than 12 weeks | 10032 | 0.59 |
| 35005 | AWLEVEL | 21.0000 | Certificates of at least 12 weeks but less than 1 year | 76145 | 4.51 |
| 35005 | AWLEVEL | 2.0000 | Certificates of at least 1 but less than 2 years | 64504 | 3.82 |
| 35005 | AWLEVEL | 4.0000 | Certificates of at least 2 but less than 4 years | 5063 | 0.30 |
| 35005 | AWLEVEL | 14.0000 | Certificates above the baccalaureate total | 38566 | 2.28 |
| 35005 | AWLEVEL | 6.0000 | Postbaccalaureate certificate | 31640 | 1.87 |
| 35005 | AWLEVEL | 8.0000 | Post-master's certificate | 10465 | 0.62 |

## Statistics
| VarNumber | VarName | N | SUM | MEAN | MIN | MAX | varTitle |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 31565 | C2MORM | 1688471 | 1028984 | 0 | 0 | 561 | Two or more races men |
| 31605 | C2MORT | 1688471 | 2575836 | 1 | 0 | 1363 | Two or more races total |
| 31570 | C2MORW | 1688471 | 1546852 | 0 | 0 | 876 | Two or more races women |
| 31515 | CAIANM | 1688471 | 159364 | 0 | 0 | 306 | American Indian or Alaska Native men |
| 31580 | CAIANT | 1688471 | 425056 | 0 | 0 | 679 | American Indian or Alaska Native total |
| 31520 | CAIANW | 1688471 | 265692 | 0 | 0 | 403 | American Indian or Alaska Native women |
| 31525 | CASIAM | 1688471 | 2017668 | 1 | 0 | 2073 | Asian men |
| 31585 | CASIAT | 1688471 | 4695188 | 2 | 0 | 4317 | Asian total |
| 31530 | CASIAW | 1688471 | 2677520 | 1 | 0 | 2256 | Asian women |
| 31535 | CBKAAM | 1688471 | 2639000 | 1 | 0 | 2176 | Black or African American men |
| 31590 | CBKAAT | 1688471 | 7770472 | 4 | 0 | 6488 | Black or African American total |
| 31540 | CBKAAW | 1688471 | 5131472 | 3 | 0 | 6331 | Black or African American women |
| 31505 | CHISPM | 1688471 | 5339980 | 3 | 0 | 6568 | Hispanic or Latino men |
| 31575 | CHISPT | 1688471 | 13750620 | 8 | 0 | 14458 | Hispanic or Latino total |
| 31510 | CHISPW | 1688471 | 8410640 | 4 | 0 | 7979 | Hispanic or Latino women |
| 31545 | CNHPIM | 1688471 | 64616 | 0 | 0 | 162 | Native Hawaiian or Other Pacific Islander men |
| 31595 | CNHPIT | 1688471 | 162832 | 0 | 0 | 396 | Native Hawaiian or Other Pacific Islander total |
| 31550 | CNHPIW | 1688471 | 98216 | 0 | 0 | 234 | Native Hawaiian or Other Pacific Islander women |
| 31015 | CNRALM | 1688471 | 2289252 | 1 | 0 | 3614 | U.S. Nonresident men |
| 31095 | CNRALT | 1688471 | 4242480 | 2 | 0 | 7712 | U.S. Nonresident total |
| 31020 | CNRALW | 1688471 | 1953228 | 1 | 0 | 4098 | U.S. Nonresident women |
| 31085 | CTOTALM | 1688471 | 28528152 | 16 | 0 | 17735 | Grand total men |
| 31130 | CTOTALT | 1688471 | 69441520 | 41 | 0 | 50234 | Grand total |
| 31090 | CTOTALW | 1688471 | 40913368 | 24 | 0 | 32499 | Grand total women |
| 31075 | CUNKNM | 1688471 | 1182852 | 0 | 0 | 2772 | Race/ethnicity unknown men |
| 31125 | CUNKNT | 1688471 | 2717420 | 1 | 0 | 7541 | Race/ethnicity unknown total |
| 31080 | CUNKNW | 1688471 | 1534568 | 0 | 0 | 4769 | Race/ethnicity unknown women |
| 31555 | CWHITM | 1688471 | 13806436 | 8 | 0 | 10592 | White men |
| 31600 | CWHITT | 1688471 | 33101616 | 19 | 0 | 32628 | White total |
| 31560 | CWHITW | 1688471 | 19295180 | 11 | 0 | 22036 | White women |

## Imputation values
| CodeValue | ValueLabel |
| --- | --- |
| A | Not applicable |
| B | Institution left item blank |
| C | Analyst corrected reported value |
| D | Do not know |
| G | Data generated from other data values |
| H | Value not derived - data not usable |
| J | Logical imputation |
| K | Ratio adjustment |
| L | Imputed using the Group Median procedure |
| N | Imputed using Nearest Neighbor procedure |
| P | Imputed using Carry Forward procedure |
| R | Reported |
| Z | Implied zero |
