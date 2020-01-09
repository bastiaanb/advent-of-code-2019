#!/usr/bin/env python3

import fileinput
import math
import numpy as np
from sortedcontainers import SortedSet, SortedDict

sign = lambda a: (a>0) - (a<0)

def read_input():
    asteroids={}
    y = 0
    for line in fileinput.input():
        x = 0
        for c in line.strip():
            if c == '#':
                asteroids[(x, y)]=0
            x+=1
        y+=1
    return asteroids

def in_between(a, b):
    if a == b:
        return []

    dx = b[0] - a[0]
    dy = b[1] - a[1]

    if dx == 0:
        return [(a[0], y) for y in range(a[1] + sign(dy), b[1], sign(dy))]

    if dy == 0:
        return [(x, a[1]) for x in range(a[0] + sign(dx), b[0], sign(dx))]

    steps = abs(math.gcd(dx, dy))
    return [(a[0] + dx * i / steps, a[1] + dy * i / steps) for i in range(1, steps)]

def is_visible(a, b):
    for c in in_between(a, b):
        if c in asteroids:
            return False
    return True

def count_visible(a):
    return sum(1 for b in asteroids.keys() if is_visible(a, b)) - 1

def best_asteroid():
    max_pos, max_visible = None, 0
    for a in asteroids:
        v = count_visible(a)
        asteroids[a]=v
        if v > max_visible:
            max_visible = v
            max_pos = a
    return max_pos, max_visible

asteroids = read_input()
max_pos, max_visible = best_asteroid()
print(f"star 19: {max_visible} at {max_pos}")

def to_polar(a):
    x,y = a
    return np.sqrt(x**2+y**2), (np.pi + np.arctan2(-x, y)) % (2 * np.pi)

def order_asteroids():
    polar_asteroids=SortedDict()
    for a in asteroids:
        r, t = to_polar((a[0] - max_pos[0], a[1] - max_pos[1]))
        polar_asteroids.setdefault(t, SortedDict())[r] = a

    while polar_asteroids:
        for t, rs in list(polar_asteroids.items()):
            a = rs.pop(rs.keys()[0])
            if not rs:
                del polar_asteroids[t]
            yield a

del asteroids[max_pos]
a200 = list(order_asteroids())[199]
print(f"star 20: {a200[0] * 100 + a200[1]}")
