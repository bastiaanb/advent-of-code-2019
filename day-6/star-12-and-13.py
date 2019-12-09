#!/usr/bin/env python3

import fileinput

orbits = {}

def sum_orbits(node, depth):
    return depth * len(orbits[node]) + sum([sum_orbits(x, depth + 1) for x in orbits[node]]) if node in orbits else 0

def find_path(current, target):
    if current == target:
        return []
    else:
        if current in orbits:
            for subnode in orbits[current]:
                r = find_path(subnode, target)
                if r is not None:
                    return [ current ] + r
        return None

for line in fileinput.input():
    (left, right) = line.rstrip().split(')')
    if left in orbits:
        orbits[left].append(right)
    else:
        orbits[left] = [ right ]

s = sum_orbits("COM", 1)
print(f"star 12: {s}")

l = len(set(find_path("COM", "YOU")) ^ set(find_path("COM", "SAN")))
print(f"star 13: {l}")
