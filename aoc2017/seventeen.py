# -*- coding: utf-8 -*-

from aoc import *


# 1547
def part1():

    steps = 369
    lock = [0]
    current_index = 0

    # i is the same as len(lock) in this case
    for i in range(1, 2018):

        insert_at = (current_index + steps) % i + 1

        head = lock[:insert_at]
        tail = lock[insert_at:]
        lock = head + [i] + tail

        current_index = insert_at

    print("Part 1: ", lock[lock.index(2017) + 1])


# 31154878
def part2():

    steps = 369
    lock = [0, 0]
    current_index = 0

    # assuming that the first register will always be 0
    # we only need to insert stuff if insert_at is = 1
    for i in range(1, 50000001):
        insert_at = (current_index + steps) % i + 1
        current_index = insert_at

        if insert_at == 1:
            lock[1] = i

    print("Part 2: ", lock[lock.index(0) + 1])


def main():
    time_it(part1)
    time_it(part2)


if __name__ == "__main__":
    main()