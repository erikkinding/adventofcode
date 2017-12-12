# -*- coding: utf-8 -*-

import aoc

programs = {}
visited = []
groups = []

def setup():
    inp = aoc.input_as_rows("twelve.txt")
    for p in inp:
        seg = p.split('<->')
        key = seg[0].strip()
        conns = seg[1].strip().split(', ')
        programs[key] = conns

    # clear for part 2
    del(visited[:])


# 130
def part1():
    
    # setup
    setup()    

    # start at '0'
    current = '0'
    # visited incl steps
    visited.append(current)
    # explore connections to starting program
    explore = programs[current]
    # go
    while any(explore):
        current = explore.pop(0)

        if current in visited:
            continue

        currents_connections = programs[current]

        for pid in currents_connections:
            if not pid in visited:
                explore.append(pid)

        visited.append(current)

    print("Part1: Group contains", len(visited), "programs")


# 189
def part2():
     # setup
    setup()

    for current, value in programs.items():
        current = str(current)

        # skip groups already processed
        # and anything we've already seen
        if current in groups or current in visited:
            continue
        
        # visited incl steps
        visited.append(current)
        # explore connections to starting program
        explore = value
        # go
        while any(explore):
            current = explore.pop(0)

            if current in visited:
                continue

            currents_connections = programs[current]

            for pid in currents_connections:
                if not pid in visited:
                    explore.append(pid)

            visited.append(current)

        groups.append(current)

    print("Part2: Number of groups: ", len(groups))


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()