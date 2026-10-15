"""Checker: "No" exactly when expected; otherwise "Yes" and a picture of
2N - 1 lines of 2M - 1 characters with knots o at even places and moves
between them, forming one closed tour through every cell in which no
cell is passed straight through (two moves in the same direction)."""

import sys

MOVES = {"-": (0, 1), "|": (1, 0), "\\": (1, 1), "/": (1, -1)}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    n, m = (int(w) for w in open(source).read().split())
    want = open(expected).read().split("\n")[0].strip()
    lines = open(output).read().rstrip("\n").split("\n")
    lines = [line.rstrip("\r") for line in lines]
    got = lines[0].strip()
    if got not in ("Yes", "No"):
        fail("the first line must be Yes or No")
    if got != want:
        fail("expected %s, got %s" % (want, got))
    if got == "No":
        if len(lines) > 1 and any(line.strip() for line in lines[1:]):
            fail("text after No")
        return
    pic = lines[1:]
    if len(pic) != 2 * n - 1:
        fail("expected %d picture lines, got %d" % (2 * n - 1, len(pic)))
    pic = [line.ljust(2 * m - 1) for line in pic]
    if any(len(line) != 2 * m - 1 for line in pic):
        fail("a picture line is too long")
    links = {(r, c): [] for r in range(n) for c in range(m)}
    for y in range(2 * n - 1):
        for x in range(2 * m - 1):
            ch = pic[y][x]
            if y % 2 == 0 and x % 2 == 0:
                if ch != "o":
                    fail("expected o at line %d, column %d" % (y + 2, x + 1))
                continue
            if ch == " ":
                continue
            if ch not in MOVES:
                fail("unexpected character %r" % ch)
            dr, dc = MOVES[ch]
            # the character between two knots: find which pair it joins
            if dr == 0:
                if y % 2 or x % 2 == 0:
                    fail("misplaced - at line %d" % (y + 2))
                a, b = (y // 2, x // 2), (y // 2, x // 2 + 1)
            elif dc == 0:
                if x % 2 or y % 2 == 0:
                    fail("misplaced | at line %d" % (y + 2))
                a, b = (y // 2, x // 2), (y // 2 + 1, x // 2)
            else:
                if x % 2 == 0 or y % 2 == 0:
                    fail("misplaced diagonal at line %d" % (y + 2))
                if dc == 1:
                    a, b = (y // 2, x // 2), (y // 2 + 1, x // 2 + 1)
                else:
                    a, b = (y // 2, x // 2 + 1), (y // 2 + 1, x // 2)
            links[a].append(b)
            links[b].append(a)
    for cell, nb in links.items():
        if len(nb) != 2:
            fail("cell %s has %d moves" % (cell, len(nb)))
        (r1, c1), (r2, c2) = nb
        if r1 + r2 == 2 * cell[0] and c1 + c2 == 2 * cell[1]:
            fail("cell %s is passed straight through" % (cell,))
    seen = {(0, 0)}
    prev, cur = (0, 0), links[(0, 0)][0]
    while cur != (0, 0):
        seen.add(cur)
        a, b = links[cur]
        prev, cur = cur, (b if a == prev else a)
    if len(seen) != n * m:
        fail("the tour does not pass every cell")


main()
