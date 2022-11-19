:warning: NOTE: this is the sandbox (scratch) repo. See other repo for full and proper Readme.

# Tracing and visualizing diachronic semantic change using contextualized embeddings

## Project formalisation

Working draft project goal proposal:

tracing and visualizing diachronic semantic change 
using contextualized embeddings (from m-BERT),
with re-training on an array of multilingual time-segmented corpora

(With 1 model per time segment. Example: Model A: 1910 english + 1910 french.
Model B: 1920 english + 1920 french.)

Tracing: putting in relation of multiple quantified (non-binary) measurements (of semantic change).

Underlying core-core part here is: get quantified measurements of semantic change from the model (m-bert).

## Extra steps and components we may add

As first step: set-up with just 1 language, for 2 time periods. 
Later, add additional languages into the corpuses and re-train the models.

Bonuses:

+ Run experiments on multi-senses vs single-averaged sense (WITHOUT testing on different types of semantic change)

+ analyzing multiple languages in comparison to each other (e.g. evolution of Sir/Monsieur in eng/fr)

+ historical event contextualization (database...)

+ future semantic change prediction

Non-goals (explicitly excluded from project scope):

- exploring the multilinguality inside multilingual models

- doing multiple monolingual applications %(in array -- rinse-repeat, each independent from the other)

## Other notes

Full COHA requires purchase ($375 minimum) but it seems a subset can be downloaded free:
https://www.corpusdata.org/formats.asps

Plaintext sample is here (9 mb zip, 25 mb extracted):
https://www.corpusdata.org/coha/samples/text.zip

Underlying core-core part here is: get quantified measurements of semantic change from the model (m-bert).
For which we need:
- Multiple Bert models (diachronically segmented)
- code to extract measurements from them
