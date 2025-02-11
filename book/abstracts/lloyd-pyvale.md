---
title: 'pyvale: A sensor simulation tool for measurement uncertainty assessment and optimising validation experiments for engineering components. '
authors:
  - name: Lloyd Fletcher
    affiliations:
      - UKAEA
  - name: Adel Tayeb
    affiliations:
      - UKAEA
  - name: Alex Marsh
    affiliations:
      - UKAEA
  - name: Lorna Sibson
    affiliations:
      - UKAEA
  - name: John Charlton
    affiliations:
      - UKAEA
  - name: Joel Hirst
    affiliations:
      - UKAEA
  - name: Allan Harte
    affiliations:
      - UKAEA
  - name: Cory Hamelin
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Engineering components in a fusion reactor are subjected to significant thermal (10’s MW/m), mechanical (MN range) and electromagnetic loads (several Tesla) making experimental validation under these conditions challenging. To reduce the cost of simulation validation experiments we have developed a sensor simulation tool called `pyvale` (the python validation engine) which is designed to optimise the deployment of point sensors and imaging diagnostics accounting for measurement uncertainties. `pyvale` is open-source and the code is available here: https://github.com/Digital-Validation-Laboratory/pyvale. We take inspiration from computer graphics and synthetic image deformation for assessing uncertainties of digital image correlation systems and extend the idea to a multi-physics scenarios including thermal (e.g. thermocouples, pyrometers, infra-red cameras) and mechanical sensors (e.g. strain gauges, digital image correlation). The `pyvale` interface is modular allowing for extension to include other multi-physics scenarios in the future such as fluid mechanics, electromagnetic or neutronic measurements. At the conference we will present an application of `pyvale` to assess sensor uncertainties for a high heat flux test of a mock-up divertor armour component. 


# Repository
https://github.com/Computer-Aided-Validation-Laboratory/pyvale

