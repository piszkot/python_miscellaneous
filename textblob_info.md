# TextBlob

#### TextBlob is a simple Python library for Natural Language Processing (NLP).
It provides easy-to-use tools for tasks such as:
- sentiment analysis (detecting if text is positive or negative)
- tokenization (splitting text into words or sentences)
- part-of-speech tagging (identifying nouns, verbs, etc.)
- translation and spell correction

# Corpora

#### Corpora (singular: corpus) are collections of text data used by NLP tools.
In the context of TextBlob, corpora include dictionaries, language models,
and datasets required for text analysis.
#
TextBlob relies on external data (mainly from NLTK) to function properly,
so these corpora often need to be downloaded separately using:
    python -m textblob.download_corpora

# In short:

- TextBlob = the tool/library
- Corpora = the data it uses to analyze language
