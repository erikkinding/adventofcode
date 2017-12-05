# -*- coding: utf-8 -*-

def part_one():
    file = open('input/five.txt', 'r')
    rows = file.read().splitlines()

    registers = [None] * len(rows)
    i = 0
    for instruction in rows:
        #print(instruction)
        registers[i] = int(instruction)
        i += 1

    pos = 0
    jumps = 0
    while pos >= 0 and pos < len(registers):
        instruction = registers[pos]
        registers[pos] = instruction + 1
        pos += instruction
        jumps += 1

    print("Part1 Jumps: ", jumps)


def part_two():
    file = open('input/five.txt', 'r')
    rows = file.read().splitlines()

    registers = [None] * len(rows)
    i = 0
    for instruction in rows:
        #print(instruction)
        registers[i] = int(instruction)
        i += 1

    pos = 0
    jumps = 0
    while pos >= 0 and pos < len(registers):
        instruction = registers[pos]
        if (instruction >= 3):
            registers[pos] = instruction - 1
        else:
            registers[pos] = instruction + 1
        
        pos += instruction
        jumps += 1

    print("part2 Jumps: ", jumps)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
