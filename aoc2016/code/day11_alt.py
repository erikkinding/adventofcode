# -*- coding: utf-8 -*-
import itertools


class Day11_alt:

    def __init__(self):
        # F4 .  .  .  .  .
        # F3 .  .  .  LG .
        # F2 .  HG .  .  .
        # F1 E  .  HM .  LM
        #
        # init state
        # state: elevator level, pairs, distance
        self.state = {}

        # hashes of pair states
        self.visited = []

    # Answer:
    def part1(self):
        self.state = {'elevator_level': 0, 'pairs': ((0, 1), (0, 2)), 'distance': 0}
        self.visited.append(self.state['pairs'])
        self.solve()

    def solve(self):
        pass

    # "reachable nodes"
    def reachable(self, state):

        pass

    @staticmethod
    def finished(state):
        # for 2 pairs, 12
        # for 3 pairs, 18
        return sum(map(lambda x: sum(x), state['pairs'])) == 12


