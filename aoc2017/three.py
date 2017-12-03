# -*- coding: utf-8 -*-

inp = 277678

# R, U, L, D
# [x, y]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

def part_one():
    square = 1
    stepLength = 1
    moveIndex = 0
    posx = 0
    posy = 0

    while True:

        # Step each length segment two times. Conclusion from studying the data
        for _ in range(0, 2):
            move = moves[moveIndex % 4]
            # Take x steps for each edge then turn.
            for _ in range(0, stepLength):
                posx += move[0]
                posy += move[1]
                square += 1
                if square == inp:
                    print("Part1-> x: ", posx, "y: ", posy, "dist: ", abs(posx) + abs(posy))
                    return

            moveIndex += 1
        stepLength += 1


def part_two():
    # yolo estimate of needed grid size
    width = 100
    height = 100
    grid = [[0 for x in range(width)] for y in range(height)]
    stepLength = 1
    moveIndex = 0
    # Start at the middle of the grid
    posx = int(width/2)
    posy = int(height/2)
    grid[posx][posy] = 1

    while True:

        # Step each length segment two times. Conclusion from studying the data
        for _ in range(0, 2):
            move = moves[moveIndex % 4]
            # Take x steps for each edge then turn.
            for _ in range(0, stepLength):
                posx += move[0]
                posy += move[1]
                nextValue = value_from_grid(posx, posy, grid)
                grid[posx][posy] = nextValue

                if nextValue > inp:
                    print("Part2-> x: ", posx, "y: ", posy, "value: ", nextValue)
                    return

            moveIndex += 1
        stepLength += 1


def value_from_grid(posx, posy, grid):
    # fuck bounds checking, grid estimate should be big enough ;)
    value = 0
    for i in range(-1, 2):
        for k in range(-1, 2):
            if not (i == 0 and k == 0):
                value += grid[posx+i][posy+k]
    return value


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
