from collections import defaultdict
import collections
from functools import reduce, cmp_to_key

f = open("6.input").read().split('\n')
f = list(filter(lambda x: x.strip(), f))

room = [[True if c == '#' else False for c in row] for row in f]
steps = [[False for _ in range(len(room[0]))] for _ in range(len(room))]
pos_y = next(i for i, row in enumerate(f) if '^' in row)
pos_x = next(i for i, c in enumerate(f[pos_y]) if c == '^')
Position = collections.namedtuple('Position', ['y', 'x'])
pos = Position(pos_y, pos_x)
dir = (-1, 0)

def turn_right(dir):
    match dir:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)

def minus(pos: Position, dir):
    return Position(pos.y - dir[0], pos.x - dir[1])

def step(pos: Position, dir):
    return Position(pos.y + dir[0], pos.x + dir[1])

def printsteps(steps):
    for row in steps:
        for val in row:
            print('X' if val else '.', sep='', end='')
        print()

steps[pos.y][pos.x] = True
while pos.y >= 0 and pos.y < len(room) and pos.x >= 0 and pos.x < len(room[0]):
    if room[pos.y][pos.x]:
        pos = minus(pos, dir)
        dir = turn_right(dir)
    steps[pos.y][pos.x] = True
    pos = step(pos, dir)
print(sum([sum(row) for row in steps]))
