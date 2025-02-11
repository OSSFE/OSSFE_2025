---
title: 'Building a new multiphysics workflow in MOOSE: application to tritium migration, trapping and advection in TMAP8'
authors:
  - name: Guillaume Giudicelli
    affiliations:
      - Idaho National Laboratory
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Fusion devices rely on the sustainable production and consumption of several kilograms of tritium to generate energy. This rare fuel resource is both highly mobile and radioactive, making inventory tracking a priority for operation and safety. The fusion safety program at Idaho National Laboratory has been developing the Tritium Migration and Analysis Program (TMAP), and the most recently developed version is a MOOSE-based application. TMAP8 is verified against its predecessors and possesses additional multi-dimensional tritium migration modeling capabilities. As we extend its capabilities towards both whole device (in multiple dimensions) and whole plant (with multiple components) simulations, the syntax of inputs must become compact, descriptive, compatible with quality assurance processes, and as error-proof as achievable.
The new physics system developed within MOOSE can set up equations and instantiate them on plant components. The system permits the automatic definition of complex discretization with consistency between object parameters achieved programmatically. The physics system can currently instantiate the equations for heat conduction and Navier Stokes weakly compressible flow. In MOOSE-terms, it automates the definition of kernels, boundary conditions, and several core and helper materials and fields. As part of this effort, physics classes were developed for tritium migration, trapping, and advection within either a multi-dimensional Navier Stokes fluid dynamics simulation or a 1D thermal hydraulics piping system.
In this presentation, we will showcase the new syntax, its application to several verification and validation cases that were already studied using the classical TMAP8 syntax, and demonstrate the new coupling capabilities for the migration of tritium into blanket coolant channels and the subsequent advection into the coolant loop.


# Repository
https://github.com/idaholab/TMAP8

