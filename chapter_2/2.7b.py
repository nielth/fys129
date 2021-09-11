from pylab import *


def gvalue(x, n):
	g = sin(x) / x**n
	return g

x = linspace(-5.0,5.0,1000)

for i in range(1, 4, 1):
	plot(x, gvalue(x, i))
	ylim(-6, 6)

show()
