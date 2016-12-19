# -*- coding: utf-8 -*-
import time

class Day19:

    def __init__(self):
        pass

    # Answer: 1830117
    def part1(self):
        t0 = time.time()
        # self.solve()
        #self.solve(5)
        #self.solve(8)
        #self.solve(11)
        #self.solve(12)
        #self.solve(13)
        #self.solve(14)
        self.solve(3012210)
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def solve(self, n_elves):
        # setup elf circle, poi sticks and presents, fuckin douche bags
        elves = []
        for i in range(n_elves):
            elves.append(i+1)

        while len(elves) > 1:
            if len(elves) % 2 > 0:
                elves = elves[::2][1:]
            else:
                elves = elves[0::2]

        print(str(n_elves) + ' | ' + str(elves[0]))