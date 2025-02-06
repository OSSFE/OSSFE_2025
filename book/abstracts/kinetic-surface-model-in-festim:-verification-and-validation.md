---
title: 'Kinetic surface model in FESTIM: Verification and Validation'
authors:
  - name: Vladimir Kulagin
    affiliations:
      - National Research Nuclear University MEPhI
  - name: Vladimir Kulagin
    affiliations:
      - National Research Nuclear University MEPhI
  - name: Remi Delaporte-Mathurin
    affiliations:
      - Massachusetts Institute of Technology
  - name: Remi Delaporte-Mathurin
    affiliations:
      - Massachusetts Institute of Technology
  - name: Etienne Hodille
    affiliations:
      - CEA IRFM
  - name: Etienne Hodille
    affiliations:
      - CEA IRFM
  - name: Mikhail Zibrov
    affiliations:
      - Max Planck Institute for Plasma Physics
  - name: Mikhail Zibrov
    affiliations:
      - Max Planck Institute for Plasma Physics
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Accumulation and transport of hydrogen (H) in materials are topical subjects of study in various research fields (nuclear fusion, hydrogen storage and transport, material science, etc.). Numerical modelling of H dynamics plays an important role in these fields allowing to perform prognostic estimations, validate theoretical models and construct new predictive ones. FESTIM (Finite Element Simulation of Tritium In Materials) [1] is a flexible open-source code developed for simulating the H transport in materials. For years, it has been successfully applied to study the H transport for fusion-related applications.

Before the v1.3 release, the physics basis of FESTIM covered a wide range of bulk and surface processes, implemented dependent on the concentration of solute H. For the latter ones, this is a simplification valid when surface processes are fast compared to bulk ones, so the concentrations of adsorbed and absorbed H are in equilibrium. However, there are conditions when the evolution of the adsorbed H concentration should be taken into account [2]. A representative example is the H retention in a material exposed to a low-energy atomic/molecular flux. When the energy of incident particles is not high enough to overcome the surface barrier for implantation, incoming particles can stick to a surface and only then be absorbed into the bulk.

In the recent release of FESTIM, a kinetic surface model was introduced, allowing users to consider the temporal evolution of the H surface concentration in H transport simulations. To ensure the correctness of the model and provide the reliability to the users, the model underwent extensive verification and validation. In this work, the correctness of the implementation is first proven using the method of manufactured solutions. Then, reliability of the model is demonstrated by reproducing four experimental cases on the dynamics of hydrogen isotope retention in different materials. An additional cross-code comparison with two other simulation packages, TESSIM-X [2] and MHIMS [3], shows an excellent agreement and strengthens the validity of the model.
 
References:
[1] R. Delaporte-Mathurin, J. Dark, G. Ferrero et al., International Journal of Hydrogen Energy 63, 786 (2024)
[2] K. Schmid, M. Zibrov, Nuclear Fusion 61, 086008 (2021)
[3] E. Hodille, B. Pavec, J. Denis, et al., Nuclear Fusion 64, 046022 (2024)

# Github repository
https://github.com/KulaginVladimir/FESTIM-SurfaceKinetics-Validation

