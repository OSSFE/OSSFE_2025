---
title: 'GEOUNED: CSG geometry production for fusion applications'
authors:
  - name: Aljaz Kolsek
    affiliations:
      - Fusion for Energy
  - name: Juan Pablo Catalan
    affiliations:
      - UNED
  - name: Patrick Sauvan
    affiliations:
      - UNED
  - name: Jonathan Shimwell
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The GEOUNED code is a tool to convert CAD models, defined using the B-rep approach, into Monte Carlo radiation transport models based on CSG approach. Currently supported Monte Carlo codes are OpenMC, PHITS, Serpent and MCNP. The tool is a python3 module package that uses FreeCAD 1.0.0 as a python API, based on OPENCASCADE CAD engine. It incorporates standard features commonly found in conversion tools, including decomposition, conversion, reverse conversion (i.e., from CSG to CAD) and an advanced automatic void generation.

In the recent months the GEOUNED tool has undergone significant refurbishment and adaptation to the industry standards. The code has been refactored to eliminate the use of global variable states, while the packaging and the distribution has been set up via conda-forge and PyPi to simplify the installation process for the users. The ever-evolving documentation, deployed on Github pages, has replaced the static PDF manual. Furthermore, Continuous Integration (CI) pipelines with automated tests have been set up, which on pull requests install GEOUNED and OpenMC, translate numerous CAD models to CSG description and run both the volume calculations and the lost particle tests using OpenMC.

The GEOUNED tool has become a crucial part of the workflow for nuclear analyses. Its recent application can be observed in the production of the Monte Carlo model of the Accelerator Systems of DONES facility, complete Equatorial Port #16 of ITER or Monte Carlo model of the HELIAS reactor, the European DEMO concept for stellarators.

# Github repository
https://github.com/GEOUNED-org/GEOUNED

