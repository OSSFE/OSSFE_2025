---
title: 'RadModeling'
authors:
  - name: Alvaro Cubi
    affiliations:
      - Fusion for Energy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

RadModeling is a collection of tools that aid and streamline the simplification of geometries, the conversion from CAD to a radiation transport model, the preparation of Monte Carlo simulations, the post-processing of results and the tracking and review of the whole process, all from a CAD-centric perspective. The tools can be used in the CAD software SpaceClaim (soon to be renamed ANSYS Discovery) or in a Python environment. The tools perform a variety of different tasks, some of them can be used independently while others are part of a dedicated workflow. 

Among the functionalities present in RadModeling there is:
- Tracking of every component independently. This includes volume deviation, material and density information and the link with MC cells.
- Automatic adjustment of surfaces to maintain components below their volume deviation limit requirements.
- Automatic detection of components exceeding volume deviation limit requirements.
- Automatic show/hide of components according to their assigned MC material composition.
- Automatic implementation of material, density, density correction factor, and comments to an MCNP input file.
- Generation of CAD plots identical to those obtained with the MCNP plotter to have a 1:1 pixel comparison.
- Automatic conversion of toroidal elbows in pipes to a set of cylinders.


# Repository
https://github.com/Fusion4Energy/RadModeling

