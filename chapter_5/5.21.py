from pylab import *


def main():
    t, F = loadtxt('baseballforce-1.md', float, unpack=True)
    t = [x * 1e3 for x in t]
    m_ball = 0.145  # kg
    dt = t[1] - t[0]
    a = zeros(len(t))
    v = zeros(len(t))
    v[0] = 0.0  # Initialverdiproblemet (antatt start-fart)

    for i in range(len(t)):
        a[i] = F[i] / m_ball

    for i in range(len(t) - 1):
        v[i+1] = v[i] + a[i] * dt

    subplot(3, 1, 1)
    plot(t, F)
    ylabel('F[N]')
    subplot(3, 1, 2)
    plot(t, a)
    ylabel('a[m/s^2]')
    subplot(3, 1, 3)
    plot(t, v)
    ylabel('v[m/s]')
    xlabel('t[s] x 1e-3')
    show()

    print(f'Velocity as the ball leaves the bat is {v[len(v) - 1]:.2f} m/s')


if __name__ == '__main__':
    main()
