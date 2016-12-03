import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
# import mpld3
from sklearn.feature_extraction.text import TfidfVectorizer
# Getting a list of stop words used
def describeStopWords():
    stopwords = nltk.corpus.stopwords.words('english')
    print(stopwords[:10]) # print first 10 stopwords
    print("Total number of stopwords={0}".format(len(stopwords)))
# describeStopWords()

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")


# here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed
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




def describePandaDataFrame() :
    wordArray = ["apple", "banana", "cantalope"]
    wordIndex = ["a", "b", "c"]

    vocab_frame = pd.DataFrame({'words': wordArray}, index = wordIndex)
    print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')

# describePandaDataFrame()


def describeTfid():
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,2))

    in_text = ["Tommy is a boy", "Mary is Tommy sister", "Maggie is both their friend"]
    text_transformed = tfidf_vectorizer.fit_transform(in_text) # This is actually
    # tfidf_vectorizer.fit(in_text)
    # text_transformed = tfidf_vectorizer.transform(in_text)

    feature_names = tfidf_vectorizer.get_feature_names()

    print("In Text          = ", in_text)
    print("Text Transformed(",type(text_transformed)," of shape ",text_transformed.shape ,") =\n", text_transformed)
    print("Vocab = ",tfidf_vectorizer.vocabulary_)
    print("Feature names    = ", feature_names)
    print("Stop words \n", tfidf_vectorizer.get_stop_words())

    # xtext_transformed = tfidf_vectorizer.transform(["Tommy is a boy", "Mary is dancing"])
    # print(">>",  xtext_transformed)

########### Start ###############################

inText = "It'll be alright in the end. If it's not alright, it's not he end! It was from a movie."
tokenizedStemmedText = tokenize_and_stem(inText)
tokenizedOnlyText = tokenize_only(inText)
print("InText={0}\nTokenizedStemmedText={1}\nTokenizedOnlyText   ={2}".format(inText, tokenizedStemmedText, tokenizedOnlyText))

print("\n--------------------------------")

describeTfid()


