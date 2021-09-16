from pylab import *


def main():
    g = 9.81
    D = 0.01
    j = 1

    r0x = 0
    r0y = 2

    v0x = 20.
    v0y = 15.

    r0 = array([r0x, r0y])
    v0 = array([v0x, v0y])

    T = 4
    dt = 0.001
    n = int(ceil(T / dt))

    a = zeros((n, 2), float)
    v = zeros((n, 2), float)
    r = zeros((n, 2), float)
    t = zeros((n, 1), float)

    v[0, :] = v0
    r[0, :] = r0

    for i in range(n - 1):
        # a[] = - (D/v) * abs(v) * v - g * j
        v[i + 1, :] = v[i, :] + a * dt
        r[i + 1, :] = r[i, :] + v[i + 1, :] * dt
        t[i + 1] = t[i] + dt

    plot(r[:, 0], r[:, 1])
    xlabel('x [m]')
    ylabel('y [m]')


if __name__ == '__main__':
    main()
