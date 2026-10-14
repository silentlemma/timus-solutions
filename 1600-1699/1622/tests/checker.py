"""Checker: Impossible exactly when expected; otherwise 31 legal jumps from
the full board with an empty centre that leave one peg on the target."""

import sys

SIDE = 7
ARM = 2
LETTERS = "ABCDEFG"
JUMPS = 31  # 32 pegs down to one


def fail(reason):
    print(reason)
    sys.exit(1)


def on_board(r, c):
    return 0 <= r < SIDE and 0 <= c < SIDE and (ARM <= r < SIDE - ARM or ARM <= c < SIDE - ARM)


def cell(s):
    if len(s) != 2 or s[0] not in LETTERS or not s[1].isdigit():
        fail("bad cell " + s)
    return int(s[1]) - 1, LETTERS.index(s[0])


def main():
    source, expected, output = sys.argv[1:4]
    target = cell(open(source).read().split()[0])
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["Impossible"]:
        if got != ["Impossible"]:
            fail("expected Impossible")
        return
    if len(got) != JUMPS:
        fail("expected %d jumps, got %d" % (JUMPS, len(got)))
    centre = SIDE // 2
    pegs = {(r, c) for r in range(SIDE) for c in range(SIDE) if on_board(r, c)}
    pegs.discard((centre, centre))
    for move in got:
        parts = move.split("-")
        if len(parts) != 2:
            fail("bad jump " + move)
        (r1, c1), (r2, c2) = cell(parts[0]), cell(parts[1])
        if sorted((abs(r1 - r2), abs(c1 - c2))) != [0, 2]:
            fail("not a jump: " + move)
        over = ((r1 + r2) // 2, (c1 + c2) // 2)
        if (r1, c1) not in pegs or over not in pegs or (r2, c2) in pegs or not on_board(r2, c2):
            fail("illegal jump " + move)
        pegs -= {(r1, c1), over}
        pegs.add((r2, c2))
    if pegs != {target}:
        fail("the last peg is not on the target")


main()
