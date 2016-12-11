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

    def print_current_step(self):
        for floor in self.steps[-1:]:
            print(floor)

    # recursion?
    def solve(self):

        while not self.completed():
            self.print_current_step()
            self.step()

        self.print_current_step()
        print('Finished after ' + str(self.count_steps()) + ' steps')


    def step(self):
        # current step should never be empty, so we don't need to check for that

        # if we're at top floor but still need to move, go down
        # if no valid moves upward for a floor, we also need to go down
        if self.elevator_position == 3:
            up = False
        else:
            up = True

        # try to take two
        items_to_move = self.steps[-1:][0][self.elevator_position][:1]
        can_move = self.can_move(items_to_move, up)

        if can_move:
            # move items
            self.move_items(items_to_move, up)

            # move elevator
            self.elevator_position = self.elevator_position + 1 if up else self.elevator_position - 1
        else:
            # pop list of steps and rollback elevator position?
            pass

    def move_items(self, items, up):
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

    # Check if items can be left at desired floor
    # Check if items that are moved can leave their floor behind
    def can_move(self, items, up):
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
        for floor in self.steps[-1:][-1:]:
            if len(floor) > 0:
                return False
        return True

    # Reducing initial step from count
    def count_steps(self):
        return len(self.steps) - 1
