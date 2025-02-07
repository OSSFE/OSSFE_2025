---
title: 'Modelling of deuterium release from tungsten co-deposited films induced by laser heating'
authors:
  - name: Vladimir Kulagin
    affiliations:
      - National Research Nuclear University MEPhI
  - name: Vladimir Kulagin
    affiliations:
      - National Research Nuclear University MEPhI
  - name: Oleg Medvedev
    affiliations:
      - National Research Nuclear University MEPhI, Ioffe Institute of Russian Academy of Sciences
  - name: Oleg Medvedev
    affiliations:
      - National Research Nuclear University MEPhI, Ioffe Institute of Russian Academy of Sciences
  - name: Ekaterina Shubina
    affiliations:
      - Ioffe Institute of Russian Academy of Sciences
  - name: Ekaterina Shubina
    affiliations:
      - Ioffe Institute of Russian Academy of Sciences
  - name: Igor Gabis
    affiliations:
      - Ioffe Institute of Russian Academy of Sciences
  - name: Igor Gabis
    affiliations:
      - Ioffe Institute of Russian Academy of Sciences
  - name: Vitaliy Efimov
    affiliations:
      - National Research Nuclear University MEPhI, Yury Gasparyan, National Research Nuclear University MEPhI
  - name: Vitaliy Efimov
    affiliations:
      - National Research Nuclear University MEPhI, Yury Gasparyan, National Research Nuclear University MEPhI
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Co-deposition of hydrogen isotopes and materials of plasma-facing components is one of the dominant fuel retention mechanisms in fusion devices [1]. The control for hydrogen isotope inventory in co-deposited layers is crucial for the sustainable operations of a device. Laser-induced desorption (LID) is a proposed technique for in situ monitoring of hydrogen content [2], which involves laser heating of a surface, followed by measurements of the released hydrogen isotopes.

In the present work, the open-source finite-element code FESTIM [3] is used to model experiments on LID of deuterium (D) from 1 μm-thick tungsten (W) films, co-deposited on a copper substrate (thickness of 3 mm). The simulation workflow included two major steps. First, the D trap properties in W films were obtained by fitting spectra from thermal desorption spectroscopy measurements [4]. Then, 2D multi-material LID simulations were conducted assuming axial symmetry. Spatiotemporal distribution of the beam power density was set according to the experimental fiber laser system (IPG, 0.1-10 ms, 1070 nm).

Considering the ratio of domain length scales, the 2D LID problem required high mesh refinement within the W region. To simplify the modelling, we conducted a series of 1D deuterium transport simulations along the radial profile of the laser beam using a discretised temperature profile from 2D simulations. For the studied problem, such an approach is shown to agree reasonably with full 2D simulations, but be more computationally efficient. It allowed to reconstruct distributions of the retention field and compare the simulation results with experimental LID data.

References:
[1] A. Widdowson, E. Alves, A. Baron-Wiechec et al., Nuclear Materials and Energy 12, 499 (2017)
[2] V. Philipps, A. Malaquias, A. Hakola et al., Nuclear Fusion 53 (9), 093002 (2013)
[3] R. Delaporte-Mathurin, J. Dark, G. Ferrero et al., International Journal of Hydrogen Energy 63, 786 (2024)
[4] R. Delaporte-Mathurin, E. A. Hodille, J. Mougenot et al., Nuclear Materials and Energy 27, 100984 (2021)


# Github repository
https://github.com/KulaginVladimir/LID-validation

