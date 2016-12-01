# -*- coding: utf-8 -*-

class Day1:

    def __init__(self):
        self.lol = 1

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
            if rotation == 0:
                for i in range(command_distance):
                    position = str(x + i) + '_' + str(y)
                    if position in visited:
                        distance = abs(x + i) + abs(y)
                        print('Hit same position at: ' + str(distance))
                        break
                    visited.append(position)
                x += command_distance
            elif rotation == 1:
                for i in range(command_distance):
                    position = str(x) + '_' + str(y + i)
                    if position in visited:
                        distance = abs(x) + abs(y + i)
                        print('Hit same position at: ' + str(distance))
                        break
                    visited.append(position)
                y += command_distance
            elif rotation == 2:
                for i in range(command_distance):
                    position = str(x - i) + '_' + str(y)
                    if position in visited:
                        distance = abs(x - i) + abs(y)
                        print('Hit same position at: ' + str(distance))
                        break
                    visited.append(position)
                x -= command_distance
            elif rotation == 3:
                for i in range(command_distance):
                    position = str(x) + '_' + str(y - i)
                    if position in visited:
                        distance = abs(x) + abs(y - i)
                        print('Hit same position at: ' + str(distance))
                        break
                    visited.append(position)
                y -= command_distance
