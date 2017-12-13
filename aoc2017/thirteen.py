# -*- coding: utf-8 -*-

from collections import defaultdict
import aoc

#inp = aoc.input_as_grid("ex.txt", int)
inp = aoc.input_as_rows("thirteen.txt")
#inp = aoc.input_as_rows("thirteen_test.txt")


# starting at zero, find current position of scanner i a given depth
# at a given time. Depth start at 0
def scanner_position(pics, srange):    
    return pics % ((srange - 1) * 2)


# 632
def part1():

    # firewall configuration
    firewall = defaultdict(int)
    last_depth = 0
    for row in inp:
        s = row.split(': ')
        depth = int(s[0])
        srange = int(s[1])
        firewall[depth] = srange
        last_depth = depth

    severity = 0
    position = 0
    pics = 0
    # go through
    while position <= last_depth:

        # validate state
        scanner_range = firewall[position]
        scanner_pos = scanner_position(pics, scanner_range)
        if scanner_pos == 0:
            severity += scanner_range * position

        # move me
        position += 1

        # update pics
        pics += 1


    print("part1 severity:", severity)


# 3849742
def part2():
    # firewall configuration
    firewall = defaultdict(int)
    last_depth = 0
    for row in inp:
        s = row.split(': ')
        depth = int(s[0])
        srange = int(s[1])
        firewall[depth] = srange
        last_depth = depth


    min_pics = 0;
    while True:
        position = 0
        pics = min_pics
        # go through
        hit = False
        while position <= last_depth:

            # validate state
            scanner_range = firewall[position]
            scanner_pos = scanner_position(pics, scanner_range)
            if scanner_range > 0 and scanner_pos == 0:
                hit = True
                break

            # move me
            position += 1

            # update pics
            pics += 1


        if not hit:
            break
        min_pics += 1

    print("part2 min pics:", min_pics)


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()