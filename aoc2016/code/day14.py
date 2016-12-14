# -*- coding: utf-8 -*-
import hashlib

class Day14:

    def __init__(self):
        self.salt = 'jlmsuwbz'
        # self.salt = 'abc'
        self.keys = []
        # self.md5cache = []
        pass

    # Answer: 35186
    def part1(self):
        self.solve()
        print('64th key: ' + str(self.keys[-1:]))

    # Answer: 22429
    def part2(self):
        self.solve_part_2()
        print('64th key: ' + str(self.keys[-1:]))

    #  44616 too high...
    def solve_part_2(self):
        # build cache
        md5cache = []
        for i in range(30000):
            dkey = hashlib.md5(self.salt + str(i)).hexdigest()
            for _ in range(2016):
                dkey = hashlib.md5(dkey).hexdigest()
            md5cache.append(dkey)

        index = 0
        sub_index = 1
        while len(self.keys) < 64:
            hash_string = md5cache[index]

            # find triplet
            triplet = self.find_n_occuring(hash_string, 3)

            # found triplet, search for quintuple
            if any(triplet):
                while sub_index <= 1000:
                    sub_hash_string = md5cache[index + sub_index]

                    if triplet[0] * 5 in sub_hash_string:
                        self.keys.append((index, sub_hash_string))
                        print(str(index) + ' | ' + str(index) + ': ' + sub_hash_string)
                        break
                    sub_index += 1
                sub_index = 1

            index += 1

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
