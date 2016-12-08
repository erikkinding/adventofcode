# -*- coding: utf-8 -*-
from time import sleep
import os

class Day8:

    def __init__(self):
        self.columns = 50
        self.rows = 6
        self.screen = list(self.get_screen(self.rows, self.columns))
        pass

    # Answer: 110 and ZJHRKCPLYJ
    def part1(self):
        file = open('aoc2016/input/day8_1.txt', 'r')
        rows = file.read().splitlines()

        for instruction in rows:
            split = instruction.split()
            if split[0] == 'rect':
                self.rect(split[1])
            elif split[1] == 'column':
                self.rot_column(split[2], split[4])
            elif split[1] == 'row':
                self.rot_row(split[2], split[4])
            sleep(0.03)
            os.system('cls')
            self.print_screen()

        # part 1, answer: 110
        #print(str(self.count_pixels()))

        # part 2, answer: ZJHRKCPLYJ
        #self.print_screen()

    def count_pixels(self):
        npixels = 0
        for r in self.screen:
            for c in r:
                npixels += c
        return npixels

    def rot_column(self, column, steps):
        colid = int(column.split('=')[1])
        nsteps = int(steps)

        # copy column
        current_column = list(self.get_column(colid))

        # clear column
        for r in self.screen:
            r[colid] = 0

        # set column values
        for i in range(self.rows):
            self.screen[(i + nsteps) % self.rows][colid] = current_column[i]

    def rot_row(self, row, steps):
        rowid = int(row.split('=')[1])
        nsteps = int(steps)

        # copy row
        current_row = list(self.get_row(rowid))

        # clear row
        for c in self.screen[rowid]:
            c = 0

        # set row values
        for i in range(self.columns):
            self.screen[rowid][(i + nsteps) % self.columns] = current_row[i]

    def get_row(self, rowid):
        return self.screen[rowid]

    def get_column(self, colid):
        for r in self.screen:
            yield r[colid]

    def rect(self, dimensions):
        xy = dimensions.split('x')
        for c in range(int(xy[0])):
            for r in range(int(xy[1])):
                self.screen[r][c] = 1

    def get_screen(self, rows, columns):
        for r in range(rows):
            row = []
            for c in range(columns):
                row.append(0)
            yield row

    def print_screen(self,):
        for r in self.screen:
            tscreen_row = []
            for c in r:
                if c == 1:
                    tscreen_row.append('#')
                else:
                    tscreen_row.append(' ')
            print(''.join(tscreen_row))


