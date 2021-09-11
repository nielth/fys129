#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: thomasg
"""
from pylab import *

g = 9.8  # m/s^2

r0x = 0  # m
r0y = 2  # m

v0x = 20.  # m/s
v0y = 15.  # m/s

# intitalverdier
r0 = array([r0x, r0y])
v0 = array([v0x, v0y])

T = 3.5  # sekunder
dt = 0.001  # Tidssteg sekunder
n = int(ceil(T / dt))

a = zeros((n, 2), float)
v = zeros((n, 2), float)
r = zeros((n, 2), float)
t = zeros((n, 1), float)

v[0, :] = v0
r[0, :] = r0

for i in range(n - 1):
    a = -g * array([0, 1])
    v[i + 1, :] = v[i, :] + a * dt
    r[i + 1, :] = r[i, :] + v[i + 1, :] * dt
    t[i + 1] = t[i] + dt

figur = figure()
plot(r[:, 0], r[:, 1])
xlabel('x [m]')
ylabel('y [m]')

show()

figur.savefig("kast2D.pdf", bbox_inches='tight')
