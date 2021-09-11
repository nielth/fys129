from pylab import *


def main():
    t = zeros(10)
    y = [0, 15, 60, 135, 240, 375, 540, 735, 960, 1215]
    for i in range(10):
        t[i] = i
    plot(t, y)
    show()


if __name__ == '__main__':
    main()
