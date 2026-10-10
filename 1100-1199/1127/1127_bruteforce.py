import sys
from collections import Counter

# face positions in the input: front, right, left, back, top, bottom
FACES = 6
FRONT, RIGHT, LEFT, BACK, TOP, BOTTOM = range(FACES)
# a quarter turn about the vertical axis (front goes right) and one about
# the left-right axis (top goes front), as "new position <- old position"
SPIN = {RIGHT: FRONT, BACK: RIGHT, LEFT: BACK, FRONT: LEFT, TOP: TOP, BOTTOM: BOTTOM}
TIP = {FRONT: TOP, BOTTOM: FRONT, BACK: BOTTOM, TOP: BACK, LEFT: LEFT, RIGHT: RIGHT}


def orientations():
    """All 24 rotations as tuples: position -> original face."""
    start = tuple(range(FACES))
    seen, stack = {start}, [start]
    while stack:
        cur = stack.pop()
        for turn in (SPIN, TIP):
            nxt = tuple(cur[turn[p]] for p in range(FACES))
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def main():
    tok = sys.stdin.read().split()
    cubes = tok[1 : 1 + int(tok[0])]
    rotations = orientations()
    # each cube can show a given ring of side colours at most once, since its
    # faces all differ; the tallest tower is the most common ring
    rings = Counter()
    for cube in cubes:
        for rot in rotations:
            rings[tuple(cube[rot[p]] for p in (FRONT, RIGHT, BACK, LEFT))] += 1
    print(max(rings.values()))


main()
