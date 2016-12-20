# -*- coding: utf-8 -*-
import time

class Day20:

    def __init__(self):
        pass

    # Answer part 1: 4793564
    # Answer part 2: 146
    def part1(self):
        t0 = time.time()
        self.solve()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def solve(self):
        data = open('aoc2016/input/day20.txt', 'r').read().splitlines()

        ranges = []
        for row in data:
            split = row.split('-')
            ranges.append((int(split[0]), int(split[1])))

        sorted_ranges = sorted(ranges)

        i = 0
        ips = 0
        lowest = 4294967294 # unsigned integer max value

        while i <= 4294967294:
            in_range = False
            for r in sorted_ranges:
                if i in range(r[0], r[1]+1):
                    in_range = True
                    i = r[1]
                    break

            if not in_range:
                if i < lowest:
                    lowest = i
                ips += 1

            i += 1

        print('Lowest: ' + str(lowest))
        print('N IPs: ' + str(ips))
