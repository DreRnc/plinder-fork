![plinder](https://github.com/user-attachments/assets/05088c51-36c8-48c6-a7b2-8a69bd40fb44)

<div align="center">
    <h1>The Protein Ligand INteractions Dataset and Evaluation Resource</h1>
</div>

---

[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/plinder-org/plinder/blob/master/LICENSE.txt)
[![publish](https://github.com/plinder-org/plinder/actions/workflows/main.yaml/badge.svg)](https://github.com/plinder-org/plinder/pkgs/container/plinder)
[![website](https://img.shields.io/badge/website-plinder-blue.svg)](https://www.plinder.sh/)
[![bioarXiv](https://img.shields.io/badge/bioarXiv-2024.07.17.603955v1-blue.svg)](https://www.biorxiv.org/content/10.1101/2024.07.17.603955)
[![docs](https://github.com/plinder-org/plinder/actions/workflows/docs.yaml/badge.svg)](https://plinder-org.github.io/plinder/)
[![coverage](https://github.com/plinder-org/plinder/raw/python-coverage-comment-action-data/badge.svg)](https://github.com/plinder-org/plinder/tree/python-coverage-comment-action-data)

![overview](https://github.com/user-attachments/assets/39d251b1-8114-4242-b9fc-e0cce900d22f)

# 📚 About

**PLINDER**, short for **p**rotein **l**igand **in**teractions **d**ataset and
**e**valuation **r**esource, is a comprehensive, annotated, high quality dataset and
resource for training and evaluation of protein-ligand docking algorithms:

- \> 400k PLI systems across > 11k SCOP domains and > 50k unique small molecules
- 500+ annotations for each system, including protein and ligand properties, quality,
  matched molecular series and more
- Automated curation pipeline to keep up with the PDB
- 14 PLI metrics and over 20 billion similarity scores
- Unbound \(_apo_\) and _predicted_ Alphafold2 structures linked to _holo_ systems
- _train-val-test_ splits and ability to tune splitting based on the learning task
- Robust evaluation harness to simplify and standard performance comparison between
  models.

The *PLINDER* project is a community effort, launched by the University of Basel,
SIB Swiss Institute of Bioinformatics, VantAI, NVIDIA, MIT CSAIL, and will be regularly
updated.

To accelerate community adoption, PLINDER will be used as the field’s new Protein-Ligand
interaction dataset standard as part of an exciting competition at the upcoming 2024
[Machine Learning in Structural Biology (MLSB)](https://mlsb.io) Workshop at NeurIPS,
one of the field's premiere academic gatherings.
More details about the competition will be announced shortly.

## 🏅 Gold standard benchmark sets

As part of *PLINDER* resource we provide train, validation and test splits that are
curated to minimize the information leakage based on protein-ligand interaction
similarity.
In addition, we have prioritized the systems that has a linked experimental `apo`
structure or matched molecular series to support realistic inference scenarios for hit
discovery and optimization.
Finally, a particular care is taken for test set that is further prioritized to contain
high quality structures to provide unambiguous ground-truths for performance
benchmarking.

![test_stratification](https://github.com/user-attachments/assets/5bb96534-f939-42b5-bf85-5ac3a71aa324)

Moreover, as we enticipate this resource to be used for benchmarking a wide range of methods, including those simultaneously predicting protein structure (aka. co-folding) or those generating novel ligand structures, we further stratified test (by novel ligand, pocket, protein or all) to cover a wide range of tasks.

# 👨💻 Getting Started

The *PLINDER* dataset is provided in two ways:

- You can either use the files from the dataset directly using your preferred tooling
  by downloading the data from the public
  [bucket](https://cloud.google.com/storage/docs/buckets),
- or you can utilize the dedicated `plinder` Python package for interfacing the data.


## Downloading the dataset

The dataset can be downloaded from the bucket with
[gsutil](https://cloud.google.com/storage/docs/gsutil_install):

```console
$ export PLINDER_RELEASE=2024-06 # Current release
$ export PLINDER_ITERATION=v2 # Current iteration
$ gsutil -m cp -r gs://plinder/${PLINDER_RELEASE}/${PLINDER_ITERATION}/* ~/.local/share/plinder/${PLINDER_RELEASE}/${PLINDER_ITERATION}/
```

## Installing the Python package

The `plinder` package can be installed via

```
git clone https://github.com/plinder-org/plinder.git
cd plinder
mamba env create -f environment.yml
mamba activate plinder
pip install .
```

# 📝 Documentation

A more detailed description is available on the
[documentation website](https://plinder-org.github.io/plinder/).

# 📃 Citation

Durairaj, Janani, Yusuf Adeshina, Zhonglin Cao, Xuejin Zhang, Vladas Oleinikovas, Thomas Duignan, Zachary McClure, Xavier Robin, Gabriel Studer, Daniel Kovtun, Emanuele Rossi, Guoqing Zhou, Srimukh Prasad Veccham, Clemens Isert, Yuxing Peng, Prabindh Sundareson, Mehmet Akdel, Gabriele Corso, Hannes Stärk, Gerardo Tauriello, Zachary Wayne Carpenter, Michael M. Bronstein, Emine Kucukbenli, Torsten Schwede, Luca Naef. 2024. “PLINDER: The Protein-Ligand Interactions Dataset and Evaluation Resource.”
[bioRxiv](https://doi.org/10.1101/2024.07.17.603955)
[ICML'24 ML4LMS](https://openreview.net/forum?id=7UvbaTrNbP)

Please see the [citation file](CITATION.cff) for details.

![plinder_banner](https://github.com/user-attachments/assets/43d129f2-3bb6-4903-81fa-182c351c64b6)
