from pylab import *


def normal(x, mu, sigma):
	p0 = 1.0 / (sqrt(2.0 * pi * sigma ** 2.0)) 
	p1 = p0 * exp(-(x-mu)**2.0 / (2.0 * sigma ** 2.0))
	return p1


x = linspace(-5,5,1000)
mu = float(input('input mu: '))
sigma0 = float(input('input sigma: '))
sigma1 = float(input('input sigma: '))


plot(x, normal(x, mu, sigma0))
plot(x, normal(x, mu, sigma1))
show()
