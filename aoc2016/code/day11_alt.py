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
            'pairs': ((0, 1), (0, 2)),
            'distance': 0
        }

        # Initialize with starting position at distance 0
        self.visited.append((self.state['pairs'], 0))
        self.solve()

        #print(str(self.valid_state(self.state['pairs'])))

    def solve(self):

        current = self.state
        moves = self.reachable(current['elevator_level'], current['pairs'])

        for move in moves:
            moves.append(self.reachable(move))

        pass

    # "reachable nodes"
    def reachable(self, elevator_level, pairs):
        attempted_state = pairs
        for pair in pairs:
            if
        return []

    def can_move(self, items, elevator_level):
        if elevator_level > 3:
            return False
        if elevator_level < 0:
            return False

        test_floor = []
        # create a setup of items to verify
        items_on_next_floor = self.steps[-1:][0][to_floor]
        if len(items_on_next_floor) > 0:
            test_floor.extend(items_on_next_floor)
        test_floor.extend(items)
        next_floor_valid = self.valid_floor(test_floor)

        if not next_floor_valid:
            return False

        # remove items from current floor and test what is left
        current_floor = list(self.steps[-1:][0][self.elevator_position])
        for item in items:
            for idx, citem in enumerate(current_floor):
                if citem == item:
                    del (current_floor[idx])

        return self.valid_floor(current_floor)

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


