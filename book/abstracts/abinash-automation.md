---
title: 'Automation of Multi-Physics Simulations: Coupling OpenFOAM and OpenMC for Fusion Application'
authors:
  - name: Abinash Manikandan
    affiliations:
      - nTtauDigital
  - name: Noe Adepoju
    affiliations:
      - nTtauDigital
  - name: Megan Crocker
    affiliations:
      - nTtauDigital
  - name: Dominic Longhorn
    affiliations:
      - nTtauDigital
  - name: Luis Garcia
    affiliations:
      - nTtauDigital
  - name: Max Moreland
    affiliations:
      - nTtauDigital
  - name: Omer Muhammad
    affiliations:
      - nTtauDigital
  - name: Frank Schoofs
    affiliations:
      - nTtauDigital
  - name: Sophie Sharpe
    affiliations:
      - nTtauDigital
  - name: Simon Woodruff
    affiliations:
      - nTtau Digital Ltd
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This study presents the development of an automated workflow for coupling OpenFOAM and OpenMC to solve complex multi-physics problems involving Computational Fluid Dynamics (CFD) and neutron transport simulations. The process begins with extracting CFD – fluid flow mesh domain including cell centers, coordinates, volume-phase fractions, and temperatures, which are then transferred into OpenMC for defining geometry and material density. Cells in OpenMC are reconstructed using the extracted cell data from OpenFOAM, ensuring a consistent mesh between the two tools. Neutron transport simulations are conducted in OpenMC to generate spatial heating profiles, which are used to calculate temperature increases at each cell center. These updated temperature fields are then fed back into OpenFOAM using the nearest-cell approach to update the flow conditions. To streamline this iterative process, a Python script developed by the authors automates the generation of the setFieldsDict file in OpenFOAM. The results demonstrate that this workflow directly addresses the challenge of accurately capturing the impact of temperature changes on a fluid flow due to neutron bombardment which is a common phenomena in fusion reactors. By providing a scalable, efficient, and automated solution, it advances the fidelity of nuclear system modelling, benefiting reactor designers, researchers, and the broader nuclear engineering community.

