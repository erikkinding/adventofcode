# -*- coding: utf-8 -*-
import time

class Day11:

    def __init__(self):

        # possible paths to target
        self.best_path_steps = 100000000

        # state with distance
        self.visited_states = {}

        # Initialize with starting position at distance 0
        #                 E  G  M  G  M   Distance
        # start_state = ([0, 1, 0, 2, 0], 0)  # 11 steps
        # start_state = ([0, 1, 0, 2, 0, 0, 0], 0)  # 21 steps

    # Answer: 37
    def part1(self):
        t0 = time.time()
        start_state = ([0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1], 0)  # 37 steps
        self.solve(start_state)
        print('Best path: ' + str(self.best_path_steps))
        print('Elapsed: ' + str(time.time() - t0) + 's')

    # Answer: 61
    def part2(self):
        t0 = time.time()
        start_state = ([0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0], 0)  # 61 steps
        self.solve(start_state)
        print('Best path: ' + str(self.best_path_steps))
        print('Elapsed: ' + str(time.time() - t0) + 's')


    def solve(self, start_state):

        # set init in visited
        self.better_path(start_state)

        possible_moves = self.possible_moves(start_state)

        while any(possible_moves):
            current = possible_moves.pop(0)
            next_from_current = self.possible_moves(current)

            for next in next_from_current:
                possible_moves.append(next)

    def hit_target(self, state):
        state_items = state[0]
        for item in state_items:
            if item < 3:
                return False

        return True

    def floor_below_has_items(self, state):
        state_items = state[0][1:]
        elevator_level = state[0][0]

        floor_idx = elevator_level
        while floor_idx > 0:
            for item in state_items:
                if item == floor_idx - 1:
                    return True
            floor_idx -= 1

        return False

    # "reachable nodes"
    def possible_moves(self, state):

        state_items = state[0][1:]
        current_distance = state[1]
        elevator_level = state[0][0]

        modifiers = []
        if elevator_level > 0 and self.floor_below_has_items(state):
            modifiers.append(-1)
        if elevator_level < 3:
            modifiers.append(1)

        items_indices_on_floor = []
        for idx,item in enumerate(state_items):
            if item == elevator_level:
                items_indices_on_floor.append(idx)

        possible_next_states = []
        combinations = self.combinations(items_indices_on_floor)
        for modifier in modifiers:
            for combination in combinations:
                next_state = []
                next_state_items = [elevator_level + modifier]
                for idx, item in enumerate(state_items):
                    if idx in combination:
                        next_state_items.append(item + modifier)
                    else:
                        next_state_items.append(item)

                next_state.append(next_state_items)
                next_state.append(current_distance + 1)

                if self.hit_target(next_state):
                    print(next_state[1])
                    if self.best_path_steps > next_state[1]:
                        self.best_path_steps = next_state[1]
                    return []

                if self.valid_state(next_state) and self.better_path(next_state):
                    possible_next_states.append(next_state)


        return possible_next_states

    @staticmethod
    def combinations(items):
        combinations = []

        for idx in range(len(items)):
            # add singles
            combinations.append([items[idx]])
            for kdx in range(len(items)):
                if idx != kdx and [items[kdx], items[idx]] not in combinations:
                    combinations.append([items[idx], items[kdx]])
                    continue
        return combinations

    @staticmethod
    def valid_state(state):

        state_items = state[0][1:]

        # If all pairs are on same floor, it's safe
        idx = 0
        all_m_with_g = True
        single_microchips = []
        while idx < len(state_items):
            if state_items[idx] != state_items[idx+1]:
                all_m_with_g = False
                single_microchips.append(idx+1)
            idx += 2

        if all_m_with_g:
            return True

        # if not, see if any single microchip is on the same floor as a generator
        for single_m in single_microchips:
            idx = 0
            while idx < len(state_items):
                if state_items[single_m] == state_items[idx]:
                    return False
                idx += 2

        return True

    def better_path(self, state):
        state_pairs = state[0][1:]
        elevator_level = [state[0][0]]

        idx = 0
        state_pair_tuples = []
        while idx < len(state_pairs):
            state_pair_tuples.append((state_pairs[idx], state_pairs[idx+1]))
            idx += 2

        to_hash = elevator_level + sorted(state_pair_tuples)
        state_hash = hash(tuple(to_hash))
        distance = state[1]

        if not state_hash in self.visited_states.keys():
            self.visited_states[state_hash] = distance
            return True
        elif self.visited_states[state_hash] > distance:
            self.visited_states[state_hash] = distance
            return True
        else:
            return False
