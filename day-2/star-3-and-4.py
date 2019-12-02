#!/usr/bin/env python3

import time

input = [
1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0
]

def run_program(noun, verb):
    mem=input.copy()

    mem[1]=noun
    mem[2]=verb

    pc=0
    while mem[pc] != 99:
        if mem[pc] == 1:
            mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
        elif mem[pc] == 2:
            mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
        else:
            raise ValueError(f"unknown opcode {mem[pc]} at {pc}")
        pc+=4

    return mem[0]

def star_3():
    return run_program(12,2)

def star_4():
    for noun in range(0, 100):
        for verb in range(0, 100):
            if run_program(noun, verb) == 19690720:
                return noun * 100 + verb

print(f"star 3: {star_3()}")

start = time.time()
answer4 = star_4()
end = time.time()

print(f"star 4: {answer4}  in {end - start} seconds")
