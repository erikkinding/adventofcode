# -*- coding: utf-8 -*-
import time

class Day21:

    def __init__(self):
        pass

    # Answer: ghfacdbe
    def part1(self):
        t0 = time.time()
        self.scramble()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # Answer: fhgcdaeb
    def part2(self):
        t0 = time.time()
        self.unscramble()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def unscramble(self):
        instructions = open('aoc2016/input/day21.txt', 'r').read().splitlines()[::-1]
        inp = ['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h']

        for instruction in instructions:
            split = instruction.split()

            # 3 types of rotate
            if split[0] == 'rotate':
                rtype = split[1]

                if rtype == 'left':
                    inp = self.rotate(inp, -int(split[2]))
                elif rtype == 'right':
                    inp = self.rotate(inp, int(split[2]))
                else:
                    inp = self.undo_rotate_from_x(inp, split[6])

            elif split[0] == 'move':
                inp = self.move_xy(inp, int(split[5]), int(split[2]))

            # 2 types of swap
            elif split[0] == 'swap':
                stype = split[1]

                if stype == 'position':
                    inp = self.swap_position(inp, int(split[5]), int(split[2]))
                else:
                    inp = self.swap_letter(inp, split[5], split[2])

            elif split[0] == 'reverse':
                inp = self.reverse_xy(inp, int(split[2]), int(split[4]))

        print('Unscrambled: ' + ''.join(inp))



    def scramble(self):
        instructions = open('aoc2016/input/day21.txt', 'r').read().splitlines()
        inp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        for instruction in instructions:
            split = instruction.split()

            # 3 types of rotate
            if split[0] == 'rotate':
                rtype = split[1]

                if rtype == 'left':
                    inp = self.rotate(inp, int(split[2]))
                elif rtype == 'right':
                    inp = self.rotate(inp, -int(split[2]))
                else:
                    inp = self.rotate_from_x(inp, split[6])

            elif split[0] == 'move':
                inp = self.move_xy(inp, int(split[2]), int(split[5]))

            # 2 types of swap
            elif split[0] == 'swap':
                stype = split[1]

                if stype == 'position':
                    inp = self.swap_position(inp, int(split[2]), int(split[5]))
                else:
                    inp = self.swap_letter(inp, split[2], split[5])

            elif split[0] == 'reverse':
                inp = self.reverse_xy(inp, int(split[2]), int(split[4]))

        print('Scrambled: ' + ''.join(inp))

    def move_xy(self, inp, x, y):
        at_x = inp[x]
        del inp[x]
        return inp[:y] + [at_x] + inp[y:]

    def reverse_xy(self, inp, x, y):
        return inp[:x] + inp[x:y+1][::-1] + inp[y+1:]

    def rotate_from_x(self, inp, x):
        x_idx = inp.index(x)
        steps = x_idx + 1
        if x_idx >= 4:
            steps += 1
        steps = steps % len(inp)
        return self.rotate(inp, -steps)

    def undo_rotate_from_x(self, inp, x):
        steps = 1
        while True:
            test = self.rotate(inp, steps)

            if inp == self.rotate_from_x(test, x):
                return test

            steps += 1
            steps = steps % len(inp)

    def rotate(self, inp, steps):
        return inp[steps:] + inp[:steps]

    def swap_letter(self, inp, x, y):
        y_idx = inp.index(y)
        x_idx = inp.index(x)
        return self.swap_position(inp, x_idx, y_idx)

    def swap_position(self, inp, x, y):
        nx = inp[y]
        ny = inp[x]
        inp[x] = nx
        inp[y] = ny
        return inp
