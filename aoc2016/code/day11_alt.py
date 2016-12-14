# -*- coding: utf-8 -*-
import itertools


class Day11_alt:

    def __init__(self):
        # F4 .  .  .  .  .
        # F3 .  .  .  LG .
        # F2 .  HG .  .  .
        # F1 E  .  HM .  LM
        #
        # init state
        # state: elevator level, pairs, distance
        self.state = {}

        # hashes of pair states
        self.visited = []

    # Answer:
    def part1(self):
        self.state = {
            'elevator_level': 0,
            #          M  G    M  G
            'pairs': [(0, 1), (0, 2)],
            'distance': 0
        }

        # Initialize with starting position at distance 0
        self.visited.append((self.state['pairs'], 0))
        # self.solve()
        #print(self.reachable(self.state['elevator_level'], self.state['pairs']))
        #print(str(self.valid_state(self.state['pairs'])))
        print(self.combinations([(0, 0), (1, 0)], 3))

    def solve(self):

        current = self.state
        moves = self.reachable(current['elevator_level'], current['pairs'])

        for move in moves:
            moves.append(self.reachable(move))

        pass

    # "reachable nodes"
    def reachable(self, elevator_level, pairs):
        # Only try to change state of items on current floor (elevator_level)
        # Include index of "pairs" for mapping later on
        to_include_in_permutations = []
        for idx, pair in enumerate(pairs):
            if pair[0] == elevator_level:
                to_include_in_permutations.append((idx, 0))
            if pair[1] == elevator_level:
                to_include_in_permutations.append((idx, 1))

        # permutations holds a list of possible states if we move something(s)
        permutations = []

        # for idx in range(len())



        # "permutations" is both all possible pairs and items alone
        # apply +- one level for the item
        #permutations = []
        #if elevator_level < 3:
        #    permutations.append(list(set(map(
        #        lambda y: tuple(sorted(y)), itertools.permutations(map(
        #            lambda x: (x[0], x[1] + 1), to_include_in_permutations), 2)))))

        #if elevator_level > 0:
        #    permutations.append(list(set(map(
        #        lambda y: tuple(sorted(y)), itertools.permutations(map(
        #            lambda x: (x[0], x[1] - 1), to_include_in_permutations), 2)))))


        # try moving pairs first

        # then singles

        #if elevator_level < 3:
        #    for item in to_include_in_permutations:
        #        permutations.append((item[0], item[1] + 1))

        #if elevator_level > 0:
        #    for item in to_include_in_permutations:
        #        permutations.append((item[0], item[1] - 1))


        # possible next states are a list of lists of tuples
        #   - a list of tuples is a state
        #
        # try to go up with all of them
        # possible_next_states = []

        return permutations

    def visited(self, pairs):
        return hash(pairs) in self.visited

    def apply_move_to_combination(self, combination):
        modified = []
        for combination

    @staticmethod
    # [tuple, (tuple, tuple), tuple]
    def combinations(items):
        combinations = []

        for idx in range(len(items)):
            # add singles
            combinations.append(items[idx])
            for kdx in range(len(items)):
                if idx != kdx and (items[kdx], items[idx]) not in combinations:
                    combinations.append((items[idx], items[kdx]))
                    continue
        return combinations

    @staticmethod
    def valid_state(pairs):
        valid = True
        for idx, pair in enumerate(pairs):
            # check so that no other item2 of pair is on same floor as item1 of current

            # Microchip and Generator is on the same level, thus Microchip is safe
            # Check next pair
            mc_is_with_g = pair[0] == pair[1]
            if mc_is_with_g:
                continue

            # If Microchip is alone on one level, check for dangerous generators
            # If any generator is on the same level as a lonely microchip, state is invalid
            other_pairs = []
            for i in range(len(pairs)):
                if i != idx:
                    other_pairs.append(pairs[i])

            for other_pair in other_pairs:
                if pair[0] == other_pair[1]:
                    valid = False
                    break

        return valid

    @staticmethod
    def finished(state):
        # for 2 pairs, 12
        # for 3 pairs, 18
        return sum(map(lambda x: sum(x), state['pairs'])) == 12


