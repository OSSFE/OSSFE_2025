---
title: 'Verification, Validation, and Demonstration of the MOOSE-based Tritium Migration Analysis Program, Version 8 (TMAP8) Application for Fusion Systems.'
authors:
  - name: Pierre-Clément A. Simon
    affiliations:
      - Idaho National Laboratory
  - name: Pierre-Clément A. Simon
    affiliations:
      - Idaho National Laboratory
  - name: Casey T. Icenhour
    affiliations:
      - Idaho National Laboratory
  - name: Casey T. Icenhour
    affiliations:
      - Idaho National Laboratory
  - name: Alexander Lindsay
    affiliations:
      - Idaho National Laboratory
  - name: Alexander Lindsay
    affiliations:
      - Idaho National Laboratory
  - name: Gyanender Singh
    affiliations:
      - Idaho National Laboratory
  - name: Gyanender Singh
    affiliations:
      - Idaho National Laboratory
  - name: Chaitanya Bhave
    affiliations:
      - Idaho National Laboratory
  - name: Chaitanya Bhave
    affiliations:
      - Idaho National Laboratory
  - name: Lin Yang
    affiliations:
      - Idaho National Laboratory
  - name: Lin Yang
    affiliations:
      - Idaho National Laboratory
  - name: Adriaan Riet
    affiliations:
      - Idaho National Laboratory
  - name: Adriaan Riet
    affiliations:
      - Idaho National Laboratory
  - name: Paul Humrickhouse
    affiliations:
      - Oak Ridge National Laboratory
  - name: Paul Humrickhouse
    affiliations:
      - Oak Ridge National Laboratory
  - name: Masashi Shimada
    affiliations:
      - Idaho National Laboratory
  - name: Masashi Shimada
    affiliations:
      - Idaho National Laboratory
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Tritium Migration Analysis Program (TMAP), developed by Idaho National Laboratory (INL), has been a central tool for analyzing tritium behavior in fusion reactor systems. Previous versions, TMAP4 and TMAP7, facilitated one-dimensional thermal and mass-diffusive transport and trapping calculations. However, their capabilities were limited. For example, both could only model one dimensional domains and were limited in the number of trapping site populations (1 for TMAP4, and 3 for TMAP7). Moreover, they did not easily lend themselves to multiphysics simulations, which limited the accuracy of their predictions. To alleviate these constraints, TMAP8, built on the Multiphysics Object-Oriented Simulation Environment (MOOSE) framework, offers high-fidelity modeling and simulation of tritium transport, enhancing previous capabilities and enabling more efficient design and safety analysis of fusion pilot plants.
TMAP4 and TMAP7 capabilities were thoroughly tested in verification and validation (V&V) cases. Following standard engineering terminology, “Verification” is the process of determining that a computational model accurately represents the underlying mathematical model and its solution. “Validation” is the process of determining the degree to which a model is an accurate representation of the real world from the perspective of the intended uses of the model – requiring comparison against experimental data. TMAP8 has been tested on the same suite of V&V cases to build trust and demonstrate its accuracy in modeling hydrogen isotope transport. These cases are an integral part of the high software quality standards set for TMAP8, which is Nuclear Quality Assurance, Level 1 (NQA-1) compliant. 
Moreover, TMAP8 is open-source, is thoroughly documented, and uses a flexible license that enables effective collaborations, including public-private partnerships. The TMAP8 online documentation describes all its capabilities, all V&V cases with the associated results and input files, and clear instructions on how to get started. The documentation also includes example and demonstration cases beyond what TMAP4 and TMAP7 were capable of doing, including simulating a complete tritium fuel cycle, two- and three-dimensional tritium migration and heat transfer within a divertor monoblock, pore scale simulations in breeder materials, and others. These cases showcase TMAP8’s ability to retain TMAP4 and TMAP7 essential features while significantly expanding capabilities for complex multiphysics and multiscale analyses on high performance computers. Despite these state-of-the-art capabilities, we will also show that TMAP8 is easy to use and is suitable for different expertise levels.

# Github repository
https://github.com/idaholab/TMAP8

