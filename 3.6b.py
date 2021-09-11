from pylab import *


def volume(r):
    v = 4 / 3 * pi * r ** 3
    return v


def main():
    r = 1.2  # mm
    v = volume(r)
    density = 7782.  # kg/m^3
    mass = density * (v * 1e-9)  # kg
    mass = mass * 1e6  # mg

    print(f'{mass:.1f} milligrams')


if __name__ == '__main__':
    main()
