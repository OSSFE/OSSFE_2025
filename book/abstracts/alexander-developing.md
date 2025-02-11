---
title: 'Developing a State-Oriented Plasma Control System'
authors:
  - name: Alexander Kachkin
    affiliations:
      - Next Step Fusion sarl
  - name: Evgeny Adishchev
    affiliations:
      - Next Step Fusion sarl
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Plasma control for fusion power plants (FPPs) represents a critical and complex challenge due to limited diagnostic access, weak actuators, and the requirement for continuous, steady-state operation. This work proposes an approach to develop a plasma-state-oriented control system that shifts focus from individual plasma parameters to maintaining robust, desirable plasma states characterized by fusion performance, stability, and reliability.

A key feature of the proposed Plasma Control System (PCS) is its architecture,
including a machine-agnostic and machine-specific layers.
The architecture enables adaptability across different magnetic confinement devices, including tokamaks and stellarators. At the kernel of the PCS lies the Plasma State Monitor (PSM), an advanced real-time classifier that integrates modeling techniques and machine learning (ML). The PSM employs a finite state machine (FSM) approach to categorize plasma states, enabling accurate state transitions based on thresholds, constraints, and predictive modeling. These states incorporate both discrete variables, such as energy confinement time and beta limits, and continuous dynamics, such as plasma density and edge-localized modes (ELMs).

The PSM interacts with the Plasma State Reconstructor and the Real-Time Plasma Evolution Model. A supervisory controller within the PCS orchestrates the coordination of plasma control tasks, including equilibrium maintenance, heating, fueling, and disruption avoidance. By leveraging predictive modeling and ML techniques such as reinforcement learning, the controller prioritizes control actions and resolves actuator conflicts.
The system is designed to minimize freely adjustable plasma control parameters, restricting operations to discrete patterns such as "start," "power control," and "stop" modes, reducing complexity and improving operator reliability.

The development of this control framework is in an early stage now. We expect the
core the system to be open-sourced and made available for new devices. To
integrate the state-oriented PCS one needs to develop the machine-agnostic layer
and define the desired operating states.

