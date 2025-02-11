---
title: 'Multiphysics Open Source Workflow for Conceptual Design of Inertial Fusion Reactors'
authors:
  - name: Alexandre Sureda Croguennoc
    affiliations:
      - IDOM UK Ltd
  - name: Juan Diego Iberico Leonardo
    affiliations:
      - IDOM UK Ltd
  - name: Fernando Scarafia
    affiliations:
      - IDOM UK Ltd
  - name: Javier Monteliu
    affiliations:
      - First Light Fusion
  - name: Jorge Fradera Fernandez
    affiliations:
      - IDOM Consulting, Engineering, Architecture
  - name: Patricio Alberto
    affiliations:
      - IDOM Consulting, Engineering, Architecture
  - name: Jonathan Shimwell
    affiliations:
      - First Light Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This work presents an open-source workflow for the conceptual design of inertial fusion reactors, integrating neutronics, thermomechanics, and fluid dynamics through a consistent and automated approach. Neutronics simulations are conducted using the Fusion ENergy Integrated multiphysi-X (FENIX) code developed by Idaho National Laboratories, which combines OpenMC via the Cardinal framework for neutron transport calculations and MOOSE for finite element thermomechanical analysis. A custom Python package is used to generate parametric reactor geometries, providing both constructive solid geometry (CSG) models for efficient sensitivity analyses and detailed CAD models using CadQuery. The CAD geometries are subsequently converted to DAGMC to enable detailed neutron transport simulations while ensuring geometrical consistency between the neutronics and thermomechanical workflows.

The neutronics analysis provides key metrics, including Tritium Breeding Ratio (TBR), displacement per atom (DPA), and heating deposition. The heating deposition results are then integrated into the thermomechanical workflow within FENIX, where thermal and structural analyses are performed to evaluate the reactor’s response to operational conditions. These analyses are validated against results obtained using commercial tools such as Abaqus and open-source alternatives like Code_Aster.

Thermal-hydraulics simulations are performed using a custom system-level code to analyze the performance of the coolant system, while computational fluid dynamics (CFD) simulations are used to study the behavior and stabilization of lithium jets, which serve as a protective layer for the reactor chamber. This workflow provides a comprehensive methodology for the integrated analysis of inertial fusion reactors, with a focus on establishing consistent processes and supporting future iterations of the conceptual design.


