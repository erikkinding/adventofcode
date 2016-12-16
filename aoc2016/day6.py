# -*- coding: utf-8 -*-
import operator
import itertools
from collections import Counter

class Day6:

    def __init__(self):
        self.haxxor = True

    # Answer: qrqlznrl
    def part1(self):
        input_file = ''
        with open('aoc2016/input/day6_1.txt') as f:
            input_file = f.readlines()

            positions = [dict({}), dict({}), dict({}), dict({}), dict({}), dict({}), dict({}), dict({})]

            for row in input_file:
                for idx, c in enumerate(row.strip()):
                    if c in positions[idx].keys():
                        positions[idx][c] += 1
                    else:
                        positions[idx][c] = 1

            message = []
            for idx, p in enumerate(positions):
                message.append(max(positions[idx].items(), key=operator.itemgetter(1))[0])

            print(''.join(message))

    # Answer: kgzdfaon
    def part2(self):
        input_file = ''
        with open('aoc2016/input/day6_1.txt') as f:
            input_file = f.readlines()

            positions = [dict({}), dict({}), dict({}), dict({}), dict({}), dict({}), dict({}), dict({})]

            for row in input_file:
                for idx, c in enumerate(row.strip()):
                    if c in positions[idx].keys():
                        positions[idx][c] += 1
                    else:
                        positions[idx][c] = 1

            message = []
            for idx, p in enumerate(positions):
                message.append(min(positions[idx].items(), key=operator.itemgetter(1))[0])

            print(''.join(message))

    def part1_alt(self):
        file = open('aoc2016/input/day6_1.txt', 'r')
        rows = file.read().splitlines()
        print(''.join(map(lambda x: Counter(x).most_common(1)[0][0], zip(*rows))))

    def part2_alt(self):
        file = open('aoc2016/input/day6_1.txt', 'r')
        rows = file.read().splitlines()
        print(''.join(map(lambda x: Counter(x).most_common()[-1][0], zip(*rows))))
