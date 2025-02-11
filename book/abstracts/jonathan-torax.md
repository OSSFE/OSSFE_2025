---
title: 'TORAX: A Fast and Differentiable Tokamak Transport Simulator in JAX'
authors:
  - name: Jonathan Citrin
    affiliations:
      - Google Deepmind
  - name: Ian Goodfellow
    affiliations:
      - Google Deepmind
  - name: Akhil Raju
    affiliations:
      - Google Deepmind
  - name: Sebastian Bodenstein
    affiliations:
      - Google Deepmind
  - name: Craig Donner
    affiliations:
      - Google Deepmind
  - name: Federico Felici
    affiliations:
      - Google Deepmind
  - name: Anushan Fernando
    affiliations:
      - Google Deepmind
  - name: Philippe Hamel
    affiliations:
      - Google Deepmind
  - name: Andrea Huber
    affiliations:
      - Google Deepmind
  - name: Tamara Norman
    affiliations:
      - Google Deepmind
  - name: David Pfau
    affiliations:
      - Google Deepmind
  - name: Brendan Tracey
    affiliations:
      - Google Deepmind
  - name: Devon Battaglia
    affiliations:
      - Commonwealth Fusion Systems
  - name: Anna Teplukhina
    affiliations:
      - Commonwealth Fusion Systems
  - name: Josiah Wai
    affiliations:
      - Commonwealth Fusion Systems
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

We introduce TORAX, an open-source differentiable tokamak core transport simulator targeting fast and accurate core-transport simulation for pulse planning and optimization, and unlocking broad capabilities for controller design and advanced surrogate physics. TORAX is written in Python using JAX, and solves coupled time-dependent 1D PDEs for core ion and electron heat transport, particle transport, and current diffusion. JAX's just-in-time compilation provides fast computation, while maintaining Python's ease of use and extensibility. JAX auto-differentiability enables gradient-based optimization techniques and trajectory sensitivity analysis for controller design, without time-consuming manual Jacobian calculations. JAX's inherent support for neural network development and inference facilitates coupling ML-surrogates of physics models, key for fast and accurate simulation. Code verification is obtained by comparison with the established RAPTOR code on ITER-like and SPARC scenarios. TORAX is an open source tool, and aims to be a foundational component of wider workflows built by the wider community for future tokamak integrated simulations.

# Repository
https://github.com/google-deepmind/torax

