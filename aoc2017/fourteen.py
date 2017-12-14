# -*- coding: utf-8 -*-

import aoc

#inp = aoc.input_as_grid("ex.txt", int)
#inp = aoc.input_as_values("ex.txt", int)

import operator
from functools import reduce

def run_hash(inp, rounds):

    inp = [ord(c) for c in inp]
    len_suffix = [17, 31, 73, 47, 23]
    inp.extend(len_suffix)

    list_len = 256
    block_size = 16

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


    i = 0
    sparse_hash = []
    while i < len(hash):
        hash_segment = hash[i:i+block_size]
        sparse_hash.append(reduce(operator.xor, hash_segment, 0))
        i += block_size

    return sparse_hash


# Hashes are each 16 chunks of 1 byte each (8 bits)
def count_bits(hashes):

    bit_sum = 0
    byte_size = 8
    for row in hashes:
        for byte in row:
            for i in range(byte_size):
                bit = (byte >> i) & 1
                bit_sum += bit

    return bit_sum



def part1():
    #inp = 'flqrgnkx'
    inp = 'ffayrhll'

    hashes = []
    for i in range(128):
        hashes.append(run_hash(inp + '-' + str(i), 64))

    n_bits = count_bits(hashes)

    print("part1", n_bits)

def part2():
    print("part2")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()