# -*- coding: utf-8 -*-
import time

class Day19:

    def __init__(self):
        pass

    # Answer: 1830117
    def part1(self):
        t0 = time.time()
        #self.solve(5)
        #self.solve(8)
        #self.solve(11)
        #self.solve(12)
        #self.solve(13)
        #self.solve(14)
        self.solve(3012210)
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # Answer:
    def part2(self):
        t0 = time.time()
        # self.solve2(5)
        # self.solve2(6)
        # self.solve2(8)
        # self.solve2(11)
        # self.solve2(12)
        # self.solve2(13)
        # self.solve2(14)
        self.solve2(3012210)
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

    # 31682 too low...
    # 620727 too low..., 1782s
    def solve2(self, n_elves):
        # setup elf circle, poi sticks and presents, fuckin douche bags
        elves = []
        for i in range(n_elves):
            elves.append(i+1)

        elf_idx = 0
        while len(elves) > 1:
            # just yank from across
            elves_left = len(elves)
            to_steal_idx = (int(elves_left / 2) + elf_idx) % elves_left

            del elves[to_steal_idx]

            # only move if something ahead in the list was removed
            if to_steal_idx > elf_idx:
                elf_idx += 1

            if elf_idx >= elves_left:
                elf_idx = 0


        print(str(n_elves) + ' | ' + str(elves[0]))