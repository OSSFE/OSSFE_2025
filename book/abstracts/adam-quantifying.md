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

[hpcflow](https://github.com/hpcflow/hpcflow-new) is an open-source, cross-platform Python package for designing, running, and sharing large-scale reproducible computational workflows on HPC systems and locally. [MatFlow](https://github.com/hpcflow/matflow-new) is an extension of hpcflow that focuses on building cohesive materials science workflows, and is particularly useful as a framework to link uncertainty quantification (UQ) algorithms with high-fidelity simulations in fusion materials applications. We discuss some recent work that uses MatFlow to predict rare-event failure probabilities via the subset simulation UQ method https://doi.org/b7z8hq, which conceptually partitions an extremely unlikely failure event into a series of conditional failure events that are more computationally accessible. In particular, we apply the workflow to a materials failure problem using full-field crystal plasticity simulations with DAMASK @10.1016/j.commatsci.2018.04.030, where the input microstructure is uncertain. After running an initial set of simulations, MatFlow then runs sets of Markov chains to iteratively direct the input space towards the failure domain. We discuss the features of MatFlow that enable reusable workflows such as these to be developed, and we further discuss how we have used MatFlow to explore and compare the efficiency of selecting different variations of the Markov Chain Monte Carlo algorithm, such as the multi-level approach, which uses simulations at multiple fidelities to improve efficiency.


# Repository
https://github.com/hpcflow

