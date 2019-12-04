#!/usr/bin/env python3

valid = 0
for p in range(231832, 767346+1):
    prev = -1;
    same = False
    increasing = True

    for ds in str(p):
        d = int(ds)
        if d < prev:
            increasing = False
            break
        if d == prev:
            same = True
        prev = d

    if increasing and same:
        valid = valid + 1

print(valid)
