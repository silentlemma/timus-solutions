import sys
from itertools import product

PARTS = 8  # passes over the cells, each with an eighth of them


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, s = data[0], data[1]
    start = [c - 1 for c in data[2 : 2 + n]]
    weights = [s**i for i in range(n)]  # a cell is the number with digits x_i in base S
    # rook directions along each axis, bishop directions along all axes at once
    dirs = []
    for i in range(n):
        for sign in (1, -1):
            v = [0] * n
            v[i] = sign
            dirs.append(v)
    dirs += [list(v) for v in product((1, -1), repeat=n)]
    dirs = [list(v) for v in {tuple(v) for v in dirs}]  # in one dimension they coincide

    def room(cell, v):
        # how many steps fit on the board from cell in direction v
        return min(s - 1 - c if d > 0 else c for c, d in zip(cell, v) if d)

    first = set()
    for v in dirs:
        for k in range(1, room(start, v) + 1):
            first.add(tuple(c + k * d for c, d in zip(start, v)))
    # the rays as (first cell, step, length, step of the first coordinate)
    rays = []
    for cell in first:
        here = sum(c * w for c, w in zip(cell, weights))
        for v in dirs:
            step = sum(d * w for d, w in zip(v, weights))
            rays.append((here + step, step, room(cell, v), cell[0] + v[0], v[0]))
    # one set of all cells takes too much memory, so count them in PARTS
    # passes, each keeping the cells whose first coordinate is r mod PARTS:
    # along a ray those are every PARTS-th cell, again a range
    total = 0
    for r in range(PARTS):
        reach = set()
        for begin, step, length, c0, d0 in rays:
            if d0 == 0:
                if c0 % PARTS == r:
                    reach.update(range(begin, begin + step * length, step))
            else:
                k = (r - c0) * d0 % PARTS  # steps from begin to the first such cell
                reach.update(range(begin + step * k, begin + step * length, step * PARTS))
        total += len(reach)
    print(total)


main()
