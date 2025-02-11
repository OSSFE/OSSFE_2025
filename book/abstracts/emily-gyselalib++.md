---
title: 'Gyselalib++: A GPU-Ready Library for Gyrokinetic Plasma Simulations'
authors:
  - name: Emily Bourne
    affiliations:
      - EPFL Switzerland
  - name: Virginie Grandgirard
    affiliations:
      - CEA France
  - name: Yuuichi Asahi
    affiliations:
      - Maison de la Simulation France
  - name: Julien Bigot
    affiliations:
      - Maison de la Simulation France
  - name: Peter Donnel
    affiliations:
      - CEA France
  - name: Alexander Hoffmann
    affiliations:
      - Max-Planck-IPP Germany
  - name: Abdelhadi Kara
    affiliations:
      - CEA France
  - name: Baptiste Legouix
    affiliations:
      - CEA France
  - name: Etienne Malaboeuf
    affiliations:
      - CNRS France
  - name: Dorian Midou
    affiliations:
      - CEA France
  - name: Yann Munschy
    affiliations:
      - CEA France
  - name: Mathieu Peybernes
    affiliations:
      - EPFL Switzerland
  - name: Kevin Obrejan
    affiliations:
      - CEA France
  - name: Thomas Padioleau
    affiliations:
      - Maison de la Simulation France
  - name: Pauline Vidal
    affiliations:
      - Max-Planck-IPP Germany
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The development of fusion energy in magnetic confinement devices relies heavily on simulations of plasma behaviour. Gyselalib++ is a new open-source C++ library under active development, providing tools to develop gyrokinetic semi-Lagrangian codes for plasma simulations. It provides mathematical tools such as splines, quadrature rules, coordinate mappings, advection operators and solvers for partial differential equations (PDEs). To achieve high performance on modern hardware, Gyselalib++ leverages the Kokkos framework, ensuring portability across both CPU and various GPU architectures.
This presentation will introduce Gyselalib++, highlight its key features, and demonstrate its potential for use in plasma simulations.

# Repository
https://github.com/gyselax/gyselalibxx

