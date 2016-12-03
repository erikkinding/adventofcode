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
            split = triangle.replace('\n', '').split('  ')
            edges = []
            for c in split:
                c = c.replace(' ', '')
                if c != '':
                    edges.append(int(c))

            if edges[0] < edges[1] + edges[2] and edges[1] < edges[0] + edges[2] and edges[2] < edges[1] + edges[0]:
                valid_triangles += 1

        print(str(valid_triangles))

    # Answer: 1921
    def day3_2(self):

        input_file = ''
        with open('aoc2016/input/day3_1.txt') as f:
            input_file = f.readlines()

        triangles = []
        for triangle in input_file:
            split = triangle.replace('\n', '').split('  ')
            edges = []
            for c in split:
                c = c.replace(' ', '')
                if c != '':
                    edges.append(int(c))
            triangles.append(edges)


        index = 0
        valid_triangles = 0
        while index+3 <= len(triangles):
            for i in range(3):
                if triangles[index][i] < triangles[index+1][i] + triangles[index+2][i] and triangles[index+1][i] < triangles[index][i] + triangles[index+2][i] and triangles[index+2][i] < triangles[index+1][i] + triangles[index][i]:
                    valid_triangles += 1
            index += 3

        print(str(valid_triangles))
