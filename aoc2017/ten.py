# -*- coding: utf-8 -*-
import operator
from functools import reduce

def run_hash(inp, rounds):
    list_len = 256
    hash = [x for x in range(0, list_len)]
    position = 0
    skip = 0

    for i in range(rounds):
        for length in inp:
            # invalid
            if length > list_len:
                continue

            take_indexes = []
            for i in range(length):
                take_indexes.append((position + i) % list_len)

            for i in range(int(len(take_indexes) / 2)):
                ai = take_indexes[i]
                bi = take_indexes[len(take_indexes) - 1 - i]

                a = hash[ai]
                b = hash[bi]

                hash[ai] = b
                hash[bi] = a

            position += (length + skip)
            skip += 1

    return hash


def check_sum_part1(hash):
    return hash[0] * hash[1]


def check_sum_part2(hash, block_size):

    checksum = ""
    i = 0
    while i < len(hash):
        hash_segment = hash[i:i+block_size]
        checksum += format(reduce(operator.xor, hash_segment, 0), '02x')
        i += block_size

    return checksum


# 15990
def part1():
    inp = [183, 0, 31, 146, 254, 240, 223, 150, 2, 206, 161, 1, 255, 232, 199, 88]
    hash = run_hash(inp, 1)
    print("part1: ", check_sum_part1(hash))

# 90adb097dd55dea8305c900372258ac6
def part2():

    inp = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'
    inp = [ord(c) for c in inp]
    len_suffix = [17, 31, 73, 47, 23]
    inp.extend(len_suffix)

    hash = run_hash(inp, 64)
    print("part2: ", check_sum_part2(hash, 16))


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()