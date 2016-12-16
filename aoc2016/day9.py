# -*- coding: utf-8 -*-
from time import sleep
import os

class Day9:

    def __init__(self):
        self.decompressed_length = 0
        # self.i = 0
        pass

    # Answer: 107035
    def part1(self):
        file = open('aoc2016/input/day9_1.txt', 'r')
        data = file.read().splitlines()[0]

        parsing_symbol = False
        symbol = ''
        decompressed = []
        i = 0
        while i < len(data):

            # begin symbol, reset old symbol
            if not parsing_symbol and len(symbol) == 0 and data[i] == '(':
                symbol = ''
                parsing_symbol = True
                i += 1
                continue
            # end symbol

            if parsing_symbol and data[i] == ')':
                parsing_symbol = False
                i += 1
                continue

            # parse symbol
            if parsing_symbol:
                symbol += data[i]
                i += 1
                continue

            # just append to decompressed
            if not parsing_symbol and len(symbol) == 0:
                decompressed.append(data[i])
                i += 1
                continue

            # decompress, jump forward
            if not parsing_symbol and len(symbol) > 0:
                split = symbol.split('x')
                length = int(split[0])
                times = int(split[1])
                decompressed.append(data[i:i+length]*times)
                symbol = ''
                i += length

        print(str(len(''.join(decompressed))))

    # answer 11451628995
    def part2(self):
        file = open('aoc2016/input/day9_1.txt', 'r')
        data = file.read().splitlines()[0]
        # data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
        # data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
        # data = '(143x8)(22x7)(4x15)XOPG(7x9)JDPAKGM(8x8)ALGCJRZQ(38x1)(4x10)VNSW(12x10)BZPAZABYKIDJ(3x14)IHF(40x15)(34x8)UGTIHCTVONZPPIWUAEGHGFJUNTIMIELOLW(6x1)XLMMKD'
        self.part2_solve(data, 1)
        print(str(self.decompressed_length))

    def part2_solve(self, data, factor):

        parsing_symbol = False
        symbol = []
        symbol_string = ''
        i = 0
        while i < len(data):
            # begin symbol, reset old symbol
            if not parsing_symbol and len(symbol) == 0 and data[i] == '(':
                symbol = []
                parsing_symbol = True
                i += 1
                continue

            # end symbol
            if parsing_symbol and data[i] == ')':
                parsing_symbol = False
                split = symbol_string.split('x')
                symbol = [int(split[0]), int(split[1])]

                new_data = data[i + 1:i + symbol[0]+1]
                self.part2_solve(new_data, factor * symbol[1])

                # +2 for ()
                data = data[data.index('(') + len(symbol_string) + 2 + symbol[0]:]

                i = 0
                symbol = []
                symbol_string = ''
                continue

            # parse symbol
            if parsing_symbol:
                symbol_string += data[i]
                i += 1
                continue

            # time for counting
            self.decompressed_length += factor
            i += 1
