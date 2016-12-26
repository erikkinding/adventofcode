# -*- coding: utf-8 -*-
import time
import itertools

class Day24:

    def __init__(self):
        self.blocked = []
        self.targets = []
        self.start_pos = ()

        self.calculated_paths = {}
        self.visited = {}

        self.shortest_path = 1000000000
        self.min = (0, 0)
        self.max = (0, 0)

    # Answer:
    def part1(self):
        t0 = time.time()
        self.solve()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def solve(self):
        self.parse_map()
        print(self.targets)

        self.print_map()

        paths = self.permuted_paths_to_try()

        for path in paths:
            path_length = 0

            for idx in range(len(path) - 1):
                path_length += self.shortest_between(path[idx], path[idx+1])

            if self.shortest_path > path_length:
                self.shortest_path = path_length
                print('new best! ' + str(path_length))

            # print('---------')

        print('Shortest: ' + str(self.shortest_path))

    def shortest_between(self, start_idx, target_idx):
        # print(str(start_idx) + '->' + str(target_idx))

        # if we already calculated the path, return result of that calculation
        # paths are stored as sorted tuples; (1,2) is the same as (2,1)
        calc_key = tuple(sorted([start_idx, target_idx]))
        if calc_key in self.calculated_paths.keys():
            return self.calculated_paths[calc_key]

        # clear visited
        self.visited = {}

        start_target = self.targets[start_idx]
        start = [start_target[0], start_target[1], 0]
        target = self.targets[target_idx]

        neighbours = self.get_neighbours(*start)
        self.better_path(*start)

        while any(neighbours):
            current = neighbours.pop(0)

            # hit target, return distance and add to calculated
            if (current[0], current[1]) == target:
                self.calculated_paths[calc_key] = current[2]
                print('Path for ' + str(calc_key[0]) + '->' + str(calc_key[1]) + ': ' + str(current[2]))
                return current[2]

            neighbours.extend(self.get_neighbours(*current))


        print('trololol???')


    def get_neighbours(self, x, y, n_moves):
        neighbours = []

        # try up, down, left, right
        n_node = [x, y - 1, n_moves + 1]
        if self.is_open(x, y - 1) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x, y + 1, n_moves + 1]
        if self.is_open(x, y + 1) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x - 1, y, n_moves + 1]
        if self.is_open(x - 1, y) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x + 1, y, n_moves + 1]
        if self.is_open(x + 1, y) and self.better_path(*n_node):
            neighbours.append(n_node)

        return neighbours


    def permuted_paths_to_try(self):
        idxs = range(len(self.targets))
        # pos 0 of targets = start, which is filtered away
        # append pos 0 to beginning as we always start from there
        return map(lambda x: [0]+list(x), itertools.permutations(idxs[1:]))

    def better_path(self, x, y, n_moves):
        c_key = (x, y)
        if c_key in self.visited:
            if self.visited[c_key] > n_moves:
                self.visited[c_key] = n_moves
                return True
            return False

        self.visited[c_key] = n_moves
        return True

    def is_open(self, x, y):
        return (x, y) not in self.blocked

    def parse_map(self):
        map = open('aoc2016/input/day24.txt', 'r').read().splitlines()

        start = ()

        for ridx, row in enumerate(map):
            for cidx, c in enumerate(row):
                if c == '#':
                    self.blocked.append((cidx, ridx))
                elif c == '.':
                    continue
                else:
                    if int(c) == 0:
                        self.start_pos = (cidx, ridx)
                        start = (cidx, ridx)
                    else:
                        self.targets.append((cidx, ridx))

        self.targets = [start] + self.targets

    def print_map(self):
        for ridx in range(5):
            row = ''
            for cidx in range(11):
                pos = (cidx, ridx)
                if pos in self.blocked:
                    row += '#'
                elif pos == self.start_pos:
                    row += 'S'
                elif pos in self.targets:
                    row += 'T'
                else:
                    row += ' '

            print(row)