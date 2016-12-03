def printIt(label, obj) :
    print("\nNote that " +label +" :\n" + str(obj) + "\nis of type " + str(type(obj)))

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

printIt("iris", iris);           # this is sklearn.datasets.base.Bunch
printIt("iris.datax", iris.data); # this is a numpy.ndarray

printIt("iris.items()",iris.items())

