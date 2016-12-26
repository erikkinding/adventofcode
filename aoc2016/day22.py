# -*- coding: utf-8 -*-
import time

class Day22:

    def __init__(self):
        self.grid = {}
        self.visited = {}
        self.x_max = 0
        self.y_max = 0

        self.target_data_position = []
        self.goal_position = [0,0]

        self.blocked = []

        self.best_path = 100000000

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

        # Initialize grid layout
        self.get_grid()

        # From these positions we can start to move things around
        #possible_moves = []
        #for x in range(self.x_max + 1):
        #    for y in range(self.y_max + 1):
        #        neighbours = self.available_neighbours(grid, x, y)
        #        if any(neighbours):
        #            possible_moves.append((x, y))

        # Start position = (22, 25)

        # position: [x, y, n_moves]
        # start_position = [22, 25, 0]
        start_position = [1, 1, [], 0]
        self.better_path(*start_position)


        movable_neighbours = self.movable_neighbours(*start_position)

        # perform bfs
        while any(movable_neighbours):
            # poping one = move
            next = movable_neighbours.pop(0)

            # move target data
            if [next[0], next[1]] == self.target_data_position:
                self.target_data_position = [next[2][-1:][0][0], next[2][-1:][0][1]]
                # movable_neighbours = []

            if self.hit_goal():
                if(self.best_path) > next[3]:
                    print('New best at: ' + str(next[3]))
                    self.best_path = next[3]

            #possible_moves = self.movable_neighbours(*next)
            movable_neighbours.extend(self.movable_neighbours(*next))
            # movable_neighbours = possible_moves
            # if not any(possible_moves):
            #    possible_moves.append(previous)

    def hit_goal(self):
        return self.target_data_position == self.goal_position

    def better_path(self, x, y, path, n_moves):
        if n_moves > self.best_path:
            return False

        c_key = (tuple(self.target_data_position), x, y)
        if c_key in self.visited:
            if self.visited[c_key] >= n_moves:
                self.visited[c_key] = n_moves
                return True
            return False

        self.visited[c_key] = n_moves
        return True

    def movable_neighbours(self, x, y, path, n_moves):
        neighbours = []

        # try up, down, left, right
        n_node = [x, y - 1, path + [(x, y)], n_moves+1]
        if self.visitable(x, y - 1) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x, y + 1, path + [(x, y)], n_moves+1]
        if self.visitable(x, y + 1) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x - 1, y, path + [(x, y)], n_moves+1]
        if self.visitable(x - 1, y ) and self.better_path(*n_node):
            neighbours.append(n_node)

        n_node = [x + 1, y, path + [(x, y)], n_moves + 1]
        if self.visitable(x + 1, y) and self.better_path(*n_node):
            neighbours.append(n_node)

        return neighbours

    def visitable(self, x, y):
        if not (x < 0 or x > self.x_max or y < 0 or y > self.y_max) and (x, y) not in self.blocked:
            return True
        return False

    def get_grid(self):
        cluster_nodes = open('aoc2016/input/day22_test.txt', 'r').read().splitlines()

        # grid = {}
        current_x = -1
        current_y = 0
        for node in cluster_nodes:

            split = node.split()

            # position
            position_split = split[0].split('-')
            x = int(position_split[1][1:])
            y = int(position_split[2][1:])

            if x != current_x:
                # grid[x] = {}
                current_x = x

            # node data
            size = int(split[1][:-1])
            #used = int(split[2][:-1])
            #available = int(split[3][:-1])

            # if size > 100:
            if size > 15:
                self.blocked.append((x, y))

            #data = {'size': size, 'used': used, 'available': available}

            #grid[x][y] = data
            current_y = y

        self.x_max = current_x
        self.y_max = current_y
        self.target_data_position = [self.x_max, 0]
        # self.grid = grid

    # for part 1...
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
