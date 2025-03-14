---
title: 'Open-source MHD modelling of turbulent flow in a molten salt breeding blanket'
authors:
  - name: M. Caravello
    affiliations:
      - NEMO group, Dipartimento Energia, Politecnico di Torino, 10129 Torino, Italy
  - name: A. Froio
    affiliations:
      - NEMO group, Dipartimento Energia, Politecnico di Torino, 10129 Torino, Italy
  - name: N. Mancini
    affiliations:
      - Research & Technological Innovation Department, Eni S.p.A., 20097 San Donato Milanese (MI), Italy
  - name: F. Podenzani
    affiliations:
      - Research & Technological Innovation Department, Eni S.p.A., 20097 San Donato Milanese (MI), Italy
  - name: R. Zanino
    affiliations:
      - NEMO group, Dipartimento Energia, Politecnico di Torino, 10129 Torino, Italy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Molten salt (MS) has emerged as a promising multi-functional material for the breeding blanket in nuclear fusion reactors, due to its radiation resistance and good heat transfer capabilities, allowing it to serve simultaneously as a breeder, neutron multiplier, and coolant. However, the flow of molten salt is affected by magnetohydrodynamic (MHD) effects in the presence of magnetic fields, leading to complex flow patterns and posing challenges in the design of the reactor cooling system. Most commercial CFD software still rely on purely hydrodynamic models, which do not directly account for Lorentz forces affecting turbulent phenomena.
In addition to addressing these MHD effects, this work introduces a neutronic module that implements diffusion equations for neutrons and is adapted for photons to account for power deposition, mimicking reactor conditions. This integration allows for a more accurate representation of the interaction between the neutron flux and the MS flow, critical for assessing power deposition profiles and their effects on the thermal and fluid dynamics within the blanket.
The proposed model is implemented in the open-source OpenFOAM code. A comparison of the performance of the modified two-equation k-ε model and Reynolds Stress Model (RSM) is presented.


# Repository
https://github.com/NEMO-Group/nemoFoam

