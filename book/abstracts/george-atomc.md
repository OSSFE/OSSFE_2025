---
title: 'AtOMC: A Port of OpenMC for Atomic transport and Plasma Interaction '
authors:
  - name: George J. Wilkie
    affiliations:
      - Princeton Plasma Physics Organization
  - name: Paul Romano
    affiliations:
      - Argonne National Laboratory
  - name: R. Michael Churchill
    affiliations:
      - Princeton Plasma Physics Laboratory
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Modern tooling is demanded for predicting the transport and reaction characteristics of atoms and molecules, especially in the context of magnetic confinement fusion. DEGAS2 and EIRENE are the most common and capable tools currently in use, and share many fundamental similarities with the OpenMC framework. OpenMC is an open source Monte Carlo transport solver that was primarily developed for neutron and photon transport. We have demonstrated that OpenMC is suitable for atomic transport calculations and have developed a version with the appropriate reactions https://doi.org/10.48550/arXiv.2411.12937. The relative error between the models is small, and the performance of OpenMC is at least comparable to DEGAS2. This is the case even without taking advantage of heterogeneous computing architectures, which is only one of several remarkable new capabilities that this demonstration heralds.


# Repository
github.com/gjwilkie/openmc

