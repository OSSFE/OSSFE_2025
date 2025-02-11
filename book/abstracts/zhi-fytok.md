---
title: 'FyTok: An Integrated Modeling Simulator for Tokamak'
authors:
  - name: Zhi Yu
    affiliations:
      - Xiaojuan Liu,  Institute of Plasma Physics, Chinese Academy of Sciences, Hefei 230031, China
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Tokamak is a highly complex system comprising a multitude of subsystems. It encompasses a diverse array of nonlinear physical processes across a range of spatial and temporal scales. These physical processes are independent yet closely related. Therefore, the description and comprehension of the entire system are highly intricate endeavours. It is essential to adopt an appropriate “integration” strategy to enhance the understanding of complex systems.

This talk describes the development of FyTok, a comprehensive simulator for Tokamaks. The simulator has been designed using a top-down approach based on ontology-based modelling, which translates the IMAS Data Dictionary-based Tokamak ontology description into a manipulable programming framework. The modelled objects are divided into subsystems and physical concepts. FyTok handles each of them separately using data bindings, formula bindings, and function bindings. FyTok can be easily configured using configuration files to organise the different module classes, generate the required physical workflows, and track the evolution of physical quantities in the workflows for modelling purposes. The ontology-based modelling approach in FyTok improves data consistency and provides the user with a generic and flexible modelling platform.

# Repository
https://github.com/fusion-yun/fytok

