# -*- coding: utf-8 -*-

from aoc import *

# This was a bad attempt at optimization...
def get_dance_moves():
    moves = []
    inp = input_as_values("sixteen.txt", str, ',')
    for move in inp:
        action = move[0]
        # Spin
        if action == 's':
            x = int(move[1:])
            moves.append(('s', x))
            
        # Exchange
        elif action == 'x':
            ab = move[1:].split('/')
            ai = int(ab[0])
            bi = int(ab[1])
            moves.append(('x', ai, bi))
            
        # Swap
        elif action == 'p':
            ab = move[1:].split('/')
            a = ab[0]
            b = ab[1]
            moves.append(('p', a, b))

    return moves

dance_log = []
def log_dance(order, i):
    order_str = ''.join(order)
    
    # is this state already seen?
    if order_str in dance_log:
        return True

    dance_log.append(order_str)
    return False


def dance(times):
    dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    n_dancers = len(dancers)
    dance_moves = get_dance_moves()

    for i in range(times):
        for move in dance_moves:
            
            action = move[0]

            # Spin
            if action == 's':
                x = move[1]
                dancers = dancers[n_dancers-x:] + dancers[:n_dancers-x]

            # Exchange
            elif action == 'x':
                ai = move[1]
                bi = move[2]
                ad = dancers[ai]
                bd = dancers[bi]

                dancers[ai] = bd
                dancers[bi] = ad
                
            # Swap
            elif action == 'p':
                ai = dancers.index(move[1])
                bi = dancers.index(move[2])
                ad = dancers[ai]
                bd = dancers[bi]

                dancers[ai] = bd
                dancers[bi] = ad

        # only run if part two, i.e more than one loop
        found_loop = log_dance(dancers, i)
        if i > 0 and found_loop:
            print("looping at", i)
            print("run again with 'times mod", i, "' (", times % i,") as iterations")
            return
        

    return ''.join(dancers)


def part1():
    print("Part1: ", dance(1))

# Hmm... Will be too slow... Try to find loop?
def part2():
    print("Part2: ", dance(16))

def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()