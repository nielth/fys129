from pylab import *


def main():
    T = 0.1
    dt = 3000
    t = linspace(0, T, dt)
    x = zeros(dt)
    y = zeros(dt)
    outside_field = False
    for i in range(0, dt):
        x[i] = 100 * t[i]
        y[i] = -10 * t[i] ** 2 - 5 / 3 * t[i] ** 3
        if y[i] >= 2 or x[i] >= 2 and outside_field is False:
            print(f'{t[i]:.2f} s before the electron leaves the field of 2 m')
            print(f'{y[i]*1e3:.2f} mm is the displacement in the y-direction when the electron leaves the box')
            dot_product = dot(array(x[i], y[0]), array(x[i], y[i]))
            a_len = sqrt(x[i]**2 + y[0]**2)
            b_len = sqrt(x[i]**2 + y[i]**2)
            cos_val = dot_product / (a_len * b_len)
            angle_val = arccos(cos_val) * 180 / pi
            print(f'{angle_val:.3f} degrees between the x-axis and where the electron leaves the 2 m box')
            outside_field = True

    plot(x, y)
    grid()
    show()


if __name__ == '__main__':
    main()
