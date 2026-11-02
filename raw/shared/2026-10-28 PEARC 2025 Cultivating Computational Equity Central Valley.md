---
url: https://dl.acm.org/doi/10.1145/3708035.3736054
fetched: 2026-10-28
publisher: "ACM, PEARC '25"
published: 2025-07-20
original: 2026-10-28 PEARC 2025 Cultivating Computational Equity Central Valley.pdf
rehost: yes
license: CC BY-ND 4.0
---

_Markdown copy of 2026-10-28 PEARC 2025 Cultivating Computational Equity Central Valley.pdf, made 2026-10-28 with pdftotext. The original is the authority._

Cultivating Computational Equity: Building a Collaborative
Research Computing Community in California’s Central Valley
Sarvani Chadalapaka

Director of Cyberinfrastructure and
Research Technologies, UC Merced
Merced, CA, USA
sarvani@ucmerced.edu

Jeffrey Weekley

Director, Research IT, UC Santa Cruz
Santa Cruz, CA, USA
jweekley@ucsc.edu

Anna Klimaszewski-Patterson

Ruth Marinshaw

Associate Professor of Geography,
Director of Geospatial Lab @ Sac
State, and Co-PI of CSUS
Paleoecology Lab
Sacramento, USA
anna.kp@csus.edu

Abstract
Institutions in California’s Central Valley face persistent barriers
to research computing, including limited local expertise, low utilization of national resources, and a lack of coordinated training.
CENVAL-ARC, a regional collaboration among UC Merced and
nearby CSU campuses, was established to address these challenges
by lowering technical barriers and fostering shared infrastructure and community. This paper presents an overview of early
activities—needs assessment, skills training, and a regional symposium—and highlights lessons from building cross-institutional
coordination. The approach offers a replicable model for other
regions aiming to strengthen research computing support at underresourced institutions through collaborative, place-based strategies.

CCS Concepts
• General and reference → Surveys and overviews; General
literature; • Human-centered computing → Accessibility theory,
concepts and paradigms.

Keywords
High Performance Computing (HPC), Computational access, Underserved regions, Hispanic-Serving Institutions (HSIs), Cross-institutional
collaboration, Equity in computing, Inclusive research ecosystems,
Community building, Regional partnerships, Sustainable infrastructure, CENVAL-ARC, Central Valley

Emily Jane McTavish

Associate Professor, Life and
Environmental Sciences, University of
California Merced
Merced, USA
ejmctavish@ucmerced.edu

Executive Director, Research
Computing Technologies, Yale
University
New Haven, CT, USA
ruth.marinshaw@yale.edu
Central Valley. In Practice and Experience in Advanced Research Computing
(PEARC ’25), July 20–24, 2025, Columbus, OH, USA. ACM, New York, NY,
USA, Article xx, 4 pages. https://doi.org/10.1145/3708035.3736054

1

Introduction

The evolution of Research Computing and Data (RCD) has transformed scientific inquiry, enabling researchers to address complex
questions at unprecedented scales[5]. Despite these advancements,
equitable access to computational resources remains concentrated
within well-resourced institutions. As highlighted by National Science Foundation (NSF)’s Missing Millions report[1]: democratizing
computing access to bridge the digital divide, the Central Valley
Accessible Research and Computational Hub (CENVAL-ARC) is
driven by the recognition that researchers and students without
extensive computing skills are often excluded from utilizing largescale computing investments. Even as cloud technologies transform
the academic enterprise landscape, barriers to cloud adoption are
both technical and financial, especially for non-R1s and smaller
institutions[3]. One participant said, "I wanted to scale beyond my
local campus resources to cloud resources like Amazon, but who’s
paying for Amazon? No one." This paper describes CENVAL-ARC’s
approach to building regional partnerships by identifying common
computational challenges and opportunities.

2

Assessing Computational Resource Gaps in
the Central Valley

