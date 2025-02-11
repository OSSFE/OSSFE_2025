---
title: 'Applying the Bluemira Fusion Power Plant Framework to Poloidal Field Coilset and Divertor Design'
authors:
  - name: Georgina Graham
    affiliations:
      - UKAEA
  - name: Matthew Bluteau
    affiliations:
      - UKAEA
  - name: Matti Coleman
    affiliations:
      - UKAEA
  - name: James Cook
    affiliations:
      - UKAEA
  - name: Oliver Funk
    affiliations:
      - UKAEA
  - name: Jonathan Matthews
    affiliations:
      - UKAEA
  - name: Athoy Nilima
    affiliations:
      - UKAEA
  - name: Alexander Pearce
    affiliations:
      - UKAEA
  - name: Dario Vaccaro
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

Bluemira is an open-source Python 3 framework for designing fusion power plants. It makes use of interdisciplinary models and incorporates a range of design activities, each of which is parameterised and automated. The Bluemira framework enables users to swiftly produce and investigate concept designs, making it a valuable tool for power plant component integration and whole-plant modelling.

One of the key aspects of designing a tokamak is maintaining a plasma equilibrium solution while optimising for poloidal field coils and divertor configurations. For example, a user might want to preserve an input equilibrium plasma shape and constrain the forces experienced by the coils whilst minimising the heat flux directed at the divertor targets.

We demonstrate the implementation of newly available Bluemira equilibria optimisation problems and constraints, and we investigate their effects for a device concept based on Spherical Tokamak for Energy Production (STEP) specifications. In particular, we present the results of poloidal field coil and, first wall and divertor designers when optimising using divertor field shaping parameters such as flux expansion and connection length. Finally, we highlight how the resulting Bluemira outputs could be used when considering whole plant design.

# Repository
https://github.com/Fusion-Power-Plant-Framework/bluemira

