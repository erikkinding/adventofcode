# -*- coding: utf-8 -*-

def part_one():
    file = open('input/five.txt', 'r')
    rows = file.read().splitlines()

    registers = [None] * len(rows)
    for idx, offset in enumerate(rows):
        registers[idx] = int(offset)

    pos = 0
    jumps = 0
    while pos >= 0 and pos < len(registers):
        offset = registers[pos]
        registers[pos] = offset + 1
        pos += offset
        jumps += 1

    print("Part1 Jumps: ", jumps)


def part_two():
    file = open('input/five.txt', 'r')
    rows = file.read().splitlines()

    registers = [None] * len(rows)
    for idx, offset in enumerate(rows):
        registers[idx] = int(offset)

    pos = 0
    jumps = 0
    while pos >= 0 and pos < len(registers):
        offset = registers[pos]
        if (offset >= 3):
            registers[pos] = offset - 1
        else:
            registers[pos] = offset + 1
        
        pos += offset
        jumps += 1

    print("part2 Jumps: ", jumps)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
