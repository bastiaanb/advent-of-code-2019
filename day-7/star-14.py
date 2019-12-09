#!/usr/bin/env python3

from itertools import permutations

input = [
    3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99
]

def read_value(mem, pos, mode):
    return mem[mem[pos]] if mode == 0 else mem[pos]

def run_program(inp):
    mem=input.copy()
    out=[]
    pc=0
    while mem[pc] != 99:
        ins = mem[pc] % 100
        mode1 = int(mem[pc] / 100) % 10
        mode2 = int (mem[pc] / 1000) % 10
        if ins == 1:
            mem[mem[pc+3]] = read_value(mem, pc+1, mode1) + read_value(mem, pc+2, mode2)
            pc+=4
        elif ins == 2:
            mem[mem[pc+3]] = read_value(mem, pc+1, mode1) * read_value(mem, pc+2, mode2)
            pc+=4
        elif ins == 3:
            mem[mem[pc+1]] = inp.pop(0)
            pc+=2
        elif ins == 4:
            out.append(read_value(mem, pc+1, mode1))
            pc+=2
        elif ins == 5:
            if read_value(mem, pc+1, mode1) != 0:
                pc=read_value(mem, pc+2, mode2)
            else:
                pc+=3
        elif ins == 6:
            if read_value(mem, pc+1, mode1) == 0:
                pc=read_value(mem, pc+2, mode2)
            else:
                pc+=3
        elif ins == 7:
            if read_value(mem, pc+1, mode1) < read_value(mem, pc+2, mode2):
                mem[mem[pc+3]] = 1
            else:
                mem[mem[pc+3]] = 0
            pc+=4
        elif ins == 8:
            if read_value(mem, pc+1, mode1) == read_value(mem, pc+2, mode2):
                mem[mem[pc+3]] = 1
            else:
                mem[mem[pc+3]] = 0
            pc+=4
        else:
            print(mem)
            raise ValueError(f"unknown opcode {mem[pc]} at {pc}")

    return out

def amplify_signal(code, inp):
    out=run_program([int(code[0]), inp])
    out=run_program([int(code[1]), out[0]])
    out=run_program([int(code[2]), out[0]])
    out=run_program([int(code[3]), out[0]])
    out=run_program([int(code[4]), out[0]])
    return out[0]

signals = [ amplify_signal(code, 0) for code in permutations('01234') ]
print(max(signals))
