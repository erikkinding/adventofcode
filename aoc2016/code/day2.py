# -*- coding: utf-8 -*-

class Day2:

    # Answer: 44558
    def day2_1(self):

        input_file = ''
        with open('aoc2016/input/day2_1.txt') as f:
            input_file = f.readlines()

        # lock
        lock = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

        # start at key 5
        position = (1, 1)
        code = []
        for line in input_file:
            for instruction in line:
                if instruction == 'U' and position[1] > 0:
                    position = (position[0], position[1]-1)
                elif instruction == 'D' and position[1] < 2:
                    position = (position[0], position[1] + 1)
                elif instruction == 'L' and position[0] > 0:
                    position = (position[0] - 1, position[1])
                elif instruction == 'R' and position[0] < 2:
                    position = (position[0] + 1, position[1])
            code.append(lock[position[1]][position[0]])

        print(code)

    # Answer: 6BBAD
    def day2_2(self):

        input_file = ''
        with open('aoc2016/input/day2_1.txt') as f:
            input_file = f.readlines()

        # lock
        lock = [['0', '0', '1', '0', '0'],
                ['0', '2', '3', '4', '0'],
                ['5', '6', '7', '8', '9'],
                ['0', 'A', 'B', 'C', '0'],
                ['0', '0', 'D', '0', '0']]

        # start at key 5
        position = (0, 2)
        code = []
        for line in input_file:
            for instruction in line:
                print('lock key: ' + str(lock[position[1]][position[0]]))
                if instruction == 'U' and position[1] > 0 and lock[position[1]-1][position[0]] is not '0':
                    position = (position[0], position[1] - 1)
                elif instruction == 'D' and position[1] < 4 and lock[position[1]+1][position[0]] is not '0':
                    position = (position[0], position[1] + 1)
                elif instruction == 'L' and position[0] > 0 and lock[position[1]][position[0]-1] is not '0':
                    position = (position[0] - 1, position[1])
                elif instruction == 'R' and position[0] < 4 and lock[position[1]][position[0]+1] is not '0':
                    position = (position[0] + 1, position[1])
            code.append(lock[position[1]][position[0]])

        print(code)
