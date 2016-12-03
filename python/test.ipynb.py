import numpy as np
import random
import math
from collections import Counter
from matplotlib import pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,Normalizer


import numpy as np
import matplotlib.pyplot as plt

import numpy as np
copus = [
    'I think this is a great movie',
    'This is not a great movie'
]
def f():
    global s
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)


s = "I am looking for a course in Paris!"
f()
print(s)

X = np.random.randint(5, size=(6, 100))
print(X[2:3])
y = np.array([1, 2, 3, 4, 5, 6])
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(X[2:3]))