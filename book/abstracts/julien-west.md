---
title: 'WEST Ion Cyclotron Antenna Electrical Model Digital Twin'
authors:
  - name: Julien Hillairet
    affiliations:
      - CEA, IRFM F-13108 Saint-Paul-lez-Durance France
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The numerical model of the WEST Ion Cyclotron Resonance Antenna consists of representing a digital twin of an antenna radiofrequency circuit. This model uses the open-source package scikit-rf to connect the different parts of the antenna. Each parts can be calculated either from analytic expressions, full-wave codes or antenna/plasma coupling codes. The antenna tuning capacitors can be automatically optimized for a given frequency. The voltages and currents at the capacitors can be evaluated for a given antenna excitation (power and phase). The code aims to help the RF operators of the antenna to select the best capacitor values for a given frequency and plasma scenario. To this aim, an online interactive graphical user interface is provided using Binder. In addition, the model can be used by other researchers working on antenna/plasma coupling models, to deduce the input voltages/powers to set up the antenna excitation for a given plasma scenario.

# Repository
https://github.com/jhillairet/WEST_IC_antenna