ACM Reference Format:
Sarvani Chadalapaka, Jeffrey Weekley, Emily Jane McTavish, Anna Klimaszewski- A foundational step in establishing CENVAL-ARC was identifying
shared challenges among Central Valley institutions: University
Patterson, and Ruth Marinshaw. 2025. Cultivating Computational Equity:
of California Merced (UCM) and California State University (CSU)
Building a Collaborative Research Computing Community in California’s

This work is licensed under a Creative Commons Attribution-NoDerivatives 4.0 International License.
PEARC ’25, Columbus, OH, USA
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1398-9/25/07
https://doi.org/10.1145/3708035.3736054

campuses in Fresno, Sacramento, and Stanislaus. In 2024, we observed scant resource use of NSF’s Advanced Cyberinfrastructure
Coordination Ecosystem: Services and Support (ACCESS) at these
institutions, with a snapshot of allocations as a percentage of total
ACCESS CPU allocations as follows 1:
• CSU Fresno: A 0.04% allocation, 3 PI projects, and 6 users
• CSU Sacramento: A 0.03% allocation, 2 projects, and 4 users

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

Chadalapaka et al.

• UCM: A 0.02% allocation, with 13 faculty members accessing
resources
• CSU Stanislaus: No allocation, no project, and no users

Serving, underrepresented minority (URM) institutions, including first-generation college students and students eligible for Pell Grants[7], positions them uniquely for collaborative initiatives to address diverse educational and research
needs. Notably, UCM is the only doctorate-granting institution in California’s Central Valley.
Table 1: Demographic Overview of CENVAL-ARC Partner
Institutions (Fall 2022)

Figure 1: ACCESS CPU utilization percentage (%) by PI institution in 2024

Institution
UC Merced
CSU Sacramento
CSU Stanislaus
CSU Fresno

% Hispanic
55%
36%
61.4%
58%

% First-Gen
66%
31%
71.5%
N/A

% Pell Eligible
58%
43%
58.2%
62%

Challenges

The common challenges across institutions quickly emerged in
detail:
• Limited Local Expertise: Many campuses reported insufficient specialized support personnel, such as research computing facilitators and HPC system administrators. This shortage often resulted in underutilization of available computing
resources and hindered the scaling of research projects.
• Insufficient Computational Training: Insufficient Computational Training: Students and faculty across institutions
faced similar gaps in training opportunities and resources,
limiting their ability to fully leverage advanced computational tools and techniques, such as user interaction via the
command line interface, parallel computing, machine learning, and data-intensive methodologies.
• Access Barriers to National Resources: As highlighted
in the white paper "The Role of Regional Organizations in Improving Access to the National Computational Infrastructure"[6],
national HPC centers often excel at community engagement
but face limitations in reaching every campus, conference, or
workshop. In contrast, regional organizations benefit from
geographical proximity, local trust, and easier access to colleges and universities, and local user communities.

2.2

% Under Represented Minorities
60%
44%
64%
76%

• Geographic Proximity: The geographic proximity of these
institutions in California’s Central Valley facilitates collaboration and STEM research advancement. This more easily
facilitates in-person workshops, joint training sessions, and
sharing of local computational expertise. All locations are
within a two-hour drive of UC Merced (Fig. 2).

Despite being eligible and potentially in need of High Performance Computing resources, researchers at these four institutions
are significantly underutilizing national supercomputing resources.
This gap highlights the importance of intermediate clusters that
offer both computational resources and researcher support. Since
small- and mid-scale HPC clusters share many features with largescale HPC (e.g. schedulers, software, job types) such as those underpinning ACCESS, building skills locally is a key step in allowing
researchers to access resources at multiple scales. CENVAL-ARC,
designed with accessibility and training in mind, aims to help address this gap.

2.1

Total UnderGrad
8,300+
28,400
8,000
21,000+

Opportunities

Simultaneously, multiple opportunities emerged that made regional
collaboration attractive and feasible:
• Connected communities: The demographic similarity of
student populations across these predominantly Hispanic

Figure 2: Geographic proximity of CENVAL-ARC partner
institutions in California’s Central Valley

3

