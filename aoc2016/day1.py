# -*- coding: utf-8 -*-

class Day1:

    def __init__(self):
        self.visited_positions = []

    # Answer: 287
    def day1_1(self):

        input_file = ''
        with open('aoc2016/input/day1_1.txt') as f:
            input_file = f.readlines()

        # Parse commands
        commands = input_file[0].split(', ')

        # Starting at assumed 0,0 in grid
        # Initial direction is that of the first command
        x = 0
        y = 0

        # 0 = north
        # 1 = east
        # 2 = south
        # 3 = west
        direction_factor = 0

        for c in commands:
            command_direction = c[0]

            # Set direction factor
            direction_factor += 1 if command_direction == 'R' else -1

            # Go
            rotation = direction_factor % 4
            command_distance = int(c[1:])
            if rotation == 0:
                x += command_distance
            elif rotation == 1:
                y += command_distance
            elif rotation == 2:
                x -= command_distance
            elif rotation == 3:
                y -= command_distance

        distance = abs(x) + abs(y)
        print('Distance: ' + str(distance))

    # Answer: 133
    def day1_2(self):

        input_file = ''
        with open('aoc2016/input/day1_1.txt') as f:
            input_file = f.readlines()

        # Parse commands
        commands = input_file[0].split(', ')

        # Starting at assumed 0,0 in grid
        # Initial direction is that of the first command
        x = 0
        y = 0

        # 0 = north
        # 1 = east
        # 2 = south
        # 3 = west
        direction_factor = 0

        visited = []
        for c in commands:
            command_direction = c[0]

            # Set direction factor
            direction_factor += 1 if command_direction == 'R' else -1

            # Go
            rotation = direction_factor % 4
            command_distance = int(c[1:])
            visited = False
            if rotation == 0:
                visited = self.check_visited(command_distance, x, y, 'ax')
                x += command_distance
            elif rotation == 1:
                visited = self.check_visited(command_distance, x, y, 'ay')
                y += command_distance
            elif rotation == 2:
                visited = self.check_visited(command_distance, x, y, 'dx')
                x -= command_distance
            elif rotation == 3:
                visited = self.check_visited(command_distance, x, y, 'dy')
                y -= command_distance

            if visited:
                break

    # adds steps and checks if already hit and if so returns True
    def check_visited(self, command_distance, x, y, op):

        position = ''
        for i in range(command_distance):
            if op == 'dy':
                position = (x, y-i)
            if op == 'dx':
                position = (x-i, y)
            if op == 'ay':
                position = (x, y+i)
            if op == 'ax':
                position = (x+i, y)

            if position in self.visited_positions:
                distance = abs(position[0]) + abs(position[1])
                print('Distance: ' + str(distance))
                return True
            else:
                self.visited_positions.append(position)

        return False
