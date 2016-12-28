# -*- coding: utf-8 -*-

# Puzzle from http://adventofcode.com/
# Day 1 - part 2.

def visit_twice(input):
    """Calculate the taxicab geometry for the first location visited twice.
    More info about taxicab geometry here: https://en.wikipedia.org/wiki/Taxicab_geometry

    input: a list of movements.
    return: Blocks away from the start point (0,0).
    """
    steps = [x.strip() for x in input.split(',')]

    direction = 0
    x = 0
    y = 0

    calc_x = [0, 1, 0, -1]
    calc_y = [1, 0, -1, 0]
    increase = {'R': +1, 'L': -1}

    visited = set()

    for step in steps:
        rotation = step[0]
        walk = int(step[1:])
        direction = (direction + increase[rotation]) % 4

        for foot in range(walk):
            x = x + calc_x[direction]
            y = y + calc_y[direction]

            current = str(x) + "," + str(y)
            if current in visited:
                return abs(x) + abs(y)

            visited.add(current)

    return abs(x) + abs(y)

assert visit_twice("R8, R4, R4, R8") == 4
print visit_twice("R8, R4, R4, R8")

input = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3"
assert visit_twice(input) == 158
print visit_twice(input)
