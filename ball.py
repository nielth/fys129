from pylab import *

t, x, y = loadtxt('ball.d', float, unpack=True)
T = len(t)
r = zeros((T, 2), float)
dt = t[1] - t[0]

g = 9.8
m = 0.49 + 0.2
L0 = 1.19

for i in range(len(x)):
    r[i] = [x[i], y[i]]

plot(r[:, 0], r[:, 1])
plot()
show()
