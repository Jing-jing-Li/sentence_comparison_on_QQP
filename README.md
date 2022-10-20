# sentence_comparison_on_QQP

## Abstract
In my work, I focused on sentence comparison on QQP dataset using count vectorizer method and SBERT method.

## Framework of the repository

This github repository includes:

(1) data files

* quora_duplicate_questions.tsv

The original data file. It can be downloaded at http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv , because it is too larget and can not be uploaded to github.

* abbreviation.csv

A list of abbreviations. It is used for the comparison of abbreviation part.

(2) data preprocession file

* data_preprocessing.py

Please download the data files and change the path of data files before using it.

(3) count vectorizer part

* count_vectorizer_original.ipynb

Include the application and evaluation of count vectorizer model on QQP dataset.

* count_vectorizer_example.ipynb

Include some examples of question pairs, typos and abbreviation comparison examples.

* count_vectorizer_noun.ipynb

It extract the nouns in sentences and compare the nouns.

(4) SBERT part

* SBERT_pretraining_evaluation.ipynb

It use the all-MiniLM-L6-v2 model to classify the question pairs.

* SBERT_model_training.ipynb

It trained the SBERT model by training set of QQP dataset.

* SBERT_training_evaluation.ipynb

The evaluation of the model trained by QQP dataset.

* SBERT_abbreviation_evaluation.ipynb

It evaluated the abbreviations using SBERT model.

(5) model

It includes the trained model of SBERT using QQP dataset. However, one file is too large, so please download it on google drive https://drive.google.com/file/d/1McSMxMHCiQCd1PPxCGPI721PpShYpu6B/view?usp=sharing befor using it.
