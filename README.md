# nlp-reading-group

These are some experiments with NLP methods applied to software (source code, comments, etc).

### Preprocessing
===

##### Tokenization

1. Simple Python 2.7 tokenizer based on [Pygments](http://pygments.org): [https://github.com/bvasiles/nlp-reading-group/blob/master/simplePyLex.py](https://github.com/bvasiles/nlp-reading-group/blob/master/simplePyLex.py). Currently only for Python, can be extended very easily.

Takes as input: (1) the path to the folder with all the source code to be tokenized; (2) the filename extension of the files to be tokenized (always `\*.py` in this prototype); (3) the path to the output file.

When run on the [Django](https://github.com/django/django) code base (download or clone the repo first), it produces [this output](https://github.com/bvasiles/nlp-reading-group/blob/master/data/django.code.lexed.txt)

Example: `python simplePyLex.py ./data/django \*.py ./data/django.code.lexed.txt`

### n-grams
===

1. 