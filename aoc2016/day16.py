# -*- coding: utf-8 -*-


class Day16:

    def __init__(self):
        pass

    # Answer: 10100011010101011
    def part1(self):
        input_string = '11100010111110100'
        input = map(lambda x: int(x), input_string)
        self.solve(input, 272)

    # Answer: 01010001101011001
    def part2(self):
        input_string = '11100010111110100'
        input = map(lambda x: int(x), input_string)
        self.solve(input, 35651584)

    def solve(self, input, disk_size):

        data = input
        while len(data) < disk_size:
            data = self.dragonize(data)

        cropped_data = data[:disk_size]

        checksum = self.get_checksum(cropped_data)

        print(''.join(map(lambda x: str(x), checksum)))

    @staticmethod
    def get_checksum(data):

        checksum = []
        n = 0
        while True:

            idx = 0
            while idx < len(data):
                if data[idx] == data[idx+1]:
                    checksum.append(1)
                else:
                    checksum.append(0)

                idx += 2

            if len(checksum) % 2 == 0:
                data = checksum
                checksum = []
            else:
                return checksum

    @staticmethod
    def dragonize(input):

        reversed_copy = list(input)[::-1]
        b = []
        for n in reversed_copy:
            if n == 0:
                b.append(1)
            else:
                b.append(0)

        dragonized = []
        dragonized.extend(input)
        dragonized.append(0)
        dragonized.extend(b)

        return dragonized
