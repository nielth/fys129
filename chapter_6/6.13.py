from pylab import *


def main():
    r_1 = array([-10.0, 80.0]) * 1e3  # m
    v_1 = array([0, 1700.0]) / 3.6  # m/s
    v_2 = array([105.0, 905.0]) / 3.6  # m/s
    T = 400  # s
    t = linspace(1, T, T)
    r_jet = zeros((len(t), 2))
    r_bus = zeros((len(t), 2))
    r_jet[0] = 0
    r_bus[0] = r_1
    alarm = False
    crash = False

    for i in range(1, T):
        r_jet[i] = v_1 * t[i]
        r_bus[i] = r_1 + v_2 * t[i]
        distance = sqrt((r_jet[i, 0] - r_bus[i, 0])**2 + (r_jet[i, 1] - r_bus[i, 1])**2)
        if distance < 60 and crash is False:
            print("Flight will crash")
            crash = True
        if distance <= 1000 and alarm is False:
            print("Alarm will go off")
            alarm = True

    r_bus = r_bus * 1e-3
    r_jet = r_jet * 1e-3
    plot(r_jet[:, 0], r_jet[:, 1])
    plot(r_bus[:, 0], r_bus[:, 1])
    ylabel("km")
    xlabel("km")
    grid()
    show()


if __name__ == '__main__':
    main()
