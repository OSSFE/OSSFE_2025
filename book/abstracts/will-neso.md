---
title: 'NESO-Particles: A Performance Portable Particle Framework For The Fusion Use Case'
authors:
  - name: Will Saunders
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Project NEPTUNE approaches one of the grand challenge problems in fusion - modelling plasma in the edge region of a tokamak. In this edge region, hot plasma interfaces with the reactor wall and cold neutral gas resulting in a computationally expensive multi-scale problem that is considered an exascale challenge. We apply finite elements as a discretisation over physical space and use a particle representation as a kinetic representation in velocity space.

In this talk we discuss NESO-Particles (NP), our particle framework, which is a library for describing particle data and looping operations on unstructured meshes. We provide a high-level API in which users can describe generic particle, grid and global properties for their simulation. Furthermore we provide a particle specific loop abstraction which separates the description of particle looping operations from their respective implementation on CPU and GPU hardware.


# Repository
https://github.com/ExCALIBUR-NEPTUNE/NESO-Particles

