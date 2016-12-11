# -*- coding: utf-8 -*-
import itertools

class Day11:

    def __init__(self):
        # init state
        self.steps = []
        self.setup_test()
        self.elevator_position = 0
        pass

    def setup_test(self):
        floors = []
        # 1st
        # floors.append(['E', 'HM', 'LM'])
        floors.append(['Hy_M', 'Li_M'])
        # 2st
        floors.append(['Hy_G'])
        # 3st
        floors.append(['Li_G'])
        # 4st
        floors.append([])
        # Add configuration as initial step. Should be deducted from step count in the end
        self.steps.append(floors)


    # Answer:
    def part1(self):
        self.solve()
        # self.elevator_position = 2
        # can_move = self.can_move(['Li_G'], self.elevator_position - 1)
        # print(str(can_move))
        self.print_current_step()
        print('Finished after ' + str(self.count_steps()) + ' steps')

    def print_current_step(self):
        for idx, floor in enumerate(self.current_step()):
            elevator = '#\t' if idx == self.elevator_position else ' \t'
            print(elevator + ' | ' + str(floor))

    def current_step(self):
        return self.steps[-1:][0]

    # recursion?
    def solve(self):

        if self.completed():
            self.print_current_step()
            print('Finished after ' + str(self.count_steps()) + ' steps')

        while not self.completed():
            # To check all possible solutions, we need try all different combinations recursively
            to_try = self.get_permutations()

            could_step = False
            # for permutations in to_try:
            idx = 0
            while len(to_try) > 0:
                # if we're at top floor but still need to move, go down
                # if no valid moves upward for a floor, we also need to go down
                if self.elevator_position == 3:
                    up = False
                else:
                    up = True

                could_step = self.step(to_try[-1:], up)
                if could_step:
                    # update permutations
                    to_try = self.get_permutations()
                    # idx = 0
                else:
                    to_try.pop()

            if not could_step:
                # back one step and reverse
                self.elevator_position = self.elevator_position - 1 if up else self.elevator_position + 1
                self.steps.pop()

    def get_permutations(self):
        to_try_tuples = list(set(map(lambda x: tuple(sorted(x)), itertools.permutations(self.current_step()[self.elevator_position], 2))))
        to_try = list(map(lambda x: list(x), to_try_tuples))
        to_try.extend(self.current_step()[self.elevator_position])
        return to_try

    def step(self, items_to_move, up):

        can_move = self.can_move(items_to_move, up)

        if can_move:
            # move items
            self.move_items(items_to_move, up)

            # move elevator
            self.elevator_position = self.elevator_position + 1 if up else self.elevator_position - 1
            return True
        else:
            # pop list of steps and rollback elevator position?
            # maybe just return...
            return False

    def move_items(self, items, up):
        # lol
        if isinstance(items, basestring):
            items = [items]

        # next floor based on direction
        to_floor = self.elevator_position + 1 if up else self.elevator_position - 1

        # next floor new items
        next_floor = []
        items_on_next_floor = self.steps[-1:][0][to_floor]
        if len(items_on_next_floor) > 0:
            next_floor.extend(items_on_next_floor)
        next_floor.extend(items)

        # old floor new items
        old_floor = list(self.steps[-1:][0][self.elevator_position])
        for item in items:
            for idx, citem in enumerate(old_floor):
                if citem == item:
                    del (old_floor[idx])

        # create step
        current_step = self.steps[-1:][0]
        next_step = []
        for idx, floor in enumerate(current_step):
            if idx == to_floor:
                next_step.append(next_floor)
                continue
            if idx == self.elevator_position:
                next_step.append(old_floor)
                continue
            # else just add old state
            next_step.append(current_step[idx])

        self.steps.append(next_step)

        # moved
        self.print_current_step()
        print('----------------' + str(self.elevator_position))
        print('...')

    # Check if items can be left at desired floor
    # Check if items that are moved can leave their floor behind
    def can_move(self, items, up):
        # lol
        if isinstance(items, basestring):
            items = [items]

        # next floor based on direction
        to_floor = self.elevator_position + 1 if up else self.elevator_position - 1

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
                    del(current_floor[idx])

        return self.valid_floor(current_floor)

    def valid_floor(self, items):
        # empty floor is safe
        if len(items) == 0:
            return True

        # only microchips is safe
        # add all microchips to list for further checks
        all_ms = True
        microchips = []
        for item in items:
            if item[-1:] != 'M':
                all_ms = False
            else:
                microchips.append(item)
        if all_ms:
            return True

        # else, no chip can be without a corresponding generator
        all_match = True
        for mc in microchips:
            matching_generator = False
            for item in items:
                if item[-1:] == 'G' and item[:2] == mc[:2]:
                    matching_generator = True
            if not matching_generator:
                return False

        return all_match

    # Completed defined as all except top floor being empty
    # Investigate last step taken
    def completed(self):
        # for floor in self.steps[-1:][0][3]:
        #    if len(floor) > 0:
        #        return False
        # return True
        return self.steps[-1:][0][3] == 4

    # Reducing initial step from count
    def count_steps(self):
        return len(self.steps) - 1
