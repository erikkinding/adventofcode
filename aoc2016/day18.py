# -*- coding: utf-8 -*-
import hashlib

class Day18:

    def __init__(self):
        self.first_row = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'.replace('^', '_')

        self.n_rows = 40
        self.n_cols = len(self.first_row)
        self.n_safe_spots = 0

    # Answer: 1926
    def part1(self):
        self.solve()
        self.count_safe()

    # Answer: 19986699
    def part2(self):
        self.n_rows = 400000
        self.solve()
        self.count_safe()

    def count_safe(self):
        print('Safe: ' + str(self.n_safe_spots))

    def solve(self):

        previous_row = self.first_row
        self.n_safe_spots += previous_row.count('.')

        for _ in range(self.n_rows - 1):
            next_row = ''
            for c in range(self.n_cols):
                # check only two first
                if c == 0:
                    next_row += self.is_trap('.' + previous_row[:2])
                # check only two last
                elif c == self.n_cols - 1:
                    next_row += self.is_trap(previous_row[-2:] + '.')
                else:
                    next_row += self.is_trap(previous_row[c-1:c+2])

            previous_row = next_row
            self.n_safe_spots += next_row.count('.')

    def is_trap(self, chars):
        trap = False
        if chars == '.._':
            trap = True
        elif chars == '_..':
            trap = True
        elif chars == '__.':
            trap = True
        elif chars == '.__':
            trap = True

        return '_' if trap else '.'

