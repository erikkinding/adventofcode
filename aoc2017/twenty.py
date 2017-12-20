# -*- coding: utf-8 -*-

from collections import defaultdict
from aoc import *
import re

inp = input_as_rows("twenty.txt")
#inp = input_as_rows("twenty_test_2.txt")

class Particle:

    def __init__(self, id, pos, vel, acc):
        self.id = id

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.pos_z = pos[2]

        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.vel_z = vel[2]

        self.acc_x = acc[0]
        self.acc_y = acc[1]
        self.acc_z = acc[2]

    def update(self):
        # acc is constant
        # update velocity
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y
        self.vel_z += self.acc_z

        # update position
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def distance_from_origo(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def get_pos(self):
        return (self.pos_x, self.pos_y, self.pos_z)


def get_particles():
    # Create particles
    particles = []
    fa = re.compile('-?\d*')
    for idx, row in enumerate(inp):
        numbers = list(map(lambda x: int(x), filter(lambda x: x != '', re.findall(fa, row))))
        pos = (numbers[0], numbers[1], numbers[2])
        vel = (numbers[3], numbers[4], numbers[5])
        acc = (numbers[6], numbers[7], numbers[8])

        p = Particle(idx, pos, vel, acc)
        particles.append(p)

    return particles


def part1():

    particles = get_particles()

    # Let them flow!
    # 200 tics, seems enough
    for i in range(500):
        for p in particles:
            p.update()


    # Find closest
    closest = particles[0]
    for p in particles:
        if p.distance_from_origo() < closest.distance_from_origo():
            closest = p



    print("part1", closest.id, closest.distance_from_origo(), "|", closest.pos_x, closest.pos_y, closest.pos_z)

# 752 too high
# 747 too high
def part2():

    # setup
    particles = get_particles()

    # Let them flow!
    for i in range(100000):
        print(i, len(particles))
        for p in particles:
            p.update()

        # remove any colliding particles
        to_delete = {}
        checked = {}
        for pid, p in enumerate(particles):
            checked[pid] = pid
            for mid, m in enumerate(particles):
                if mid not in checked and p.get_pos() == m.get_pos():
                    to_delete[pid] = pid
                    to_delete[mid] = mid

        particles = [i for j, i in enumerate(particles) if j not in to_delete]

    print("part 2:", len(particles), "remaining")


def main():
    time_it(part1)
    time_it(part2)

if __name__ == "__main__":
    main()