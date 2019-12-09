#!/usr/bin/env python3

import fileinput
import networkx as nx

objects = nx.Graph()

for line in fileinput.input():
    (left, right) = line.rstrip().split(')')
    objects.add_edge(left, right)

s = sum([len(nx.shortest_path(objects, "COM", x)) - 1 for x in objects.nodes])
print(f"star 12: {s}")

l = len(nx.shortest_path(objects, "YOU", "SAN")) - 2
print(f"star 13: {l}")
