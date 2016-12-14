# -*- coding: utf-8 -*-
import hashlib
import time

class Day14:

    def __init__(self):
        self.salt = 'jlmsuwbz'
        # self.salt = 'abc'
        self.keys = []
        self.md5cache = []
        pass

    # Answer: 35186
    def part1(self):
        self.solve()
        print('64th key: ' + str(self.keys[-1:]))

    # Answer: 22429
    def part2(self):
        start = time.time()
        print('Starting at: ' + str(start))

        self.solve_part_2()
        print('64th key: ' + str(self.keys[-1:]))

        end = time.time()
        print('Ending at: ' + str(end))
        print('Elapsed: ' + str(end - start))

    def solve_part_2(self):
        index = 0
        sub_index = 1
        while len(self.keys) < 64:
            hash_string = self.get_cached_md5(index)

            # find triplet
            quintuple_for_triplet = self.find_n_occuring(hash_string, 3)

            # found triplet, search for quintuple
            if any(quintuple_for_triplet):
                while sub_index <= 1000:
                    sub_hash_string = self.get_cached_md5(index + sub_index)

                    if quintuple_for_triplet in sub_hash_string:
                        self.keys.append((index, sub_hash_string))
                        # print(str(index) + ' | ' + str(index) + ': ' + sub_hash_string)
                        break
                    sub_index += 1
                sub_index = 1

            index += 1

    def get_cached_md5(self, index):
        if index >= len(self.md5cache):
            key = hashlib.md5((self.salt + str(index)).encode('UTF-8')).hexdigest()
            for _ in range(2016):
                key = hashlib.md5(key.encode('UTF-8')).hexdigest()
            self.md5cache.append(key)
            return key
        else:
            return self.md5cache[index]

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
                triplets.append((hash_string.index(triplet), c))

        if any(triplets):
            return sorted(triplets)[1][1]*5

        return triplets
