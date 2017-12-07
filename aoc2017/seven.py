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
        connections = []
        if len(rs) > 1:
            connections = list(map(lambda x : (x.strip(), []), rs[1].split(", ")))
            shit.extend(sc)
            tree.append((name, connections))
        
        # weight data outside of tree
        programs[name] = weight

    return tree


def resolve_tree(tree):
    
    print_stuff(tree)
    print("root is ", tree[0])


def part1():
    programs = []
    for r in inp:
        rs = r.split()
        name = rs[0] 
        
        rs = r.split("->")
        connections = []
        if len(rs) > 1:
            connections = list(map(lambda x : x.strip(), rs[1].split(", ")))
            programs.extend(connections)
            
        programs.append(name)

    counts = Counter(programs)
    print(counts)

def part2():
    print("part2")

def main():
    #print(inp)
    part1()
    part2()

if __name__ == "__main__":
    main()