## download the movie review data set
import sys, os
import urllib.request
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
from nltk import pos_tag


import pandas as pd
import sklearn as sk
import numpy as np
import scipy as sc
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# set http proxy env variable
import os
os.environ['http_proxy'] = 'proxy.sin.sap.corp:8080'

count_vectorizer = None

def countVectorize(reviewData) :
    global count_vectorizer
    count_vectorizer = CountVectorizer(stop_words='english')
    #Fit countvectorizer
    counts = count_vectorizer.fit_transform(reviewData['message'].values)
    countsDense = counts.todense()
    return  pd.DataFrame(countsDense)

def transposeRating(reviewData) :
    codingDict = {"pos":1,"neg":0}
    reviewData['labelNew']=reviewData['rating'].map(codingDict)
    targets = reviewData['labelNew'].values
    return targets

# list to store the examples
reviews = []

# load positive reviews
for file_name in os.listdir(os.path.join(os.getcwd(), 'txt_sentoken/pos/')):
    with open(os.path.join(os.getcwd(), 'txt_sentoken/pos/', file_name)) as fin:
        # append sentiment 'pos' label and review text
        reviews.append(('pos', fin.read()))

# load negative reviews
for file_name in os.listdir(os.path.join(os.getcwd(), 'txt_sentoken/neg/')):
    with open(os.path.join(os.getcwd(), 'txt_sentoken/neg/', file_name)) as fin:
        # append sentiment 'neg' label and review text
        reviews.append(('neg', fin.read()))

# great, there are 2000 reviews in the datax set now
print(len(reviews))

# randomly split datax into 80% training and 20% testing
# each example is a tuple consisting of a (pos/neg)  sentiment label
# and the text of the review
import random
random.seed(42)
random.shuffle(reviews)

reviews = pd.DataFrame(reviews)
reviews.columns = ["rating", "message"]

size_train = int(len(reviews)*0.8)
reviews_train = reviews[:size_train]
reviews_test = reviews[size_train:]

print("size of training set:", len(reviews_train))
print("size of test set:", len(reviews_test))

# let's look at a few examples of the training set
import pprint
pp = pprint.PrettyPrinter(indent=3)
#pp.pprint(reviews_train[:3])

print("""-------------------------------- Data ready : Exploring ---------------------------""")
def printReviewSummary(reviewData) :
    print(reviewData.groupby('rating').describe())

def prepareReviewData(reviewData) :
    # Add length column of message size
    reviewData['length'] = reviewData['message'].map(lambda text : len(text))

def plotReviewLengthHistogram(reviewData) :
    #reviewData.length.plot(bins=20, kind="hist")
    reviewData.hist(column='length', by = 'rating', bins=30)
    plt.show()

def buildNaiveBayesModel(X,Y) :
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X,Y)
    return classifier


printReviewSummary(reviews_train)
prepareReviewData(reviews_train)
# plotReviewLengthHistogram(reviews_train)

print("""-------------------------------- Naive Bayes ---------------------------""")
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()
def lemmatize(token):
    tag = pos_tag([token])
    #return tag[0][1]
    return lemmatizer.lemmatize(token, tag[0][1])

def stem_tokens(tokens,stemmer):
    tokenLower=[token.lower() for token in tokens]
    return [stemmer.stem(token) for token in tokenLower]

def tokenize(text):
    stemmer=PorterStemmer()
    text = "".join([ch for ch in text if ch not in string.punctuation]) # Strips punctuation
    tokens = nltk.word_tokenize(text)
    tokensNoStop=[]
    stems = stem_tokens(tokens, stemmer)
    #lemma = list([lemmatize(t) for t in stems ])
    #print(">>>" + str(stems))
    #print(">>>" + str(lemma))
    return " ".join(stems)

def processReviewData(reviewData) :
    reviewData['message'] = reviewData["message"].apply(tokenize)

#reviews = reviews[0:10]
processReviewData(reviews)

#print(reviews)
X = countVectorize(reviews) # This is starting from the full dataset
Y = transposeRating(reviews)
print(X)
print(type(X))
print("====")
print(Y)
print(type(Y))

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=4)

print("Data Set Shapes trainX%s trainY%s testX%s testY%s" %(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape))

model = buildNaiveBayesModel(X_train, Y_train)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

#print(">>>prediction  =" + str(len(test_pred)))
print("Prediction score is " , model.score(X,Y))
from sklearn import metrics
print( "Train Accuracy :", metrics.accuracy_score(Y_train, train_pred))
print( "Test Accuracy :", metrics.accuracy_score(Y_test, test_pred))

# One record test
X_test1 = X_test[0:1]
Y_test1 = Y_test[0:1]

print(X_test.shape)
print(X_test1.shape)
test_pred1 = model.predict(X_test1)
print("Actual " + str(test_pred1) + " vs expected " + str(Y_test1))
print( "Test Accuracy:", metrics.accuracy_score(Y_test1, test_pred1))

def classifyText(text) :
    cv = CountVectorizer(stop_words='english', vocabulary=count_vectorizer.vocabulary_);
    X_test2 = cv.transform([text])
    return model.predict(X_test2)


"""------------------------------ Flask -----------------------"""
from flask import Flask, render_template
from flask import request
import traceback
app = Flask(__name__)
@app.route("/")
def main():
    #render_template('index.html')
    review_text = request.args.get('review_text')
    result = None
    try :
        if(review_text) :
            result =  classifyText(review_text)
    except :
            print('>>> traceback <<<')
            traceback.print_exc()
            print('>>> end of traceback <<<')
    resultString =""

    if(len(result)) :
        if(result[0] == 1 ) :
            print("I am hereasdfasdf")
            resultString = "This review is <b>positive<b> :<br>"
        else :
            print("I am here")
            resultString = "This review is negative :<br>"
    else :
        print("What the hell?")
    print(resultString)
    return """
    <html>
    """ + resultString + str(review_text) + """
        <hr>
        <form>
        Enter text : <textarea rows="5" cols="50" name="review_text"></textarea>
        <input type="submit"></input>
        </form>
    <html>
    """

if __name__ == "__main__":
    app.run()

"""---------------------------------------------------------------------"""

print( classifyText("This is a great movie with strong performances") )
print( classifyText("This is a bad movie with strong performances") )
#idx = len(X_train)
#rawRec = reviews[idx:idx+1]
#pd.options.display.max_colwidth = 6000



#print(count_vectorizer.vocabulary_)







