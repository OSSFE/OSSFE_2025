---
title: 'Open-source framework for infrared thermography exploitation in fusion'
authors:
  - name: Léo Dubus
    affiliations:
      - CEA-IRFM
  - name: Victor Moncada
    affiliations:
      - CEA-IRFM
  - name: Erwan Grelier
    affiliations:
      - CEA-IRFM
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Infrared (IR) Thermography diagnostics are widely adopted in tokamaks due to their importance for both machine protection and physics studies. Each IR instrument manufacturer provides its own video file format, which does not necessarily fit tokamak acquisition ecosystems. Furthermore, exploiting IR data to ensure components safety requires advanced software tools to manage video thermal events. For more than a decade, IRFM has developed its infrared video exploitation framework, and used it on WEST and since 2022, IRFM opened it to the community and keeps maintaining it: 
-	librir: A bedrock library standardizing IR video file format, providing efficient video compression and processing for fusion applications and simplifying I/O manipulation, written in C++/Python. 
-	thermal-events: A Python package handling the thermal events and the interaction with the thermal events database.

These libraries, available on GitHub, can be used on every fusion machine exploiting IR videos. Indeed, they enable users to efficiently handle their infrared video data pool and create relevant thermal event datasets from infrared video data in a research-friendly manner. These datasets are employed to train and assess deep-learning models for the automatic analysis of the thermal scene using IR movies. The thermal-event library can store/retrieve thermal events to/from JSON files as well as MySQL databases.
In order to promote cross-machine collaboration, these standards aim to make it easier for researchers to share data, such as infrared video and annotations, across multiple machines. They address the need for standardized infrastructure, enabling seamless integration of diverse machine systems through a complete framework. By addressing this challenge, we establish a common foundation for joint research initiatives in fusion technology development. 

Currently, this framework is being used in various use cases on different machines:
1)	Thermavip software (also presented in this conference) is available on WEST, EAST and W7-X for offline video analysis and video annotation.
2)	A cross-machine dataset was deployed on the EUROfusion gateway, serving as a foundational resource for training intelligent models that leverage these datasets
3)	WEST IR video data storage on IMAS (Integrated Modelling and Analysis Suite), the ITER standard for storing data, will be in the format defined by librir for WEST.

Both librir and thermal-events are under the BSD 3-Clause License.


# Repository
https://github.com/IRFM/librir

