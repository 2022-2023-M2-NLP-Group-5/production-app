# OpenSemShift

Sources of our web application for our tool [Open SemShift](https://github.com/2022-2023-M2-NLP-Group-5/OpenSemShift).  

Open SemShift is available [here](https://opensemshift.herokuapp.com/).

Find more about [Open SemShift](https://github.com/2022-2023-M2-NLP-Group-5/OpenSemShift).  

## Authors 
It was realised by [Aguiar Mathilde](https://github.com/MathildeAguiar), [So Averie Ho Zoen](https://github.com/averieso), [Tankard Scott](https://github.com/tabbyrobin) and [NGO Van Duy](https://github.com/thebugcreator) for the 2022-2023 Software Project (UE905 EC1) at IDMC (Nancy), under the supervision of [Esteban Marquer](https://emarquer.github.io/) and [Miguel Couceiro](https://members.loria.fr/mcouceiro/).

## Abstract
Lexical semantic change is a topic that attracts interest from a wide range of audiences, ranging from historical linguists to the general public. The OpenSemShift project aims to answer a question like "how does the word *gay* change from meaning *merry* to *homosexual*?" Traditionally, the answers may be answered by etymological accounts or by citing historical events. By temporally adapting pre-trained, contextualised word embeddings with the mBERT model and clustering, we present a tool that can visualise this kind of semantic change over time. We find that our multilingual model achieves comparable performance in semantic change detection compared to previous approaches, and additionally, that multilingually fine-tuned mBERT is beneficial to such a task. We present several case studies via our visualisation component and discuss wider implications for future research.

## Content
- [Install and usage instructions](#install-and-usage-instructions)
- [Repository structure](#repository-structure)

## Install and usage instructions

To build the webapp locally follow these instructions. 

First install dependencies with:
```bash
  pip3 install -r requirement.txt
```

Then to access the website in local:
```bash
  $ python3 run.py
```
Access it at the following [address](http://127.0.0.1:5000/). 

## Repository structure
- [`README.md`](/README-example.md): this file.
- [`run.py`](/run.py): To launch the Flask server and access to the website.
- [`historical_events_data/`](/historical_events_data/): List of the historical events used for our visualizations.
- [`model_outputs/`](/model_outputs/): Raw CSV outputs from our models.
- [`words_data/`](/words_data/): folder for the words available to query.
- [`app/`](/app/): folder containing all the main source code for the webapp.
    - [`results/templates/`](/results/templates/): folder containing the templates (HTML files).
    - [`results/static/`](/results/static/): folder containing the images/static files.
