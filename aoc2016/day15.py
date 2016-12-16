# -*- coding: utf-8 -*-


class Day15:

    def __init__(self):
        pass

    # Answer: 376777
    @staticmethod
    def part1():
        t = 0
        while True:
            match = ((2 + t) % 13 +
                     (11 + t+1) % 19 +
                     (3 + t+2) % 3 +
                     (2 + t+3) % 7 +
                     (4 + t+4) % 5 +
                     (6 + t+5) % 17) == 0

            if match:
                print('Time: ' + str(t) + ' seconds')
                break
            t += 1

    # Answer: 3903937
    @staticmethod
    def part2():
        t = 0
        while True:
            match = ((2 + t) % 13 +
                     (11 + t + 1) % 19 +
                     (3 + t + 2) % 3 +
                     (2 + t + 3) % 7 +
                     (4 + t + 4) % 5 +
                     (6 + t + 5) % 17 +
                     (1 + t + 6) % 11) == 0

            if match:
                print('Time: ' + str(t) + ' seconds')
                break
            t += 1
