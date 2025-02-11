---
title: 'An automated pipeline from powerplant concept to parametric neutronics model in Bluemira'
authors:
  - name: Oliver Funk
    affiliations:
      - UKAEA
  - name: Jame Cook
    affiliations:
      - UKAEA
  - name: Ocean Wong
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Bluemira is an open-source, integrated, interdisciplinary design tool for future fusion reactors. With Bluemira, a modeller or engineer can rapidly explore the design space for many aspects of a fusion reactor concept. 

Often, of particular interest is the effect differing plasma properties, geometries and materials have on quantities caused by neutron radiation, such as the tritium breeding ratio, displacement per atom, heat flux and more. 

To explore these quantities, neutronics simulations must be run. However, converting CAD to neutronics-ready models often involves numerous time-consuming steps, each demanding manual input to execute. 

In this work, we demonstrate a pipeline that automates this conversion process. Starting with a Bluemira design run and ending in a DAGMC model ready for use in a neutronics code such as OpenMC. 

This automation creates an effective parametric neutronics model generation tool and allows users to explore the neutronics design space using Bluemira rapidly. 

# Repository
https://github.com/Fusion-Power-Plant-Framework/bluemira

