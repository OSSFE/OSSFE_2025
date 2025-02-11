---
title: 'A package for differentiable evaluation of fusion rate coefficients'
authors:
  - name: J. A. Schwartz
    affiliations:
      - Princeton Plasma Physics Laboratory
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Many codes performing fusion power plant scoping or optimization must calculate the fusion reaction rate of D-T or other reactions. The most complex part of this is the 'rate coefficient' <σv>, which involves an integral over fusing species' distribution functions and the velocity-dependent reaction cross section. We present a python package which aims to provides access to cross sections for all the technologically relevant fusion reactions.
For each of these the package computes rate coefficients for Maxwellian distributions, with plans for expansion to other distributions of interest such as beam-target and bi-Maxwellian. Derivatives of the cross sections with respect to energy and of the rate coefficients with respect to their parameters (e.g. temperature) are provided using either analytic derivatives or automatic derivatives via jax. Special care is taken to provide reasonable results at very low or very high energies or temperatures in order to avoid issues during automated optimization procedures.

This work was supported by the U.S. Department of Energy under contract numbers DE-AC02-09CH11466.

# Repository
https://github.com/PrincetonUniversity/fusionrate

