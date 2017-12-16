# -*- coding: utf-8 -*-

import aoc

#inp = aoc.input_as_grid("ex.txt", int)
#inp = aoc.input_as_values("ex.txt", int)

import operator
from functools import reduce
from collections import defaultdict

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
                bit = (byte >> byte_size-i-1) & 1
                bit_sum += bit

    return bit_sum


# rewrite to return dict using (x, y) tuple as key?
# guess it's a good idea, helps with bounds checking...
def bit_grid(hashes):

    grid = []
    byte_size = 8
    for row in hashes:
        grid_row = []
        for byte in row:
            for i in range(byte_size):
                bit = (byte >> byte_size-i-1) & 1 == 1
                grid_row.append(bit)

        grid.append(grid_row)


    return grid


# 8190
# test 8108
def part1():
    #inp = 'flqrgnkx' # test inp
    inp = 'ffayrhll'

    hashes = []
    for i in range(128):
        hashes.append(run_hash(inp + '-' + str(i), 64))

    n_bits = count_bits(hashes)

    print("part1", n_bits)


def get_neighbours(x, y, grid):

    neighbours = []

    if y < 127 and grid[y+1][x]:
        neighbours.append((x, y+1))
    
    if y > 0 and grid[y-1][x]:
        neighbours.append((x, y-1))

    if x < 127 and grid[y][x+1]:
        neighbours.append((x+1, y))

    if x > 0 and grid[y][x-1] :
        neighbours.append((x-1, y))
    

    return neighbours


def count_groups(grid):

    groups = 0
    # check each cell in grid. if 'used', do bfs and when done incr group count
    # after group count, set all those as not used 
    for y in range(128):
        for x in range(128):
            
            if grid[y][x]:
                grid[y][x] = False
                groups += 1
                
                neighbours = get_neighbours(x, y, grid)
                while any(neighbours):
                    # Set any member in group as False as this
                    # represent the "visited" state
                    current = neighbours.pop(0)
                    grid[current[1]][current[0]] = False
                    neighbours.extend(get_neighbours(current[0], current[1], grid))

    return groups


# 1134
# test: 1242
def part2():
    #inp = 'flqrgnkx' # test inp
    inp = 'ffayrhll'

    hashes = []
    for i in range(128):
        hashes.append(run_hash(inp + '-' + str(i), 64))

    grid = bit_grid(hashes)
    print('Got grid, checking groups...')
    groups = count_groups(grid)

    print("part2", groups)


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()