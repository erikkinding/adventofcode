# -*- coding: utf-8 -*-
from collections import Counter
import re

class Day4:

    def __init__(self):
        self.lol = 0

    # Answer: 245102
    def day4_1(self):

        input_file = ''
        with open('aoc2016/input/day4_1.txt') as f:
            input_file = f.readlines()


        sector_id_sum = 0
        for row in input_file:

            stripped = row.strip()
            # sector_id
            m = re.search('\d{3}', stripped)
            sector_id = int(m.group(0))

            # checksum
            m = re.search('\[\w{5}\]', stripped)
            checksum = m.group(0)[1:6]

            # clean
            clean = stripped[:stripped.rfind('-')].replace('-','')

            # most common
            c = Counter(clean)
            most_common = sorted(c.items(), key=lambda pair: (-pair[1], pair[0]))

            # is valid
            calculated_checksum = [str(i[0]) for i in most_common[:5]]
            if ''.join(calculated_checksum) == checksum:
                sector_id_sum += sector_id

        print('sum: ' + str(sector_id_sum))

    # Answer: 324
    def day4_2(self):

        input_file = ''
        with open('aoc2016/input/day4_1.txt') as f:
            input_file = f.readlines()

        sector_id_sum = 0
        for row in input_file:

            stripped = row.strip()
            # sector_id
            m = re.search('\d{3}', stripped)
            sector_id = int(m.group(0))

            # clean
            clean = stripped[:stripped.rfind('-')]

            a_offset = 97
            alphabet_len = 26

            unenc = ''
            for c in clean:
                if c == '-':
                    unenc += ' '
                else:
                    unenc += chr((ord(c) + sector_id - a_offset) % alphabet_len + a_offset)

            if 'north' in unenc:
                print(str(sector_id) + ' | ' + unenc)
                break
