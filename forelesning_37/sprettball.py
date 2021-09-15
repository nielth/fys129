#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:16:56 2020

@author: thomasg
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:33:46 2020

@author: thomasg
"""
from pylab import *

m = 0.2  # kg
g = 9.81  # m/sˆ2

# vT = 20.0 # m/s terminalhastighet.
D = 0.001

h = 2.0  # m
R = 0.1  # m
k = 10000.0  # N/m

r0 = array([0.0, h])
v0 = array([10.0, 10.0])  # m/s

time = 20.0  # s
dt = 0.001  #
n = int(round(time / dt))

a = zeros((n, 2), float)
r = zeros((n, 2), float)
v = zeros((n, 2), float)
t = zeros(n, float)
FF = zeros(n, float)

r[0] = r0
v[0] = v0
t[0] = 0.0

# Simulation loop
for i in range(n - 1):
    if r[i, 1] < R:
        N = k * (R - r[i, 1]) * array([0, 1])
    else:
        N = array([0, 0])
    FD = - D * norm(v[i]) * v[i]
    G = -m * g * array([0, 1])
    Fnet = N + FD + G
    a[i + 1] = Fnet / m
    v[i + 1] = v[i] + a[i + 1] * dt
    r[i + 1] = r[i] + v[i + 1] * dt
    t[i + 1] = t[i] + dt
    FF[i + 1] = norm(Fnet)

plot(r[:, 0], r[:, 1])
xlabel("x [m]")
ylabel("y [m]")
show()

plot(t, r[:, 1])
show()
plot(t, FF)
