---
title: 'CAD_to_OpenMC - an easy to use tool converting CAD-design to neutronics-ready geometry'
authors:
  - name: Erik B Knudsen
    affiliations:
      - United Neux
  - name: Lorenzo Chierici
    affiliations:
      - Copenhagen Atomics A/S
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Most particle transport pckages rely on the concept of Constructive Solid Geometry (CSG)
to describe the geometry or scene relevant to the problem. While this has advantages, such as being
computationally efficient it is often cumbersome and error prone to create a geometry description, not to mention that not too many design engineers have experience with the concept.
CAD-tools on the other hand, are widely used and optimized for geometry generation. Thus, beidging the gap between the two worlds would be very beneficial.
Several routes have been proposed to solve this problem, e.g.:
1. Allow transport directly on CAD-generated objects.
2. Convert the CAD-geometry into CSG; Inverse CSG (Du, 2018), GEOUNED (Catalan, 2024)
3. Distretize CAD-geometry and create a library to allow a general polygonalized surface inside CSG.
DAGMC(Mouginot, 2021) is a very efficient library created to allow triangularized surfaces to be used within a CSG-geometry, what remains to complete item 3 is an easy-to-use open source tool to create triangularized surfaces from CAD-geometry. We present CAD_to_OpenMC, a python based tool to do precisely that, with a focus on generating geometry for the transport package OpenMC(Romano, 2018). It is fully open and available on github. N.b. despite its name, the generated geometry may be used in several transport packages, such as MCNP, fluka, and GEANT4 owing to the generality of DAGMC.

So far we have been able to create complete geometries from models of MSRE, MSBR (Rosenthal, 1970), and GODIVA_IV (Goda, 2021) using CAD_to_OpenMC to name a few - these we will present on our poster, including the necessary steps and scripts to put the models together.

References:
Catalán, J. P., et al. "GEOUNED: a new conversion tool from CAD to Monte Carlo geometry." Nuclear Engineering and Technology 56.6 (2024): 2404-2411.
Du, Tao, et al. "Inversecsg: Automatic conversion of 3d models to csg trees." ACM Transactions on Graphics (TOG) 37.6 (2018): 1-16.
Goda, Joetta, et al. "A new era of nuclear criticality experiments: the first 10 years of Godiva IV Operations at NCERC." Nuclear Science and Engineering 195.sup1 (2021): S55-S79.
Mouginot, B., et al. "DAGMC-Direct Accelerated Geometry Monte Carlo Toolkit." (2021).
Romano, Paul K., et al. "OpenMC: A state-of-the-art Monte Carlo code for research and development." Annals of Nuclear Energy 82 (2015): 90-97.
Rosenthal, M. W., P. R. Kasten, and R. B. Briggs. "Molten-salt reactors — history, status, and potential." Nuclear Applications and Technology 8.2 (1970): 107-117.


# Repository
https://github.com/united-neux/CAD_to_OpenMC

