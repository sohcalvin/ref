from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,10)
y1 = x * 10
y2 = x**2
plt.plot(x,y1,marker='o', linestyle="-" )
plt.plot(x,y2,marker='o', linestyle="-", color="red")

plt.show()