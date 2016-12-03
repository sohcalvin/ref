import numpy as np
import math

from matplotlib.pyplot import subplots, xlim, ylim, xlabel, ylabel, title, savefig
from matplotlib import pyplot as plt
from scipy.stats import poisson
import scipy
# s = np.random.poisson(0.1,[15,15])
# print(s)

#
# import matplotlib.pyplot as plt
# plt.scatter(s)
# # count, bins, ignored = plt.plot(s, 14, normed=True)
# plt.show()


def myPoisson(lam, k) :
    return (math.e**-lam)  * float(lam)**float(k)/ math.factorial(k)

for k in [1,2,3,4] :
    lam = 1
    print("myPossson lam={0} k={1} : {2} ".format(lam, k, myPoisson(1,k)) )

scypi_poisson = poisson.pmf([1,2,3,4],1 )
print("\nscipy poission : ", scypi_poisson)

# numpi_poisson = np.random.poisson(1.0, 1000)
# # print(numpi_poisson)
# from matplotlib import pyplot as plt
# entries, bin_edges, patches = plt.hist(numpi_poisson, bins=11, range=[-0.5, 10.5], normed=True)
# plt.show()


def PoissonPP( rt, Dx, Dy=None ):
    '''
    Determines the number of events `N` for a rectangular region,
    given the rate `rt` and the dimensions, `Dx`, `Dy`.
    Returns a <2xN> NumPy array.
    '''
    if Dy == None:
        Dy = Dx
    N = scipy.stats.poisson( rt*Dx*Dy ).rvs()
    N = 110
    x = scipy.stats.uniform.rvs(0,Dx,((N,1)))
    y = scipy.stats.uniform.rvs(0,Dy,((N,1)))
    P = np.hstack((x,y))
    return P



rate , Dx = 1, 2
P = PoissonPP( rate, Dx ).T
fig, ax = subplots()
ax = fig.add_subplot(111)
ax.scatter( P[0], P[1], edgecolor='b', facecolor='none', alpha=0.5 )
# lengths of the axes are functions of `Dx`
xlim(0,Dx) ; ylim(0,Dx)
# label the axes and force a 1:1 aspect ratio
xlabel('X') ; ylabel('Y') ; ax.set_aspect(1)
title('Poisson Process, <img src="http://connor-johnson.com/wp-content/ql-cache/quicklatex.com-2b5c45836864531b8e37025dabadd24a_l3.svg" class="ql-img-inline-formula quicklatex-auto-format" alt="\lambda" title="Rendered by QuickLaTeX.com" height="13" width="10" style="vertical-align: 0px;">={}'.format(rate))
savefig( 'poisson_lambda_0p3.png', fmt='png', dpi=100 )
plt.show()
