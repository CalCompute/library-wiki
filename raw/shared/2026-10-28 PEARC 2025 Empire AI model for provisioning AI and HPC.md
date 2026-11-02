---
url: https://dl.acm.org/doi/10.1145/3708035.3736070
fetched: 2026-10-28
publisher: "ACM, PEARC '25"
published: 2025-07-20
original: 2026-10-28 PEARC 2025 Empire AI model for provisioning AI and HPC.pdf
rehost: yes
license: CC BY 4.0
---

_Markdown copy of 2026-10-28 PEARC 2025 Empire AI model for provisioning AI and HPC.pdf, made 2026-10-28 with pdftotext. The original is the authority._

Empire AI: A new model for provisioning AI and HPC for
academic research in the public good
Stacie Bloom∗

New York University
New York, NY, USA
blooms03@nyu.edu

Robert Harrison

Empire AI
New York, NY, USA
rharrison@empireai.edu

Joshua Brumberg

Ian Fisk

City University of New York Graduate
Center
New York, NY, USA
jbrumberg@gc.cuny.edu

Flatiron Institute
New York, NY, USA
ifisk@flatironinstitute.org

Robert Hull

Melur Ramasubramanian

Rensselaer Polytechnic Institute
Troy, NY, USA
hullr2@rpi.edu

Krystyn Van Vliet

Cornell University
Ithaca, NY, USA
krystyn.vv@cornell.edu

State University of New York
Albany, NY, USA
rammk@suny.edu

Jeannette Wing

Columbia University
New York, NY, USA
wing@columbia.edu

Figure 1: The Empire AI Alpha system, October 2024.

Abstract
Launched in April 2024 by New York State Governor Kathy Hochul,
Empire AI is a consortium of New York’s leading public and private
universities collaborating to establish a state-of-the-art artificial
intelligence computing center, to be housed at SUNY’s University
at Buffalo. We describe this new national model in ethical AI innovation and how it is pioneering safe, equitable, and accessible AI

research and development that is benefiting every corner of New
York. Our technology and facility roadmap is presented along with
preliminary estimates of economic impacts. In summer 2025, Empire AI will be the first academic deployment of an NVIDIA DGX
GB200 NVL72 SuperPOD that will have 288 B200 GPUs delivering
exascale performance in 16-bit tensor operations and able to train
multi-trillion parameter models.

∗ All authors contributed equally to this research.

This work is licensed under a Creative Commons Attribution 4.0 International License.
PEARC ’25, Columbus, OH, USA
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1398-9/25/07
https://doi.org/10.1145/3708035.3736070

CCS Concepts
• Computer systems organization; • Social and professional
topics; • Applied computing;

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

Keywords
artificial intelligence, high-performance computing, supercomputing
ACM Reference Format:
Stacie Bloom, Joshua Brumberg, Ian Fisk, Robert Harrison, Robert Hull,
Melur Ramasubramanian, Krystyn Van Vliet, and Jeannette Wing. 2025. Empire AI: A new model for provisioning AI and HPC for academic research in
the public good. In Practice and Experience in Advanced Research Computing
(PEARC ’25), July 20–24, 2025, Columbus, OH, USA. ACM, New York, NY,
USA, 4 pages. https://doi.org/10.1145/3708035.3736070

1

Introduction

