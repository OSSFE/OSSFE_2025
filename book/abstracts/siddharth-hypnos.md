---
title: 'Hypnos: parametric geometry preparation for fusion-relevant applications'
authors:
  - name: Siddharth Mungale
    affiliations:
      - Helen Brooks, Luke Humphrey
  - name: Siddharth Mungale
    affiliations:
      - Helen Brooks, Luke Humphrey
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Geometry creation is often a time-consuming and laborious process in the analysis of fusion power-plant components. Neutronics workflows require watertight geometry to avoid particle leakage. Iterative studies become impractical if dependant on overly manual geometry preparation. To address these and similar challenges we introduce Hypnos, a parametric geometry engine focused on breeder blanket design. It aims to ease the process of geometry creation and mesh generation. It uses Coreform Cubit for CAD generation and meshing, due to its reliability, automatic meshing capabilities, and support for a wide range of export formats. As far as possible, this has been decoupled from the code to allow for switching out of the backend. Geometrical parameters are specified in json files, which are provided as inputs. Hypnos has two modes of operation. The first is as a standalone python script run from the terminal. This simply generates and exports the described geometry or mesh file. The second is as a python library. This allows for bespoke workflows, for example a parametric design optimisation. Currently Hypnos contains a parametrised breeder blanket model based off of a DEMO HCPB blanket pre-conceptual design. However, it has been developed to allow users to create their own models. Geometry creation aims to be modular and extensible to facilitate re-usability. Hypnos automatically tracks blocks, sidesets, and materials of components (with the latter for use with DAGMC for neutronics calculations).

# Github repository
https://github.com/aurora-multiphysics/hypnos

