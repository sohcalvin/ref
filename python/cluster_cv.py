import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import cvrml.common.constants as CONSTANTS
from cvrml.common.ntlk_utility import chunkArrayOfStringForNoun
from cvrml.common.file_utility import directoryFilesToArrayString
from cvrml.common.file_utility import stripTags
import codecs
from sklearn import feature_extraction
import pickle

from cvrml.common.model_utility import load_training_cv_for_cat

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def br():
    print("----------------------------------------------------------------------")

def load_training_cv_category(location):
    outdata= []
    for file_name in os.listdir(location):
        if file_name.startswith(".") : continue
        with open(os.path.join(location,file_name), encoding="utf-8") as fin:
            doc = fin.read()
            outdata.append(doc)
    return outdata

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

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

# cv_jobs = load_training_cv_category(CONSTANTS.TRAINING_CV["job"])
def readAndSave():
    dataDirs = ["C:/tmp/datax-cv/resumes_and_jobs/backend_developer_jobs"
        ,"C:/tmp/datax-cv/resumes_and_jobs/business_developer_jobs" ]

    docData = []
    for dir in dataDirs :
        docData.extend(directoryFilesToArrayString(dir))
    print("Number of Files = ", len(docData))

    cv_jobs = stripTags(docData)
    cv_jobs = chunkArrayOfStringForNoun(cv_jobs)
    pickle.dump(cv_jobs, open("deleteme.p", "wb"))
    # exit()

# readAndSave()

cv_jobs = pickle.load(open("deleteme.p","rb"))
print("Number of jobs cv = {0}".format(len(cv_jobs)))

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in cv_jobs:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print(vocab_frame)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,2))

tfidf_matrix = tfidf_vectorizer.fit_transform(cv_jobs)
terms = tfidf_vectorizer.get_feature_names()
print(tfidf_matrix.shape)
print(tfidf_matrix)
print(terms)

# from sklearn.metrics.pairwise import cosine_similarity
# dist = 1 - cosine_similarity(tfidf_matrix)
# print(len(dist[0]))
# exit()

from sklearn.cluster import KMeans
num_clusters = 2
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
print(km.n_clusters)

clusters = km.labels_.tolist()
print("Length of cluster variable= {0}".format(len(clusters)))
print(clusters)

br()

import pandas as pd

data = { 'doc': cv_jobs, 'cluster': clusters}
frame = pd.DataFrame(data, index = [clusters] , columns = ['doc', 'cluster'])
# print(frame)

br()

# from __future__ import print_function

print("Top terms per cluster:")
print()
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
print(km.cluster_centers_.argsort())
for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind], end=',')
        # print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print()
    print()
    print("Cluster %d doc:\n" % i, end='')
    for title in frame.ix[i]['doc'].values.tolist():
        print(title[:230])
    print()
    print()

