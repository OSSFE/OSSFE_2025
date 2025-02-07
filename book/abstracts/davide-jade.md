---
title: 'JADE v4, a more robust and expandable architecture for neutronics V&V'
authors:
  - name: Davide Laghi
    affiliations:
      - Fusion For Energy
  - name: Davide Laghi
    affiliations:
      - Fusion For Energy
  - name: Alberto Bittesnich
    affiliations:
      - Fusion For Energy
  - name: Alberto Bittesnich
    affiliations:
      - Fusion For Energy
  - name: Alex Valentine
    affiliations:
      - United Kingdom Atomic Energy Authority
  - name: Alex Valentine
    affiliations:
      - United Kingdom Atomic Energy Authority
  - name: Steve C. Bradnam
    affiliations:
      - United Kingdom Atomic Energy Authority
  - name: Steve C. Bradnam
    affiliations:
      - United Kingdom Atomic Energy Authority
  - name: Marco Fabbri
    affiliations:
      - Fusion For Energy
  - name: Marco Fabbri
    affiliations:
      - Fusion For Energy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The development of JADE started in 2019 as a joint effort between Fusion For Energy, the University of Bologna and NIER engineering. At the time, JADE was focused on bringing automation and standardization to the Verification and Validation (V&V) procedures of nuclear data libraries. From the very beginning, the ambitious objective was to build an expandable open-source framework that could centralize the efforts of a community, the one of nuclear data libraries evaluators, that was characterized by limited and fragmented manpower. Since then, the tool was applied with success in helping the V&V procedures of many new nuclear data libraries releases, with a special focus on FENDL, by which JADE was officially endorsed. In the last couple of years, the tool development has been pushed forward by Fusion For Energy and UKAEA with a new objective: use the JADE framework also to perform code to code comparisons. This new collaboration led to JADE v3, a first proof of concept that ported the tool on the linux platform and allowed for the first time to run benchmarks not only with MCNP but also with OpenMC. During this phase, the JADE environment was restructured and components with different scopes were made independent and separated in different repositories. Despite all these achievements, it became clearer that adding new features to JADE was becoming increasingly harder because JADE was not initially conceived with this broader scope in mind. The code base reached a high degree of complexity and was becoming a barrier for the onboarding of new developers in the project. These reasons led to the work presented here, which focus on the latest iteration of JADE development: JADE v4. The entire core architecture has been refactored following two main principles. The first is that JADE is conceived now from the very beginning to be a framework for comparison of code-library results and not simply for library to library or for code to code. The second is that the csv data produced by JADE, which are essentially the results of the different simulations in a table format, will be now a key interface. That is, all post-processing that is transport code dependent will end with the production of the csv. This allows the JADE post-processing (plots and excel summaries) to be completely transport code independent. A side benefit of this is that a better interface is created for the JADE web app. Moreover, this will allow to expand the JADE benchmark suite only through configuration files and input templates, without the need for additional coding. Finally, the extensive refactoring also allowed to implement a series of software design best practices which significantly increased JADE robustness and expandability.

# Github repository
https://github.com/JADE-V-V/JADE

