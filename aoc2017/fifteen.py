# -*- coding: utf-8 -*-

from aoc import *
import time

af = 16807
bf = 48271
t = 2147483647

def part1():

    a = 783
    b = 325
    score = 0
    for i in range(40000000):
        a = (a * af) % t
        b = (b * bf) % t

        if a & 65535 == b & 65535:
            score += 1

    print("Part 1 score: ", score)


# 336
def part2():
    a = 783
    b = 325
    score = 0
    pairs_counted = 0
    has_a = False
    has_b = False
    while pairs_counted < 5000000:
        #print(pairs_counted)
        if not has_a:
            a = (a * af) % t
            # Multiples of 4
            if a & 3 == 0:
                has_a = True

        if not has_b:
            b = (b * bf) % t
            # Multiples of 8
            if b & 7 == 0:
                has_b = True


        if has_a and has_b:
            if a & 65535 == b & 65535:
                score += 1
            has_a = False
            has_b = False
            pairs_counted += 1


    print("Part 2 score: ", score)

def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()