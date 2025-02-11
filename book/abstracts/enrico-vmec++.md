---
title: 'VMEC++: a Python-friendly VMEC reimplementation in C++'
authors:
  - name: Enrico Guiraud
    affiliations:
      - Proxima Fusion
  - name: Jonathan Schilling
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

VMEC++ is a Python-friendly reimplementation in C++ of the Variational Moments Equilibrium Code (VMEC), a fixed- and free-boundary ideal-MHD 3D equilibrium solver for stellarators and tokamaks. The first VMEC implementation was written by Steven P. Hirshman and colleagues in the 1980s and 1990s and its latest Fortran incarnation (PARVMEC, https://github.com/ORNL-Fusion/PARVMEC) is widely used in stellarator optimization systems.

Our work improves on previous implementations with regard to various critical aspects: special care has been put in providing an idiomatic Python experience, from installation to actual usage. VMEC++ has a zero-crash policy; it supports inputs in the original INDATA format as well as friendlier JSON files. VMEC++ execution times are typically less than or equal to previous implementations, and time to convergence can be decreased dramatically by leveraging a hot-restart feature: by providing the output of a VMEC++ run as initial state for a subsequent one, VMEC++ is initialized using the previously converged equilibrium. This can dramatically decrease runtimes when running on many similar configurations as it typically happens in stellarator optimization pipelines.
This contribution will present the open-source VMEC++ package publicly for the first time, including relevant performance benchmarks and a discussion of the methodology used to verify close numerical compatibility with previous implementations.

# Repository
https://github.com/proximafusion/vmecpp

