---
title: 'SYSTEM MODELING AND OPTIMIZATION OF TOKAMAK TRITIUM FUEL CYCLE'
authors:
  - name: Sergey S. Ananev
    affiliations:
      - NRC Kurchatov Institute
  - name: Ac. Kurchatov sq.
    affiliations:
      - 1/1, Moscow RU-123182, Russia
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

For the conceptual design of fusion reactors, it is necessary to estimate the amount of fuel required to start the facility, and at the stage of technical design of the facility, to formulate requirements for them. The fuel component flows must be injected into the vacuum chamber/plasma of the facility are many times (up to 1000 times) higher than the burnup rate in the fusion reaction. Steady-state fusion reactors will require a fuel cycle design different from the generally accepted one (for experimental facilities), as well as a steady-state mode of all fuel cycle systems (to prevent tritium accumulation). This requires matching the fuel injection processes with the processes occurring in the main and divertor plasmas of the facility.
Particle flows in the fuel cycle (FC) are determined primarily by the requirements for the parameters of the plasma core provided by the injection system, as well as the flows in the pumping system coming from the vacuum chamber to the management systems. Therefore, the modeling of FC systems and the calculation of the particle flux should be related to the model of the core and divertor plasma. Interaction of FC with core and divertor plasmas employs the SOLPS, ASTRA, and FC-FNS codes. FC modeling is performed by open-source tools - FC-FNS code. 
This code was created and tested for projects of the steady-state tokamak-based fusion neutron source (FNS). The range of operation parameters is found for the core plasma, in which the tritium fraction is controlled by pellet injection with a different T/D isotopic composition. Impact of neutral beam heating and fueling by recycling and neutrals flow from divertor was accounted for as well. The neutral beams with different D/T composition and the core plasma were studied, as well as the total inventory at the facility site and the localization of tritium in FC. The influence of HFS and LFS pellet injection on the plasma core fuelling and ELM triggering is considered.
An important feature of the described approach is that it allows us to link the plasma discharge parameters with candidate/applied fuel cycle technologies (as well as to formulate requirements for them).

# Repository
https://github.com/Sergey-Ananev/FC-FNS

