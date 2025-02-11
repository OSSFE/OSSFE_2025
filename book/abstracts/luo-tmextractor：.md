---
title: 'TMExtractor： A software toolkit to extract Tearing Modes features'
authors:
  - name: Luo Runyu
    affiliations:
      - Zheng Wei*, Shen Chengshuo, Xue Fengming, Ai Xinkun, Zhong Yu, Ren Zhengkang, Ding Yonghua, Wang Nengchao
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

Tearing modes (TMs) can significantly degrade plasma confinement performance, thereby impacting the operational efficiency of fusion reactors. Severe tearing modes may lead to plasma disruptions, which pose considerable risks to the safe operation of these devices. Recent studies have highlighted novel approaches for tearing mode suppression, with deep learning-based methods showing promise for predicting and effectively mitigating tearing modes in the future. However, training a deep learning model requires a large amount of labeled TM data, which presents several challenges for feature extraction.

One challenge is the labor-intensive nature of labeling, as recognizing and labeling all types of modes requires extensive human expertise. Deep learning models need a large number of labeled samples, but manually annotating TM features is time-consuming and labor-intensive. Some researchers have attempted to manually label a small number of TM features and then use machine learning methods to expand the dataset. While this approach mitigates the labeling workload to some extent, it relies on training machine learning models on small datasets, which can lead to overfitting and limit the generalization ability of the model in practical applications. Another challenge is the distribution of magnetic probes. Many existing methods, such as spatial Fourier decomposition and singular value decomposition, rely on high spatial resolution magnetic probes evenly distributed along a fixed toroidal angle. However, due to engineering constraints, such as the addition of internal coils, magnetic probes on fusion devices cannot be symmetrically distributed along the toroidal angle. This asymmetry complicates the accurate extraction of mode numbers and amplitudes.

To address these issues, we have developed a procedural TM feature extraction method into a software toolkit, TMExtractor. This tool is built on the J-TEXT Disruption Database Framework (JDDB), an open-source software developed by the J-TEXT team for disruption prediction. It supports efficient parallel processing, enabling the rapid batch processing of thousands or even tens of thousands of experimental discharges, laying the groundwork for tearing mode research, especially machine learning-based methods, by providing an extensive and robust labeled tearing mode database.

TMExtractor takes as input the measurements from toroidal and poloidal magnetic probes, plasma current, and toroidal magnetic field signals. The output includes TM mode numbers, amplitudes, frequencies, and information on the odd-even coupling modes under n=1 conditions. Its core algorithms combine multiple methods, including cross-power spectrum analysis, phase analysis, Fourier decomposition, and high-low field side asymmetry decoupling, which effectively overcome the issue of asymmetric magnetic probe distribution.

To use TMExtractor, users need to install Python, JDDB, and dependencies such as NumPy and SciPy. With a simple command-line interface, users can load experimental data and execute the feature extraction algorithm. The results are stored directly in the JDDB database and exported in HDF5 format, facilitating subsequent data analysis and model training.

# Repository
https://github.com/jtext-103/jddb

