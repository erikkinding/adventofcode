# -*- coding: utf-8 -*-
import itertools


class Day3:

    def __init__(self):
        self.lol = 0

    # Answer: 1050
    def day3_1(self):

        input_file = ''
        with open('aoc2016/input/day3_1.txt') as f:
            input_file = f.readlines()

        valid_triangles = 0
        for triangle in input_file:
            edges = triangle.strip().split()

            if int(edges[0]) < int(edges[1]) + int(edges[2]) \
                    and int(edges[1]) < int(edges[0]) + int(edges[2]) \
                    and int(edges[2]) < int(edges[1]) + int(edges[0]):
                valid_triangles += 1

        print(str(valid_triangles))

    # Answer: 1921
    def day3_2(self):

        input_file = ''
        with open('aoc2016/input/day3_1.txt') as f:
            input_file = f.readlines()

        triangles = []
        for triangle in input_file:
            edges = triangle.strip().split()
            triangles.append([int(edges[0]), int(edges[1]), int(edges[2])])

        index = 0
        valid_triangles = 0
        while index+3 <= len(triangles):
            for i in range(3):
                if triangles[index][i] < triangles[index+1][i] + triangles[index+2][i] \
                        and triangles[index+1][i] < triangles[index][i] + triangles[index+2][i] \
                        and triangles[index+2][i] < triangles[index+1][i] + triangles[index][i]:
                    valid_triangles += 1
            index += 3

        print(str(valid_triangles))
