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

    # Answer:
    def part2(self):
        t0 = time.time()
        self.unscramble()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def test(self):
        inp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        inp = ['e', 'c', 'a', 'b', 'd']
        inp = self.rotate_from_x(inp, 'd')
        print (inp)


    def unscramble(self):
        instructions = open('aoc2016/input/day21_test.txt', 'r').read().splitlines()[::-1]
        inp = ['a', 'b', 'c', 'd', 'e']



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
