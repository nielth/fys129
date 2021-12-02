from pylab import *


def main():
    t, x, y = loadtxt('Data.d', float, unpack=True)
    T = len(t)
    r = zeros((T, 2), float)
    v = zeros((T, 2), float)
    vv = zeros((T, 2), float)
    dt = t[1] - t[0]
    for i in range(len(x)):
        r[i] = [x[i], y[i]]

    v[0] = (r[1] - r[0]) / dt
    for i in range(T - 1):
        v[i + 1] = (r[i + 1] - r[i]) / dt

    average_v = sum(v[:, 0]) / T
    vv[0] = ((0.02 + 0.049) * ((0.02 * average_v) / (0.02 + 0.049))) / 0.02
    for i in range(T - 1):
        vv[i + 1] = ((0.02 + 0.049) * ((0.02 * average_v) / (0.02 + 0.049))) / 0.02
    print(f'Average velocity: {average_v:.4f}')

    plot(t, v[:, 0])
    #plot(t, vv[:, 0])
    xlabel('t [s]')
    ylabel('v [m/s]')
    ylim(4, 10)
    grid()
    savefig('plot')
    show()


if __name__ == '__main__':
    main()