Empire AI Consortium, Inc., is a not-for-profit company incorporated in New York State in July 2024 "to create and launch a
state-of-the-art artificial intelligence computing center in Upstate
New York to be used by New York’s leading institutions to promote
responsible research and development, create jobs, and unlock AI opportunities focused on public good [9]." Specifically, Empire AI seeks
to address the dominance by large technology companies of the AI
ecosystem due, in part, to the massive scale of computer resources
available to them. This is in sharp contrast to the past when, for
decades, it was academia at the forefront of computation due to
supercomputers operated by nations for open scientific research.
As a result, academic research in both the foundations and applications of AI is lagging, with implications for AI safety and society
at large. By addressing this disparity, we enable trusted, in-state
academic institutions to direct AI capabilities towards public benefit
rather than relying upon the good intentions of external commercial entities. We also position our institutions to be nationally and
internationally competitive whether recruiting faculty and students
or capturing research funding. In turn, "this pioneering AI research
and development will also help educational institutions incubate the
AI-focused technology startups of the future, driving job growth [9]."
The Consortium presently includes City University of New York
(CUNY), Columbia University, Cornell University, New York University (NYU), Rensselaer Polytechnic Institute (RPI), and State
University of New York (SUNY), with the Simons Foundation as a
close partner. In April 2024, the state committed $250M in capital
funds that is complemented by $150M of contributions through
these academic institutions for operations over the first decade.
Pending approval in the State budget is an additional $90M to
bring in 3 new members and provide an additional allocation to
SUNY. Thus, we anticipate the final budget being well over $0.5B
Initially scoped as a 10-year project, the consortium already has a
much longer-term vision. Empire AI’s board of directors includes a
member from each institution, and 3 independent and 2 advisory
members. The chair is Tom Secunda [2], whose vision and philanthropy have been essential to the establishment of Empire AI. The
initial capital investments will be the purchase of an interim computer, and construction of a new data center. These and future plans
are described in more detail below, including our initial computer
resource (Alpha) and its upcoming major upgrade (Beta).

2

Alpha system

Alpha is on loan to Empire AI as a philanthropic gift from the
Simons’ Foundation [8] and is generously operated by staff of

Bloom et al.

their Flatiron Institute [7]. It is housed at the University of Buffalo
(UB) Center for Computational Research (UB-CCR). The air-cooled
Lenovo HGX system comprises: (1) 13 HGX nodes each with 8 H100
80GB GPUs, 2 TB memory, and 30TB NVMe; (2) Dual 400Gb/s nonblocking NDR Infiband networks; (3) 2 login nodes; (4) 2 cluster
management nodes for NVIDIA Base Command; (5) 2 data transfer
nodes; (6) 2.8PB of DDN flash storage for training data, snap shots;
and (7) 2PB effective of VAST flash storage for home directories.

3

Current research activities using Alpha

Over 300 proposals were submitted to use Alpha but, due to the
limited resource, only 90 projects were started. Starting April 2025,
a new cohort of projects is to be onboarded. The following categorization of active projects is edited from content generated by
Gemini Advanced 2.0 Flash from the project descriptions (the only
use of generative AI in this paper):
Foundation Models and Generative AI: Developing and
improving large-scale AI models that can generate various
types of data (text, images, code, etc.) and serve as a base for
more specialized applications.
AI for Scientific Discovery and Simulation: Leveraging
AI and machine learning to accelerate scientific research
across various disciplines, including developing surrogate
models for complex physical simulations.
AI in Healthcare and Biomedical Research: Applying AI
to improve healthcare, diagnostics, and our understanding
of biological systems, including models for medical image
analysis, biomolecular structure prediction and drug design,
or creating personalized AI for assistive communication and
mental health.
Natural Language Processing and Understanding:
Advancing the capabilities of AI to process, understand, and
generate human language including analysis of hate speech,
and exploring the ethical implications of LLMs.
Robotics and Embodied AI: Developing intelligent agents
that can interact with the physical world including creating
robots with improved perception and AI-powered interactive
speech therapy agents.
Machine Learning Methodology and Applications:
Research on fundamental machine learning techniques and
their application to diverse problems not categorized above.
We highlight one project from each institution:
Columbia University: Prof. Tian Zheng is building models of
the climate, which can help communities prepare for future
impact of extreme weather events.
Cornell University: Prof. Ekta Khurana at Weill Cornell
Medicine will use Empire AI to improve prostate cancer
diagnosis and treatment, helping patients in New York State
and reducing healthcare costs.
CUNY: Prof. Rabinda Mandal is studying how malaria affects
the gut microbiome, pioneering new strategies to combat
infectious diseases.
NYU: Prof. Christine Constantinople is using AI to better understand the human brain, in particular how we make decisions and solve problems.

Empire AI: A new model for provisioning AI and HPC for academic research in the public good

RPI: Profs. Ge Wang and Pingkun Yan are building models to
analyze CT scans to better diagnose/treat lung cancer.
SUNY: Prof. Srirangaraj Setlur and team at UB are developing
technologies that will provide adaptive speech and language
therapies to children with special needs.

