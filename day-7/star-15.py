#!/usr/bin/env python3

from itertools import permutations

input = [
    3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99
]

# input = [
# 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
# ]

class IntCode:
    def __init__(self, program, input=[]):
        self.mem = { i : program[i] for i in range(0, len(program) ) }
        self.pc = 0
        self.relbase = 0
        self.input = input
        self.output = []

    def read_value(self, pos, mode):
        if mode == 0:
            return self.mem.get(self.mem[pos], 0)
        elif mode == 1:
            return self.mem[pos]
        elif mode == 2:
            return self.mem.get(self.mem[pos] + self.relbase, 0)
        else:
            raise ValueError(f"unknown mode {mode}")

    def write_value(self, pos, val, mode):
        if mode == 0:
            self.mem[pos] = val
        elif mode == 2:
            self.mem[self.relbase + pos] = val
        else:
            raise ValueError(f"unknown mode {mode}")

    def run(self):
        while self.mem[self.pc] != 99:
            ins = self.mem[self.pc] % 100
            mode1 = int(self.mem[self.pc] / 100) % 10
            mode2 = int(self.mem[self.pc] / 1000) % 10
            mode3 = int(self.mem[self.pc] / 10000) % 10
            if ins == 1:
                self.write_value(self.mem[self.pc+3], self.read_value(self.pc+1, mode1) + self.read_value(self.pc+2, mode2), mode3)
                self.pc+=4
            elif ins == 2:
                self.write_value(self.mem[self.pc+3], self.read_value(self.pc+1, mode1) * self.read_value(self.pc+2, mode2), mode3)
                self.pc+=4
            elif ins == 3:
                if len(self.input) > 0:
                    value = self.input.pop(0)
                    self.write_value(self.mem[self.pc+1], value, mode1)
                    self.pc+=2
                else:
                    return False
            elif ins == 4:
                self.output.append(self.read_value(self.pc+1, mode1))
                self.pc+=2
            elif ins == 5:
                if self.read_value(self.pc+1, mode1) != 0:
                    self.pc=self.read_value(self.pc+2, mode2)
                else:
                    self.pc+=3
            elif ins == 6:
                if self.read_value(self.pc+1, mode1) == 0:
                    self.pc=self.read_value(self.pc+2, mode2)
                else:
                    self.pc+=3
            elif ins == 7:
                self.write_value(self.mem[self.pc+3], int(self.read_value(self.pc+1, mode1) < self.read_value(self.pc+2, mode2)), mode3)
                self.pc+=4
            elif ins == 8:
                self.write_value(self.mem[self.pc+3], int(self.read_value(self.pc+1, mode1) == self.read_value(self.pc+2, mode2)), mode3)
                self.pc+=4
            elif ins == 9:
                self.relbase += self.read_value(self.pc+1, mode1)
                self.pc+=2
            else:
                print(self.mem)
                raise ValueError(f"unknown opcode {self.mem[self.pc]} at {self.pc}")

        return True

def amplify_signal(code, signal = 0):
    amps = [ IntCode(input, [int(code[i])] ) for i in range(0, 5) ]
    done = False
    round = 0
    while not done:
        for i in range(0, 5):
            round += 1
            amps[i].input.append(signal)
            done = amps[i].run()
            signal = amps[i].output.pop(0)

    return { 'signal': signal, 'rounds': round, 'mem': sum([len(amp.mem) for amp in amps]) }

signals = [ amplify_signal(code) for code in permutations('56789') ]
print(f"signal: {max([s['signal'] for s in signals])}")
print(f"rounds: {max([s['rounds'] for s in signals])}")
print(f"mem: {max([s['mem'] for s in signals])}")
