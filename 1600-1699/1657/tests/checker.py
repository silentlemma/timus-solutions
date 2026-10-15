"""Checker: IMPOSSIBLE exactly when expected; otherwise 26 moves that keep
the direction after a straight cube, turn after a turning one, never
revisit a place and fill a 3 x 3 x 3 cube."""

import sys

SIDE = 3
MOVES = {"R": (1, 0, 0), "L": (-1, 0, 0), "F": (0, 1, 0), "B": (0, -1, 0), "U": (0, 0, 1), "D": (0, 0, -1)}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    snake = open(source).read().split()[0]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["IMPOSSIBLE"] or got == ["IMPOSSIBLE"]:
        if got != want:
            fail("expected %s" % ("IMPOSSIBLE" if want == ["IMPOSSIBLE"] else "a folding"))
        return
    if len(got) != 1 or len(got[0]) != len(snake) - 1 or any(c not in MOVES for c in got[0]):
        fail("expected 26 letters of RLFBUD")
    moves = [MOVES[c] for c in got[0]]
    at = (0, 0, 0)
    seen = {at}
    for k, step in enumerate(moves):
        if k:
            same = step == moves[k - 1]
            back = all(a == -b for a, b in zip(step, moves[k - 1]))
            if snake[k] == "F" and not same:
                fail("cube %d is straight but the snake turns" % (k + 1))
            if snake[k] == "T" and (same or back):
                fail("cube %d turns but the snake goes straight" % (k + 1))
        at = tuple(a + b for a, b in zip(at, step))
        if at in seen:
            fail("two cubes in one place")
        seen.add(at)
    for axis in range(SIDE):
        values = [p[axis] for p in seen]
        if max(values) - min(values) >= SIDE:
            fail("the snake does not fit in a 3 x 3 x 3 cube")


main()
