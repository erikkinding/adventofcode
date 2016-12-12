# -*- coding: utf-8 -*-


class Day12:

    def __init__(self):
        self.registers = {}

    # Answer: 318077
    def part1(self):
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.run_instructions()

    # Answer: 9227731
    def part2(self):
        self.registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        self.run_instructions()

    def run_instructions(self):
        data = open('aoc2016/input/day12.txt', 'r').read().splitlines()

        idx = 0
        while idx < len(data):
            split = data[idx].split()

            if split[0] == 'cpy':
                value = self.get_value(split[1])
                self.registers[split[2]] = value

            if split[0] == 'inc':
                self.registers[split[1]] += 1

            if split[0] == 'dec':
                self.registers[split[1]] -= 1

            if split[0] == 'jnz':
                value = self.get_value(split[1])
                if value != 0:
                    idx += self.get_value(split[2])
                    continue

            idx += 1

        print(self.registers)

    def get_value(self, value):
        value = value
        try:
            value = int(value)
        except:
            value = self.registers[value]

        return value
