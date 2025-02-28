---
title: 'OFELIA: Openmc-FEnicsx for muLtiphysics tutorIAl'
authors:
  - name: Lorenzo Loi
    affiliations:
      - Politecnico di Milano
  - name: Stefano Riva
    affiliations:
      - Politecnico di Milano
  - name: Carolina Introini
    affiliations:
      - Politecnico di Milano
  - name: Antonio Cammi
    affiliations:
      - Politecnico di Milano
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The state of an operating nuclear reactor depends on several physical phenomena that coexist and are interdependent: they should be taken into account simultaneously by adopting a multi-physics approach, allowing a higher level of detail of the system properties. Amongst all coupled physics, neutron physics and thermal hydraulics are of great importance in this framework, as their interdependence is the most fundamental coupling effect in nuclear reactors: their interaction determines the power and temperature profiles, being quantities of interest during the design and safety analysis phases and during monitoring and control. This work focuses on developing a fully open-source multi-physics and multi-scale tool, OFELIA (Openmc-FEnicsx for muLtiphysics tutorIAl) capable of retrieving the coupled temperature profile of a reactor with solid fuel, such as PWR or space reactors when the power generated by the system is known. This methodology is implemented in a Python environment, coupling the open source library FEniCSx for the thermal-hydraulic analysis with the OpenMC Monte Carlo code for the description of the fissionable system: regarding the former, FEniCSx handles the thermal calculations, whereas a 1D model is used to predict the axial coolant temperature distribution. The coupling applies an explicit method, whose convergence is based on Picard iterations, using an adaptive relaxation scheme. This coupling strategy is compared with literature data (OpenFOAM-Serpent), providing a good agreement with a fully Multi-Physics solver with lower computational costs and a full Python implementation. This implementation, openly available on GitHub, is intended as a tutorial for introducing multi-physics solvers, offering an accessible starting point for students or those new to this field.

# Repository
https://github.com/ERMETE-Lab/MP-OFELIA

