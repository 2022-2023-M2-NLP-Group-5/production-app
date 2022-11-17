# My Awesome Readme project

>*A sandbox dedicated to the S9's project. Here our work can be a bit messy, like a draft.*

> *Just a draft of the readme we need to hand over*

The current repository contains the data, code and results of the PROJECT NAME project.
It was realised by Mathilde AGUIAR, NGO Van Duy, Averie (Ho Zoen) SO, and Scott TANKARD, 
for the 2022-2023 Software Project (UE905 EC1) at IDMC (Nancy), under the supervision of Esteban Marquer and Miguel Couceiro.

## Abstract

> this section TBD

The My Awesome Readme project is designed as a guideline and a starting point for the `README.md` file requested for the Software Project GitHub repository. It is not meant to represent a specific project but to give key points to write a readme following the instructions.

## Content
- [Install instructions](#install-instructions)
- [Usage instructions](#usage-instruction)
- [Repository structure](#repository-structure)

## Install instructions

This project was designed and tested using Python 3.10.
To setup the project, you have to:
1. clone the repository;
2. [install the Python dependencies](#python-dependencies);
3. [download the datasets](#).

### Python dependencies
It is recommended to use Anaconda to have a dedicated environment for the project.
You can also use Pip.

#### Anaconda setup
Follow the following steps to setup the project with Anaconda.
1. Install Anaconda.
2. Create the environement:
    ```bash
    conda create --name my-awesome-readme python==3.10 pip
    ```
3. Install the necessary packages:
    ```bash
    conda install -y --name my-awesome-readme .............
    ```

Any command mentionned further in this file will assume that you have activated the Anaconda environment using `conda activate my-awesome-readme`.

#### Pip setup
Follow the following steps to setup the project with Pip.
1. Install Python 3.10.
2. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

### Dataset
To download the dataset, do as follows....

## Usage instructions
### Basic usage
To run this project using the existing models, run the following after replacing `[file to process.txt]` by the name of your file:
```bash
python main.py [file to process.txt]
```

### Reproduce the experiments mentionned in the report
To reproduce the experiments mentionned in the report, run the following commands:
```bash
python experiment1.py
python experiment2.py
```

## Repository structure

- [`README.md`](/README.md): this file.
- [`articles/`](/articles/): folder containing all the articles read or mentioned in the report, as PDFs. Each file is labled using the template `[article topic]-[publication year]-[authors' last names].pdf`; if more than 3 authors are present, `[authors' last names]` is replaced by `[first author's last name]-et-al` instead. *You can dump all the interesting papers that you find.*

> below here is TBD 

- [`main.py`](/main.py): Python script for training the models.
- [`experiment1.py`](/experiment1.py): Python script to run the experiment on the synthetic data, mentionned in section 4.2. of the report.
- [`experiment2.py`](/experiment2.py): Python script to run the experiment on the real-world data from ..., mentionned in section 4.4. of the report.
- [`report/`](/report/): folder for project report PDF `Final_report-My_Awesome_Readme.pdf`.
- [`presentations/`](/presentations/): folder containing all the intermediate presentations as PDF (must be updated before each presentation session). Each file is labled using the template `[date]-Presentation_[presentation number]-My_Awesome_Readme.pdf`. *This template is my personal preference. You can use your own, as long as it is clear from the name which presentation corresponds to which file.*
- [`results/`](/results/): folder containing all the results generated during the project.
    - [`results/models/`](/results/models/): folder containing the models trained during the project.
    - [`results/plots/`](/results/plots/): folder containing the plots describing the performance and the experiments.
    - [`results/solutions/`](/results/solutions/): folder containing the solutions to the Ultimate Question of Life, The Universe, and Everything.

Note: Readme file based on template by E. Marquer: https://gist.github.com/EMarquer/b6dec298d23e82440cf49b69b2d71ebc
