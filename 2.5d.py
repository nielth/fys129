from pylab import *


def normal(x, mu, sigma):
	p0 = 1.0 / (sqrt(2.0 * pi * sigma ** 2.0)) 
	p1 = p0 * exp(-(x-mu)**2.0 / (2.0 * sigma ** 2.0))
	return p1


x = linspace(-5,5,1000)
mu0 = float(input('input mu: '))
mu1 = float(input('input mu: '))
mu2 = float(input('input mu: '))
sigma = float(input('input sigma: '))


plot(x, normal(x, mu0, sigma))
plot(x, normal(x, mu1, sigma))
plot(x, normal(x, mu2, sigma))
xlabel('x')
ylabel('P(x, mu, sigma)')
show()
