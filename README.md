# sentence_comparison_on_QQP

# Abstract
In my work, I focused on sentence comparison on QQP dataset using count vectorizer method and SBERT method.
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

* 

(4) SBERT part

One model file is large so I can't upload it on github. So I upload it on google drive https://drive.google.com/file/d/1McSMxMHCiQCd1PPxCGPI721PpShYpu6B/view?usp=sharing
Please download this file to the model folder before using the model.

# {MODEL_NAME}

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 256 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('{MODEL_NAME}')
embeddings = model.encode(sentences)
print(embeddings)
```

