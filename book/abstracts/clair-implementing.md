---
title: 'Implementing Toroidal Harmonic Flux Constraints in Bluemira'
authors:
  - name: Clair Mould
    affiliations:
      - UKAEA
  - name: Oliver Bardsley
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
  - name: Georgina Graham
    affiliations:
      - UKAEA
  - name: Jonathan Maddock
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
  - name: Ocean Wong
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Bluemira is an open-source, integrated interdisciplinary design tool for future fusion power plants. With Bluemira, the design space of many physics and engineering aspects of a fusion reactor concept design can be rapidly explored. 

Bluemira has previously incorporated a Spherical Harmonic (SH) feature which enables the user to constrain the plasma equilibrium for spherical tokamak designs. We expand upon this work to include the use of Toroidal Harmonics (TH), which can be used to describe magnetic flux configurations for tokamaks with conventional aspect ratios, thereby enabling us to use harmonic constraints for a much wider range of device designs. These harmonic constraints can be used in tokamak design workflows when optimising for poloidal field (PF) coilset configuration and divertor shaping objectives, or even in plasma control scenarios (e.g., MAST-U, Bardsley et al., 2024). 

TH are used to approximate the PF coilset contribution to the magnetic flux, and this allows us to separate the 'core' and 'vacuum' contributions and enables optimisation of the PF coil currents and positions for a given design, while keeping the core plasma shape fixed. Additionally, when using TH constraints, the Grad-Shafranov calculation does not need to be performed for each iteration, which is advantageous as it reduces the computational time required.  

We present the implementation of the TH constraint method in the Bluemira framework and explore the effects on the optimisation of the plasma and magnetic field design using EU-DEMO baseline reactor specifications. 

# Repository
https://github.com/Fusion-Power-Plant-Framework/bluemira

