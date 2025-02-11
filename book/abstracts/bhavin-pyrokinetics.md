---
title: 'Pyrokinetics - A python library to standardise gyrokinetic analysis'
authors:
  - name: Bhavin Patel
    affiliations:
      - UKAEA
  - name: Peter Hill
    affiliations:
      - University of York
  - name: Liam Pattinson
    affiliations:
      - University of York
  - name: Arkaprava Bokshi
    affiliations:
      - University of York
  - name: Francis Casson
    affiliations:
      - UKAEA
  - name: David Dickinson
    affiliations:
      - University of York
  - name: Harry Dudding
    affiliations:
      - UKAEA
  - name: Maurizio Giacomin
    affiliations:
      - Università degli Studi di Padova
  - name: David Hatch
    affiliations:
      - University of Texas Austin
  - name: Aaron Ho
    affiliations:
      - MIT
  - name: Daniel Kennedy
    affiliations:
      - UKAEA
  - name: Tom Neiser
    affiliations:
      - General Atomics
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Turbulence can be a major cause of particle and heat losses in magnetically-confined fusion plasmas, making its mitigation critical for achieving fusion. Gyrokinetic modelling aims to quantify turbulent transport and identifies its drivers, requiring robust, standardised tools for reliable predictions. Pyrokinetics is a Python-based project designed to simplify and standardise gyrokinetic analysis. A wide variety of gyrokinetic solvers are used in practice, each utilising different input file formats and normalisations for plasma parameters such as densities, temperatures, velocities, and magnetic fields and each have bespoke output data, which makes cross-code comparisons non-trivial. Pyrokinetics will automatically handle the conversions of inputs and outputs, enabling seamless benchmarking across codes. Using xarray and pint, Pyrokinetics consolidates multidimensional outputs into a unified, standardised format for consistent comparisons. The tool offers advanced features like automated input generation, derived outputs (e.g., linear growth rates), and compatibility with Python’s rich ecosystem for analyses like parameter scans and machine learning models. Additionally, it includes sophisticated diagnostics (e.g., Poincaré plots, bicoherence analysis, ideal ballooning analysis, synthetic turbulence diagnostics, quasilinear modelling) and supports IMAS, the standard metadata schema used by ITER, fostering broader interoperability and the potential for an international gyrokinetic database. Pyrokinetics enhances accessibility, streamlines analysis, and boosts confidence in gyrokinetic modelling tools, advancing fusion research efforts.

# Repository
https://github.com/pyro-kinetics/pyrokinetics

