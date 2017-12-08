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
        connections = []
        if len(rs) > 1:
            connections = list(map(lambda x : (x.strip(), []), rs[1].split(", ")))
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


#def find_rec(tree, target):
#    return find_rec(tree, target, 0)

def find_mod_rec(tree, target, replacement, ret):
    for node in tree:
        if any(node[1]):
            find_mod_rec(node[1], target, replacement, ret)

        #print(node)
        if node[0] == target:
            print(node)
            print(replacement)
            print("HIT!")
            node = replacement


def find_rec(tree, target, depth):
    for node in tree:
        #print(node)
        if any(node[1]):
            find_rec(node[1], target, depth+1)

        if node[0] == target:
            print("Hit taget at depth ", depth)

    return


def print_tree_rec(tree, depth):
    for node in tree:
        offset = "--" * depth
        print("|" + offset + str(node[0]))
        if any(node[1]):
            print_tree_rec(node[1], depth+1)

    return


sums = {}
def part2():
    tree = setup_programs()

    for node in tree:
        key = ""
        ksum = 0
        for c in node[1]:
            key += c[0]
            ksum += int(programs[c[0]]) + int(programs[node[0]])
        sums[key] = ksum

    print(sums.items())


    print_stuff(tree)
    print_stuff(programs.items())

def part3():

    tree = [('root', [ ('b1', [ ('c1', []), ('c2', []), ('c3', [('d1', []), ('d2', [])]), ('c4', [])]), ('b2', [])])]

    print_tree_rec(tree, 1)
    #find_rec(tree, 'c4', 0)
    tree = find_mod_rec(tree, 'd1', ('d1', [('e1', [])]), [])
    print_tree_rec(tree, 1)

    print("part2")

def main():
    #print(inp)
    #part1()
    part2()

if __name__ == "__main__":
    main()
