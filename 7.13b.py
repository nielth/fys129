from pylab import *


def y_direction(t, theta):
    return 2 + (50 * tan(radians(theta)) * t) - 0.5 * 9.81 * t ** 2


def main():
    theta_0 = 30    # degrees
    t_0 = 0         # initial-time
    t_1 = 1000      # arbitrary long end
    dt = 0.01
    steps = int(t_1 / dt)
    arrow_landing = 0

    t = linspace(t_0, t_1, steps)
    r = zeros((steps, 2), float)

    i = 0
    theta_steps = 0
    while True:
        r[i, 0] = 50 * t[i]
        r[i, 1] = y_direction(t[i], theta_0)
        if i > 50 and r[i, 1] <= 0:
            arrow_landing = i
            plot(r[range(0, arrow_landing), 0], r[range(0, arrow_landing), 1])
            arrow_landing = 0
            r[:] = ([0, 0])
            if theta_steps == 0:
                theta_0 = 40
            elif theta_steps == 1:
                theta_0 = 50
            elif theta_steps == 2:
                break
            theta_steps += 1
            i = 0
        i += 1

    ylim(0, 650)
    xlim(0, 650)
    xlabel('x[m]')
    ylabel('y[m]')
    legend(['θ = 30°', 'θ = 40°', 'θ = 50°'])
    savefig('7.13b.svg')
    show()


if __name__ == '__main__':
    main()
