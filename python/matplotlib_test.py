import numpy as np

from matplotlib import pyplot

def plotLineChart():
    # Line chart
    x = np.linspace(0,15)
    pyplot.plot(x, np.log(x))
    pyplot.plot(x, np.sin(x))
    pyplot.plot(x, np.cos(x))
    pyplot.plot(x,np.cos(x*1.1), color="red", marker='x', linestyle='solid')
    pyplot.title("Sometitle")
    pyplot.ylabel("ylabel")
    pyplot.xlabel("xlabel")
    pyplot.savefig("sincos.png")
    pyplot.show()



def plotBarChart():
    # Bar chart
    contestant = ["Tom", "John", "Max", "Don" ]
    height = [161,150, 180, 155]
    xs = [i + 0.1 for i, _ in enumerate(contestant)]
    pyplot.bar(xs, height,0.7)  # 0.7 is the bar width
    # label x-axis with movie names at bar centers
    pyplot.xticks([i + 0.5 for i, _ in enumerate(contestant)], contestant)

    pyplot.axis([0, 4, 0, 200])   # x-axis from 0 to 4,
                                # y-axis from 0 to 200
    pyplot.show()

plotLineChart()
#plotBarChart()