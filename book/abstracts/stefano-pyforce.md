---
title: 'pyforce: Python Framework for data-driven model Order Reduction of multi-physiCs problEms'
authors:
  - name: Stefano Riva
    affiliations:
      - Politecnico di Milano
  - name: Carolina Introini
    affiliations:
      - Politecnico di Milano
  - name: Antonio Cammi
    affiliations:
      - Politecnico di Milano
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

pyforce (Python Framework for data-driven model Order Reduction of multi-physiCs problEms) is an open-source Python package implementing Data-Driven Reduced Order Modelling techniques, focusing on state estimation and sensor placement. The framework targets multi-physics problems, focusing on nuclear reactor applications, by combining mathematical models with real data to enhance system understanding and state estimation. The package has been built on dolfinx and pyvista packages; pyforce is able to handle mesh and high-dimensional datasets handling, calculation of integrals, and ensures compatibility with OpenFOAM through pyvista and fluidfoam while offering an efficient workflow for reduced order modelling purposes. 

The package includes all the fundamental steps for generating Reduced Order Models of Multi-Physics problems: generation/import of the snapshots, generation of a linear reduced representation and subsequent compression, creation of surrogate models in the latent space and knowledge update through measure in a Data Assimilation framework. 
Techniques such as Proper Orthogonal Decomposition, Generalized Empirical Interpolation Method, and Parametrized-Background Data-Weak are integrated within the framework to address sensor placement, data reconstruction, and field estimation. This package also allows for integration with Machine Learning techniques (within scikit-learn package) to enhance the reduced order model accuracy, efficiency and robustness.

Even though the pyforce package has been extensively used for nuclear applications, the algorithms can be applied to any engineering field, providing valuable tools for researchers working in computational science and engineering. pyforce aims to bridge the gap between traditional ROM workflows and emerging data-driven techniques, making it a valuable resource for both academic and industrial applications.

# Repository
https://github.com/ERMETE-Lab/ROSE-pyforce

