# -*- coding: utf-8 -*-
from time import sleep
import os

class Day9:

    def __init__(self):
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

    # Answer:
    def part2(self):
        file = open('aoc2016/input/day9_1.txt', 'r')
        data = file.read().splitlines()[0]

        parsing_symbol = False
        symbol = ''
        symbol_stack = []
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
