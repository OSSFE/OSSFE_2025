---
title: 'DisruptionPy: an open-source Python library for disruption study.'
authors:
  - name: Y Wei
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: GL Trevisan
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: C Rea
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: J Lorincz
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: AR Saperstein
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: A Decker
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: RS Granetz
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
  - name: MIT PSFC Disruption Studies Group
    affiliations:
      - Massachusetts Institute of Technology, Plasma Science and Fusion Center, Cambridge MA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

DisruptionPy is an interoperable open-source library for data access across different magnetic fusion experiment (MFE) devices. This library, developed in Python, contains built-in pipelines for processing and analyzing experimental data through a unified workflow, allowing users to quickly, easily, and robustly design machine learning (ML) applications such as for disruption prediction and avoidance. Development of this library is aligned with Findable, Accessible, Interoperable, Reusable (FAIR) and Open Science (OS) guidelines. Currently, development of DisruptionPy has mainly focused on the following areas: 1. Continuously incorporating additional physics methods for the currently supported machines including Alcator C-Mod and DIII-D. 2. Improving framework capability by measures such as recomputing EFIT with finer time resolution and adopting Xarray backend. 3. Aligning the development with best software development practices such as systematic and automated linting and testing. 4. Expanding support to new machines such as EAST, HBT-EP, and CTH. DisruptionPy has recently been released as a pip-installable open source library. Using this library, a curated Alcator C-Mod disruption prediction dataset will be released in the near future.

Work supported by the DOE FES under Award DE-SC0024368.

# Repository
https://github.com/MIT-PSFC/disruption-py

