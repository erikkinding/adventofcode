# -*- coding: utf-8 -*-
import hashlib

class Day17:

    def __init__(self):
        self.passcode = ''
        self.best_path = []
        self.target = (3, 3)
        self.skip_check_distance = False
        self.paths = []

    # Answer: DRDRULRDRD
    def part1(self):
        self.passcode = 'vwbaicqe'
        self.solve()
        print(''.join(self.best_path))

    # Answer: DRDRULRDRD
    def part2(self):
        self.skip_check_distance = True
        self.passcode = 'vwbaicqe'
        self.solve_2()

        worst = sorted(self.paths, key=lambda x: len(x))[-1:][0]

        print(str(len(worst)) + ' | ' + worst)

    def solve(self):

        possible_steps = self.get_possible_steps([])

        while any(possible_steps):

            step = possible_steps.pop()

            possible_next = self.get_possible_steps(step)
            for pn in possible_next:

                if self.hit_target(pn):
                    self.best_path = pn
                else:
                    possible_steps.append(pn)

    def solve_2(self):

        possible_steps = self.get_possible_steps([])

        while any(possible_steps):

            step = possible_steps.pop()

            possible_next = self.get_possible_steps(step)
            for pn in possible_next:

                if self.hit_target(pn):
                    self.paths.append(''.join(pn))
                else:
                    possible_steps.append(pn)


    def hit_target(self, path):
        return self.position_from_path(path) == self.target

    def position_from_path(self, path):
        x = 0
        y = 0
        for step in path:
            if step[0] == 'U':
                y -= 1
            if step[0] == 'D':
                y += 1
            if step[0] == 'L':
                x -= 1
            if step[0] == 'R':
                x += 1

        return (x, y)

    def get_possible_steps(self, path):
        position = self.position_from_path(path)

        # current distance
        current_distance = len(path)

        # U D L R
        open_doors = self.open_doors(path)

        new_paths = []

        # UP
        if position[1] > 0 and open_doors[0]:
            if self.better_path(current_distance):
                new_path = path + ['U']
                new_paths.append(new_path)

        # DOWN
        if position[1] < 3 and open_doors[1]:
            if self.better_path(current_distance):
                new_path = path + ['D']
                new_paths.append(new_path)

        # LEFT
        if position[0] > 0 and open_doors[2]:
            if self.better_path(current_distance):
                new_path = path + ['L']
                new_paths.append(new_path)

        # RIGHT
        if position[0] < 3 and open_doors[3]:
            if self.better_path(current_distance):
                new_path = path + ['R']
                new_paths.append(new_path)

        return new_paths

    def better_path(self, current_distance):
        if self.skip_check_distance:
            return True
        else:
            if len(self.best_path) == 0:
                return True
            if current_distance <= len(self.best_path):
                return True

    def open_doors(self, possible_path):
        # U D L R
        open_doors = []
        pass_string = self.passcode + ''.join(map(lambda x: x[0], possible_path))
        open_doors_hash = hashlib.md5(pass_string.encode('UTF-8')).hexdigest()[:4]

        open_chars = ['b', 'c', 'd', 'e', 'f']
        for c in open_doors_hash:
            open_doors.append(c in open_chars)

        return open_doors
