# -*- coding: utf-8 -*-

from aoc import *

inp = input_as_grid("nineteen.txt", str)

# xy
moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
diagram = ['|', '-', '+', '.']
letters = []
visited = []

def move(direction, pos):
    # apply move
    mod = moves[direction]
    x = pos[0] + mod[0]
    y = pos[1] + mod[1]
    
    # new position
    return (x, y)


def moves_from_position(direction, position):
    # What symbol in the diagram are we currently on?
    diagram_symbol = inp[position[1]][position[0]]

    # If . we reached the end
    if diagram_symbol == '.':
        print("Reached the end!")
        return []

    # If + we should turn and possibly explore more than one direction
    next_moves = []
    if diagram_symbol == '+':
        for md, mm in moves.items():
            
            pn = move(md, position)
            if pn[1] < 0 or pn[1] >= len(inp):
                continue
            if pn[0] < 0 or pn[0] >= len(inp[0]):
                continue

            if inp[pn[1]][pn[0]] is not '.' and pn not in visited:
                next_moves.append(md)
                

        return next_moves

    # Else, keep on moving the same direction. This is the case for |, - and letters
    #if diagram_symbol in ['-', '|']:
    return [direction]


def part1and2():

    # Starting position and direction
    posy = 0
    posx = inp[0].index('|')
    pos = (posx, posy)
    visited.append(pos)
    
    next_moves = ['D']
    while any(next_moves):
        direction = next_moves.pop(0)
        pos = move(direction, pos)
        
        # log our travel
        current_symbol = inp[pos[1]][pos[0]]
        # reached the end, stop!
        if current_symbol == '.':
            break

        visited.append(pos)
        # see what we found!
        if current_symbol not in diagram:
            letters.append(current_symbol)

        next_moves.extend(moves_from_position(direction, pos))


    print("Letters:", ''.join(letters))
    print("Steps:", len(visited))


def main():
    time_it(part1and2)

if __name__ == "__main__":
    main()