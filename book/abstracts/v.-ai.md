---
title: 'AI-enabled generative design of fusion components'
authors:
  - name: V. I. Perumal
    affiliations:
      - CAMINNO
  - name: R. Frye
    affiliations:
      - CAMINNO
  - name: A. Manikandan
    affiliations:
      - CAMINNO
  - name: D. Beckett
    affiliations:
      - CAMINNO
  - name: A. Stein
    affiliations:
      - CAMINNO
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Commercialization of fusion power plants requires advanced design and engineering workflows. Current design workflows limit the design possibilities due to computational overheads associated with design optimization. Additionally, these design paradigms relies on developing complex coupled physical processes that drive the performance of a component in each of the different physics realms. In practice, this paradigm is typically plagued with two main limitations: (i) transition across multiple physics necessitates downsampling information, thus potentially filter useful information; (ii) this framework is computationally expensive, practically infeasible for multiple design development runs,and rather complex to use. Additionally, the computational complexity leads to an increase in design and manufacturing costs.

In this work, we present our use of open-source simulation tools to create simulation workflows. These workflows simulate structural, thermal, fluidic, and electromagnetic physics & manufacturing processes using open-source software. These simulation workflows are used to prepare a database for our machine learning (ML) models. The ML models are used as surrogates in a gradient-based multidisciplinary design optimization technique and can be used to expedite exploration for ideal target design. The algorithm achieves computational efficiency by replacing standard finite element solvers with their ML surrogates having similar accuracy. These surrogates can capture scale transitions in a computationally inexpensive framework compared to hierarchical scale transition approaches using high-fidelity simulations. Further surrogates provide a means to rapidly calibrate models against experimental data (i.e. formal model calibration techniques), to quantify model form uncertainty, and to quantify parametric uncertainty. Extension of this approach to other applications are also discussed.

# Repository
https://github.com/idaholab/moose

