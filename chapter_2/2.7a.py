from pylab import *


def gvalue(x, n):
	g = sin(x) / x**n
	return g

print(format(gvalue(pi/2, 2.0), ".2f"))
