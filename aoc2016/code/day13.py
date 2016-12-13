# -*- coding: utf-8 -*-


class Day13:

    def __init__(self):
        self.office_number = 1350
        self.target = (31, 39)

        self.check_max_distance = False
        self.max_distance = 50
        # self.office_number = 10
        # self.target = (7, 4)

        self.grid_x = 10
        self.grid_y = 10

        self.visited = {}
        self.possible_routes = []

    # Answer: 92
    def part1(self):
        self.find_path()
        print('Shortest trip to target: ' + str(sorted(self.possible_routes)[0]))

    # Answer: 124
    def part2(self):
        self.check_max_distance = True
        self.find_path()
        # +1 to include starting position
        print('Reached within 50: ' + str(len(self.visited) + 1))


    def find_path(self):
        # Breadth first finding algorithm, as we can only go up, down, left, right
        #   and nodes are at fixed distances (i.e. steps of length 1)

        # start with distance 0 at 1, 1, with parent None
        move = (0, 1, 1, None)

        possible_moves = [move]
        while any(possible_moves):
            # where are we?
            # self.print_grid()

            # remove one from queue
            move = possible_moves.pop()

            # add neighbours to queue
            possible_moves.extend(self.possible_moves(*move))

    def possible_moves(self, distance, x, y, parent):
        moves = []
        distance += 1
        if self.is_possible(distance, x - 1, y):
            moves.append((distance, x - 1, y, (x, y)))

        if self.is_possible(distance, x + 1, y):
            moves.append((distance, x + 1, y, (x, y)))

        if self.is_possible(distance, x, y - 1):
            moves.append((distance, x, y - 1, (x, y)))

        if self.is_possible(distance, x, y + 1):
            moves.append((distance, x, y + 1, (x, y)))

        # m[1] = x, m[2] = y
        # this is pretty much A* logic i guess...
        # best_order = map(lambda c: c[1], sorted(list(zip(map(lambda m: abs(self.target[0] - m[1]) + abs(self.target[1] - m[2]), moves), moves))))
        best_order = moves

        # self.visited.extend(map(lambda m: m[1:], moves))
        # update visited with new distance
        for move in moves:
            self.visited[(move[1], move[2])] = move[0]
            if (move[1], move[2]) == self.target:
                self.possible_routes.append(move[0])
                print("Target reached at: " + str(move[0]))

        return best_order

    def sort_to_best(self, moves):
        pass


    def is_possible(self, distance, x, y):
        if self.check_max_distance:
            return distance < self.max_distance and self.is_open(x, y) and not self.is_visited(distance, x, y)
        else:
            return self.is_open(x, y) and not self.is_visited(distance, x, y)

    def is_visited(self, distance, x, y):
        # simply checking if visited is not enough for finding the best path
        # return (x, y) in self.visited
        if (x, y) in self.visited.keys():
            visited_distance = self.visited[(x, y)]
            if visited_distance <= distance:
                return True
        return False

    def is_open(self, x, y):
        if x < 0:
            return False
        if y < 0:
            return False

        n = x*x + 3*x + 2*x*y + y + y*y + self.office_number
        return len(bin(n)[2:].replace('0', '')) % 2 == 0

    def print_grid(self):
        grid = []
        for y in range(self.grid_y):
            row = []
            for x in range(self.grid_x):
                point = ' ' if self.is_open(x, y) else '#'
                if (x, y) in self.visited:
                    point = 'o'
                if (x, y) == self.target:
                    point = 'G'
                row.append(point)
            grid.append(row)

        headers = []
        for i in range(len(grid[0])):
            headers.append(str(i))

        print(' ' + ' '.join(headers))

        for idx, row in enumerate(grid):
            print(str(idx) + ' '.join(row))

        print('-------------------------')
