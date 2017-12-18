# -*- coding: utf-8 -*-

from aoc import *
from collections import defaultdict

inp = input_as_rows("eighteen.txt")


def get_value(reg_val):
    reg_val = reg_val
    try:
        reg_val = int(reg_val)
    except:
        reg_val = registers[reg_val]

    return reg_val

def set_value(register, value):
    registers[register] = value

# 7071
registers = defaultdict(int)
def part1():
    
    # run program
    program = inp
    recorded = 0
    program_len = len(program)
    i = 0
    while True:
        if i < 0 or i >= program_len:
            print("Jumped outside of program, quitting...")
            break

        instr_args = program[i].split()
        instr = instr_args[0]
        args = instr_args[1:]
        if instr == 'snd':
            value = get_value(args[0])
            recorded = value
            
        elif instr == 'set':
            x = args[0]
            y = get_value(args[1])
            set_value(x, y)

        elif instr == 'add':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value + y_value
            set_value(x, new_x)
            
        elif instr == 'mul':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value * y_value
            set_value(x, new_x)

        elif instr == 'mod':
            x = args[0]
            y = args[1]
            x_value = get_value(x)
            y_value = get_value(y)
            new_x = 0
            if y_value != 0:
                new_x =  x_value % y_value

            set_value(x, new_x)

        elif instr == 'rcv':
            x = args[0]
            x_value = get_value(x)
            if x_value != 0:
                break
            
        elif instr == 'jgz':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            if x_value > 0:
                i += y_value
                continue
            
        i += 1

    print("part1 recorded value", recorded)


class ProgInstance:
    def __init__(self, id):
        self.id = id
        self.mq = []
        self.registers = defaultdict(int)
        self.blocked = False
        self.running = True
        self.registers['p'] = id
        self.packages_sent = 0
        self.program_index = 0
        pass

    def can_run(self):
        return self.running or not self.blocked

    def get_value(self, reg_val):
        reg_val = reg_val
        try:
            reg_val = int(reg_val)
        except:
            reg_val = self.registers[reg_val]

        return reg_val

    def set_value(self, register, value):
        self.registers[register] = value

def get_receiver(sender):
    if sender == 0:
        return 1
    else:
        return 0


# This is the definition of a deadlock state in our case:
# Both programs blocked while having empty message queues
def deadlocked(instances):
    if instances[0].blocked and instances[1].blocked and len(instances[0].mq) == 0 and len(instances[1].mq) == 0:
        print("Deadlock!")
        return True
    return False

def part2():
    # setup
    program = inp
    program_len = len(program)
    instances = [ProgInstance(0), ProgInstance(1)]
    
    # Run each program in turn until it either:
    # - runs out of instruction set and stops
    # - reaches blocked state waiting for a message to it's queue
    #
    # If both programs are in a stopped state, stop and report messages sent
    p_toggle = 0

    while not deadlocked(instances) and (instances[0].can_run() or instances[1].can_run()):

        p = instances[p_toggle]
        #print("running", p.id, p.registers, p.mq, p.packages_sent, p.running, p.blocked)
        while True:
            if p.program_index < 0 or p.program_index >= program_len:
                print("Jumped outside of program, quitting", p.id)
                p.running = False
                break

            instr_args = program[p.program_index].split()
            instr = instr_args[0]
            args = instr_args[1:]

            # send to the other programs queue
            if instr == 'snd':
                value = p.get_value(args[0])
                receiver = instances[get_receiver(p.id)]
                receiver.mq.append(value)
                p.packages_sent += 1
                
            elif instr == 'set':
                x = args[0]
                y = p.get_value(args[1])
                p.set_value(x, y)

            elif instr == 'add':
                x = args[0]
                x_value = p.get_value(x)
                y_value = p.get_value(args[1])
                new_x =  x_value + y_value
                p.set_value(x, new_x)
                
            elif instr == 'mul':
                x = args[0]
                x_value = p.get_value(x)
                y_value = p.get_value(args[1])
                new_x =  x_value * y_value
                p.set_value(x, new_x)

            elif instr == 'mod':
                x = args[0]
                y = args[1]
                x_value = p.get_value(x)
                y_value = p.get_value(y)
                new_x = 0
                if y_value != 0:
                    new_x =  x_value % y_value

                p.set_value(x, new_x)

            elif instr == 'rcv':
                # we got mail
                if len(p.mq) > 0:
                    value = p.mq.pop(0)
                    x = args[0]
                    x_value = p.set_value(x, value)
                    p.blocked = False

                # no mail, wait...
                else:
                    p.blocked = True
                    break

            elif instr == 'jgz':
                x = args[0]
                x_value = p.get_value(x)
                y_value = p.get_value(args[1])
                if x_value > 0:
                    p.program_index += y_value
                    continue
                
            p.program_index += 1

        # change program instance
        if p_toggle == 0:
            p_toggle = 1
        else:
            p_toggle = 0

    print("part2 p1 sent", instances[1].packages_sent, "packages")

def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()

