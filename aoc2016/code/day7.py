# -*- coding: utf-8 -*-
import operator

class Day7:

    def __init__(self):
        self.haxxor = True

    # Answer: 118
    def part1(self):
        input_file = ''
        with open('aoc2016/input/day7_1.txt') as f:
            input_file = f.readlines()

        n_tls = 0
        for row in input_file:

            row_valid = False
            in_brackets = False
            stripped = row.strip()
            for idx, c in enumerate(stripped):
                if c == '[':
                    in_brackets = True
                    continue
                elif c == ']':
                    in_brackets = False
                    continue

                pair = stripped[idx:idx+2]
                if (len(pair) == 2) and (pair[0] == pair[1]):
                    continue

                reverse_pair = stripped[idx+2:idx+4][::-1]
                if pair == reverse_pair and in_brackets:
                    row_valid = False
                    break
                elif pair == reverse_pair and not in_brackets:
                    row_valid = True

            if row_valid:
                n_tls += 1

        print(str(n_tls))

    # Answer: 260
    def part2(self):
        input_file = ''
        with open('aoc2016/input/day7_1.txt') as f:
            input_file = f.readlines()

        n_ssl = 0
        for row in input_file:

            in_brackets = False
            stripped = row.strip()
            abas = []
            babs = []
            for idx, c in enumerate(stripped):
                if c == '[':
                    in_brackets = True
                    continue
                elif c == ']':
                    in_brackets = False
                    continue

                triplet = stripped[idx:idx + 3]
                if (len(triplet) == 3) and (triplet[0] == triplet[1]) and (triplet[0] == triplet[2]):
                    continue

                if not in_brackets and len(triplet) == 3 and self.is_xyx(triplet):
                    abas.append(triplet)

                if in_brackets and len(triplet) == 3 and self.is_xyx(triplet):
                    babs.append(triplet)

            for aba in abas:
                if self.aba_to_bab(aba) in babs:
                    n_ssl += 1
                    break

        print(str(n_ssl))

    def is_xyx(self, str):
        return str[0] == str[2] and str[0] != str[1]

    def aba_to_bab(self, aba):
        return ''.join([aba[1], aba[0], aba[1]])