3.1

Proposals, export control, allocations, and
scheduling

Only faculty, staff, postdocs, and students of member institutions
who live in the US are allowed to use Empire AI resources, and
consortium members approve all projects and teams. Direct access
to Empire AI systems is blocked from countries of concern including China. Project proposals are centrally collected by Empire AI
using a uniform format and process, and then member institutions
perform their own screening and prioritization. These processes
and policies follow academic norms including those of NSF ACCESS
[1, 3], and are strongly aligned with federal requirements including
NIST frameworks, NSPM-33 [14], export control laws and trade
compliance, and OSTP guidelines. Note that Empire AI is presently
conceived to only support unclassified, fundamental research as
defined in NSDD-189 [6] that is exempt from export control restrictions; indeed, several of our member institutions only perform such
research. Nevertheless, Empire AI and its consortium members already have strong and comprehensive protections that help prevent
export control violations. As detailed by the AAU [13], these include: compliance trainings and security requirements, monitoring
and disclosure requirements on university staff and faculty, and
coordination with Federal law enforcement to investigate issues.
For the upcoming Beta system (see below), we anticipate soliciting several classes of proposals, including "capability" (e.g., to train
massive models) and "capacity" (e.g., high-throughput workflows).
On Alpha we experimented with scheduling policies to achieve
efficient and equitable system use while also facilitating large jobs
to use all available resources. Each institution has its own Slurm
partition. Initially, each week a different institution would have
high priority on 12 of the 13 nodes in Alpha. As intended, this
achieved equity between institutions and also reduced the drain
time associated with scheduling large jobs. However, often only a
few users dominated usage in a priority week and relatively few
large jobs were run since workloads were still ramping up. Also,
with six (and potentially soon nine) member institutions, users
would have a long wait for their priority week, which was hard to
align with the natural schedule of research. So we now allocate just
six of the nodes in a priority week, with the remaining nodes open
to all, and with fair-share scheduling within all Slurm partitions.
We do not anticipate needing the priority week on Beta since it will
be much larger and we aim to achieve equity between institutions
through finite project allocations, fair-share and, hopefully minimal,
manual priority adjustments.

4

Establishing a community and
crowd-sourcing operations

Alpha is generously operated by the Flatiron Foundation team led
by Dr. Ian Fisk. Already serving about 250 users and growing, the
work load is substantial. Even when we have a full Empire AI staff,
there will be a challenge meeting the full scale and diversity of

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

users and workflows, including for user training. Following the
campus champion model [4], we identified at each institution a
technical point-of-contact (PoC) who is typically a senior person
in the local research-computing or IT department. Each site also
identifies several agents (typically scientific research support staff)
who can login in to Empire AI computers and about two of whom
will access our ticket system. These agents are charged with primarily supporting users from their own site, whom they presumably
already know and support, as well as building up documentation,
etc., used by all sites. All PoCs and agents meet virtually every
two weeks, to discuss issues and implementation choices, etc. The
PoCs and agents are now being trained in the containerized software technologies to be deployed on Beta, and will then scale that
training to the full user base.

5

Beta system

