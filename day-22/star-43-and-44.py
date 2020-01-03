#!/usr/bin/env python3

import fileinput
import functools

def affine(c, t):
    return t[0] * c[0] % m, (t[0] * c[1] + t[1]) % m

def inverse_affine(c, t):
    d = pow(t[0], m - 2, m)
    return  d * c[0] % m, d * (c[1] - t[1]) % m

def repeat_affine(r, c, z):
    while(r > 0):
        if r & 1:
            c = affine(c, z)
        z = affine(z, z)
        r >>= 1
    return c

shuffles = [
    (1, -int(l[1])) if l[0] == 'cut' else
    (int(l[3]), 0)  if l[1] == 'with' else
    (-1, -1)
    for l in map(lambda x: x.split(), fileinput.input())
]

m=10007
dummy, result43 = functools.reduce(affine, shuffles, (1, 2019))
print(f"{result43}")

m=119315717514047
t44 = functools.reduce(inverse_affine, reversed(shuffles), (1,0))
dummy, result44 = repeat_affine(101741582076661, (1, 2020), t44)
print(f"{result44}")
