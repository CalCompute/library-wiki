---
url: https://scienceit-docs.lbl.gov/hpc/
fetched: 2026-11-20
publisher: "Lawrence Berkeley National Laboratory, Science IT"
published: unknown
original: 2026-11-20 Berkeley Lab Lawrencium recharge rates.html
rehost: yes
---

_Markdown copy of 2026-11-20 Berkeley Lab Lawrencium recharge rates.html, made 2026-11-20. The original is the authority._
[ ]
[ ]

[Skip to content](#high-performance-computing)

[![logo](../assets/scienceitlogo.png)](.. "ScienceIT Technical Documentation")

ScienceIT Technical Documentation

Lawrencium Overview

Initializing search

* [Home](..)
* [High Performance Computing](./)
* [Kubernetes](../kubernetes/)
* [Globus Transfer System](../data/globus/)
* [Cloud Services](../cloud/)
* [ComputeView](https://computeview.lbl.gov/)
* [Support & Training](../help/)

[![logo](../assets/scienceitlogo.png)](.. "ScienceIT Technical Documentation")
ScienceIT Technical Documentation

* [Home](..)
* [x]

  [High Performance Computing](./)

  High Performance Computing
  + [Getting Started](getting-started/)
  + [Frequently Asked Questions](faqs/)
  + [Jobscript Generator](https://lbnl-science-it.github.io/lrc-jobscript/)
  + [ ]

    Account Management

    Account Management
    - [Project Accounts](accounts/project-accounts/)
    - [User Accounts](accounts/user-accounts/)
    - [Using the MyLRC Portal](accounts/mylrc/)
    - [Charges and Billing](accounts/charges/)
    - [Logging in](accounts/loggingin/)
    - [Multi-Factor Authentication](accounts/mfa/)
  + [ ]

    Computing Systems

    Computing Systems
    - [CPU Cluster](systems/lawrencium/)
    - [GPU Cluster](systems/einsteinium/)
    - [ ]

      Supported Research Clusters

      Supported Research Clusters
      * [ALSACC](systems/supported/alsacc/)
      * [CATAMOUNT](systems/supported/catamount/)
      * [CATSCAN](systems/supported/catscan/)
      * [DIRAC1](systems/supported/dirac1/)
      * [ETNA](systems/supported/etna/)
      * [MHG](systems/supported/mhg/)
  + [ ]

    Data Transfer

    Data Transfer
    - [Using the lrc-xfer DTN](data-transfer-node/)
    - [Globus for Lawrencium](../data/globus-instructions/)
  + [ ]

    Software

    Software
    - [Software Module Farm](software/software-module-farm/)
    - [Module Management](software/module-management/)
    - [ ]

      Compilers

      Compilers
      * [GCC](software/compilers/gcc/)
      * [Intel](software/compilers/intel/)
      * [NVHPC](software/compilers/nvhpc/)
    - [ ]

      Languages

      Languages
      * [Python](software/languages/python/)
      * [Julia](software/languages/julia/)
      * [R](software/languages/R/)
    - [ ]

      Machine Learning

      Machine Learning
      * [PyTorch](software/ml/pytorch/)
      * [Ray](software/ml/ray/)
      * [TensorFlow](software/ml/tensorflow/)
      * [Alphafold3](software/ml/alphafold3/)
    - [ ]

      Applications

      Applications
      * [VASP](software/applications/vasp/)
    - [ ]

      MPI

      MPI
      * [Open MPI](software/mpi/openmpi/)
      * [Intel MPI](software/mpi/intelmpi/)
    - [ ]

      Libraries

      Libraries
      * [FFTW](software/libraries/fftw/)
      * [HDF5](software/libraries/hdf5/)
      * [NetCDF](software/libraries/netcdf/)
      * [MKL](software/libraries/mkl/)
      * [CUDA](software/libraries/cuda/)
    - [ ]

      Profiling Tools

      Profiling Tools
      * [GNU Gprof](software/performance/gnu-gprof/)
      * [Intel VTune](software/performance/intel-vtune/)
    - [ ]

      LLMs

      LLMs
      * [Ollama](software/llms/ollama/)
      * [vLLM](software/llms/vllm/)
    - [ ]

      Containers

      Containers
      * [Apptainer](software/containers/apptainer/)
  + [ ]

    Running Jobs

    Running Jobs
    - [Slurm Overview](running/slurm-overview/)
    - [Example Scripts](running/script-examples/)
    - [Monitor Jobs](running/monitor-jobs/)
    - [GNU Parallel](running/gnu-parallel/)
  + [ ]

    Using Open OnDemand

    Using Open OnDemand
    - [Open OnDemand Overview](openondemand/overview/)
    - [Jupyter Server](openondemand/jupyter-server/)
    - [Ollama with Jupyter and VS Code](openondemand/ollama-jupyter-vscode/)
    - [Adding Packages and Kernels](openondemand/packages-kernels/)
  + [ ]

    AI Tools

    AI Tools
    - [Using AI Agents on Lawrencium](ai-tools/ai-agents/)
    - [Running AI Agents on Compute Nodes](ai-tools/tmux-slurm/)
    - [Lawrencium Skill](ai-tools/lawrencium-skill/)
    - [Using Claude Science with Lawrencium](ai-tools/claude-science/)
  + [Acknowledgement](acknowledgement/)
* [ ]

  [Kubernetes](../kubernetes/)

  Kubernetes
  + [Berkelium Portal](https://berkelium.scs.lbl.gov)
  + [National Research Platform](../nrp/)
* [ ]

  Globus Transfer System

  Globus Transfer System
  + [Globus](../data/globus/)
  + [Globus for Lawrencium](../data/globus-instructions/)
  + [Globus for Google Drive](../data/globus-google-drive/)
  + [Using the Globus AWS S3 Connector](../data/globus-aws-s3-connector/)
  + [Using the Globus Google Cloud Storage Connector](../data/globus-google-cloud-storage-connector/)
* [ ]

  [Cloud Services](../cloud/)

  Cloud Services
  + [ ]

    Cloud Service Providers

    Cloud Service Providers
    - [Amazon Web Services](../cloud/aws/)
    - [Google Cloud Platform](../cloud/gcp/)
  + [Google Cloud Skills Boost](../cloud/gcp-skills-boost/)
* [ComputeView](https://computeview.lbl.gov/)
* [ ]

  [Support & Training](../help/)

  Support & Training
  + [Training](../help/training/)
  + [Asking LLMs](../help/llms/)

Table of contents

* [Hardware Configuration](#hardware-configuration)
* [Storage and Backup](#storage-and-backup)
* [Recharge Model](#recharge-model)

  + [CPU Partitions Recharge Rates](#cpu-partitions-recharge-rates)
  + [GPU Partitions Recharge Rates](#gpu-partitions-recharge-rates)
* [Scheduler Configuration](#scheduler-configuration)

# High Performance Computing[¶](#high-performance-computing "Permanent link")

**Lawrencium** is the platform for the [LBNL Condo Cluster Computing (LC3)](https://it.lbl.gov/service/scienceit/high-performance-computing/lrc/computing-on-lawrencium/condo-cluster-service/)  program, which provides a sustainable way to meet the midrange computing requirement for Berkeley Lab. Lawrencium is part of the LBNL Supercluster and shares the same Supercluster infrastructure. This includes the system management software, software module farm, scheduler, storage and backend network infrastructure.

Berkeley Data Center

Lawrencium is located at the Berkeley Data Center in Building 50B-1275. The datacenter is a 5000 sq. ft. facility dedicated for Berkeley Lab's scientific computing resources such as Lawrencium.

* **Hardware Configuration**

  ---

  Partitions and node types across the Lawrencium CPU cluster, the Einsteinium GPU cluster, and supported research clusters.

  [View the hardware](#hardware-configuration)
* **Storage and Backup**

  ---

  HOME, GROUP, and SCRATCH file systems, their quotas and backup policies, plus condo private storage.

  [View storage systems](#storage-and-backup)
* **Recharge Model**

  ---

  How condo and normal users are charged, with per-partition Service Unit ratios and effective recharge rates.

  [View recharge rates](#recharge-model)
* **Charges and Billing**

  ---

  The $25/month account fee (LRCACT) that applies to every user account, and compute charges (LRCCPU) for recharge accounts.

  [View charges and billing](accounts/charges/)
* **Scheduler Configuration**

  ---

  Slurm partitions, accounts, and QoS options, along with the fair-share policy and job prioritization.

  [View scheduler details](#scheduler-configuration)

## Hardware Configuration[¶](#hardware-configuration "Permanent link")

Lawrencium is composed of multiple generations of hardware hence it is separated into several partitions to facilitate management and to meet the requirements to host Condo projects. The following table lists the hardware configuration for each individual partition.

* [Lawrencium CPU Cluster](systems/lawrencium/)
* [Einsteinium GPU Cluster](systems/einsteinium/)

In addition, there are several **Supported Research Clusters**; more information on each of these can be found by selecting the desired supported cluster under `Computing Systems > Supported Research Clusters`.

## Storage and Backup[¶](#storage-and-backup "Permanent link")

Lawrencium cluster users are entitled to access the following storage systems so please get familiar with them.

| Name | Location | Quota | Backup | Allocation | Description |
| --- | --- | --- | --- | --- | --- |
| HOME | `/global/home/users/$user` | 30GB | Yes | Per User | Home directory for permanant data storage |
| GROUP-SW | `/global/home/groups-sw/$group` | 200GB | Yes | Per Group | Group directory for software and data sharing with backup |
| GROUP | `/global/home/groups/$group` | 400GB | No | Per Group | Group directory for data sharing without backup |
| SCRATCH | `/global/scratch/users/$user` | None | No | Per User | Scratch directory with Lustre high performance parallel file system |

Project Group Directories

Project group directories are not created by default. If you would like to create group directories where your group members can share data and software, please submit a [service request on freshservice](https://lbl.freshservice.com/a/catalog/request-items/169).

Private storage for condo users follow the structure `/clusterfs/$CONDO_NAME/$USER`. For example:

| Name | Location | Quota | Backup | Allocation | Description |
| --- | --- | --- | --- | --- | --- |
| CLUSTERFS | `/clusterfs/axl/$USER` | None | No | Per User | Private storage for AXL condo |
| CLUSTERFS | `/clusterfs/cumulus/$USER` | None | No | Per User | Private storage for CUMULUS condo |
| CLUSTERFS | `/clusterfs/esd/$USER` | None | No | Per User | Private storage for ESD condo |
| CLUSTERFS | `/clusterfs/geoseq/$USER` | None | No | Per User | Private storage for CO2SEQ condo |
| CLUSTERFS | `/clusterfs/nokomis/$USER` | None | No | Per User | Private storage for NOKOMIS condo |

## Recharge Model[¶](#recharge-model "Permanent link")

LBNL has made a significant investment in developing this platform to meet the midrange computing requirement at Berkeley Lab. The primary purpose is to provide a sustainable way to host all the condo projects while meeting the computing requirements from other users. To achieve this goal, condo users are allowed to run within their condo contributions for free. However normal users who would like to use the Lawrencium cluster are subject to the LBNL recharge rate.

Condo users who would need to run outside of their condo contributions are also subject to the same recharge rate as normal users. For this purpose, condo users will obtain either one or two projects/accounts when their accounts are created on Lawrencium, per the instruction we receive from the PI of the condo project. They would need to provide the correct project when running jobs inside or outside of their condo contributions, which will be explained in detail in the Scheduler Configuration section below. The current recharge rate is $0.01 per Service Unit (1 cent per service unit, SU). Due to the hardware architecture difference we discount effective recharge rate for older generations of hardware. Please refer to the following table for the current recharge rate for each partition.

Compute charges vs. the account fee

The recharge rates below apply only to jobs run under recharge (`ac_*`) accounts, and appear as LRCCPU in the LBL Cost Browser. Separately, every user account is charged a $25/month account fee (LRCACT), whether or not jobs are run. See [Charges and Billing](accounts/charges/).

### CPU Partitions Recharge Rates[¶](#cpu-partitions-recharge-rates "Permanent link")

| Partition | Shared or Exclusive | SU to Core CPU Hour Ratio | Effective Recharge Rate |
| --- | --- | --- | --- |
| lr4 | Exclusive | 0 | free |
| lr5 | Exclusive | 0.50 | $0.0050 per Core CPU Hour |
| lr6 | Exclusive | 0.75 | $0.0075 per Core CPU Hour |
| lr7 | Shared | 1.0 | $0.01 per Core CPU Hour |
| lr8 | Shared | 1.0 | $0.01 per Core CPU Hour |
| lr\_bigmem | Exclusive | 1.5 | $0.015 per Core CPU Hour |
| cf1 | Exclusive | 0.4 | $0.004 per Core CPU Hour |
| cm1 | Shared | 0.75 | $0.0075 per Core CPU Hour |
| cm2 | Exclusive | 1.0 | $0.01 per Core CPU Hour |
| ood\_inter | Shared | 1.0 | $0.01 per Core CPU Hour |

### GPU Partitions Recharge Rates[¶](#gpu-partitions-recharge-rates "Permanent link")

| Partition | Shared or Exclusive | SU to Core CPU Hour Ratio | Effective Recharge Rate |
| --- | --- | --- | --- |
| es0 | Shared | 0 | free |
| es1 | Shared | 1.0 | $0.01 per Core CPU Hour |
| es2 | Shared | 4.0 | $0.04 per Core CPU Hour |
| es3 | Shared | 1.0 | $0.01 per Core CPU Hour |

GPU-hour cost on `es2` and `es3`

GPU jobs are charged for the CPU cores allocated with each GPU: 14 cores per GPU on `es2` and 32 cores per GPU on `es3`. One GPU-hour therefore costs 56 SU ($0.56) on `es2` and 32 SU ($0.32) on `es3`.

Usage Calculation

The usage calculation is based on the resource that is allocated to the job instead of the actual usage of the job. For example, if a job asked for one `lr5` node with one CPU requirement (typical serial job case), and the job ran for 24 hours, since **lr5** nodes are allocated **exclusively** to the job (please refer to the following Scheduler Configuration section for more detail), the charge that this job incurred would be:

**$0.0050/(core x hour) x 1 node x 24 cores/node x 24 hours = $2.88**

instead of: $0.0050/(core x hour) x 1 core x 24 hours = $0.12.

You can use the [LRC Jobscript Generator](https://lbnl-science-it.github.io/lrc-jobscript/) page to generate sample slurm job submission scripts targeting different partitions, and to get an estimate of the Service Units (SUs) based on the system and number of hours of usage.

## Scheduler Configuration[¶](#scheduler-configuration "Permanent link")

Lawrencium cluster uses [SLURM to submit jobs](running/slurm-overview/) as the scheduler to manage jobs on the cluster. To use Lawrencium through slurm, the partition (`lr4, lr5, lr6, lr7, lr8, es0, es1, es2, es3, cm1, cm2` must be specified (`--partition=xxx`) along with account (`--account=xxx`). Currently the available QoS (Quality of Service)s are `lr_normal` and `lr_debug` and `lr_lowprio` on most `lr` partitions and `lr8_normal` on `lr8`.

* For normal users to use the Lawrencium resource the proper project account, e.g., `--account=ac_abc`, is needed. The QoS `lr_normal` is also required based on the partition that the job is submitted to, e.g., `--qos=lr_normal`.
* If a debug job is desired the `lr_debug` QoS should be specified, e.g., `--qos=lr_debug` so that the scheduler can adjust job priority accordingly.
* Condo users please use the proper condo QoS, e.g., `--qos=condo_xyz`, as well as the proper condo account `--account=lr_xyz`.
* The partition name is always required in all cases, e.g., `--partition=lr6`.

Fair-share policy

A standard fair-share policy with a decay half life value of 14 days (2 weeks) is enforced. All accounts are given equal shares value of 1. All users under each account associated within a partition is subjected to decay’g in priority based on the resources used and the overall parent account usage. Usage is a value between 0.0 and 1.0 that associates proportional usage of the system. A value of 0 indicates that the association is over-served. In other words that account has used its share of the resources and will be given a lower value of shares compared to users who have not used as much resources.

* Job prioritization is based on Age, Fairshare, Partition and QOS. Note: `lr_lowprio` qos jobs are not given any prioritization and some QOS have higher values than others.
* Low priority QoSes (`*_lowprio`, e.g., `lr_lowprio`, `es_lowprio`, `es3_lowprio`) are not available to PI Computing Allowance (PCA) accounts (`pc_*`).
* If a node feature is not provided, the job will be dispatched to nodes based on a predefined order; for `lr5` the order is: `lr5_c28`, `lr5_c20`.

October 28, 2026

Back to top

[Previous

Home](..)
[Next

Getting Started](getting-started/)

[![logo](/assets/11_BL_IT_logo_white.png)](https://scienceit.lbl.gov "Lawrence Berkeley National Laboratory")

[Science IT](https://scienceit.lbl.gov) - [IT Division](https://it.lbl.gov) - [Lawrence Berkeley National Laboratory](https://lbl.gov) | [Privacy & Security Notice](https://www.lbl.gov/terms-and-conditions/)
