from matplotlib import pyplot as plt
import numpy as np
def simplePlot() :
    x = np.arange(0,10)
    y1 = x * 10
    y2 = x**2
    plt.plot(x,y1,marker='o', linestyle="-" )
    plt.plot(x,y2,marker='o', linestyle="-", color="red")
    plt.show()

def xEqualY(x):
    y_intercept =4
    return x + y_intercept

def functionPlot(func) :
    x = np.arange(-10, 10)
    y = [ func(v) for v in x]
    print(x)
    print(y)
    plt.plot(x, y, marker='o', linestyle="-")
    plt.show()

# functionPlot(xEqualY)
import math
def logFunc(x) :
    return 1/ (1+ math.exp(-x))
functionPlot(logFunc)

