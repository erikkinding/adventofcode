# -*- coding: utf-8 -*-

from aoc import *

inp = input_as_grid("twentytwo.txt", str)
#inp = input_as_values("ex.txt", int)

# state where only infected nodes are part of the set
def init_state_set():
    state = set()
    for ydx, y in enumerate(inp):
        for xdx, x in enumerate(y):
            if x == '#':
                state.add((xdx, ydx))

    return state

# state where only non-clean nodes are part of the dict
# states will be I, W or F
def init_state_dict():
    state = {}
    for ydx, y in enumerate(inp):
        for xdx, x in enumerate(y):
            if x == '#':
                state[(xdx, ydx)] = 'I'

    return state

# 5261
def part1():
    # starting move
    move_idx = 0
    # moves (x, y) U R D L
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    # init state holding (x, y) tuples
    state = init_state_set()
    # starting at center of grid
    pos_x = int(len(inp[0]) / 2)
    pos_y = int(len(inp) / 2)
    
    infections = 0
    bursts = 10000
    for i in range(bursts):
        # current
        current = (pos_x, pos_y)
        
        # check node
        infected = current in state
        
        # infect / disinfect
        if infected:
            state.remove(current)
        else:
            infections += 1
            state.add(current)

        # turn
        turn = 1 if infected else -1
        move_idx = (move_idx + turn) % 4

        # move
        pos_x += moves[move_idx][0]
        pos_y += moves[move_idx][1]

    print("Part1 infections", infections)

# 2511927
def part2():
    # starting move
    move_idx = 0
    # moves (x, y) U R D L
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    # init state holding (x, y) tuples
    state = init_state_dict()
    # starting at center of grid
    pos_x = int(len(inp[0]) / 2)
    pos_y = int(len(inp) / 2)
    
    infections = 0
    bursts = 10000000
    for i in range(bursts):
        # current
        current = (pos_x, pos_y)
        
        # check node
        node_status = 'clean'
        try:
            node_status = state[current]
        except:
            pass
        
        # infect / disinfect
        if node_status == 'clean':
            state[current] = 'W'
        elif node_status == 'W':
            infections += 1
            state[current] = 'I'
        elif node_status == 'I':
            state[current] = 'F'
        elif node_status == 'F':
            del state[current]

        # turn
        if node_status == 'clean':
            turn = -1
        elif node_status == 'W':
            turn = 0 # do not turn
        elif node_status == 'I':
            turn = 1
        elif node_status == 'F':
            turn = 2

        # only change move idx if we're changing direction
        if turn != 0:
            move_idx = (move_idx + turn) % 4

        # move
        pos_x += moves[move_idx][0]
        pos_y += moves[move_idx][1]

    print("Part2 infections", infections)

def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()