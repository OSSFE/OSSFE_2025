---
title: 'Quantifying uncertainty in fusion materials with MatFlow, an open-source computational workflow manager for materials science'
authors:
  - name: Adam Plowman
    affiliations:
      - UKAEA
  - name: Pratheek Shanthraj
    affiliations:
      - UKAEA
  - name: Ubaid Qadri
    affiliations:
      - Hartree Centre
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

hpcflow [1] is an open-source, cross-platform Python package for designing, running, and sharing large-scale reproducible computational workflows on HPC systems and locally. MatFlow [2] is an extension of hpcflow that focuses on building cohesive materials science workflows, and is particularly useful as a framework to link uncertainty quantification (UQ) algorithms with high-fidelity simulations in fusion materials applications. We discuss some recent work that uses MatFlow to predict rare-event failure probabilities via the subset simulation UQ method [3], which conceptually partitions an extremely unlikely failure event into a series of conditional failure events that are more computationally accessible. In particular, we apply the workflow to a materials failure problem using full-field crystal plasticity simulations with DAMASK [4], where the input microstructure is uncertain. After running an initial set of simulations, MatFlow then runs sets of Markov chains to iteratively direct the input space towards the failure domain. We discuss the features of MatFlow that enable reusable workflows such as these to be developed, and we further discuss how we have used MatFlow to explore and compare the efficiency of selecting different variations of the Markov Chain Monte Carlo algorithm, such as the multi-level approach, which uses simulations at multiple fidelities to improve efficiency.

[1] https://github.com/hpcflow/hpcflow-new
[2] https://github.com/hpcflow/matflow-new
[3] Au, Siu-Kui, and James L. Beck. ‘Estimation of Small Failure Probabilities in High Dimensions by Subset Simulation’. Probabilistic Engineering Mechanics 16, no. 4 (October 2001): 263–77. https://doi.org/10.1016/S0266-8920(01)00019-4.
[4] Roters, F., M. Diehl, P. Shanthraj, P. Eisenlohr, C. Reuber, S. L. Wong, T. Maiti, et al. ‘DAMASK – The Düsseldorf Advanced Material Simulation Kit for Modeling Multi-Physics Crystal Plasticity, Thermal, and Damage Phenomena from the Single Crystal up to the Component Scale’. Computational Materials Science 158 (15 February 2019): 420–78. https://doi.org/10.1016/j.commatsci.2018.04.030.

# Repository
https://github.com/hpcflow

