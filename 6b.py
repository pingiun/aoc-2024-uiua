from collections import defaultdict
import collections
from functools import reduce, cmp_to_key

f = open("6.test").read().split('\n')
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

def printcircles(steps):
    for i,row in enumerate(steps):
        for j,val in enumerate(row):
            c = 'O' if val else '.'
            c = '#' if room[i][j] else c
            print(c, sep='', end='')
        print()

def printsteps(steps):
    for i,row in enumerate(steps):
        for j,val in enumerate(row):
            if val == (-1, 0):
                c = '^'
            elif val == (1, 0):
                c = 'v'
            elif val == (0, -1):
                c = '<'
            elif val == (0, 1):
                c = '>'
            elif room[i][j]:
                c = '#'
            else:
                c = '.'
            print(c, sep='', end='')
        print()


def intheroom(pos):
    return pos.y >= 0 and pos.y < len(room) and pos.x >= 0 and pos.x < len(room[0])

circles = [[False for _ in range(len(room[0]))] for _ in range(len(room))]
steps[pos.y][pos.x] = dir
while intheroom(pos):
    if room[pos.y][pos.x]:
        pos = minus(pos, dir)
        dir = turn_right(dir)
    else:
        if steps[pos.y][pos.x] == turn_right(dir):
            # Found a circle point, if the next point in the path is inside the room
            nextpos = step(pos, dir)
            if intheroom(nextpos):
                circles[nextpos.y][nextpos.x] = True
                # steps = [[False for _ in range(len(room[0]))] for _ in range(len(room))]
        steps[pos.y][pos.x] = dir
    printsteps(steps)
    print()
    pos = step(pos, dir)
print(sum([sum(row) for row in circles]))
printcircles(circles)
print()

