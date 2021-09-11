from pylab import *


def volume(r):
    v = 4/3 * pi * r**3
    return v


def main():
    r = 1.2
    v = volume(r)
    print(f'{v:.1f} mm^3')


if __name__ == '__main__':
    main()
