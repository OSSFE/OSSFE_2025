---
title: 'Thermavip: an open source framework for multi-sensor data acquisition, processing and visualization'
authors:
  - name: Victor Moncada
    affiliations:
      - CEA
  - name: Xavier Courtois
    affiliations:
      - CEA
  - name: Leo Dubus
    affiliations:
      - CEA
  - name: Erwan Grelier
    affiliations:
      - CEA
  - name: Sebastien Vives
    affiliations:
      - CEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Current tokamaks are equipped with more and more diagnostics generating huge amount of sensor data, especially when considering video diagnostics like visible and infrared (IR) cameras. Developing software tools for sensor acquisition, online multi-sensor display and offline visualization/processing is a complex task that requires dedicated libraries.

In this paper, we introduce the Thermavip open-source software platform dedicated to these tasks. This software aims to gather within the same framework libraries for 1) Firm real-time sensor acquisition and display in control rooms, 2) offline visualization and post processing of multi-sensor data with a strong emphasis on video ones, 3) video annotation and thermal event database management to train deep-learning models, like Region Based Convolutional Neural Network, for automatic detection and classification of thermal events based on IR movies. This software platform is widely used on the WEST tokamak for offline study of all WEST diagnostics data using the Librir open-source library, but also for online display of IR videos and temperature time traces for critical Plasma Facing Components (PFC). Thermavip platform is also used on the EAST tokamak (ASIPP/China) for IR video post-processing, and on the W7-X Stellarator (IPP/Germany) for the IR diagnostic acquisition (during OP1.0), PFC monitoring, online display and offline video analysis.

The Thermavip framework is composed of a C++ Software Development Kit (SDK) providing high-level classes for offline/real-time analysis and visualization of multi-sensor data. Its strength comes from its unique component block architecture, allowing to build multicore and distributed processing pipelines for both offline and real-time applications. The framework can be used as a foreign library for external application, or as an independent software relying on third party plugins. Thermavip is available on Github with a liberal 3-Clause BSD License.


# Repository
https://github.com/IRFM/thermavip

