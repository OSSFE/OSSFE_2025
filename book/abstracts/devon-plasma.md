---
title: 'Plasma Operation Contours (POPCON) with cfspopcon'
authors:
  - name: Devon Battaglia
    affiliations:
      - CFS
  - name: Tom Body
    affiliations:
      - CFS
  - name: Alex Creely
    affiliations:
      - CFS
  - name: Christoph Hasse
    affiliations:
      - CFS
  - name: James Logan
    affiliations:
      - CFS
  - name: Tom Looby
    affiliations:
      - CFS
  - name: Robert Mumgaard
    affiliations:
      - CFS
  - name: Pablo Rodriguez-Fernandez
    affiliations:
      - MIT
  - name: Audrey Saltzman
    affiliations:
      - MIT
  - name: Isaac Savona
    affiliations:
      - DIFFER
  - name: Nicholas Schneider
    affiliations:
      - CFS
  - name: Brandon Sorbom
    affiliations:
      - CFS
  - name: Ching Tse
    affiliations:
      - CFS
  - name: Matthew Vernacchia
    affiliations:
      - CFS
  - name: Allen Wang
    affiliations:
      - MIT
  - name: Oak Nelson
    affiliations:
      - Columbia University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Plasma Operation Contour (POPCON) analysis employs time-independent, 0-D equations to provide a "back-of-the-envelope" estimate for steady-state plasma performance.  This type of calculation is used for rapid scoping of tokamak pulse performance over a wide range of design and operation parameters.  CFS has built a fully Python, open-source POPCON code, called cfspopcon, that is easily extensible, with automatic variable passing in workflows, automatic loop generation for input scans using xarray and powerful unit-handling based on the pint library. The code is routinely used to inform scenario development on SPARC, design iterations on ARC and guiding investigations with higher-fidelity plasma calculations. All models in cfspopcon are referenced to published work and, due to the nature of compact, high-field tokamak devices, have a particular focus on identifying pulse scenarios that satisfy the requirement to have a viable boundary solution. Beyond CFS, cfspopcon is a useful teaching aid for graduate-level tokamak design studies.

# Repository
https://github.com/cfs-energy/cfspopcon

