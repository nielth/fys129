from pylab import *
from turtle import *


def acceleration(v, x, k, C):
    a = -k * x - C * v
    return a


def main():
    x0 = 0.
    v0 = 1.0
    dt = 0.01
    t = zeros(100)
    x = zeros(100)
    v = zeros(100)
    a = zeros(100)
    t[0] = 0
    x[0] = x0
    v[0] = v0
    for i in range(0, 99, 1):
        a[i] = acceleration(v[i], x[i], 10, 5)
        v[i+1] = v[i] + acceleration(v[i], x[i], 10, 5) * dt
        x[i+1] = x[i] + v[i] * dt
        t[i+1] = t[i] + dt

    subplot(3, 1, 1)
    plot(t, x)
    legend(['x(t)'])
    subplot(3, 1, 2)
    plot(t, v, 'g')
    legend(['v(t)'])
    subplot(3, 1, 3)
    plot(t, a, 'r')
    legend(['a(t)'])
    show()


if __name__ == '__main__':
    main()
