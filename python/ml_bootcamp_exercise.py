import matplotlib.pyplot as plt

import pandas as pd
from pandas.tools.plotting import radviz

iris_filename = './datasets-uci-iris.csv'
#Task :  read iris dataset to a dataframe named iris
iris = pd.read_csv(iris_filename, header=None, names= ['sepal length', 'sepal width', 'petal length', 'petal width', 'target'])
iris_less= iris.drop(["petal width"],axis=1)
#print(iris.head())
#print(iris.tail())
def demoRadviz(data) :
    radviz(data, 'target')
    plt.show()
#demoRadviz(iris)
#demoRadviz(iris_less)

Y= iris.target
X= iris.drop(["target"],axis=1)

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.40, random_state=4)

#Task 3
#Build Model on Training Data and Evaluate It

#Decision Trees

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

#init a DecisionTressClassifier object
classifier = DecisionTreeClassifier(max_depth=3)

#fit the training datax
classifier.fit(X_train, Y_train)

#predict on training datax
train_pred = classifier.predict(X_train)

#predict on test datax
test_pred = classifier.predict(X_test)



from sklearn import metrics
print( "Train Accuracy:", metrics.accuracy_score(Y_train, train_pred))
print( "Test Accuracy:", metrics.accuracy_score(Y_test, test_pred))

cmTest = metrics.confusion_matrix(Y_test, test_pred)
cmTrain = metrics.confusion_matrix(Y_train, train_pred)

print(list(Y_test))
print(test_pred)
combo = [ i for i in zip(list(Y_train), train_pred) if i[0] != i[1]]
for f in (combo) :
    print(f)

print("Confusion Matrix for Training Data")
print(cmTrain)

print("Confusion Matrix for Test Data")
print(cmTest)

#of the items we predicted to belong to a class C, how many did we get right
print ("Precision:", metrics.precision_score(Y_test, test_pred, average='weighted'))

#of the items which belong to class C, how many did we get right
print ("Recall:", metrics.recall_score(Y_test, test_pred, average='weighted'))

# a single number to represent performance, F1_Score = (2PR/(P+R))
print ("F1 Score:", metrics.f1_score(Y_test, test_pred, average='weighted'))

print(X.columns)
print(classifier.feature_importances_)

from IPython.display import Image
from sklearn.externals.six import StringIO

with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(classifier, out_file=f)
#lets reduce iris dataset dimensionality to 2 from 4

""" ---------------------------------------------------------------------------------"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,Normalizer

#Step 1: Normalize Numerical Data Columns
#PCA requires all columns to be scaled to a similar range (Preprocessing)
#Normalizer Normalize samples individually to unit norm.
scaler=Normalizer()


Xscaled=scaler.fit_transform(X)
#print(Xscaled[0:5,:])
print(Xscaled)