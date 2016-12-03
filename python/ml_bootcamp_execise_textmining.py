
import pandas as pd
import sklearn as sk
import numpy as np
import scipy as sc
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(sum(map(ord, "aesthetics")))
from sklearn.metrics.pairwise import euclidean_distances

# Set some pandas options for controlling output
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
plt.style.use('ggplot')


import nltk
#Python Natural Language Processing ToolKit
#nltk.datax.path.append("/usr/share/nltk_data-3")

corpusx = [
'UNC played Duke in basketball',
'Duke lost the basketball game'
]
corpus = [
'three two goat cow three a in',
'three two one'
]

import csv
messages = pd.read_csv('./spamHam.txt', sep='\t', quoting=csv.QUOTE_NONE,names=["label", "message"])
print (messages)
#CountVectorizer is a class for feature extraction from text datax

from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer(stop_words='english')

#todense converts it into a Numpy dense matrix
'''
v = vectorizer.fit_transform(corpus);
array_ = v.todense()
print (array_)
print (vectorizer.vocabulary_)

print ('Distance between 1st and 2nd documents:'
       , euclidean_distances(array_[0], array_[1]))

       '''