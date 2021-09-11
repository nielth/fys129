from pylab import *

d0 = 7.75
d1 = 8.05

r = float(input('Input radius (cm): '))
m0 = (4*pi/3)*d0*r**3
m1 = (4*pi/3)*d1*r**3

if m0 < 1000:
	print('Mass of sphere is between ', format(m0, ".3f"), 'g^3', ' and ', format(m1, ".3f"), 'g^3', sep='') 
else:
	print('Mass of sphere is between ', format(m0/1000, ".3f"), 'kg^3', ' and ', format(m1/1000, ".3f"), 'kg^3', sep='')
