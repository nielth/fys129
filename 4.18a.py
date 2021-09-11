from pylab import *


def main():
    t = linspace(0, 1, 10)
    vF = zeros(10)
    vE = zeros(10)
    vE[0] = 50
    freightVel = 50  # km/h
    expressPos = zeros(10)  # km
    expressVel = 200  # km/h
    for i in range(10):
        vF[i] = freightVel * t[i]
        vE[i] = 50 + expressVel * -t[i]
    plot(t, vF)
    plot(t, vE)
    ylim(-20, 50)
    grid()
    show()


if __name__ == '__main__':
    main()
