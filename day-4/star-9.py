#!/usr/bin/env python3

valid = 0
for p in range(231832, 767346+1):
    prev = -1;
    twosame = False
    increasing = True
    repeat = 1

    for ds in str(p):
        d = int(ds)
        if d < prev:
            increasing = False
            break
        if d == prev:
            repeat = repeat + 1
        else:
            if repeat == 2:
                twosame = True
            prev = d
            repeat = 1

    if increasing and (twosame or repeat == 2):
        valid = valid + 1

print(valid)
