---
url: https://docs.nersc.gov/systems/perlmutter/architecture/
fetched: 2026-11-11
publisher: "National Energy Research Scientific Computing Center (NERSC)"
published: unknown
original: 2026-11-11 NERSC Perlmutter architecture.html
rehost: yes
---

_Markdown copy of 2026-11-11 NERSC Perlmutter architecture.html, made 2026-11-11. The original is the authority._
[ ]  [ ]

[Skip to content](#perlmutter-architecture)

   [![logo](../../../assets/images/logo.png)](../../.. "NERSC Documentation")

NERSC Documentation

Architecture

Initializing search

[GitLab/NERSC/docs](https://gitlab.com/NERSC/nersc.gitlab.io "Go to repository")

[![logo](../../../assets/images/logo.png)](../../.. "NERSC Documentation")  NERSC Documentation

[GitLab/NERSC/docs](https://gitlab.com/NERSC/nersc.gitlab.io "Go to repository")

* [Home](../../..)
* [Getting Started at NERSC](../../../getting-started/)
* [Absolute Beginner's Guide](../../../beginner-guide/)
* [x]    Understanding Our Systems       Understanding Our Systems
  + [NERSC Systems](../../)
  + [x]    Perlmutter       Perlmutter
    - [ ]    Architecture     [Architecture](./)     Table of contents
      * [System Specifications](#system-specifications)
      * [System Performance](#system-performance)
      * [Interconnect](#interconnect)
        + [NIC](#nic)
      * [Node Specifications](#node-specifications)
        + [GPU nodes](#gpu-nodes)
        + [CPU Nodes](#cpu-nodes)
        + [Login nodes](#login-nodes)
      * [Storage](#storage)
    - [Timeline](../timeline/)
    - [Current Known Issues](../../../current/)
* [ ]    Getting and Managing Your Account       Getting and Managing Your Account
  + [Accounts](../../../accounts/)
  + [Passwords](../../../accounts/passwords/)
  + [Policy](../../../accounts/policy/)
  + [Collaboration Accounts](../../../accounts/collaboration_accounts/)
  + [Iris Guide for Users](../../../iris/iris-for-users/)
  + [Associating Publications with Your Account](../../../iris/iris-publications/)
* [ ]    Connecting to NERSC       Connecting to NERSC
  + [Establishing Connections](../../../connect/)
  + [Multi-Factor Authentication](../../../connect/mfa/)
  + [Federated Identity](../../../connect/federatedid/)
  + [ThinLinc](../../../connect/thinlinc/)
  + [Visual Studio Code / VSCode](../../../connect/vscode/)
* [ ]    Working in a NERSC Shell       Working in a NERSC Shell
  + [Customizing and Troubleshooting Shells](../../../environment/)
  + [Shell Startup](../../../environment/shell_startup/)
  + [Lmod](../../../environment/lmod/)
  + [ ]    Containers       Containers
    - [Containers](../../../development/containers/)
    - [ ]    Podman-hpc       Podman-hpc
      * [Podman-hpc for Beginners Tutorial](../../../development/containers/podman-hpc/podman-beginner-tutorial/)
      * [Using Podman-hpc at NERSC](../../../development/containers/podman-hpc/overview/)
    - [ ]    Shifter       Shifter
      * [Shifter](../../../development/containers/shifter/)
      * [Shifter for Beginners Tutorial](../../../development/containers/shifter/shifter-beginner-tutorial/)
      * [How to use Shifter](../../../development/containers/shifter/how-to-use/)
      * [FAQ and Troubleshooting](../../../development/containers/shifter/faq-troubleshooting/)
      * [Example Shifter Containers](../../../development/containers/shifter/examples/)
    - [NERSC Registry](../../../development/containers/registry/)
* [ ]    Running Jobs       Running Jobs
  + [Basics of Running Jobs](../../../jobs/)
  + [Running Jobs on Perlmutter](../running-jobs/)
  + [Resource Usage Policies](../../../policies/resource-usage/)
  + [Scheduling](../../../jobs/scheduling/)
  + [Queues and Charges](../../../jobs/policy/)
  + [Interactive](../../../jobs/interactive/)
  + [Example Jobs](../../../jobs/examples/)
  + [Best Practices](../../../jobs/best-practices/)
  + [Jobscript Generator](../../../jobs/jobscript-generator/)
  + [Job Cost Calculator](../../../jobs/cost/)
  + [How Do I Choose a Job QOS?](../../../jobs/qos-flow-chart/)
  + [Troubleshooting Jobs](../../../jobs/troubleshooting/)
  + [Monitoring](../../../jobs/monitoring/)
  + [Affinity](../../../jobs/affinity/)
  + [Reservations](../../../jobs/reservations/)
  + [GPU Power Capping](../../../jobs/power-capping/)
  + [ ]    Checkpoint/Restart       Checkpoint/Restart
    - [Checkpoint/Restart Overview](../../../development/checkpoint-restart/)
    - [DMTCP](../../../development/checkpoint-restart/dmtcp/)
    - [MANA](../../../development/checkpoint-restart/mana/)
    - [Containerized checkpoint restart](../../../development/checkpoint-restart/containers/)
* [ ]    Running Workflows       Running Workflows
  + [Workflow Tools](../../../jobs/workflow/)
  + [Workflow queue](../../../jobs/workflow/workflow-queue/)
  + [Scrontab](../../../jobs/workflow/scrontab/)
  + [GNU Parallel](../../../jobs/workflow/gnuparallel/)
  + [TaskFarmer](../../../jobs/workflow/taskfarmer/)
  + [FireWorks](../../../jobs/workflow/fireworks/)
  + [Nextflow](../../../jobs/workflow/nextflow/)
  + [Papermill](../../../jobs/workflow/papermill/)
  + [Parsl](../../../jobs/workflow/parsl/)
  + [Snakemake](../../../jobs/workflow/snakemake/)
  + [libEnsemble](../../../jobs/workflow/libensemble/)
  + [Maestro](../../../jobs/workflow/maestro/)
  + [Community Supported Tools](../../../jobs/workflow/community_tools/)
* [ ]    Using Applications and Frameworks       Using Applications and Frameworks
  + [Applications Overview](../../../applications/)
  + [ ]    Supported Applications and Frameworks       Supported Applications and Frameworks
    - [AMBER](../../../applications/amber/)
    - [BerkeleyGW](../../../applications/berkeleygw/)
    - [CP2K](../../../applications/cp2k/)
    - [Dask](../../../analytics/dask/)
    - [E4S](../../../applications/e4s/)
    - [Gromacs](../../../applications/gromacs/)
    - [ ]    Jupyter       Jupyter
      * [Jupyter Overview](../../../services/jupyter/)
      * [How-To Guides](../../../services/jupyter/how-to-guides/)
      * [Reference](../../../services/jupyter/reference/)
      * [Background](../../../services/jupyter/background/)
    - [LAMMPS](../../../applications/lammps/)
    - [Mathematica](../../../applications/mathematica/)
    - [ ]    MATLAB       MATLAB
      * [MATLAB](../../../applications/matlab/)
      * [MATLAB Compiler](../../../applications/matlab/matlab_compiler/)
    - [NAMD](../../../applications/namd/)
    - [NCL](../../../applications/ncl/)
    - [NWChem](../../../applications/nwchem/)
    - [ORCA](../../../applications/orca/)
    - [ParaView](../../../applications/paraview/)
    - [PyTorch](../../../machinelearning/pytorch/)
    - [Q-Chem](../../../applications/qchem/)
    - [Quantum ESPRESSO](../../../applications/quantum-espresso/)
    - [ROOT](../../../development/languages/cernroot/)
    - [TensorBoard](../../../machinelearning/tensorboard/)
    - [TensorFlow](../../../machinelearning/tensorflow/)
    - [VASP](../../../applications/vasp/)
    - [VisIt](../../../applications/visit/)
    - [ ]    WRF       WRF
      * [Introduction to WRF](../../../applications/wrf/)
      * [WPS](../../../applications/wrf/wps/)
      * [WRF](../../../applications/wrf/wrf/)
      * [WRF module](../../../applications/wrf/wrf_module/)
      * [WRF benchmark](../../../applications/wrf/wrf_benchmark/)
  + [Analytics](../../../analytics/analytics/)
  + [ ]    Machine Learning       Machine Learning
    - [Machine Learning at NERSC](../../../machinelearning/)
    - [Distributed training](../../../machinelearning/distributed-training/)
    - [ ]    Machine Learning Tools       Machine Learning Tools
      * [Overview](../../../machinelearning/tools-overview/)
      * [Training Launchers](../../../machinelearning/launchers/)
      * [Training Libraries](../../../machinelearning/training/)
      * [Hyperparameter Optimization](../../../machinelearning/hpo/)
  + [Software Support Policy](../../../policies/software-policy/)
* [ ]    Developing and Installing Software       Developing and Installing Software
  + [ ]    AI Coding Tools       AI Coding Tools
    - [Overview](../../../development/coding-agents/)
    - [Claude Code on Perlmutter](../../../development/coding-agents/claude-code/)
    - [Codex on Perlmutter](../../../development/coding-agents/codex/)
  + [ ]    Compilers       Compilers
    - [Compilers Overview](../../../development/compilers/)
    - [Base Compilers](../../../development/compilers/base/)
    - [Compiler Wrappers (recommended)](../../../development/compilers/wrappers/)
    - [Compiling a Code](../../../tutorials/playbooks/compiling/)
  + [ ]    Build Tools       Build Tools
    - [Autoconf and Make](../../../development/build-tools/autoconf-make/)
    - [CMake](../../../development/build-tools/cmake/)
    - [Spack](../../../development/build-tools/spack/)
  + [Installing and Sharing Software](../../../development/installing-sharing-software/)
  + [ ]    Programming Models       Programming Models
    - [Programming Models Overview](../../../development/programming-models/)
    - [ ]    MPI       MPI
      * [Introduction to MPI](../../../development/programming-models/mpi/)
      * [Cray MPICH](../../../development/programming-models/mpi/cray-mpich/)
      * [Open MPI](../../../development/programming-models/mpi/openmpi/)
      * [Upstream MPICH](../../../development/programming-models/mpi/mpich/)
    - [OpenMP](../../../development/openmp/)
    - [OpenACC](../../../development/programming-models/openacc/)
    - [CUDA](../../../development/programming-models/cuda/)
  + [ ]    Languages       Languages
    - [C++](../../../development/languages/cpp/)
    - [UPC](../../../development/languages/upc/)
    - [Fortran](../../../development/languages/fortran/)
    - [Julia](../../../development/languages/julia/)
    - [R](../../../development/languages/r/)
    - [Rust](../../../development/languages/rust/)
    - [IDL](../../../development/languages/idl/)
    - [ ]    Python       Python
      * [Python Overview](../../../development/languages/python/)
      * [Intro to Python at NERSC](../../../development/languages/python/python-intro/)
      * [Using Python at NERSC](../../../development/languages/python/nersc-python/)
      * [Parallel Python](../../../development/languages/python/parallel-python/)
      * [Python in Shifter](../../../development/languages/python/python-shifter/)
      * [Profiling Python](../../../development/languages/python/profiling-debugging-python/)
      * [Python on AMD CPUs](../../../development/languages/python/python-amd/)
      * [Using Python on Perlmutter](../../../development/languages/python/using-python-perlmutter/)
      * [Porting Python to Perlmutter GPUs](../../../development/languages/python/perlmutter-prep/)
      * [FAQ and Troubleshooting](../../../development/languages/python/faq-troubleshooting/)
  + [ ]    Libraries       Libraries
    - [Math Libraries](../../../development/libraries/)
    - [FFTW](../../../development/libraries/fftw/)
    - [LAPACK](../../../development/libraries/lapack/)
    - [MKL](../../../development/libraries/mkl/)
    - [LibSci](../../../development/libraries/libsci/)
    - [HDF5](../../../development/libraries/hdf5/)
    - [NetCDF](../../../development/libraries/netcdf/)
  + [ ]    Performance       Performance
    - [Perlmutter Readiness](../../../performance/readiness/)
    - [Vectorization](../../../performance/vectorization/)
    - [Parallelism](../../../performance/parallelism/)
    - [ ]    I/O       I/O
      * [DVS](../../../performance/io/dvs/)
      * [I/O Resources at NERSC](../../../performance/io/)
      * [I/O Tuning](../../../performance/io/library/)
      * [Lustre](../../../performance/io/lustre/)
      * [File system in memory](../../../performance/io/dev-shm/)
    - [Portability](../../../performance/portability/)
    - [Variability](../../../performance/variability/)
    - [Network](../../../performance/network/)
    - [ ]    Performance Tools       Performance Tools
      * [Performance Tools Overview](../../../tools/performance/)
      * [CrayPat](../../../tools/performance/craypat/)
      * [ ]    Darshan       Darshan
        + [Darshan I/O Profiler](../../../tools/performance/darshan/)
        + [DXT Explorer](../../../tools/performance/darshan/dxt/)
        + [Drishti](../../../tools/performance/darshan/drishti/)
      * [MAP](../../../tools/performance/map/)
      * [NVIDIA Profiling Tools](../../../tools/performance/nvidiaproftools/)
      * [Performance Reports](../../../tools/performance/performancereports/)
      * [Reveal](../../../tools/performance/reveal/)
      * [Roofline Performance Model](../../../tools/performance/roofline/)
  + [ ]    Debugging Tools       Debugging Tools
    - [Debugging Tools Overview](../../../tools/debug/)
    - [Compute Sanitizer](../../../tools/debug/compute-sanitizer/)
    - [CUDA-GDB](../../../tools/debug/cuda-gdb/)
    - [DDT](../../../tools/debug/ddt/)
    - [GDB](../../../tools/debug/gdb/)
    - [gdb4hpc and CCDB](../../../tools/debug/gdb4hpc_ccdb/)
    - [Sanitizers and sanitizers4hpc](../../../tools/debug/sanitizers/)
    - [STAT and ATP](../../../tools/debug/stat_atp/)
    - [TotalView](../../../tools/debug/totalview/)
    - [Valgrind and Valgrind4hpc](../../../tools/debug/valgrind/)
* [ ]    Managing Data       Managing Data
  + [Unix File Permissions](../../../filesystems/unix-file-permissions/)
  + [PI Toolbox](../../../filesystems/pitoolbox/)
  + [Quotas](../../../filesystems/quotas/)
  + [ ]    Filesystems       Filesystems
    - [Filesystems Overview](../../../filesystems/)
    - [Perlmutter scratch](../../../filesystems/perlmutter-scratch/)
    - [Community](../../../filesystems/community/)
    - [DnA](../../../filesystems/dna/)
    - [ ]    Archive (HPSS)       Archive (HPSS)
      * [The HPSS Archive System](../../../filesystems/archive/)
      * [HPSS Best Practices](../../../filesystems/HPSS-best-practices/)
      * [HPSS Charging and Data Sharing](../../../filesystems/HPSS-charging-sharing/)
      * [hsi](../../../filesystems/hsi/)
      * [htar](../../../filesystems/htar/)
      * [Storage Statistics](../../../filesystems/archive-stats/)
    - [Global Home](../../../filesystems/global-home/)
    - [Global Common](../../../filesystems/global-common/)
    - [Backups](../../../filesystems/backups/)
  + [Databases](../../../services/databases/)
  + [ ]    Moving Data       Moving Data
    - [File Transfer Software](../../../services/)
    - [Data Transfer Nodes](../../dtn/)
    - [Globus](../../../services/globus/)
    - [CVMFS](../../../services/cvmfs/)
    - [Frontier Cache](../../../services/frontiercache/)
    - [GridFTP](../../../services/gridftp/)
    - [Scp](../../../services/scp/)
    - [Bbcp](../../../services/bbcp/)
    - [Files from Non-Users](../../../services/nonuser-files/)
  + [Sharing Data](../../../filesystems/sharing/)
  + [Data Policy](../../../policies/data-policy/policy/)
* [ ]    Building Your Own Services       Building Your Own Services
  + [ ]    Hosting Services with Spin       Hosting Services with Spin
    - [Spin Overview](../../../services/spin/)
    - [Terminology](../../../services/spin/terminology/)
    - [ ]    Getting Started       Getting Started
      * [Local Development](../../../services/spin/local/)
      * [Running Your App in Spin](../../../services/spin/running/)
      * [Attaching Storage](../../../services/spin/storage/)
      * [Connecting to a Spin App](../../../services/spin/connecting/)
    - [ ]    Advanced Concepts       Advanced Concepts
      * [Using the Rancher CLI](../../../services/spin/cli/)
      * [Development and Production environments](../../../services/spin/envs/)
      * [Managing Spin Apps with Helm](../../../services/spin/helm/)
      * [Migrating Apps from Docker Compose](../../../services/spin/migrate/)
    - [FAQ](../../../services/spin/faq/)
    - [Examples](../../../services/spin/examples/)
  + [ ]    API       API
    - [The Superfacility API](../../../services/sfapi/)
    - [Authentication](../../../services/sfapi/authentication/)
    - [Examples](../../../services/sfapi/examples/)
    - [Version](../../../services/sfapi/versioning/)
  + [Science Gateways](../../../services/science-gateways/)
* [ ]    Managing Projects and Allocations       Managing Projects and Allocations
  + [Making an Allocation Request](../../../allocations/ercap_form/)
  + [ERCAP 2027 Guidance](../../../allocations/ercap_2027/)
  + [Iris Guide for PIs and Project Managers](../../../iris/iris-for-pis/)
  + [Requesting More Resources](../../../allocations/request_increase/)
  + [Allocation Reductions](../../../allocations/allocation_reductions/)
  + [DOE Allocation Managers](../../../allocations/doe.allocation_managers/)
  + [ERCAP and Iris Guide for Allocation Managers](../../../iris/iris-for-allocation-managers/)
* [Acronyms](../../../help/acronyms/)

Table of contents

* [System Specifications](#system-specifications)
* [System Performance](#system-performance)
* [Interconnect](#interconnect)
  + [NIC](#nic)
* [Node Specifications](#node-specifications)
  + [GPU nodes](#gpu-nodes)
  + [CPU Nodes](#cpu-nodes)
  + [Login nodes](#login-nodes)
* [Storage](#storage)

# Perlmutter Architecture[¶](#perlmutter-architecture "Permanent link")

![PerlmutterCabinetsFinal](../images/PerlmutterCabinetsFinal.jpg)

Perlmutter is a HPE (Hewlett Packard Enterprise) Cray EX supercomputer, named in honor of [Saul Perlmutter](https://en.wikipedia.org/wiki/Saul_Perlmutter), an astrophysicist at Berkeley Lab who shared the 2011 Nobel Prize in Physics for his contributions to research showing that the expansion of the universe is accelerating. Dr. Perlmutter has been a NERSC user for many years, and part of his Nobel Prize-winning work was carried out on NERSC machines and the system name reflects and highlights NERSC's commitment to advancing scientific research.

Perlmutter, based on the HPE Cray Shasta platform, is a heterogeneous system comprised of 3,072 CPU-only and 1,792 GPU-accelerated nodes.

## System Specifications[¶](#system-specifications "Permanent link")

| Partition | # of nodes | CPU | GPU | NIC |
| --- | --- | --- | --- | --- |
| GPU | 1536 | 1x [AMD EPYC 7763](https://www.amd.com/en/products/cpu/amd-epyc-7763) | 4x [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) (40GB) | 4x [HPE Slingshot 11](https://www.hpe.com/us/en/compute/hpc/slingshot-interconnect.html) |
|  | 256 | 1x [AMD EPYC 7763](https://www.amd.com/en/products/cpu/amd-epyc-7763) | 4x [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) (80GB) | 4x [HPE Slingshot 11](https://www.hpe.com/us/en/compute/hpc/slingshot-interconnect.html) |
| CPU | 3072 | 2x [AMD EPYC 7763](https://www.amd.com/en/products/cpu/amd-epyc-7763) | - | 1x [HPE Slingshot 11](https://www.hpe.com/us/en/compute/hpc/slingshot-interconnect.html) |
| Login | 40 | 2x [AMD EPYC 7713](https://www.amd.com/en/products/cpu/amd-epyc-7713) | 1x [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) (40GB) | - |

## System Performance[¶](#system-performance "Permanent link")

| Partition | Type | Aggregate Peak FP64 (PFLOPS) | Aggregate Memory (TB) |
| --- | --- | --- | --- |
| GPU | CPU | 4.5 | 448 |
| GPU | GPU | 69.5 tensor: 140 | 328 |
| CPU | CPU | 15.4 | 1536 |

## Interconnect[¶](#interconnect "Permanent link")

The network has a 3-hop dragonfly topology.

* A GPU compute cabinet is segmented into 8 chassis, each containing 8 compute blades and 4 switch blades.
* A GPU compute blade contains 2 GPU-accelerated nodes.
* GPU-accelerated compute cabinets have Slingshot 11 interconnect fabric with HPE Cray's proprietary Cassini NICs.
* Each GPU-accelerated compute node is connected to 4 NICs.
* GPU cabinets contain 32 switch blade across two 16-switch Dragonfly groups.
* A CPU-only compute cabinet has 8 chassis, each containing 8 compute blades and 2 switch blades.
* A CPU-only compute blade contains 4 CPU nodes.
* Each CPU-only compute node is connected to 1 NIC.
* CPU-only cabinets contain one 16-switch Dragonfly group per cabinet.
* CPU compute cabinets have Slingshot 11 interconnect fabric with Cassini NICs.
* There is no backplane in the chassis to provide the network connections between the compute blades. Network connections are achieved by having the switch blades at the rear of the cabinet, providing the interconnection between the compute blades in the in the front side.
* A full all-to-all electrical network is provided within each group. All switches in a switch group are directly connected to all other switches in the group.
  + Copper Level 0 (L0) cables connect nodes to network switches. L0 cables carry two links and are split to provide two single link node connections. L0 links are called "host links" or "edge links".
  + Copper Level 1 (L1) cables are used to interconnect the switches within a group. The 16-switch groups are internally interconnected with two cables (four links) per switch pair. L1 links are called "group links" or "local links".
* Optical Level 2 (L2) cables interconnect groups within a subsystem (e.g., the compute subsystem consisting of compute nodes). L2 links are called "global links". Each optical cable carries two links per direction.
* L2 cables also interconnect subsystems - there are 3 subsystem on a HPE Cray EX system, each with its own dragonfly interconnect topology: compute, IO, and service subsystems.

| ![CPU/GPU compute chassis network diagram](../images/PMNodeNetworkConnections.png) |
| --- |
| Figure: (Top) Diagram of a single CPU compute chassis showing network switches and connection types. (Bottom) Diagram of a single GPU compute chassis. |

### NIC[¶](#nic "Permanent link")

* PCIe 4.0 connection to nodes
* 200G (25 GB/s) bandwidth
* 1x NIC per node for CPU partition
* 4x NICs per node for GPU partition

## Node Specifications[¶](#node-specifications "Permanent link")

### GPU nodes[¶](#gpu-nodes "Permanent link")

![Perlmutter GPU nodes](../images/perlmutter_gpu_node_p2_c.png)

![A100's NVLink](../images/nvidia-nvlink-a100-diagram-dlt-2.svg)

* Single [AMD EPYC 7763](https://www.amd.com/en/products/cpu/amd-epyc-7763) (Milan) CPU
* 64 cores per CPU
* Four [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) (Ampere) GPUs
* PCIe 4.0 GPU-CPU connection
* PCIe 4.0 NIC-CPU connection
* 4 [HPE Slingshot 11](https://www.hpe.com/us/en/compute/hpc/slingshot-interconnect.html) NICs
* 256 GB of DDR4 DRAM
* 204.8 GB/s CPU memory bandwidth
* 1555 GB/s GPU memory bandwidth per 40GB HBM2 GPU and 2039 GB/s GPU memory bandwidth per 80GB HBM2e GPU
* 4 third generation NVLink connections between each pair of GPUs
  + 25 GB/s/direction for each link

| Data type | GPU TFLOPS |
| --- | --- |
| FP32 | 19.5 |
| FP64 | 9.7 |
| TF32 (tensor) | 155.9 |
| FP16 (tensor) | 311.9 |
| FP64 (tensor) | 19.5 |

Further details:

* [A100 whitepaper](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/nvidia-ampere-architecture-whitepaper.pdf)
* [NVIDIA Ampere Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/)

### CPU Nodes[¶](#cpu-nodes "Permanent link")

![Perlmutter CPU nodes](../images/perlmutter_cpu_node.png)

* 2x [AMD EPYC 7763](https://www.amd.com/en/products/cpu/amd-epyc-7763) (Milan) CPUs
* 64 cores per CPU
* AVX2 instruction set
* 512 GB of DDR4 memory total
* 204.8 GB/s memory bandwidth per CPU
* 1x [HPE Slingshot 11](https://www.hpe.com/us/en/compute/hpc/slingshot-interconnect.html) NIC
* PCIe 4.0 NIC-CPU connection
* 39.2 GFlops per core
* 2.51 TFlops per socket
* 4 NUMA domains per socket (NPS=4)

Further details:

* [High Performance Computing (HPC) Tuning Guide for AMD EPYC 7003 Series Processors](https://www.amd.com/system/files/documents/high-performance-computing-tuning-guide-amd-epyc7003-series-processors.pdf).

### Login nodes[¶](#login-nodes "Permanent link")

* 2x [AMD EPYC 7713](https://www.amd.com/en/products/cpu/amd-epyc-7713) (Milan) CPUs
* 512 GB of memory in total
* 1x [NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/) GPU with 40 GiB of memory
* Two NICs connected via PCIe 4.0
* 960 GB of local SSD scratch
* 1 NUMA node per socket (NPS=1)

## Storage[¶](#storage "Permanent link")

The Perlmutter Scratch File System is an all-flash file system. It has 44 PB of disk space, an aggregate bandwidth of 7.8 TB/sec (reads) and 6.6 TB/s (writes), and 4 million IOPS (4 KiB random). It has 16 MDS (metadata servers) and 370 I/O servers called OSSs.

[Perlmutter SCRATCH Usage details](../../../filesystems/perlmutter-scratch/)

[![LBL Home](/assets/images/lbl_logo.png)](https://www.lbl.gov/ "LBL")   [![DOE Office of Science Home](/assets/images/doe_logo.png)](https://science.energy.gov "DOE Office of Science")

[Acknowledge NERSC](../../../accounts/policy/#acknowledge-use-of-nersc-resources "Acknowledge NERSC")
 [Privacy and Security Notice](https://www.lbl.gov/disclaimers/ "Privacy and Security Notice")
 [Contact Us](https://www.nersc.gov/users#e74 "Contact Us")
