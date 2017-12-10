# -*- coding: utf-8 -*-
from collections import Counter
import aoc

inp = aoc.input_as_rows("seven.txt")

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


sums = {}
def part2():
    print("...")


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
    part1()
    #part2()

if __name__ == "__main__":
    main()
