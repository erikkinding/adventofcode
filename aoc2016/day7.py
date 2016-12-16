# -*- coding: utf-8 -*-


class Day7:

    def __init__(self):
        pass

    # Answer: 118
    @staticmethod
    def part1():
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
                if self.is_xxx(triplet):
                    continue

                if self.is_xyx(triplet):
                    if not in_brackets:
                        abas.append(triplet)
                    elif in_brackets:
                        babs.append(triplet)

            for aba in abas:
                if self.aba_to_bab(aba) in babs:
                    n_ssl += 1
                    break

        print(str(n_ssl))

    @staticmethod
    def is_xxx(triplet):
        return len(triplet) == 3 and (triplet[0] == triplet[1]) and (triplet[0] == triplet[2])

    @staticmethod
    def is_xyx(triplet):
        return len(triplet) == 3 and triplet[0] == triplet[2] and triplet[0] != triplet[1]

    @staticmethod
    def aba_to_bab(aba):
        return ''.join([aba[1], aba[0], aba[1]])