import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import cvrml.common.constants as CONSTANTS
import codecs
from sklearn import feature_extraction
from bs4 import BeautifulSoup
from cvrml.common.ntlk_utility import chunkArrayOfString

from cvrml.common.file_utility import directoryFilesToArrayString
from cvrml.common.file_utility import stripTags

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def br():
    print("----------------------------------------------------------------------")


def stripTagsOfSummary(arrayOfString) :
    arrayOfSummary = []
    for j in arrayOfString :
      soup = BeautifulSoup(j, 'html.parser')
      jobtitle = soup.select_one(".jobtitle")
      jobsummary = soup.select_one("#job_summary")
      arrayOfSummary.append(jobsummary.get_text())
    return arrayOfSummary

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tfidIt(arrayOfText):
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=200000,
                                 min_df=0, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem)#, ngram_range=(1,3))
    dummyMatrix = tfidf_vectorizer.fit_transform(arrayOfText)
    terms = tfidf_vectorizer.get_feature_names()
    # print(dummyMatrix)
    print(len(terms))
    print(terms)

data = directoryFilesToArrayString("c:/tmp/jobs/")

print(stripTags(data[0:1]))

# arrayOfSummary = []
# for j in datax :
#       soup = BeautifulSoup(j, 'html.parser')
#       jobtitle = soup.select_one(".jobtitle")
#       jobsummary = soup.select_one("#job_summary")
#       arrayOfSummary.append(jobsummary.get_text())
# br()
#
# grammar="NP: {<NN|NNP|NNPS|NNS><NN|NNP|NNPS|NNS>?}"
# chunkedArrayOfSummary = chunkArrayOfString(arrayOfSummary, grammar)
# print(chunkedArrayOfSummary[1])




