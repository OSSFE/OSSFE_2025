---
title: 'F4Enix, a new Python API for pre and post processing of MCNP inputs and outputs'
authors:
  - name: Alberto Bittesnich
    affiliations:
      - ATG Science and Engineering, Universitat Politecnica de Catalunya
  Davide Laghi, Fusion for Energy
  Alvaro Cubi, Fusion for Energy
  Aljaz Kolsek, Fusion for Energy
  Marco Fabbri, Fusion for Energy
  - name: Alberto Bittesnich
    affiliations:
      - ATG Science and Engineering, Universitat Politecnica de Catalunya
  Davide Laghi, Fusion for Energy
  Alvaro Cubi, Fusion for Energy
  Aljaz Kolsek, Fusion for Energy
  Marco Fabbri, Fusion for Energy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The reliable computation of nuclear responses for fusion reactor (e.g., ITER) and components are a complex and resource-intensive process. It encompasses the preparation of exceptionally large and detailed computer models that could not possibly handled by hand and need a high degree of automatization to be dealt with. To give an order of magnitude of the problem, E-lite, which is an MCNP detailed model of the entire ITER tokamak, is composed by more than 400 thousands cells and output files produced by simulations performed on these models can easily occupy more than a few Gb of storage.

To address these kinds of challenges, a great number of scripts was produced during the years at Fusion For Energy (F4E) that presented a wide range of maturity, verification level and documentation quality. The neutronics team of F4E recently decided to collect all these codes, refactor them, generalize them, and aggregate them into a unique pip installable python package named F4Enix distributed under the EUROPEAN UNION PUBLIC LICENCE v. 1.2 terms. The primary objectives of F4Enix are:
•	Automate and streamline the pre and post-processing operations involved in nuclear response computations for ITER or similar projects.
•	Significantly enhance the efficiency, capability, and overall quality of the entire nuclear analysis workflow.
•	Allow to maintain, test, and document all code related to nuclear analyses workflows in a single place.
•	Build synergies between the different code parts.
•	Provide a useful tool to F4E suppliers.

F4Enix also provides a comprehensive and up-to-date documentation that describes the installation, usage, and API of the package. The documentation is hosted online using Read the Docs, a service that builds and serves the documentation whenever the code is updated. Finally, F4Enix is automatically built and uploaded to the PyPi index every time a new version is tagged, making it available through a simple pip install.


# Github repository
https://github.com/Fusion4Energy/F4Enix

