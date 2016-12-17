# -*- coding: utf-8 -*-
import itertools


class Day11_alt:

    def __init__(self):
        # F4 .  .  .  .  .
        # F3 .  .  .  LG .
        # F2 .  HG .  .  .
        # F1 E  .  HM .  LM
        # [ [0, 1, 0, 2, 0]
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
        print(self.reachable(self.state['elevator_level'], self.state['pairs']))

    def solve(self):

        current = self.state
        moves = self.reachable(current['elevator_level'], current['pairs'])

        for move in moves:
            moves.append(self.reachable(move))

        pass

    def possible_states(self, combinations):
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
        combinations = self.combinations(to_include_in_permutations)

        # start with (0, 1)
        # then  with ((1,0), (0,1))
        states = []
        for combination in combinations:
            possible_state = list(pairs)
            idx = 0
            while idx < len(combination):
                if isinstance(combination[idx], tuple):
                    # handle move of two items
                    for sub_part in combination:
                        current = possible_state[sub_part[0]]
                        new_value = possible_state[idx][sub_part[1]] + 1
                        possible_state[sub_part[idx]] = self.change_tuple(current, sub_part[0], new_value)
                        idx +=1

                    if self.valid_state(possible_state):
                        states.append(possible_state)
                    idx += 2
                    # handle sinlge move
                else:
                    # the pair to affect, and what item in pair
                    current = possible_state[combination[idx]]
                    new_value = possible_state[combination[idx]][combination[idx]] + 1
                    possible_state[combination[idx]] = self.change_tuple(current, combination[0], new_value)

                    if self.valid_state(possible_state):
                        states.append(possible_state)

                    # jump forward
                    idx+=2


        return combinations

    @staticmethod
    def change_tuple(values, idx, new_value):
        if idx == 0:
            return (new_value, values[1])
        return (values[0], new_value)


    def visited(self, pairs):
        return hash(pairs) in self.visited

    def apply_move_to_combination(self, combination):
        modified = []

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


