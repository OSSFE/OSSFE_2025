---
title: 'Accelerating Plasma Physics Simulations with Pyccel: A PyGyro Case Study.'
authors:
  - name: Jalal Maaouni
    affiliations:
      - The UM6P Vanguard Center, Morocco
  - name: Emily Bourne
    affiliations:
      - EPFL Switzerland
  - name: Yaman Güçlü
    affiliations:
      - Max-Planck-IPP Germany
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

This demonstration presents Pyccel[1], a Python-to-C/Fortran translator designed to optimize performance-critical bottlenecks in scientific workflows. Pyccel transforms high-level Python code, including object-oriented structures, into efficient compiled routines, enabling significant performance improvements while preserving code readability and maintainability. PyGyro[2], a modular library for computational plasma physics, will be used as an example to illustrate Pyccel’s ability to accelerate numerical methods such as splines, advection operators, and solvers. We will demonstrate how to apply Pyccel to accelerate specific routines and seamlessly integrate the optimized code into existing workflows.
[1]:Bourne et al., (2023). Pyccel: a Python-to-X transpiler for scientific high-performance computing. Journal of Open Source Software, 8(83), 4991,
[2]:Emily Bourne and Yaman Güçlü. Highly parallel drift-kinetic semi-Lagrangian simulations in Python

# Repository
https://github.com/pyccel/pyccel

