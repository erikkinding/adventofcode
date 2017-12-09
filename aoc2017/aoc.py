 # -*- coding: utf-8 -*-

def get_file(filename):
    return open("input/" + filename, 'r')


def input_as_string(filename):
    return get_file(filename).read()

def input_as_rows(filename):
    return get_file(filename).read().splitlines()


def input_as_values(filename, t):
    return map(t, get_file(filename).read().split())


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
