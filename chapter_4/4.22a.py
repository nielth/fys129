from pylab import *


def main():
    v0 = 10  # m/s
    t = linspace(0, 0.2, 10)
    v = zeros(10)
    a = zeros(10)
    for i in range(10):
        v[i] = 10 - 10 * t[i]
        a[i] = -50
    subplot(2, 1, 1)
    plot(t, v)
    legend(['v(t)'])
    grid()
    subplot(2, 1, 2)
    plot(t, a)
    legend(['a(t)'])
    grid()
    show()


if __name__ == '__main__':
    main()