Laying the Groundwork: Skills Development
and Regional Coordination

To address the challenges outlined above, an early CENVAL-ARC
activity included hosting an online Introduction to Unix training
session in February 2025, attended by over 30 participants from
multiple campuses. The session was designed to help faculty and
students begin working with command-line environments—an essential entry point to using HPC systems[8].
In conversations with stakeholders from participating institutions, the divide between computation for research and computation
for instruction was highlighted. One symposium participant noted,
"democratization of access is a core role of education in computing.
In order to do research you need access to these clusters, trainings and resources. Through this conference, I have learned a lot
about accessible resources." Integrating computational approaches
into the classroom builds a pathway for students to engage in
computationally-focused research, both as undergraduates and as
graduate students.

Cultivating Computational Equity: Building a Collaborative Research Computing Community in California’s Central Valley

4

CENVAL-ARC Symposium: Laying the
Groundwork for Regional Cooperation and
Training

The CENVAL-ARC Symposium at UC Merced was a multi-day,
multi-mode event featuring sessions on HPC and high-throughput
computing (HTC), approaches to research computing and dataintensive workflows, as well as computational research and training.
The event brought together faculty, graduate and undergraduate
student researchers who require computational power beyond their
laptops or local resources[2].

4.1

• Understand the regional and national landscape of RCD.
• Be familiar with the Campus Research Computing Consortium (CaRCC) capabilities model in order to assist Central
Valley institutions in evaluating and enhancing their RCD
support systems and capabilities[4].
• Develop basic HPC skills, including:
– Build foundational skills in command-line, environments
– Edit and implement sample Bash scripts,
– Log into and utilize Open Science Grid (OSG) systems.
Virtual sessions further reinforced practical skills and offered
additional hands-on opportunities and deeper engagement with
computational practices and tools:
• Office hours for OSG and CaRCC Cyberinfrastructure planning allowed direct, personalized support for attendees addressed specific questions arising from the hands-on workshops.
• Pre-symposium training for "Introduction to Unix" familiarized participants with the Unix command, and was attended
by over 30 participants from multiple campus.
• UC Merced computational faculty led discipline-specific sessions that helped participants apply their new skills to their
own research areas.
• The session on best practices in writing research software
complements practical computational skills by emphasizing
reproducibility, maintainability, and broader research impact.

Outreach and Engagement Strategy

With no prior regional event of this kind, building attendance for
the inaugural symposium required a grassroots strategy. Organizers used personalized email campaigns and reciprocal outreach
through institutional leaders and faculty contacts to grow awareness. Established personal and professional networks were also key,
especially for the organizers.

4.3

Figure 3: Institutions and Institutional Roles of CENVALARC Symposium Participants

Learning Objectives

The program’s learning objectives for attendees were to:

4.2

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

Interdisciplinary Expertise and Research
Themes at the Symposium

The focus areas represented at the symposium spanned a wide
range of disciplines, with significant emphasis on computational
science, AI/ML (artificial intelligence/machine learning), HPC, and
data science. There was a strong interdisciplinary theme.

4.4

Participant Feedback

Participant feedback highlighted the symposium’s impact in raising awareness of computational resources and fostering regional
collaboration. Attendees reported new insights, stronger connections, and a clear interest in continued engagement—early signs of
momentum toward addressing shared computational challenges.
As one panelist noted, "democratization of access is a core role of
education in computing. In order to do research you need access to
these clusters, trainings and resources. Through this conference, I
have learned a lot about accessible resources."
An attendee shared via email, "Thank you very much one more
time for holding such a unique conference on your campus. If there
is one next year, I will surely attend." Another attendee succinctly
commented, "It was a good symposium. Thank you!" These responses signal growing collaboration and confirm the symposium’s
role in addressing regional computational needs.

5

Reflections and Future Work

