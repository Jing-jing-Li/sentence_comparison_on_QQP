# sentence_comparison_on_QQP

## Abstract
In my work, I focused on sentence comparison on QQP dataset using count vectorizer method and SBERT method.

## Notice

* Since some files are too large to upload to github, please download the two files before using it:

(1) quora_duplicate_questions.tsv at http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv

(2) a model file at https://drive.google.com/file/d/1McSMxMHCiQCd1PPxCGPI721PpShYpu6B/view?usp=sharing

* Please change the data file path before using it

## Framework of the repository

This github repository includes:

### (1) data files

* quora_duplicate_questions.tsv

The original data file.

* abbreviation.csv

A list of abbreviations. It is used for the comparison of abbreviation part.

### (2) data preprocession file

* data_preprocessing.py

Please change the path of data in this file

### (3) count vectorizer part

* count_vectorizer_original.ipynb

Include the application and evaluation of count vectorizer model on QQP dataset.

* count_vectorizer_example.ipynb

Include some examples of question pairs, typos and abbreviation comparison examples.

* count_vectorizer_noun.ipynb

It extract the nouns in sentences and compare the nouns.

### (4) SBERT part

* SBERT_pretraining_evaluation.ipynb

It use the all-MiniLM-L6-v2 model to classify the question pairs.

* SBERT_model_training.ipynb

It trained the SBERT model by training set of QQP dataset.

* SBERT_training_evaluation.ipynb

The evaluation of the model trained by QQP dataset.

* SBERT_abbreviation_evaluation.ipynb

It evaluated the abbreviations using SBERT model.

### (5) model

It includes the trained model of SBERT using QQP dataset. Please put the downloaded model file in this file befor using it.
