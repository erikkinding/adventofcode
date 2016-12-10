# -*- coding: utf-8 -*-


class Day10:

    def __init__(self):
        self.bots = {}
        # self.goal = [2, 5]
        self.goal = [17, 61]
        self.check_goal = False
        # self.output = {}
        pass

    # Answer: 101
    def part1(self):
        self.check_goal = True
        data = open('aoc2016/input/day10_1.txt', 'r').read().splitlines()

        # initial values to bots
        for row_index, row in enumerate(data):
            split = row.split()
            if split[0] == 'value':
                del (data[row_index])
                self.value_to_bot(split[1], split[5])

        # parse instructions
        row = 0
        while True:
            row_index = row % len(data)
            split = data[row_index].split()

            bot = split[1]
            hit = False
            if self.bot_can_act(bot):
                low_to = split[5] + '_' + split[6]
                high_to = split[10] + '_' + split[11]
                hit = self.act(bot, low_to, high_to)
            if hit:
                print('Hit goal, comparison by: ' + bot)
                break
            row += 1

    # Answer: 37789
    def part2(self):
        data = open('aoc2016/input/day10_1.txt', 'r').read().splitlines()

        # initial values to bots
        for row_index, row in enumerate(data):
            split = row.split()
            if split[0] == 'value':
                del (data[row_index])
                self.value_to_bot(split[1], split[5])

        # parse instructions
        row = 0
        while self.bots_with_two_chips():
            row_index = row % len(data)
            split = data[row_index].split()

            bot = split[1]
            if self.bot_can_act(bot):
                low_to = split[5] + '_' + split[6]
                high_to = split[10] + '_' + split[11]
                self.act(bot, low_to, high_to)

            keys = self.bots.keys()
            if 'output_0' in keys and 'output_1' in keys and 'output_2' in keys:
                print('Multiplied: ' + str(self.bots['output_0'][0] * self.bots['output_1'][0] * self.bots['output_2'][0]))
                break
            row += 1

    def bots_with_two_chips(self):
        for bot_key in self.bots.keys():
            if len(self.bots[bot_key]) == 2:
                return True
        return False

    def act(self, bot, low_to, high_to):
        bot_key = 'bot_' + bot
        bot_values = sorted(self.bots[bot_key])
        if self.check_goal and bot_values == self.goal:
            return True
        else:
            self.add_value(bot_values[0], low_to)
            self.add_value(bot_values[1], high_to)
            # clear bots values
            self.bots[bot_key] = []
            return False

    def bot_can_act(self, bot):
        act = False
        bot_key = 'bot_' + bot
        if bot_key in self.bots.keys() and len(self.bots[bot_key]) == 2:
            act = True
        return act

    def value_to_bot(self, value, bot):
        self.add_value(value, 'bot_' + bot)

    def add_value(self, value, key):
        if key in self.bots.keys():
            self.bots[key].append(int(value))
        else:
            self.bots[key] = [int(value)]
