---
title: 'Automated Testing and Continuous Integration for the KORC Codebase'
authors:
  - name: Ian Gibbs
    affiliations:
      - ORNL
  - name: Steven Hahn
    affiliations:
      - ORNL
  - name: Mark Cianciosa
    affiliations:
      - ORNL
  - name: Matthew Beidler
    affiliations:
      - ORNL
  - name: Omar Lopez
    affiliations:
      - ORNL
  - name: Rinkle Juneja
    affiliations:
      - ORNL
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Runaway electrons (RE) generated during disruptions in burning fusion plasmas pose a major risk for plasma-facing components in the ITER Tokamak reactor. The ORNL-developed Kinetic Orbit Runaway electrons Code (KORC) paired with the NIMROD extended-magnetohydrodynamic (MHD) solver, brings quantitative dynamics simulation capabilities for studying ways to mitigate reactor damage.  Efforts are underway expand KORC to run on Perlmutter using the OpenACC framework.  We use the GitHub Actions Matrix Strategy, facilitating a succinct, parameterized approach for automating builds across a wide variety of operating systems and hardware.  In the same manner, we leverage Spack's combinatorial versioning capability for managing toolchains and software stacks.  CMake allows for feature selection and adjustments to KORC during build time, while CTest automates testing KORC driven calculations against golden data.  Together, these tools comprise a robust paradigm for enhancing the KORC project's software development cycle.  Finally, a secure human-in-the-loop CI mechanism is devised, allowing safe CI interoperability with self-hosted ExCL (ORNL Experimental Computing Lab) GPU accelerated machines.

# Repository
https://github.com/ORNL-Fusion/KORC

