# -*- coding: utf-8 -*-

import aoc

inp = aoc.input_as_values("eleven.txt", str, ',')

# (y, x, z)
moves = { 'n': (1, 0, -1), 'ne': (0, 1, -1), 'se': (-1, 1, 0), 's': (-1, 0, 1), 'sw': (0, -1, 1), 'nw': (1, -1, 0) }

# Position (0, 0, 0) is the starting point
# Not practically needed but kept for clarity
def distance(x, y, z):
    return max(abs(0 - x), abs(0 - y), abs(0 - z))

def part1and2():
    
    # Trace position using a cubical coordinate system representation of the hex grid
    y = 0
    x = 0
    z = 0
    furthest = 0
    for move in inp:
        modifier = moves[move]
        y += modifier[0]
        x += modifier[1]
        z += modifier[2]

        current_distance = distance(x, y, z)
        if current_distance > furthest:
            furthest = current_distance
    

    print("Dist: ", distance(x, y, z))
    print("Furthest: ", furthest)


def main():
    part1and2()
    

if __name__ == "__main__":
    main()