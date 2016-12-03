# import modules & set up logging

import os
import string

import re
import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from eg_tfidf_vectorizer_nltk import stemmer

x= np.array([
        [1,1,1],
        [1,1,2]
    ])
y= np.array([
        [1,1,1]
  ])

sim = cosine_similarity(x,y)
print("Cosine Similarity results :\n", sim)
