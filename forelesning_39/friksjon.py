from pylab import *


def main():
    g = 9.81
    T = 5.
    alp = 0.3
    t = linspace(0, T, 1000)
    a = zeros(1000)
    for i in range(0, 1000):
        a[i] = g * (cos(alp) + sin(alp))

    plot(t, a)
    show()


if __name__ == '__main__':
    main()
