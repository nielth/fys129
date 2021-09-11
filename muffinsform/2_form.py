from pylab import *
from numpy import *

t, x = loadtxt('data/data2.md', unpack=True)
v = zeros(len(x) - 1)
a = zeros(len(t) - 2)
dt = t[1] - t[0]

for i in range(len(t) - 1):
    v[i] = - (x[i+1] - x[i]) / dt

for i in range(len(t) - 2):
    a[i] = (v[i+1] - v[i]) / dt

subplot(3, 1, 1)
grid()
plot(t, x)

subplot(3, 1, 2)
grid()
plot(t[0:len(t)-1], v)

subplot(3, 1, 3)
grid()
plot(t[0:len(t)-2], a)

print(f'Average velocity: {x[0] / t[len(t) - 1]:.2f} m/s')

show()
