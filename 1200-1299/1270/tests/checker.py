"""Checker: an answer of 0 is right only when the reference finds no
assignment. Otherwise there must be M distinct cube numbers from 1 to N,
and each cube must meet the colour demands of its cell in one of the 24
rotations, taken here as the face permutations that keep opposite faces
opposite and have determinant +1."""

import sys
from itertools import permutations

FACES = 6
COORDS = 3
# faces front, up, right, down, left, back as unit vectors
AXES = [(0, 1, 0), (0, 0, 1), (1, 0, 0), (0, 0, -1), (-1, 0, 0), (0, -1, 0)]


def fail(reason):
    print(reason)
    sys.exit(1)


def det(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def rotations():
    out = []
    for p in permutations(range(FACES)):
        # the rotation sends face p[f] to face f; it is linear on the axes
        image = {AXES[p[f]]: AXES[f] for f in range(FACES)}
        if any(image[tuple(-x for x in a)] != tuple(-x for x in image[a]) for a in AXES):
            continue
        cols = [image[(1, 0, 0)], image[(0, 1, 0)], image[(0, 0, 1)]]
        if det([[cols[j][i] for j in range(COORDS)] for i in range(COORDS)]) == 1:
            out.append(p)
    return out


def main():
    inp, ans, output = sys.argv[1:4]
    nums = iter(int(t) for t in open(inp).read().split())
    n = next(nums)
    cubes = [[next(nums) for _ in range(FACES)] for _ in range(n)]
    m = next(nums)
    cells = [[next(nums) for _ in range(COORDS + FACES)][COORDS:] for _ in range(m)]
    reference = open(ans).read().split()
    try:
        got = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if got == [0]:
        if reference != ["0"]:
            fail("an assignment exists, but 0 is printed")
        return
    if len(got) != m:
        fail("expected %d cube numbers" % m)
    if any(not 1 <= c <= n for c in got) or len(set(got)) != m:
        fail("cube numbers out of range or repeated")
    turns = rotations()
    for j, (c, need) in enumerate(zip(got, cells), 1):
        cube = cubes[c - 1]
        if not any(all(x == 0 or x == cube[p[f]] for f, x in enumerate(need)) for p in turns):
            fail("cube %d does not fit cell %d" % (c, j))


if __name__ == "__main__":
    main()
