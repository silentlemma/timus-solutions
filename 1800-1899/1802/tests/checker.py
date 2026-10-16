"""Checker: "No" exactly when the expected answer is "No"; otherwise
"Yes" and n layers of n x n part numbers from 1 to 6, where the cells of
each part are exactly that part put on a face of the cube, lacquer
outside, in one of four turns, and no two parts share a face."""

import sys

FACES = 6
TURNS = 4


class Bad(Exception):
    pass


def face_cell(n, face, r, c):
    last = n - 1
    starts = [((0, r, c), (1, 0, 0)), ((last, last - r, c), (-1, 0, 0)),
              ((r, last, c), (0, -1, 0)), ((r, 0, last - c), (0, 1, 0)),
              ((r, c, 0), (0, 0, 1)), ((r, last - c, last), (0, 0, -1))]
    return starts[face]


def cells_of(n, heights, face, k):
    out = set()
    for r in range(n):
        for c in range(n):
            rr, cc = r, c
            for _ in range(k):
                rr, cc = cc, n - 1 - rr
            (y, z, x), (dy, dz, dx) = face_cell(n, face, rr, cc)
            for step in range(heights[r][c]):
                out.add((y + step * dy, z + step * dz, x + step * dx))
    return out


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n = data[0]
    size = n * n
    parts = [[data[1 + p * size + r * n:1 + p * size + (r + 1) * n] for r in range(n)]
             for p in range(FACES)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[:1] == ["No"]:
        if got != ["No"]:
            raise Bad("no cube can be built, expected No")
        return
    if not got or got[0] != "Yes":
        raise Bad("a cube can be built, expected Yes")
    labels = got[1:]
    if len(labels) != n * size or not all(w.isdigit() and 1 <= int(w) <= FACES for w in labels):
        raise Bad("expected %d part numbers from 1 to %d" % (n * size, FACES))
    owned = [set() for _ in range(FACES)]
    for i, w in enumerate(labels):
        owned[int(w) - 1].add((i // size, i // n % n, i % n))
    options = [sorted({f for f in range(FACES) for k in range(TURNS)
                       if cells_of(n, parts[p], f, k) == owned[p]}) for p in range(FACES)]
    for p in range(FACES):
        if not options[p]:
            raise Bad("the cells of part %d are not that part on a face" % (p + 1))
    # each part needs a face of its own: try to give the faces out

    def assign(p, taken):
        if p == FACES:
            return True
        return any(assign(p + 1, taken | {f}) for f in options[p] if f not in taken)

    if not assign(0, frozenset()):
        raise Bad("two parts would need the same face")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
