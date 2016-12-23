# -*- coding: utf-8 -*-
import time

class Day23:

    def __init__(self):
        self.registers = {}

        # parse instructions
        self.instructions = []
        self.get_instructions()

    # Answer: 11004
    def part1(self):
        self.registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}

        t0 = time.time()
        self.run_instructions()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # 6 -> 6684
    # 7 -> 11004
    # 8 -> 312954
    # 9 -> 368844
    # X -> 3634764
    def part2(self):
        self.registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

        t0 = time.time()
        self.run_instructions()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # 0.14s
    # 0.11s
    def run_instructions(self):
        idx = 0
        loops = 0

        while idx < len(self.instructions):
            loops += 1
            instruction = self.instructions[idx]

            # print(str(idx) + ' : ' + self.instructions[idx])
            # print(self.registers)

            steps = 1
            if instruction[0] == 'cpy':
                self.cpy(instruction[2], instruction[1])

            if instruction[0] == 'inc':
                self.inc(instruction[1])

            if instruction[0] == 'dec':
                self.dec(instruction[1])

            if instruction[0] == 'jnz':
                steps = self.jnz(instruction[1], instruction[2])

            if instruction[0] == 'tgl':
                self.tgl(idx, instruction[1])

            idx += steps



        print(self.registers)
        print('Loops: ' + str(loops))

    def tgl(self, current_instruction, steps_away):
        steps_away = self.get_value(steps_away)
        if current_instruction + steps_away >= len(self.instructions):
            return

        to_modify_idx = current_instruction + steps_away
        to_modify = self.instructions[to_modify_idx]

        if to_modify[0] == 'cpy':
            self.instructions[to_modify_idx][0] = 'jnz'

        # toggle toggle
        elif to_modify[0] == 'inc':
            self.instructions[to_modify_idx][0] = 'dec'

        # dec becomes inc
        elif to_modify[0] == 'dec':
            self.instructions[to_modify_idx][0] = 'inc'

        # change to cpy...
        elif to_modify[0] == 'jnz':
            self.instructions[to_modify_idx][0] = 'cpy'

        # tgl is also a one-argument instruction, resulting in inc
        elif to_modify[0] == 'tgl':
            self.instructions[to_modify_idx][0] = 'inc'

    def jnz(self, x, y):
        value = self.get_value(x)
        steps = 1
        if value != 0:
            steps = self.get_value(y)
        return steps

    def inc(self, register):
        self.registers[register] += 1

    def dec(self, register):
        self.registers[register] -= 1

    def cpy(self, register, value):
        value = self.get_value(value)
        if not isinstance(register, int):
            self.registers[register] = value

    def get_value(self, value):
        value = value
        try:
            value = int(value)
        except:
            value = self.registers[value]

        return value

    def get_instructions(self):
        instructions = open('aoc2016/input/day23.txt', 'r').read().splitlines()

        for instruction in instructions:
            split = instruction.split()
            self.instructions.append(split)
