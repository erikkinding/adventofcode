 # -*- coding: utf-8 -*-
import time

def time_it(f, *args):
    t0 = time.time()
    ret = f(*args)
    t1 = time.time()
    td = t1 - t0
    print("Executed in", td, "seconds")
    return ret

def get_file(filename):
    return open("input/" + filename, 'r')


def input_as_string(filename):
    return get_file(filename).read()

def input_as_rows(filename):
    return get_file(filename).read().splitlines()


def input_as_values(filename, t, delimiter):
    return map(t, get_file(filename).read().split(delimiter))

def input_as_grid(filename, t):
    rows = input_as_rows(filename)
    grid = []
    for row in rows:
        grid.append(map(t, row.split()))

    return grid


def input_as_grid(filename):
    rows = input_as_rows(filename)
    grid = []
    for row in rows:
        grid.append(row.split())

    return grid
