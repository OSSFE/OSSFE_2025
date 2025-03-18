---
title: 'Modeling Magnetic Confinement Fusion Energy Systems with MOOSE-based Capabilities'
authors:
  - name: Pierre-Clément A. Simon
    affiliations:
      - Idaho National Laboratory
  - name: Casey T. Icenhour
    affiliations:
      - Idaho National Laboratory
  - name: Masashi Shimada
    affiliations:
      - Idaho National Laboratory
  - name: Guillaume Giudicelli
    affiliations:
      - Idaho National Laboratory
  - name: Logan H. Harbour
    affiliations:
      - Idaho National Laboratory
  - name: Derek Gaston
    affiliations:
      - Idaho National Laboratory
  - name: Lin Yang
    affiliations:
      - Idaho National Laboratory
  - name: Helen Brooks
    affiliations:
      - United Kingdom Atomic Energy Agency
  - name: Mahmoud Eltawila
    affiliations:
      - University of Illinois Urbana-Champaign
  - name: April J. Novak
    affiliations:
      - University of Illinois Urbana-Champaign
  - name: Grayson Gall
    affiliations:
      - North Carolina State University
  - name: Amanda M. Lietz
    affiliations:
      - North Carolina State University
  - name: Trevor Franklin
    affiliations:
      - Virginia Commonwealth University
  - name: Lane B. Carasik
    affiliations:
      - Virginia Commonwealth University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Modeling and simulation are increasingly leveraged to accelerate the deployment of fusion energy technology. High-fidelity multiphysics computational tools are essential to understand, model, and quantify the complex interactions between plasma, neutron exposure, materials performance, and engineering processes. This is evident when considering plasma facing components, which are under extreme thermal loads (~1-20 MW/m2), endure repeated thermal shocks, and are irradiated by plasma ions, photons, and high-energy neutrons throughout their lifecycle. Before deployment of a fusion energy system, the design of plasma-facing components with acceptable lifetime degradation is highly challenging.
The Fusion ENergy Integrated multiphys-X (FENIX) framework meets these needs by leveraging the Multiphysics Object-Oriented Simulation Environment (MOOSE) framework, partly-developed by international collaborators, the United States Department of Energy's Nuclear Energy Advanced Modeling and Simulation (NEAMS) program, and several INL’s Laboratory Directed Research-funded programs. FENIX integrates various existing MOOSE capabilities, such as the heat conduction, solid mechanics and thermal hydraulics modules, with MOOSE-based applications including Cardinal (neutronics and computational fluid dynamics) and TMAP8 (Tritium Migration Analysis Program, version 8). Moreover, FENIX contains dedicated capabilities for plasma edge modeling, which will support multiphysics plasma-material interaction simulations. This comprehensive and modular integration built on the MOOSE framework allows FENIX to perform massively parallel multiphysics simulations, which are essential for the design, safety analysis, and performance evaluation of fusion systems. FENIX aims to model the harsh environment in which these components operate, thus accelerating their design and evaluation processes. Moreover, FENIX is developed in an open-source manner, with a continuous integration system to facilitate rigorous testing and high software quality assurance (SQA) standards. The framework's modularity, open and collaborative development, extensive documentation, and adherence to high SQA standards fosters rapid training, workforce development in universities, and effective collaborations - including public-private partnerships with national laboratories. These capabilities have been demonstrated on plasma facing components such as the ITER divertor monoblocks needed for removal of plasma impurities and high heat loads.
This presentation will cover the current capabilities of FENIX and showcase preliminary results modeling plasma facing components. We will also discuss how FENIX and other MOOSE-based applications are being utilized in the fusion community to address critical scientific and engineering challenges, ultimately supporting the deployment of fusion energy as a sustainable power source.


# Repository
https://github.com/idaholab/fenix

