# -*- coding: utf-8 -*-


class Day10:

    def __init__(self):
        self.bots = {}
        # self.goal = [2, 5]
        self.goal = [17, 61]
        # self.output = {}
        pass

    # Answer: 101
    def part1(self):
        data = open('aoc2016/input/day10_1.txt', 'r').read().splitlines()

        # initial values to bots
        row = 1
        while True:
            row_index = row % len(data)
            split = data[row_index].split()
            if split[0] == 'value':
                del(data[row_index])
                self.value_to_bot(split[1], split[5])
            else:
                bot = split[1]
                hit = False
                if self.bot_can_act(bot):
                    low_to = split[5] + '_' + split[6]
                    high_to = split[10] + '_' + split[11]
                    hit = self.act(bot, low_to, high_to)
                if hit:
                    break
            row += 1

        print(self.bots)

    def act(self, bot, low_to, high_to):
        bot_key = 'bot_' + bot
        bot_values = sorted(self.bots[bot_key])
        if bot_values == self.goal:
            print('Hit goal, comparison by: ' + bot)
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
