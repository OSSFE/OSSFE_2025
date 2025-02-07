---
title: 'Struphy - solving plasma physics PDEs within the Python ecosystem'
authors:
  - name: Stefan Possanner
    affiliations:
      - Max Planck Institute for Plasma Physics in Garching, Germany
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Struphy provides easy access to partial differential equations (PDEs) in plasma physics. The package combines performance (for HPC), flexibility (models and physics features) and usabilty (documentation). Struphy is an object-oriented code entirely written in Python. The concept of inheritance is heavily used in its basic design; this enables the streamlined addition of new models and Physics features into Struphy. Model discretization is based on finite element exterior calculus (FEEC) for the fluid/field quantities and particle-in-cell (PIC) methods for the kinetic species. We will give a basic Tutorial by means of Jupyter notebooks that show the use of Struphy objects such as Propagators, Domains and MHD equilibria.

# Github repository
https://gitlab.mpcdf.mpg.de/struphy/struphy

