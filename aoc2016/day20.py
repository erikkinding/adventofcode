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


    def solve(self):
        data = open('aoc2016/input/day20.txt', 'r').read().splitlines()

        ranges = []
        for row in data:
            split = row.split('-')
            ranges.append((int(split[0]), int(split[1])))

        sorted_ranges = sorted(ranges)

        i = 0
        lowest = 2147483647
        allowed = []
        while i <= 2147483647:
            in_range = False
            for r in sorted_ranges:
                if i in range(r[0], r[1]+1):
                    in_range = True
                    break

            if not in_range:
                #if i < lowest:
                #    lowest = i
                allowed.append(i)
                print('New IP: ' + str(i))
                # i+= 1

            i += 1

        print('-----------------------')
        print('Lowest: ' + str(lowest))
        print('N IPs: ' + str(len(allowed)))

        # part 2: 73 too low...