# -*- coding: utf-8 -*-

from aoc import *

#inp = input_as_grid("twentyone.txt", int)
inp = input_as_rows("twentyone.txt")
inp = input_as_rows("twentyone_test.txt")

def part1():
    print(inp)
    print("part1")

def part2():
    print("part2")

def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()