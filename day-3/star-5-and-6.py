#!/usr/bin/env python3

import fileinput
import math

dx = { 'R': 1, 'L': -1, 'U': 0, 'D': 0 }
dy = { 'R': 0, 'L': 0, 'U': 1, 'D': -1 }

def draw(line):
    l = line.rstrip().split(',')
    x = 0
    y = 0
    path = {}
    delay = 0
    for step in l:
        dir = step[0]
        dist = int(step[1:])
        for i in range(0, dist):
            delay = delay + 1
            x = x + dx[dir]
            y = y + dy[dir]
            p = f"{x}:{y}"
            if not p in path:
                path[p] = {
                    'dist': abs(x) + abs(y),
                    'delay': delay
                }
    return path

paths=[]
input = fileinput.input()
path0 = draw(next(input))
path1 = draw(next(input))

intersects = set(path0.keys()).intersection(path1.keys())

distances = [ path0[x]['dist'] for x in intersects ]
print(f"star 5: {min(distances)}")

delays = [ path0[x]['delay'] + path1[x]['delay'] for x in intersects ]
print(f"star 6: {min(delays)}")