Beta serves three main roles: (1) substantial compute power including both capability and capacity; (2) technology exploration
for Gamma; and (3) establishing Empire AI Consortium’s leadership by being the first academic initiative to employ this advanced
hardware and software technology. Beta will start operations in
early fall 2025 and will be temporarily located with Alpha in the
UB-CCR. Its NVIDIA Blackwell GPUs are faster with more memory
than those in Alpha. Once software and user workflows are fully
tuned, Beta should be up to ∼7x faster than Alpha on ML training
and up to ∼20x on inference. The DGX GB200 NVL72 SuperPOD
technology tightly integrates the GPUs, enabling efficient training
of multi-trillion parameter models. Each rack of the liquid-cooled
NVL72 consumes up to 135kW power with up to 20% released to air.
The Grace-Grace nodes (∼ 500kW each) will also be liquid cooled.
UB is making substantial power upgrades to accommodate Beta and
also temporarily relocating equipment. Both Alpha and Beta will
be relocated to the new facility (see below) so that UB can recoup
their investment. Beta will include:
• An NVIDIA DGX GB200 NVL72 SuperPOD with 288 B200
GPUs for AI applications;
• 60 nodes of NVIDIA Grace-Grace Superchip for HPC and
data processing;
• 20+ Petabytes effective flash storage from VAST as our primary advanced data platform;
• 10+ Petabytes flash storage from DDN for high-performance
data
• The NVIDIA Run:ai and AI Enterprise commercial-grade AI
software for training and inference; and
• 100 Gbit/s connection to NYSERNET [12], the New York
State Education and Research Network.
The SuperPOD will include ∼70 TByte of LPDDR5X memory at
up to 18.4 Tbyte/s and ∼54 TByte of HBM3e memory at up to 512
Tbyte/s. The tensor cores will achieve 5.76 exaFLOP/s in FP4, 2.88 in
FP8, 1.44 in BF16/FP16, and 0.72 in FP32. Non-tensor performance
is 23.0 petaFLOP/s in FP32 and 11.0 petaFLOP/s in FP64. Grace is
a general-purpose processor with high memory bandwidth that
delivers excellent floating-point and integer performance across
a wide range of applications [5, 15]. It also maintains binary compatibility with the rest of Beta. Each node includes 144 cores of
ARM Neoverse V2 at 3.5Hz (8 teraFLOP/s FP64) with 0.9 Tbyte

PEARC ’25, July 20–24, 2025, Columbus, OH, USA

of LPDDR5X memory (0.95 Tbyte/s). Alpha will also be expanded
with 6 HGX H200 nodes (48 H200 GPUs). Note that Alpha employs
x86 CPUs. Thus, between Alpha, the Grace-Grace nodes, and the
SuperPOD, researchers can pick the tool best suited for their needs.

6

Future facility and technology roadmap

The conceptual design of the final facility is underway with expected completion in Summer 2025. The design goal is 5MW for
the first phase of operations, with cost-efficient incremental upgrade to 15MW. The facility’s location on the SUNY UB campus
was required in the state funding commitment. This geographic
location is considered strategic for the sustainability and operational cost efficiency of the facility. It will be powered by Niagara
Falls hydroelectric power [11] and will eventually be cooled with
water from the UB central chilled water plant, to which warm water
will be returned, enabling recovery of heat to warm buildings in
the extended cold winter. Very efficient dry coolers will provide
resilience and cover summer peak loads.
To track technology, software, and algorithms, we presently plan
to install over the next 10 years three generations of computer in
the new facility, each at circa $100M. The first such system, Gamma,
is expected to start operations by spring 2027 and should be at least
3x more capable than Beta. We have so far made no technology
selection for Gamma, with our future experience with Beta being
highly relevant.

7

Preliminary economic impact

In March 2025, HR&A Advisors, Inc. performed a preliminary economic impact study using IMPLAN’s input-output model and multipliers [10] of Empire AI’s initial investments in Alpha, Beta, construction of the future computer facility, and its first generation of
computers that together will total about $196 million.
• Together, these investments will generate a one-time total
impact of 750 job-years, $67 million in labor income, and
$155 million in economic output in New York State between
2024 and 2026.
• The Alpha and Beta clusters will generate 220 job-years, $20
million in labor income, and nearly $46 million in economic
output.
• The investment into the permanent Center will generate a
total impact of 530 job-years, $47 million in labor income, and
$109 million in economic output in New York State between
Q2 2025 and Q4 2026.
These are preliminary projections will continue to be refined, and
do not account for economic impacts generated through future operations or associated research activity, inventions produced, startups
created, faculty and student recruitment, and other activities.

Acknowledgments
We gratefully acknowledge use of the research computing resources
of the Empire AI Consortium, Inc, with support from the State of
New York, the Simons Foundation, and the Secunda Family Foundation.

Bloom et al.

