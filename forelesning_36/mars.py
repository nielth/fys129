from pylab import *


def main():
    t, x, y = loadtxt('marsexpresslr.d', usecols=[0, 1, 2], unpack=True)
    n = len(t)
    dt = t[1] - t[0]
    r = zeros((n, 2), float)
    r[:, 0] = x
    r[:, 1] = y
    AU = 14959800.0
    r = r / AU
    for i in range(n - 1):
        plot(r[i, 0], r[i, 1], 'o')
        dr = r[i + 1, :] - r[i, :]
        quiver(r[i, 0], r[i, 1], dr[0], dr[1], angles='xy', scale_units='xy', scale=1)
    show()
    pass


if __name__ == '__main__':
    main()
