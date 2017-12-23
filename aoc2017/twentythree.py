# -*- coding: utf-8 -*-

from aoc import *
from collections import defaultdict

inp = input_as_rows("twentythree_opt.txt")

def debug_instructions(index):
    print(registers)
    for row_i, row in enumerate(inp):
        marker = '<---' if row_i == index else ''

        print(row, marker) 

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
    program_len = len(program)
    i = 0
    mul_times = 0
    while True:
        if i < 0 or i >= program_len:
            print("Jumped outside of program, quitting...")
            break

        instr_args = program[i].split()
        instr = instr_args[0]
        args = instr_args[1:]

        if instr == 'set':
            x = args[0]
            y = get_value(args[1])
            set_value(x, y)
        
        elif instr == 'sub':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value - y_value
            set_value(x, new_x)

        elif instr == 'mul':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value * y_value
            set_value(x, new_x)
            mul_times += 1
            
        elif instr == 'jnz':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            if x_value != 0:
                i += y_value
                continue
            
        i += 1

    print("part1 mul times", mul_times)

# 1001 too high
def part2():
    # special register setup:
    registers['a'] = 1

    # run program
    program = inp
    program_len = len(program)
    i = 0

    while True:
        debug_instructions(i)
        #print(registers)
        if i < 0 or i >= program_len:
            print("Jumped outside of program, quitting...")
            break

        instr_args = program[i].split()
        instr = instr_args[0]
        args = instr_args[1:]

        # commented instruction
        if instr == '#':
            i+=1
            continue

        elif instr == 'set':
            x = args[0]
            y = get_value(args[1])
            set_value(x, y)
        
        elif instr == 'sub':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value - y_value
            set_value(x, new_x)

        elif instr == 'mul':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            new_x =  x_value * y_value
            set_value(x, new_x)
            
        elif instr == 'jnz':
            x = args[0]
            x_value = get_value(x)
            y_value = get_value(args[1])
            if x_value != 0:
                i += y_value
                continue
            
        i += 1

    print("part2 registers[h] ->", registers['h'])

# 501 too low...
def part2_rewrite():
    # initial state:
    # set b 84
    # set c b -- not needed, redundant
    # jnz a 2 -- in part two when a is initiated with one we skip the next line
    # jnz 1 5
    # mul b 100
    # sub b -100000
    # set c b
    # sub c -17000
    # a = 1 -- only used to skip stuff for part 1
    b = 108400
    c = 125400
    #c = -108600
    d, e, f, g, h = 0, 0, 0, 0, 0

    reg = {'a': 1, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h }

    # start beginning of outer loop:

    while True:
        print(reg)
        #print("1")
        # set f 1
        # set d 2
        reg['f'] = 1
        reg['d'] = 2
        #while True:
            #print("2")
            # set e 2
        reg['e'] = 2

            # this entire loop only seem to toggle f between 1 and 0
            #reg['f'] = reg['d'] % 2
            # second level loop begins here
        while True:

            #print(reg)
            #print("3")
            # set g d
            # mul g e
            # sub g b
            reg['g'] = reg['d']
            reg['g'] = reg['g'] * reg['e']
            reg['g'] -= reg['b']

            # first condition, skip if g is not 0
            # jnz g 2
            # set f 0
            if reg['g'] == 0:
                reg['f'] = 0

            # sub e -1
            # set g e
            # sub g b
            reg['e'] += 1
            reg['g'] = reg['e']
            reg['g'] -= reg['b']

            # should we break out of loop?
            # jnz g -8
            if reg['g'] == 0:
                break

            # sub d -1
            # set g d
            # sub g b
            reg['d'] += 1
            #reg['g'] = reg['d']
            #reg['g'] -= reg['b']

            #print(reg)
            # jnz g -13
            #if reg['g'] == 0:
            #    break


        # jnz f 2
        # sub h -1
        if reg['f'] == 0:
            reg['h'] += 1

        # set g b
        # sub g c
        reg['g'] = reg['b']
        reg['g'] -= reg['c']

        # jnz g 2
        # jnz 1 3
        # this is where we would break out of the program!
        if reg['g'] == 0:
            print(reg)
            print('Breaking, H is:', reg['h'])
            break

        # sub b -17
        reg['b'] += 17
        # jnz 1 -23 -- this simply means we loop...


def main():
    #time_it(part1)
    #time_it(part2)
    time_it(part2_rewrite)

if __name__ == "__main__":
    main()

