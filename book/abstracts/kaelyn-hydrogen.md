---
title: 'Hydrogen Inventory Simulations for PFCs (HISP) in ITER'
authors:
  - name: Kaelyn Dunnell
    affiliations:
      - MIT PSFC
  - name: Remi Delaporte-Mathurin
    affiliations:
      - MIT PSFC
  - name: Tom Wauters
    affiliations:
      - ITER
  - name: Etienne Hodille
    affiliations:
      - CEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Tritium inventory is an issue of critical study for the International Thermonuclear Experimental Reactor (ITER), which has an in-vessel safety limit of 700g of tritium. Simulating tritium transport through Plasma Facing Components (PFCs) is necessary to determine the tritium stored throughout the reactor. This research develops an open-source simulation tool, Hydrogen Inventory Simulations for PFCs (HISP), to simulate the evolution of hydrogen inventory in nuclear fusion reactors. HISP is being used to determine the optimal tritium removal strategy for ITER by simulating various cleaning scenarios and evaluating their impact on hydrogen inventory in ITER’s PFCs. HISP breaks the problem into three parts: development of a binning structure to describe the geometry of a given reactor (in our case ITER), comprehension of output plasma data from plasma source codes (such as DINA, SOLPS, SOLEDGE, etc.), and set up of a requested scenario (such as one full power pulse followed by one cleaning pulse). HISP uses these frameworks to simulate hydrogen transport with Finite Elements Simulation of Tritium in Materials (FESTIM), producing hydrogen inventory estimations. In the case of ITER, the main chamber and divertor are split into 102 bins that are each simulated in one dimension. A total of 6 scenarios are being tested, which vary the duration, order, and scenario position of cleaning pulses. The considered removal techniques are Ion Cyclotron Wall Conditioning (ICWC), Glow Discharge Conditioning (GDC), tokamak plasma with Inner Strike Point sweeps, and baking. Future work includes the competition of the HISP simulation package for simulating complete ITER campaigns and determination of the most efficient tritium removal strategy in ITER. 

# Repository
https://github.com/kaelyndunnell/hisp

