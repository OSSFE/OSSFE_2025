---
title: 'Surrogate Modelling of Classical and Quantum Electrodynamic Laser Plasma Simulations at Intensities Above 10^22 Wcm^-2'
authors:
  - name: Joel Adams
    affiliations:
      - University of York
  - name: Chris Ridgers
    affiliations:
      - University of York
  - name: Peter Hill
    affiliations:
      - University of York
  - name: Nathan Smith
    affiliations:
      - University of York
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

High-intensity laser-plasma interactions (10²²–10²⁴ W/cm²) offer a pathway to understanding ultra-relativistic plasma physics, compact particle accelerators, and extreme astrophysical conditions. However, accurately modelling these phenomena is computationally prohibitive, necessitating the development of efficient surrogate models.

This work focuses on creating surrogate models from 3D particle-in-cell simulations using the EPOCH framework. These models incorporate quantum electrodynamic (QED) processes, radiation reaction effects, and relativistic transparency to predict electron energy distributions and refine the equation of motion under extreme conditions. Gaussian Process Regression (GPR) serves as the foundation for these models, enabling predictions with uncertainty quantification.

Supporting this effort is the open-source Broad EPOCH Analysis Modules (BEAM) toolkit, which integrates tools like sdf-xarray for SDF file processing, epydeck for simulation input management, and epyscan for parameter space sampling. These tools streamline large-scale simulations, ensuring reproducibility and extensibility for the community.

This presentation will detail the surrogate modelling methodology, insights into laser absorption and QED effects, and the future development of the BEAM toolkit to enable active learning and higher-dimensional simulations. By accelerating simulation workflows, this work aims to support the growing network of international facilities exploring high-intensity laser-matter interactions.

# Github repository
https://github.com/PlasmaFAIR/sdf-xarray, https://github.com/PlasmaFAIR/epyscan, https://github.com/PlasmaFAIR/epydeck

