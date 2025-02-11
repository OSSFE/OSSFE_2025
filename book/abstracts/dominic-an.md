---
title: 'An open-source python package for atomic kinetics studies in tokamak plasmas'
authors:
  - name: Dominic Power
    affiliations:
      - LLNL
  - name: Stefan Mijin
    affiliations:
      - UKAEA
  - name: Kevin Verhaegh
    affiliations:
      - TUV
  - name: Fulvio Militello
    affiliations:
      - UKAEA
  - name: Robert J. Kingham
    affiliations:
      - Imperial College London
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Plasma-impurity reaction rates are a crucial part of modelling tokamak plasmas, particularly in the scrape-off layer, where they play an important role in determining particle balance, impurity transport, energy flows, etc. Commonly used datasets for this task, such as ADAS [1], assume Maxwellian electrons, but this assumption may be violated due to non-local parallel transport [2]. There is a lack of alternatives to ADAS which are both open source and can treat non-Maxwellian electrons. For this reason, SIKE has been developed (Scrape-off layer Impurities with Kinetic Electrons): an open-source python package for atomic kinetics studies. Generating high-quality atomic data is a delicate and time-consuming task, and is largely independent from solving the rate equations, so SIKE has in-built separation between the rate equation solver and the atomic data. This, along with a straightforward JSON schema for the input data, facilitates iterative improvement in the underlying data and improves the transparency of generated outputs.  

[1] https://open.adas.ac.uk/
[2] D. Power et al 2023 Nucl.Fusion 63 086013

# Repository
https://github.com/plasdom/sike

