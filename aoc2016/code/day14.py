# -*- coding: utf-8 -*-
import hashlib

class Day14:

    def __init__(self):
        self.salt = 'jlmsuwbz'
        self.salt = 'abc'
        self.keys = []
        pass

    # Answer:
    def part1(self):
        self.solve()
        print('64th key: ' + str(self.keys[-1:]))

    def part2(self):
        self.solve_part_2()
        print('64th key: ' + str(self.keys[-1:]))

    #  44616 too high...
    def solve_part_2(self):
        index = 0
        sub_index = 1
        while len(self.keys) < 64:
            hash_string = hashlib.md5(self.salt + str(index)).hexdigest()

            for i in range(2016):
                hash_string = hashlib.md5(hash_string).hexdigest()

            # find triplet
            triplet = self.find_n_occuring(hash_string, 3)

            # found triplet, search for quintuple
            if any(triplet):
                while sub_index <= 1000:
                    hash_string = hashlib.md5(self.salt + str(index + sub_index)).hexdigest()

                    for k in range(2016):
                        hash_string = hashlib.md5(hash_string).hexdigest()

                    if triplet[0] * 5 in hash_string:
                        self.keys.append((index, hash_string))
                        print(str(index) + ' | ' + str(index) + ': ' + hash_string)
                        break
                    sub_index += 1
                sub_index = 1

            index += 1
            print('index ' + str(index))

    def solve(self):
        index = 0
        sub_index = 1
        while len(self.keys) < 64:
            hash_string = hashlib.md5(self.salt + str(index)).hexdigest()

            # find triplet
            triplet = self.find_n_occuring(hash_string, 3)

            # found triplet, search for quintuple
            if any(triplet):
                while sub_index <= 1000:
                    hash_string = hashlib.md5(self.salt + str(index + sub_index)).hexdigest()
                    if triplet[0]*5 in hash_string:
                        self.keys.append((index, hash_string))
                        break
                    sub_index += 1
                sub_index = 1

            index += 1

    @staticmethod
    def find_n_occuring(hash_string, multiplier):
        triplets = []
        for c in hash_string:
            triplet = c*multiplier
            if triplet in hash_string:
                triplets.append((hash_string.index(triplet), triplet))

        if any(triplets):
            return sorted(triplets)[1][1]

        return triplets
