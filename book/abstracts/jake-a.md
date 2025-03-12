---
title: 'A Complete Open Source Workflow for CAD Based Reactor Neutronics with Unstructured Mesh Tallying'
authors:
  - name: Jake Harter
    affiliations:
      - Marathon Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Neutronics analysis is an important tool within the fusion industry, providing insights on the effects of neutron radiation within fusion reactors to inform future design, material, and safety choices. Neutronics analysis typically takes the form of Monte Carlo particle transport simulations using codes such as MCNP, Tripoli and OpenMC. Whilst there are many open source tools that can be used in Monte Carlo neutronics workflows there are no readily available end to end open source workflows that support CAD geometry and unstructured mesh tallying. This presentation details the development and use of a complete open source workflow using OpenMC that is easily deployable via docker. When used to perform neutronics analysis of the ARC reactor this workflow produced benchmark results comparable to the recent paper by Pettinari et al.

# Repository
https://github.com/jakemarathon/neutronics_workflow
