from pylab import *


def main():
    g = 9.8
    k = 20
    m = 5
    L0 = 5

    r0x = 0.
    r0y = -5.

    v0x = 0.
    v0y = 0.

    r0 = array([r0x, r0y])
    v0 = array([v0x, v0y])

    T = 20
    dt = 0.001
    n = int(ceil(T / dt))

    v = zeros((n, 2), float)
    r = zeros((n, 2), float)
    t = zeros((n, 1), float)

    r[0] = r0
    v[0] = v0

    for i in range(n - 1):
        a = -g * array([0, 1]) - (k / m) * ((norm(r[i])) - L0) * (r[i] / norm(r[i]))
        v[i + 1] = v[i] + a * dt
        r[i + 1] = r[i] + v[i + 1] * dt
        t[i + 1] = t[i] * dt

    plot(r[:, 0], r[:, 1])
    xlim(-15, 15)
    ylim(-13, 1)
    grid()
    show()


if __name__ == '__main__':
    main()
