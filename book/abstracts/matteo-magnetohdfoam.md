---
title: 'magnetoHDFoam:  a novel open-source OpenFOAM library for magnetohydrodynamics'
authors:
  - name: Matteo Lo Verso
    affiliations:
      - Politecnico di Milano
  - name: Carolina Introini
    affiliations:
      - Politecnico di Milano
  - name: Antonio Cammi
    affiliations:
      - Politecnico di Milano
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Magnetohydrodynamics (MHD) investigates the dynamics of electrically conducting fluids under the influence of a magnetic field. The complex interaction between magnetic fields and fluid dynamics presents a significant challenge for understanding the MHD phenomena occurring in magnetic confinement fusion as their nature is intrinsecally multiphysics. The current open-source OpenFOAM libraries are limited in their modelling capabilities to incompressible, isothermal, and laminar flows. This constraint has resulted in a demand for a comprehensive MHD tool capable of addressing the conditions relevant to fusion research, involving, for example, the confinement of thermonuclear plasmas and MHD effects occurring in liquid metal or molten salt blankets. This study introduces magnetoHDFoam, a novel OpenFOAM computational solver tailored for simulating intricate and realistic magnetohydrodynamic scenarios, including compressible, turbulent, buoyancy and thermal effects. The solver is verified by comparing its performance against well-established benchmark tests (for which analytical solutions are provided in MHD literature), representing MHD phenomena within fusion reactors, focusing on lead-lithium flows subjected to magnetic fields. The results demonstrate strong agreement with theoretical expectations, confirming the accuracy of the library in capturing the effects of magnetic fields on thermohydraulics. Consequently, this library represents a valuable computational tool for advancing the comprehension of MHD phenomena within the context of nuclear fusion research. Future works will address a validation phase as soon as suitable experimental data become available.

# Repository
https://github.com/ERMETE-Lab/MHD-magnetoHDFoam

