---
title: 'A fast electromagnetics library with Rust and Python'
authors:
  - name: James Logan
    affiliations:
      - CFS
  - name: Matt Vernacchia
    affiliations:
      - CFS
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Designing superconducting magnets for fusion energy requires quasi-steady electromagnetic calculations, such as the magnetic field due to a current path, or the mutual inductance between current paths. Here, specialized, filament-based programs can be faster and more accurate than general-purpose finite element software. The physicists and electrical engineers using the tool want to work in Python, and also want the tool to be fast.
cfsem is an electromagnetics library with a high-level Python API and Rust bindings for the numerical "heavy lifting", made with PyO3/Maturin. The Rust code is engineered for single-thread performance (e.g. by ensuring LLVM uses SIMD instructions and avoids run-time bounds checks), and some functions are parallelized with Rayon.
This talk will review the library's API, benchmarks, performance engineering details, and example applications. Most functions' throughput is ~10^8 elements / second on one core of an Apple M1 Pro, within a factor of a few of fully utilizing the FLOPS capacity. The library is easy to use from python, and is fast enough for applications like design sweeps, iterative solvers, and interactive visualizations. Within Commonwealth Fusion Systems, it is a component of internal tools that advance our design and understanding of superconducting magnets and tokamaks. It also forms the core of our open-source device_inductance library, which provides rapid estimates of 2D-axisymmetric mutual inductances in a tokamak.

# Repository
https://github.com/cfs-energy/cfsem-py ; https://github.com/cfs-energy/cfsem-rs ; https://github.com/cfs-energy/device_inductance

