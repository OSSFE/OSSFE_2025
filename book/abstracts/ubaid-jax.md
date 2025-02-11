---
title: 'Jax-GS: A differentiable free-boundary Grad-Shafranov equilibrium solver for CPUs and GPUs '
authors:
  - name: Ubaid Ali Qadri
    affiliations:
      - STFC Hartree Centre
  - name: Nicola Amorisco
    affiliations:
      - UK Atomic Energy Authority
  - name: George K. Holt
    affiliations:
      - STFC Hartree Centre
  - name: Adriano Agnello
    affiliations:
      - STFC Hartree Centre
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The nonlinear Grad-Shafranov (GS) equation governs the balance of forces in tokamak plasmas. Free-boundary GS solvers are extensively used for equilibrium reconstruction and plasma shape design and control. In addition to knowing how the plasma behaves, we want to understand sensitivity to model parameters and control variables and use this to quantify uncertainty in the results. In this work, we solve this problem by using JAX - an open-source Python library developed for scalable numerical computations and machine learning. We implement vectorizable and differentiable routines to identify critical points and the plasma domain. We use the automatic differentiation capabilities of JAX to efficiently assemble the Jacobian matrix of the nonlinear GS problem and use it as part of a robust Newton-based method. The AD capability also gives us access to the sensitivities of the plasma state with respect to all the input parameters - using an adjoint formulation and the implicit function theorem, these are obtained by solving just a single additional system of linear equations. Finally, we showcase how our solver seamlessly operates on GPUs without any change to the source code.

