
# FORK NOTES

This fork adds install scripts and version pinning of most the dependencies. This has been tested to run on Ubuntu 22.04LTS.

To install, run the following:

```bash
curl -sSL https://raw.githubusercontent.com/zackees/Lucid_Somnambulist/main/install.sh | bash
```

Then activate the environment
```bash
conda activate somn
```

Then run the command
```bash
somn
```

And you should see the tool activate and ask for input.

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SOMN CLI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the somn CLI, select an operation (e.g. add, calculate, partition, learn, or predict) followed by the
operation-specific arguments. Documentation should describe the required arguments.

Here is a simple summary/guide:


Welcome to the somn command-line interface. 

[NORMAL USE] To make predictions from pre-trained models, use:
predict [project ID with pre-trained models] [model set ID of specific pre-trained models]  [new prediction ID]

[POWER USER USE] To retrain models, two steps are required: generating a particular set of partitions, then optimizing hyperparameters
partition-wise. These are separated so that custom preprocessing or features can be incorporated at the partition step,
and custom modeling changes can be incorporated or tested at the modeling step. New data for training should be 
incorporated into the dataset_yields.hdf5 file for inclusion in the retraining process.

To create new partitions, use:
partition [project ID, new or old project with no partitions] 

To train a new model set on partitions, use:
learn [project ID with partitions] [new ID for model set]
```

Relevant papers:

This paper explains how this codebase is supposed to be used:

https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/63e81a7afcfb27a31f9b6e66/original/development-and-validation-of-a-chemoinformatic-workflow-for-predicting-reaction-yield-for-pd-catalyzed-c-n-couplings-with-substrate-generalizability.pdf


# ORIGINAL NOTES


(C) 2023 N. Ian Rinehart and the Denmark laboratory

# Lucid_Somnambulist
Welcome to the public repository for code developed in collaboration between Hoffmann-La Roche (Process Chemistry & Catalysis in Basel, Switzerland) and the Scott E. Denmark Laboratory (University of Illinois at Urbana Champaign) to provide experimentalists rapid access to predicted reaction yields for Buchwald-Hartwig couplings. 

This repository is under development.

This work has a dependency on code developed within the Denmark Laboratories, which can be found here: https://github.com/SEDenmarkLab/molli_firstgen.git. 

# Description
 This repository contains a working project for a command-line tool that is meant for a non-expert. That tool still requires a basic understanding of how to install and run a command-line program on a Linux machine. The input of structures will be restricted to smiles strings (which can be obtained from most molecular drawing programs), cdxml (Chemdraw XML), or mol2 files. From those inputs, the workflows module has scripts which can be used from command-line to generate 3D geometries, perform a conformer search, calculate atomic properties necessary for RDF descriptors, and then calculate those RDF descriptors. Following that, a workflow to generate predictions for said new reactants can be used, and will take a set of pre-trained neural network models to make predictions. 
 The output, for now, will be a .csv file (which can be opened in text editors or Microsoft Excel) with predicted yields and their associated reaction handles. Visualizations have been developed which are more user-friendly, and they will be released when they are ready [5.10.2023]. Note that expectations of performance should be based on the discussion in the manuscript (10.26434/chemrxiv-2022-hspwv-v2). Specifically, requesting predictions for couplings far outside of the scope of the dataset will produce suboptimal performance. The best way to understand this is by looking at the supporting information, where a list of dataset couplings is provided along with a one-page summary for each coupling of the models’ prediction performance on each coupling.
 
 This repository contains the code necessary to "restart" the active learning workflow described in the associated preprint article with this work: 10.26434/chemrxiv-2022-hspwv-v2. Doing so can improve predictive power for new types of couplings, as described in the manuscript. To do this, clone this repository and read the documentation on how to use the "workflows" section. Please note that this portion is still under development as of 5.10.2023, but supports the calculation of new reactant descriptors from smiles/cdxml/mol2 input structures, a workflow to update models when new data is added, and a workflow for making predictions on new reactants. There are further "utility" components which are still under development, in particular the prediction processing and visualization workflows. As of 5.10.2023, raw predictions are available as a .csv file. 
 
  To apply this project framework to another chemical system, the somn.data module, which contains descriptors for catalyst, solvent, and base, as well as reactants, can be changed. Doing this requires an understanding of programming. The radial distance function (RDF) descriptor developed in this work can be modified to apply to other types of reactants. For now, it is implemented for nitrogen nucleophiles, (hetero)aryl bromides, and (hetero)aryl chlorides. The necessary change (outside of the scope of this repository) would involve identifying the reactive atom, which serves as an origin for defining the RDF descriptor spherical slices (see manuscript), which is a relatively simple problem to solve. The calculation of molecular geometries and atomic properties necessary for RDF descriptor calculation will still work. 
  
# Requirements
  This code was developed on Ubuntu OS (used with 20.04 and 22.04), and has been tested some on wsl2. Further testing is planned, with the ultimate goal of releasing a container image with the necessary programs, but we recommend using Ubuntu 20.04 if possible. 
  NVidia GPUs with a compute capability above 8.6 are recommended, and will require installation of the appropriate drivers. We strongly encourage a user to see tensorflow documentation to look for latest tested linux GPU builds to ensure that the CUDA and cuDNN versions match a tested build configuration. [https://www.tensorflow.org/install/source#tested_build_configurations]
  If using CPUs, keep in mind that this tool has not been optimized for distributed CPU support during neural network training, so that may require some development. This is only recommended for users with some expertise and familiarity with tensorflow documentation. However, to run this program for just making predictions as a non-expert, this can be done without changes because that process uses pre-trained models. 
  
# Installation

This code was developed with miniconda as a package manager, and it is strongly recommended to use that. An export of the environment is provided, and this can be installed with the following command:
  
 ```bash
 conda env create --name somn --file somn.yml
 ```

Then, activate the environment:

```bash
conda activate somn
```

 Next, install molli_firstgen using pip:

- Download molli_firstgen, branch 0.2.3 [https://github.com/SEDenmarkLab/molli_firstgen.git].
- Install using pip into the somn environment following installation instructions.

Finally, download and install this package by running the following command in the top-level directory (/path/to/package/Lucid_Somnambulist/):
 
 ```bash
 pip install .
 ```
 
 Test an import:
 
  ```bash
 conda activate somn
 
 python -c "import somn"
 ```
  
 # Getting Started
 (Under development)
  
