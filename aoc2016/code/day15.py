# -*- coding: utf-8 -*-
import hashlib
import time

class Day15:

    def __init__(self):
        pass

    # Answer: 376777
    def part1(self):
        t = 0
        while True:
            match = ((2 + t) % 13 == 0
                    and (11 + t+1) % 19 == 0
                    and (3 + t+2) % 3 == 0
                    and (2 + t+3) % 7 == 0
                    and (4 + t+4) % 5 == 0
                    and (6 + t+5) % 17 == 0)

            if match:
                print('Time: ' + str(t) + ' seconds')
                break
            t += 1

    # Answer: 3903937
    def part2(self):
        t = 0
        while True:
            match = ((2 + t) % 13 == 0
                     and (11 + t + 1) % 19 == 0
                     and (3 + t + 2) % 3 == 0
                     and (2 + t + 3) % 7 == 0
                     and (4 + t + 4) % 5 == 0
                     and (6 + t + 5) % 17 == 0
                     and (1 + t + 6) % 11 == 0)

            if match:
                print('Time: ' + str(t) + ' seconds')
                break
            t += 1
