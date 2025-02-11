---
title: 'Integrating OpenMC and PUMIPic to enable GPU Acceleration of Unstructured Mesh Tallies for Monte Carlo Transport Simulations'
authors:
  - name: Fuad Hasan
    affiliations:
      - Rensselaer Polytechnic Institute
  - name: George Wilke
    affiliations:
      - Princeton Plasma Physics Laboratory
  - name: Paul Romano
    affiliations:
      - Argonne National Laboratory
  - name: Patrick Shriwise
    affiliations:
      - Argonne National Laboratory
  - name: Michael Churchill
    affiliations:
      - Princeton Plasma Physics Laboratory
  - name: Cameron Smith
    affiliations:
      - Rensselaer Polytechnic Institute
  - name: Jacob Merson
    affiliations:
      - Rensselaer Polytechnic Institute
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Open-source software will play an outsized role in enabling the national academies ambitious goal to bring fusion power to the grid by 2035. Due to the highly specialized nature of fusion simulations, the closed-source software model that drives traditional computer-aided engineering (CAE) software companies will not be effective at addressing the diverse set of needs. Instead, the fusion sector needs tools that can be rapidly modified to take advantage of novel mathematical formulations and an evolving understanding of underlying plasma and material physics.

In recent years, the fusion community has made strides towards supporting CAD-based models that are not easily supported through hand-coded CSG trees in open-source transport simulations through tools such as OpenMC, DAGMC, and Degas2. However, fundamental challenges such as understanding neutral recycling, heating from 14MeV neutrons, and whole facility radiation dose calculations require new developments to support larger and more geometrically complex models. Although progress has been made in CAD based transport simulations using OpenMC with DAGMC, tallies on unstructured meshes remains a bottleneck. This talk addresses that bottleneck by integrating PUMIPic, a GPU accelerated library for hybrid particle and mesh calculations, into OpenMC. Using this approach, we demonstrate better scaling with both number of particles and number of elements on CPU and GPU based calculations on unstructured meshes.

This talk highlights the effectiveness of building upon the burgeoning open-source ecosystem in support of fusion power applications.

# Repository
https://github.com/SCOREC/pumi-pic, https://github.com/openmc-dev/openmc

