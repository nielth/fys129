from pylab import *


def main():
    s1 = zeros(100)
    s2 = zeros(100)
    v = linspace(0, 15, 100)
    for i in range(100):
        s1[i] = v[i] ** 2 / 10
        s2[i] = v[i] ** 2 / (20 / 3)
    plot(v, s1)
    plot(v, s2)
    grid()
    xlabel('v [m/s]')
    ylabel('s [m]')
    legend(['5 m/s^2', '10/3 m/s^2'])
    show()


if __name__ == '__main__':
    main()
