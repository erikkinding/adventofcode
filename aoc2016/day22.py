# -*- coding: utf-8 -*-
import time

class Day22:

    def __init__(self):
        self.x_max = 0
        self.y_max = 0
        pass

    # Answer: 1007
    def part1(self):
        t0 = time.time()
        self.solve()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # Answer:
    def part2(self):
        t0 = time.time()
        self.solve2()
        print('Elapsed: ' + str(time.time() - t0) + 's')

    def solve(self):
        nodes = list(self.get_nodes())
        viable_pairs = 0
        for node in nodes:
            for try_pair_node in nodes:
                # you can't be a pair with yourself
                if (node['x'], node['y']) != (try_pair_node['x'], try_pair_node['y']):
                    if self.node_fits_in_node(node, try_pair_node):
                        viable_pairs += 1

        print('Viable pairs: ' + str(viable_pairs))

    def solve2(self):
        grid = self.get_grid()

        neighbours = self.available_neighbours(grid, 0, 0)

        pass

    def available_neighbours(self, grid, x, y):
        neighbours = []

        current = self.get_node(grid, x, y)

        # try up, down, left, right
        n_node = self.get_node(grid, x, y - 1)
        if n_node is not None:
            pass


    def node_fits_in_node(self, node1, node2):
        used = node1['used']
        available = node2['available']
        return used > 0 and used <= available

    def get_node(self, grid, x, y):
        if not x < 0 or x > self.x_max or y < 0 or y > self.y_max:
            return grid[x][y]

    def get_grid(self):
        cluster_nodes = open('aoc2016/input/day22.txt', 'r').read().splitlines()[2:]

        grid = {}
        current_x = -1
        current_y = 0
        for node in cluster_nodes:

            split = node.split()

            # position
            position_split = split[0].split('-')
            x = int(position_split[1][1:])
            y = int(position_split[2][1:])

            if x != current_x:
                grid[x] = {}
                current_x = x

            # node data
            size = int(split[1][:-1])
            used = int(split[2][:-1])
            available = int(split[3][:-1])

            data = {'size': size, 'used': used, 'available': available}

            grid[x][y] = data
            current_y = y

        self.x_max = current_x
        self.y_max = current_y
        return grid

    def get_nodes(self):
        cluster_nodes = open('aoc2016/input/day22.txt', 'r').read().splitlines()[2:]

        for node in cluster_nodes:
            split = node.split()

            # position
            position_split = split[0].split('-')
            x = int(position_split[1][1:])
            y = int(position_split[2][1:])

            # node info
            size = int(split[1][:-1])
            used = int(split[2][:-1])
            available = int(split[3][:-1])

            yield {'x': x, 'y': y, 'size': size, 'used': used, 'available': available}
