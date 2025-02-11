---
title: 'FREEGSNKE: A PURE-PYTHON EVOLUTIVE EQUILIBRIUM CODE FOR TOKAMAK PLASMAS'
authors:
  - name: Nicola C. Amorisco
    affiliations:
      - UKAEA
  - name: George K. Holt
    affiliations:
      - STFC Hartree Centre
  - name: Kamran Pentland
    affiliations:
      - UKAEA
  - name: Adriano Agnello
    affiliations:
      - STFC Hartree Centre
  - name: Alasdair Ross
    affiliations:
      - STFC Hartree Centre
  - name: Matthijs Mars
    affiliations:
      - UCL
  - name: Stan Pamela
    affiliations:
      - UKAEA
  - name: James Buchanan
    affiliations:
      - UKAEA.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

We present FreeGSNKE, a pure-Python, open-source, finite-difference simulation code for the two-dimensional dynamic plasma equilibrium problem. It builds on FreeGS, introducing i) a static Grad-Shafranov solver, based on the Newton-Krylov (NK) method; ii) solvers for the evolutive problem, also based on the NK method. Both solvers have been validated against MAST-U equilibria: the static solver against equilibria from Fiesta and EFIT++ and the evolutive solver against measured poloidal field coil currents and plasma shape targets. FreeGSNKE is currently being used at MAST-U to support modelling strongly shaped plasmas and has been released (https://github.com/FusionComputingLab/freegsnke) under the GNU Lesser General Public License version 3. 
One aim of FreeGSNKE is to lower the entry barrier for those seeking to deploy machine-learning-based approaches for plasma control. Entirely written in Python, it can seamlessly integrate with established machine-learning libraries and algorithms, overcoming the need for cross-language binders or socket interfaces for multi-language interaction. For the same reasons, FreeGSNKE is a stateful code, which is advantageous in control, design, and reinforcement learning studies. Directions of development currently being pursued include compatibility with IMAS structures, JAX-ification of the core solvers to enable auto-differentiability, implementation of the current diffusion equation, and coupling with transport solvers. 

# Repository
https://github.com/FusionComputingLab/freegsnke

