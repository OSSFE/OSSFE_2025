---
title: 'An Open-Source Workflow for Multi-Physics Analysis of Tritium Breeder Blankets'
authors:
  - name: Alexandre Sureda
    affiliations:
      - IDOM
  - name: Juan Diego Iberico
    affiliations:
      - IDOM
  - name: Marcel Walkington
    affiliations:
      - IDOM
  - name: Fernando Scarafia
    affiliations:
      - IDOM
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The efficient and accurate design of tritium breeder blankets is essential for the success of nuclear fusion reactors, particularly in achieving optimal performance and safety. This study presents an open-source workflow that integrates parametric geometry generation, meshing, and multiphysics simulation tools to analyze tritium breeder blanket architectures, specifically the Helium-Cooled Pebble Bed (HCPB), Helium-Cooled Lithium Lead (HCLL), and Dual-Coolant Lead–Lithium (DCLL) designs.

The workflow begins with parametric geometry modeling, allowing for flexible design variations tailored to specific requirements. The generated geometries are meshed using Salome, ensuring the creation of high-quality, simulation-ready grids. Multiphysics analyses are performed using the Fusion ENergy Integrated multiphysi-X (FENIX) code developed by Idaho National Laboratory. This software integrates neutronics simulations using OpenMC, thermal-hydraulics, and thermomechanics to comprehensively evaluate the performance of these systems under fusion reactor conditions. Key outputs include neutronic heat deposition, tritium breeding ratio (TBR), displacement per atom (DPA), thermal performance, structural integrity, and coolant behavior within the blanket modules.

This study demonstrates the capability of the proposed open-source workflow to address the challenges posed by the multiphysics nature of breeder blanket analysis, providing a reproducible and cost-effective methodology for advancing fusion technology. The results offer critical insights into the performance of HCPB, HCLL, and DCLL designs and provide guidance for optimizing blanket architectures to meet the stringent requirements of future fusion reactors.

# Repository
https://github.com/idaholab/fenix

