---
title: 'Facilitating Iterative Multi-physics Analysis of Fusion Components with Catbird'
authors:
  - name: Helen Brooks
    affiliations:
      - UK Atomic Energy Authority
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Reducing the minimal pathway and cost for delivering first-of-a-kind fusion power plants necessitates in-silico design and qualification. To ensure robustness of conclusions for any digital engineering framework, underlying multi-physics models must be subject to rigorous verification, validation and uncertainty quantification. To facilitate discovery of novel configurations in design parameters, and to identify experimental regimes which maximise information gain may entail employing advanced algorithms like active learning.  All such activities are inherently iterative, therefore processes containing any manual elements will become prohibitively labourious. It is therefore essential to facilitate automatic workflows utilizing a broad set of computational tools and capabilities. In this vein, we introduce an open source Python module, Catbird, which provides a generalized interface to the multi-physics platform, MOOSE. Catbird assembles Python objects from the MOOSE application’s input syntax with object attributes that include type checking, documentation, and translation to MOOSE input blocks. This natural integration with Python provides a form that is conducive to automatic iterative study with the MOOSE framework. In this contribution we present Catbird, and describe the set-up for a simple example problem. As indicative of potential applications, we consider tritium production and transport in a helium-cooled pebble bed breeder blanket and perform a sensitivity analysis over material properties. As a future outlook, we discuss considerations for improving the technological maturity and quality assurance of the software.

# Repository
https://github.com/helen-brooks/catbird

