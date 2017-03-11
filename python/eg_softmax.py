from matplotlib import pyplot as plt
import numpy as np
import math

# Basically takes a list of values and apply a normalized exponential function
# returns a list of normalized exponential (strongly weighting high values) ( values between 0 to 1)
def softmax(x_list) :
    results = []
    exp_x_list = [math.exp(x) for x in x_list]
    sum_exp = sum(exp_x_list)
    for x in x_list :
        results.append(math.exp(x)/sum_exp)
    return results

vals = [-2,-1,0, 1,7,14,15,16]
softmaxed_vals = softmax(vals)
print("Orginal list of values    :", vals)
print("Normalized list of values :", softmaxed_vals)

#Plotting vals against sotmaxed_vals
# plt.plot(vals, softmaxed_vals, marker='o', linestyle="-")
plt.plot(vals, softmaxed_vals, marker='o')
plt.text(1, 0.55,'Softmax function for x={}'.format(vals)
     # ,horizontalalignment='center'
     # ,verticalalignment='center'
         )
plt.grid(True)
plt.axhline(0, color='orange') # origin axis line
plt.axvline(0, color='orange') # origin axis line
plt.axes([-5,17,0,1])

    # ,
    #  transform = ax.transAxes)
plt.show()



