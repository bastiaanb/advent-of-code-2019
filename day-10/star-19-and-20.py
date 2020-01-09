#!/usr/bin/env python3

import fileinput
import math
import numpy as np
from sortedcontainers import SortedSet, SortedDict

asteroids={}

sign = lambda a: (a>0) - (a<0)

y = 0
for line in fileinput.input():
    x = 0
    for c in line.strip():
        if c == '#':
            asteroids[(x, y)]=0
        x+=1
    y+=1

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

max_pos, max_visible = None, 0
for a in asteroids:
    v = count_visible(a)
    asteroids[a]=v
    if v > max_visible:
        max_visible = v
        max_pos = a

print(f"star 19: {max_visible} at {max_pos}")

def to_polar(a):
    x,y = a
    return np.sqrt(x**2+y**2), (np.pi + np.arctan2(-x, y)) % (2 * np.pi)

del asteroids[max_pos]
polar_asteroids=SortedDict()
for a in asteroids:
    r, t = to_polar((a[0] - max_pos[0], a[1] - max_pos[1]))
    if t in polar_asteroids:
        polar_asteroids[t][r] = a
    else:
        polar_asteroids[t] = SortedDict({r: a})

i = 1
while i < 200:
    for t, rs in polar_asteroids.items():
        if len(rs) > 0:
            r = rs.keys()[0]
            a = rs.pop(r)
#            print(f"{i} ({t},{r}): {a}")
            if i == 200:
                print(f"star 20: {a[0] * 100 + a[1]}")
                break
            i+=1
