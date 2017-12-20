# -*- coding: utf-8 -*-
from collections import Counter
from collections import defaultdict
import aoc

inp = aoc.input_as_rows("seven.txt")

# node? (name, weight, connections)
def print_stuff(stuff):
    for s in stuff:
        print(s)


class Node:
    def __init__(self, name, weight):
        this.connections = []
        this.weight = 0
        this.name = name

class Config:
    def __init__(self):
        self.name_weight = {}
        self.name_connections = {}

def setup():
    config = Config()
    nc_temp = defaultdict(list)
    nw_temp = {}
    for r in inp:
        rs = r.split()

        # map programs to their weight
        name = rs[0]
        weight = int(rs[1].replace('(', '').replace(')', ''))
        nw_temp[name] = weight

        # if a program has connections, setup
        rs = r.split(" -> ")
        if len(rs) > 1:

            connections = rs[1].split(', ')
            nc_temp[name] = connections
            if name == 'inwmb':
                print("DEBUG", connections)
        else:
            nc_temp[name] = []

    config.name_connections = dict(nc_temp)
    config.name_weight = dict(nw_temp)

    return config

# 53037 too high...
def part2():
    config = setup()

    # start at root, traverse tree
    current = 'tknk' # test
    current = 'azqje'

    previous_connections = []
    current_connections = []
    while True:
        print('ncl', len(config.name_connections))
        if current == 'inwmb':
            print("MATCH")
        print("nc", config.name_connections[current])
        current_connections = config.name_connections[current][:]

        towers = []
        for cc in current_connections:
            towers.append((cc, get_tower_weight(cc, config)))

        # get diffing tower
        dt = diffing_tower(towers)
        
        # indicates diffs were among previous connections
        if dt is None:
            print('NONE BREAK:', towers)
            break
        # else select diffing tower to continue the hunt
        else:
            previous_connections = towers[:]
            print("else, setting current to", dt[0])
            current = dt[0]
        
    for t in previous_connections:
        print(t, config.name_weight[t[0]])


def diffing_tower(towers):
    for t in towers:
        count = 0
        for ws in [w[1] for w in towers]:
            if t[1] == ws:
                count += 1
        
        if count == 1:
            return t

    return None

def get_tower_weight(node, config):
    weight = config.name_weight[node]

    current_co = config.name_connections[node][:]
    while any(current_co):
        cc = current_co.pop()
        weight += config.name_weight[cc]
        current_co.extend(config.name_connections[cc])

    return weight



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

    sorted_counts = list(sorted(Counter(programs).items(), key = lambda x: x[1]))

    # Answer based on the fact that the root would only be referenced once in the file
    print("Root node:", sorted_counts[0])


def main():
    #print(inp)
    #part1()
    part2()

if __name__ == "__main__":
    main()
