from matplotlib import pyplot as plt
import numpy as np
import math

def simplePlot() :
    x = np.arange(0,10)
    y1 = x * 10
    y2 = x**2
    plt.plot(x,y1,marker='o', linestyle="-" )
    plt.plot(x,y2,marker='o', linestyle="-", color="red")
    plt.show()

def functionPlot(func, x_values = np.arange(-10, 10)) :
    x = x_values
    y = [ func(v) for v in x]
    plt.plot(x, y, marker='o', linestyle="-" )
    plt.grid(True)
    plt.axhline(0, color='blue') # origin axis line
    plt.axvline(0, color='blue') # origin axis line
    plt.show()

# 1) y = x + 2 plot
# functionPlot(lambda x :  x +2)

# 2) y = x +4
def yEqualXPlus4(x):
    y_intercept =4
    return x + y_intercept
# functionPlot(yEqualXPlus4)

# 3) logFunc or sigmoid
def logFunc(x) :
    return 1/ (1+ math.exp(-x))

# 3) logFunc Modified
def customLogFunc(x) :
    return 1/ (math.pow(2,x))

# 3) logFunc
def logFunc2(x) :
    return 1/ (math.exp(0.1* x))

functionPlot(logFunc2,x_values= np.arange(0,50))



