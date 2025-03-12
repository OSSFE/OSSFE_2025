---
title: 'The Open FUSION Toolkit: An open-source suite of fusion modeling tools for engineering, analysis, and education'
authors:
  - name: C. Hansen
    affiliations:
      - Columbia University
  - name: A. Battey
    affiliations:
      - Columbia University
  - name: A. Braun
    affiliations:
      - Columbia University
  - name: D. Burgess
    affiliations:
      - Columbia University
  - name: J. Fu
    affiliations:
      - Columbia University
  - name: S. Guizzo
    affiliations:
      - Columbia University
  - name: R. Lopez
    affiliations:
      - Columbia University
  - name: S. Miller
    affiliations:
      - Columbia University
  - name: A.O. Nelson
    affiliations:
      - Columbia University
  - name: M. Pharr
    affiliations:
      - Columbia University
  - name: A. Vergara
    affiliations:
      - Columbia University
  - name: C. Paz-Soldan
    affiliations:
      - Columbia University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The [Open FUSION Toolkit](https://github.com/hansec/OpenFUSIONToolkit) is an open-source suite of tools for fusion modeling with a focus on ease of use, tight integration with engineering workflows, and education. The present suite of physics tools include:
1. [TokaMaker](https://doi.org/10.1016/j.cpc.2024.109111): a 2D static and time-dependent Grad-Shafranov equilibrium tool designed as an user-friendly and open tool for design, control development and education
2. [ThinCurr](https://doi.org/10.48550/arXiv.2412.14962): a 3D thin-wall current modeling tool used to study currents in 3D device structures (eg. ports) and as an alternative to fourier-based current potential formulations in stellarator coil optimization,
3. [MUG](https://doi.org/10.1063/1.4917476): a 3D linear/nonlinear time-dependent MHD tool for plasma dynamics in arbitrary domains, and
4. [Marklin](https://doi.org/10.1088/1741-4326/abd41c): a 3D force-free, uniform  ideal MHD equilibrium solver. A common core provides capabilities to all tools, including: meshing from CAD models, scalable linear and nonlinear solvers, extensible finite element representations, parallelization via OpenMP+MPI, and 3D visualization. Core functionality is implemented in C/C++/Fortran with Python interfaces for interactive applications and scripting. This talk will present a summary of the toolkit (highlighting applications in each domain) and describe methods to support community adoption including: binary packaging, documentation, and code design.

Work supported by US DOE awards DE-SC0019239 and DE-SC0024898 and Commonwealth Fusion Systems

# Repository
https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit

