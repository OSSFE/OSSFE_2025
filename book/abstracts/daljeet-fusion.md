---
title: 'Fusion Data Lake: An IAEA proposal for international data sharing for AI/ML applications in fusion energy research'
authors:
  - name: Daljeet Singh Gahle
    affiliations:
      - IAEA
  - name: Matteo Barbarino
    affiliations:
      - IAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The scale and accessibility of AI/ML techniques have exploded over the past 10 years. A number of open-source and/or freemium AI tools such as Tensor Flow, PyTorch, Chat-GPT, and DeepSeek as brought AI from a niche area of research to a mainstream aspect of people’s lives. AI is reshaping daily life and industry alike, spanning personal, professional, and enterprise-scale operations.

Experimental and computational fusion energy research in both magnetic and inertial confinement fusion are embracing a broad and novel applications of AI. To support and enhance this effort the International Atomic Energy Agency (IAEA) is running a 5-year Coordinated Research Project (CRP) “Artificial Intelligence for Accelerating Fusion Research and Development", or AI for Fusion (AI4F) from 2022 to 2027 bringing together 24 institutions from 11 countries across 4 continents [1]. The AI for Fusion CRP is taking a holistic approach to the development of AI tools by going beyond applications for research, by including data platforms and workforce development. The Fusion Data Lake, an IAEA initiative, aims to design, build, and operate a modern data platform that simplifies data sharing across borders and institutions, offering a seamless and reliable way to query data both manually and programmatically.

The Fusion Data Lake will have two core functionalities:
1)	A centralised portal of federated database of all publicly accessible fusion data,
2)	A modern data platform which can be programmatically integrated into data pipelines for collaborations to store their data,

And the technological components fit into three main areas:
1)	Platform design and architecture
2)	Metadata and data model
3)	Platform and data regulations

The platform architecture uses standard tools in data engineering (such as Microsoft Azure, Python, and Terraform) and best practices from software engineering to design a simple data lake which builds dynamically from the metadata. This solves both the problems of developing a data catalogue, and having a storage structure that is automated and intuitive to humans. On top of this storage system will be two user-interfaces: (1) Python API for programmatic access, and (2) a publicly accessible containerised webapp. The Python API will provide the functionality to ingest, query, and egress data, while the focus of the webapp will be to query, view, and download data. In the configuration of computation resources there will be a bias towards the API to enable timely access to the data to enable integration in AL/ML pipelines. The computational resource for the webapp will be provisioned to allow a number of users to query and view data in parallel. 

The metadata and data model for the platform will build on and support the development of the ITER Organization’s Integrated Modelling & Analysis Suite (IMAS) Data Dictionary to provide the descriptive framework for all data in the Fusion Data Lake [2]. This model is integral in the design of the data lake as a subset of the metadata is used dynamically to build the lake structure while simultaneously build the data catalogue for the Fusion Data Lake. By entwining the storage structure with the metadata, the data catalogue is inherently built as the data lake is populated. This mitigates a common problem of data platforms of having unknown and unregistered data in storage.

The platform regulations and data protections are key to the adoption of the Fusion Data Lake and to facilitate institutional support for the use of the platform. The sensitivity of a collaboration depends on a number of factors including the age of the data, the policies of the institution, and interactions between the public and private sector. Consequently, the Fusion Data Lake will have a tiered approach to data access. These tiers will be:
1)	Public – The data will be accessible to anyone. No login credentials required. 
2)	Internal – The data will be accessible to anyone with login credentials to the platform.
3)	Restricted – The data will only be accessible to individuals with login credentials from institutions approved by the data owner.
4)	Closed – The data will only be accessible to individuals approved by the data owner, with login credentials to the platform.

This will give researchers a medium to share their data to a level of privacy they choose and to integrate the platform into their AI/ML analysis pipelines programmatically. In addition to this the federated part of the data base giving access to FAIR and open data hosted by the IAEA’s external partners. 

The Fusion Data Lake can play a pivotal role in bridging the gap in data infrastructure to facilitate Big Data analytics as currently there are no scalable, accessible, and inclusive platforms to facilitate Big Data analytics. Developments in fusion energy research have always been the result of large collaborations. Data sharing platforms, by increasing the access to data inline with open science and FAIR data principles, will accelerate progress towards achieving commercial fusion energy be enabling AI/ML and Big Data methods. 

References:
1.	AI for Fusion – https://nucleus.iaea.org/sites/ai4atoms/ai4fusion/SitePages/AI4F.aspx 
2.	IMAS Data Dictionary documentation – https://imas-data-dictionary.readthedocs.io/en/latest/ 


