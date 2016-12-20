# -*- coding: utf-8 -*-
import time

class Day20:

    def __init__(self):
        pass

    # Answer: 4793564
    def part1(self):
        t0 = time.time()
        self.solve()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def part2(self):
        t0 = time.time()
        self.solve2()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def solve(self):
        data = open('aoc2016/input/day20.txt', 'r').read().splitlines()

        ranges = []
        for row in data:
            split = row.split('-')
            ranges.append((int(split[0]), int(split[1])))

        sorted_ranges = sorted(ranges)

        i = 0
        lowest = 2147483647

        while i <= 2147483647:
            in_range = False
            for r in sorted_ranges:
                if i in range(r[0], r[1]+1):
                    in_range = True
                    break

            if not in_range:
                lowest = i
                print('New lowest: ' + str(i))
                break

            i += 1

        print('Lowest: ' + str(lowest))


    # part 2: 73 too low...
    def solve2(self):

        data = open('aoc2016/input/day20.txt', 'r').read().splitlines()

        ranges = []
        for row in data:
            split = row.split('-')
            ranges.append( [int(split[0]), int(split[1])])

        sorted_ranges = sorted(ranges)
        print(sorted_ranges)
        stretched_ranges = [sorted_ranges[0]]

        for r in sorted_ranges:
            for sr in stretched_ranges:
                # if hit, stretch range
                if r[0] in range(sr[0], sr[1]+1):
                    sr[1] = r[1]
                # no hit, add new range
                else:
                    stretched_ranges.append(r)

        print(stretched_ranges)

        print('N ranges: ' + str(len(sorted_ranges)))
        print('S ranges: ' + str(len(stretched_ranges)))

        allowed = []
        print('N IPs: ' + str(len(allowed)))
        pass