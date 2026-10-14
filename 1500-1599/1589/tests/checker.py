"""Checker: the plan, played on the level, only walks on free floor, pushes
one box at a time into free floor, ends with every box on a goal and has
at most 10000 moves. Any such plan is accepted."""

import sys

LONGEST = 10000
STEPS = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}


def main():
    path_in, _, output = sys.argv[1:4]
    rows = [line.rstrip("\r\n") for line in open(path_in).read().split("\n")]
    walls, goals, boxes = set(), set(), set()
    player = None
    for r, line in enumerate(rows):
        for c, ch in enumerate(line):
            if ch == "#":
                walls.add((r, c))
            if ch in ".+*":
                goals.add((r, c))
            if ch in "$*":
                boxes.add((r, c))
            if ch in "@+":
                player = (r, c)
    words = open(output).read().split()
    plan = words[0] if words else ""
    if len(words) > 1 or len(plan) > LONGEST:
        print("the plan is not one line of at most %d moves" % LONGEST)
        sys.exit(1)
    for i, move in enumerate(plan):
        if move.lower() not in STEPS:
            print("unknown move %r" % move)
            sys.exit(1)
        dr, dc = STEPS[move.lower()]
        to = (player[0] + dr, player[1] + dc)
        if to in walls:
            print("move %d walks into a wall" % (i + 1))
            sys.exit(1)
        if move.isupper():
            beyond = (to[0] + dr, to[1] + dc)
            if to not in boxes or beyond in walls or beyond in boxes:
                print("move %d is not a push of one box into free floor" % (i + 1))
                sys.exit(1)
            boxes.remove(to)
            boxes.add(beyond)
        elif to in boxes:
            print("move %d walks into a box" % (i + 1))
            sys.exit(1)
        player = to
    if boxes != goals:
        print("not every box is on a goal")
        sys.exit(1)


if __name__ == "__main__":
    main()