To build upon the early momentum generated by the CENVALARC initiative, ongoing efforts will prioritize sustained community
engagement, inclusive access, and continuous improvement. Key
strategies include:
• Regular Community Engagement: CENVAL-ARC will
maintain quarterly meetings to foster ongoing collaboration, knowledge exchange, and continuous feedback to help
sustain the dialogue initiated at the symposium, providing
participants with consistent opportunities to connect, learn,
and share resources.
• Expanding Computational Training : Future training programs will be responsive to the evolving needs of researchers,
emphasizing hands-on experience in cloud computing, data
management, and software development practices.
• Enhanced Inclusivity and Accessibility: To ensure that
CENVAL-ARC’s resources are equitably accessible, the initiative will actively engage underrepresented researchers and
students through targeted outreach and tailored programming.
• Capturing Richer Demographic Data Figure 3 shows participating institutions and roles. To evaluate online versus inperson training, we need richer participant data—including
demographics across formats, learner assessments, learning
perception, and higher-order thinking measures.

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

6

Conclusion

Moving forward, CENVAL-ARC will strengthen collaborations and
address evolving computational needs through responsive programming. Gathering of data more systematically will allow CENVALARC investigators to better serve CENVAL-ARC community, while
increasing the value of annual reports and academic papers, such as
this. Stakeholder engagement will inform future directions, ensuring that initiatives remain relevant and beneficial to the evolving
landscape of computational research.

Acknowledgments
This material is based upon work supported by the National Science
Foundation under NSF OAC Award 2346744. Open AI’s Consensus
was used in the authoring of this paper as a research tool. Headings
and subheadings were generated using OpenAI’s ChatGPT-4 in
some cases.

References
[1] Alan Blatecky, Damian Clarke, Joel E. Cutcher-Gershenfeld, Deborah Dent,
Rebecca Hipp, Ana Hunsinger, Al Kuslikis, and Lauren Michael. 2021. The
Missing Millions: Democratizing Computation and Data to Bridge Digital

Chadalapaka et al.

Divides and Increase Access to Science for Underrepresented Communities. Report published by the National Science Foundation.
Available
at https://www.rti.org/publication/missing-millions-democratizing-computationdata-bridge-digital-divides-increase-access-science-under.
[2] CENVAL-ARC Consortium. 2025. CENVAL-ARC Symposium at UC Merced. https:
//cenval-arc.ucmerced.edu/Symposium. Accessed: 2025-03-24.
[3] Derek Foster, Laurie White, Joshua Adams, D Cenk Erdil, Harvey Hyman, Stan
Kurkovsky, Majd Sakr, and Lee Stott. 2018. Cloud computing: developing contemporary computer science curriculum for a cloud-first future. In Proceedings
Companion of the 23rd Annual ACM Conference on Innovation and Technology in
Computer Science Education. 130–147.
[4] John Hicks, Dana Brunson, Sarvani Chadalapaka, Forough Ghahramani, Lauren
Michael, and Caroline Carver Weilhamer. 2024. Kickstarting Research Support at
Under-Resourced Institutions: A Starter Guide to Advance Your Self-Assessment of
Research Computing and Data Capabilities. In Practice and Experience in Advanced
Research Computing 2024: Human Powered Computing. ACM, 1–4.
[5] Tom Hope, Doug Downey, Daniel S Weld, Oren Etzioni, and Eric Horvitz. 2023.
A computational inflection for scientific discovery. Commun. ACM 66, 8 (2023),
62–73.
[6] Gregory Monaco and Rick Mcmullen. 2016. Improving Access to the National
Computational Infrastructure The Role of Regional Organizations. ECAR Research
Bulletin (10 2016).
[7] Santa Monica College Transfer Center. 2022. 2021–2022 Total Transfers to UC and
CSU. https://www.smc.edu/student-support/academic-support/transfer-center/
statistics/documents/2021-22/2021-2022-total-transfers-to-uc-and-csu.pdf. Accessed March 24, 2025.
[8] Jeffrey Weekley and Sri Kurniawan. 2023. Towards a Human-centered Tutorial
Design for the Nautilus Cluster. In Practice and Experience in Advanced Research
Computing 2023: Computing for the Common Good. ACM, 386–389.

