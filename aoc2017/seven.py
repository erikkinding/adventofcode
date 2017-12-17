# -*- coding: utf-8 -*-
from collections import Counter
import aoc

inp = aoc.input_as_rows("seven_test.txt")

# node? (name, weight, connections)
def print_stuff(stuff):
    for s in stuff:
        print(s)

programs = {}
def setup_programs():
    tree = []
    for r in inp:
        rs = r.split()
        name = rs[0] 
        weight = int(rs[1].replace('(', '').replace(')', ''))

        rs = r.split("->")
        
        if len(rs) > 1:
            connections = list(map(lambda x : (x.strip(), []), rs[1].split(", ")))
            tree.append((name, connections))
        
        # weight data outside of tree
        programs[name] = weight

    return tree


name_value = {}
name_connections = {}
def part2():
    for r in inp:
        rs = r.split()

        # map programs to their weight
        name = rs[0]
        value = int(rs[1].replace('(', '').replace(')', ''))
        name_value[name] = value

        # if a program has connections, setup
        rs = r.split(" -> ")
        if len(rs) > 1:
            connections = rs[1].split(', ')
            name_connections[name] = connections


    # start at root, traverse tree
    current = 'tknk' # test

    while True:
        break;






# azqje
def part1():
    programs = []
    for r in inp:
        rs = r.split()
        name = rs[0]

        rs = r.split("->")
        if len(rs) > 1:
            connections = list(map(lambda x: x.strip(), rs[1].split(", ")))
            programs.extend(connections)

        programs.append(name)

    counts = Counter(programs)

    # Answer based on the fact that the root would only be referenced once in the file
    print(counts)


def main():
    #print(inp)
    #part1()
    part2()

if __name__ == "__main__":
    main()