References
[1] ACCESS. 2025. The national research cyberinfrastructure (CI) ecosystem. https:
//access-ci.org/
[2] Bloomberg. 2025. Tom Secunda. Retrieved March 25, 2025 from https://www.
bloomberg.com/company/values/tech-at-bloomberg/features/tom-secunda/
[3] Timothy J. Boerner, Stephen Deems, Thomas R. Furlani, Shelley L. Knuth, and
John Towns. 2023. ACCESS: Advancing Innovation: NSF’s Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support. (July 2023), 173–6.
doi:10.1145/3569951.3597559
[4] Marisa Brazil, Dana Brunson, Aaron Culich, Lizanne DeStefano, Douglas Jennewein, Tiffany Jolley, Timothy Middelkoop, Henry Neeman, Lorna Rivera, Jack
Smith, and Julie Wernert. 2019. Campus Champions: Building and sustaining a
thriving community of practice around research computing and data. In Practice
and Experience in Advanced Research Computing 2019: Rise of the Machines (Learning) (Chicago, IL, USA) (PEARC ’19). Association for Computing Machinery, New
York, NY, USA, Article 78, 7 pages. doi:10.1145/3332186.3332200
[5] David Carlson, Nikolay Simakov, Rodrigo Ristow Hadlich, Anthony Curtis, Joshua
Martin, Gaurav Verma, Smeet Chheda, Firat Coskun, Raul Gonzalez, Daniel Wood,
Feng Zhang, Robert Harrison, and Eva Siegmann. 2025. The AmpereOne A19232X in Perspective: Benchmarking a New Standard. doi:10.13140/RG.2.2.35135.
21925
[6] National Security Decision Directives. 1985. National Policy on the Transfer of
Scientific, Technical, and Engineering Information. Retrieved March 25, 2025 from
https://irp.fas.org/offdocs/nsdd/nsdd-189.htm
[7] Simons Foundation. 2025. Flatiron Institute. Retrieved March 25, 2025 from
https://www.simonsfoundation.org/flatiron/
[8] Simons Foundation. 2025. Simons Foundation. Retrieved March 25, 2025 from
https://www.simonsfoundation.org/
Governor Hochul Unveils Fifth Proposal
[9] Governor Kathy Hochul. 2024.
of 2024 State of the State: Empire AI Consortium to Make New York the
National Leader in AI Research and Innovation.
Retrieved March 25,
2025 from https://www.governor.ny.gov/news/governor-hochul-unveils-fifthproposal-2024-state-state-empire-ai-consortium-make-new-york
[10] IMPLAN. 2025. Economic impact analysis. Retrieved March 25, 2025 from
https://implan.com/economic-impact-analysis/
[11] New York Power Authority (NYPA). 2025. The Niagara Power Project: Clean
Energy for NY. Retrieved March 25, 2025 from https://www.nypa.gov/power/
generation/niagara-power-project
[12] NYSERNet Inc. 2025. New York State Education and Research Network. Retrieved
March 25, 2025 from https://nysernet.org/home
[13] Association of American Universities. 2020. University Actions to Address Concerns about Security Threats and Undue Foreign Government Influence on Campus.
Retrieved March 25, 2025 from https://www.aau.edu/sites/default/files/AAUFiles/Key-Issues/Science-Security/2020-Effective-Science-Security-PracticesSummary.pdf
[14] National Science and Technology Council. 2022. Guidance for Implementing National Security Presidential Memorandum 33 (NSPM-33) on National Security Strategy for United States Government-Supported Research and Development: A Report
by the Subcommittee on Research Security Joint Committee on the Research Environment. Retrieved March 25, 2025 from https://bidenwhitehouse.archives.gov/wpcontent/uploads/2022/01/010422-NSPM-33-Implementation-Guidance.pdf
[15] Nikolay A. Simakov, Matthew D. Jones, Thomas R. Furlani, Eva Siegmann, and
Robert J. Harrison. 2024. First Impressions of the NVIDIA Grace CPU Superchip
and NVIDIA Grace Hopper Superchip for Scientific Workloads. In Proceedings
of the International Conference on High Performance Computing in Asia-Pacific
Region Workshops (Nagoya, Japan) (HPCAsia ’24 Workshops). Association for
Computing Machinery, New York, NY, USA, 36–44. doi:10.1145/3636480.3637097

