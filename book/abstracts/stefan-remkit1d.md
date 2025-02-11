---
title: 'ReMKiT1D - Designing a novel framework for reactive multifluid and kinetic model development for the tokamak Scrape-Off Layer'
authors:
  - name: Stefan Mijin
    affiliations:
      - UKAEA
  - name: Dominic Power
    affiliations:
      - LLNL
  - name: Alfie Adhemar
    affiliations:
      - Imperial College London, Sid Leigh, UKAEA
  - name: Ryan Holden
    affiliations:
      - University of Surrey
  - name: William Hornsby
    affiliations:
      - UKAEA
  - name: David Moulton
    affiliations:
      - UKAEA
  - name: Fulvio Militello
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

From 1D fluid model simulations of detachment [1] to various kinetic models [2,3,4], simulations of parallel transport along open field lines in the tokamak Scrape-Off Layer have produced insight into the complexities of divertor physics. Most existing approaches focus on a specific set of equations tailored to a subset of problems. While this focused approach has produced a massive number of important physical results, many applications, such as reduced modelling for machine learning and control, require the equations to be frequently and easily modified, while keeping all of the complexities of the models in check. As such, a flexible user-friendly framework is desirable. 

This contribution aims to present our attempt at such a framework - ReMKiT1D (Reactive Multifluid and Kinetic Transport in 1D)[5]. ReMKiT1D focuses on enabling the solution of stiff systems of 1D fluid equations with support for coupling kinetic electron effects and for reactive physics. The open-source software is composed of a Modern Fortran backend and a Python interface that enables flexibility and rapid iteration in model development. In particular, the recent developments of v2.0.0 of the Python interface introduce Domain Specific Language elements, and the focus of this contribution will be both on the software design aspects of the backend and the v2.0.0 Python interface, as well as showcasing the ongoing physics-related exploitation of the framework.

This work used the ARCHER2 UK National Supercomputing Service (https://www.archer2.ac.uk).
This work has been part-funded by the EPSRC Energy Programme [grant number EP/W006839/1].

References:
[1] Dudson, B. D. et al. Plasma Phys. Control. Fusion, 61(6) (2019)
[2] Tskhakaya, D. et al. Contrib. Plasma Phys., 48(1–3), 89–93 (2008)
[3] Chankin, A. V. et al. Plasma Phys. Control. Fusion, 60 (2018)
[4] Mijin, S. et al. Plasma Phys. Control. Fusion, 62(9) (2020)
[5] Mijin, S. et al. Comp. Phys. Comm. 300 (2024)

# Repository
https://github.com/ukaea/ReMKiT1D-Python 

