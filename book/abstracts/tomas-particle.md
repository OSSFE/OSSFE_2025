---
title: 'Particle transport and radiation modeling by AURORA toolbox'
authors:
  - name: Tomas Odstrcil
    affiliations:
      - General Atomics
  - name: Francesco Sciortino
    affiliations:
      - Proxima Fusion
  - name: A. Zito
    affiliations:
      - MPI-IPP
  - name: D. Fajardo
    affiliations:
      - MPI-IPP
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Aurora is a package to simulate impurity transport and radiation in magnetically-confined plasmas. It includes a 1.5D impurity transport forward model which inherits many of the methods from the historical STRAHL code and has been thoroughly benchmarked with it. It also offers routines to analyze neutral states of hydrogen isotopes, both from the edge of  plasmas and from neutral beam injection. The package includes a public release of the Fast and Accurate Collisional Impurity Transport (FACIT) model for the calculation of neoclassical transport coefficients. Aurora’s code is mostly written in Python 3 and Fortran 90. A Julia interface has also recently been added. The package enables radiation calculations using ADAS atomic rates, which can easily be applied to the output of Aurora’s own forward model. 

# Repository
https://github.com/fsciortino/Aurora

