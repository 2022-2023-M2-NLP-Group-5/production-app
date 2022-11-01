## literature
### on analogy
1. [Transferring Learned Models of Morphological Analogy (Esteban Marquer, Pierre-Alexandre Murena and Miguel Couceiro)](https://github.com/pmonnin/ata2022-papers-slides/raw/main/papers/ICCBR_2022_Workshop_paper_71.pdf) [<ins>slides</ins>](https://github.com/pmonnin/ata2022-papers-slides/raw/main/slides/ATA_2022_emarquer.pdf) [<ins>workshop link</ins>](https://iccbr-ata2022.loria.fr/schedule/)
2. [E. Marquer, M. Couceiro, S. Alsaidi, A. Decker, Siganalogies - morphological analogies from Sigmorphon 2016 and 2019, 2022.](https://hal.inria.fr/hal-03313591/)
3. [Lim, S., Prade, H., Richard, G.: Solving word analogies: A machine learning per- spective. In: the Proceedings of the 5th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty, ECSQARU 2019. vol. 11726, pp. 238–250 (2019)](https://link.springer.com/chapter/10.1007/978-3-030-29765-7_20)
4. [On word analogies and negative results in NLP (Anna Rogers)](https://hackingsemantics.xyz/2019/analogies/)

### on detecting diachronic semantic change
1. [A Wind of Change: Detecting and Evaluating Lexical Semantic Change across Times and Domains, 2019](https://arxiv.org/pdf/1906.02979.pdf)
2. [Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change,2019](https://arxiv.org/pdf/1605.09096.pdf)
3. [Dynamic Language Models for Continuously Evolving Content, 2021](https://dl.acm.org/doi/pdf/10.1145/3447548.3467162)
4. [Mind the Gap: Assessing Temporal Generalization in Neural Language Models, 2021](https://proceedings.neurips.cc/paper/2021/file/f5bf0ba0a17ef18f9607774722f5698c-Paper.pdf)
5. [Diachronic word embeddings and semantic shifts: a survey, 2018](https://arxiv.org/pdf/1806.03537.pdf)
6. [SemEval-2020 Task 1: Unsupervised Lexical Semantic Change Detection](https://aclanthology.org/2020.semeval-1.1.pdf) - manually annotated test set available [<ins>talk</ins>](https://underline.io/lecture/6403-semeval-2020-task-1-unsupervised-lexical-semantic-change-detection)

### on using analogy to detect diachronic semantic change (also see codebase)
1.  [Yating Zhang, Adam Jatowt, Sourav Bhowmick, and Katsumi Tanaka. 2015. Omnia mutantur, nihil interit: Connecting past with present by finding corresponding terms across time.](https://aclanthology.org/P15-1063.pdf)
      - main finding: using reference points (like an analogy pair) is better than just doing a global search
3.  [Andrey Kutuzov, Erik Velldal, and Lilja Øvrelid. 2017a. Temporal dynamics of semanticrelations in word embeddings: an application to predicting armed conflict participants.](https://arxiv.org/pdf/1707.08660.pdf)
4.  [Guy D. Rosin, Eytan Adar, and Kira Radinsky. 2017. Learning word relatedness over time.](https://arxiv.org/pdf/1707.08081.pdf%C2%A0%E2%86%A9%EF%B8%8E%C2%A0%E2%86%A9%EF%B8%8E)

## data
1. [google books ngram](https://storage.googleapis.com/books/ngrams/books/datasetsv3.html)
2. [Test Data for SemEval-2020 Task 1: Unsupervised Lexical Semantic Change Detection](https://www.ims.uni-stuttgart.de/en/research/resources/corpora/sem-eval-ulscd/)
3. [Various evaluation benchmarks regarding semantic analogies for English and for German (uni stuttgart)](https://www.ims.unistuttgart.de/en/research/resources/lexica/analogies/)
4. [Google analogy test set by Mikolov 2013 (State of the art)](https://aclweb.org/aclwiki/Google_analogy_test_set_(State_of_the_art))

## codebase
1. [Terrence Szymanski. 2017. Temporal word analogies: Identifying lexical replacement with diachronic word embeddings.](https://researchrepository.ucd.ie/bitstream/10197/9166/1/insight_publication.pdf) [<ins>github</ins>](https://github.com/tdszyman/twapy)
   - methodology: train vector spaces independently for each time period, then map into a common space via matrix transformation
