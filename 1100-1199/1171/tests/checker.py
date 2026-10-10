"""Checker: the ratio must equal the stored best, and the moves must form a
trip that never leaves a level's grid, never enters a room twice, goes
down only through doors, ends on level 1 and gives that ratio."""

import sys

SIDE = 4
ROOMS = SIDE * SIDE
STEP = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
# the ratio is printed with four decimals
TOL = 1.5e-4


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = iter(map(int, open(inp).read().split()))
    n = next(data)
    foods, doors = [], []
    for _ in range(n):
        foods.append([next(data) for _ in range(ROOMS)])
        doors.append([next(data) for _ in range(ROOMS)])
    r, c = next(data) - 1, next(data) - 1
    best = float(open(ans).read().split()[0])
    got = open(output).read().split()
    try:
        ratio, length = float(got[0]), int(got[1])
    except (IndexError, ValueError):
        fail("expected the ratio and the length")
    moves = got[2] if length > 0 and len(got) > 2 else ""
    if len(got) != (3 if length > 0 else 2) or len(moves) != length:
        fail("the moves do not match the length")
    if abs(ratio - best) > TOL:
        fail("ratio %.4f instead of %.4f" % (ratio, best))
    level = 0
    seen = {(level, r, c)}
    total = foods[level][r * SIDE + c]
    for m in moves:
        if m == "D":
            if not doors[level][r * SIDE + c]:
                fail("no door down here")
            level += 1
        elif m in STEP:
            r, c = r + STEP[m][0], c + STEP[m][1]
            if not (0 <= r < SIDE and 0 <= c < SIDE):
                fail("left the grid")
        else:
            fail("bad move %r" % m)
        if level >= n or (level, r, c) in seen:
            fail("a room entered twice or no level below")
        seen.add((level, r, c))
        total += foods[level][r * SIDE + c]
    if level != n - 1:
        fail("the trip does not end on level 1")
    if abs(total / (length + 1) - ratio) > TOL:
        fail("the moves give ratio %.4f" % (total / (length + 1)))


if __name__ == "__main__":
    main()
