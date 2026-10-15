import sys
from math import comb

EDGES = 30
COLOURS = 30
ROTATIONS = 60
# the rotations other than the identity, as (how many, cycle length on the
# edges); a half-turn about an axis through two edge midpoints also keeps
# those two edges in place
FACE_TURNS = (24, 5)
VERTEX_TURNS = (20, 3)
HALF_TURNS = (15, 2)
KEPT = 2


def cycles(counts, length):
    """Colourings of the cycles of the given length that use each colour
    the given number of times, or 0 if a count does not split."""
    if any(c % length for c in counts):
        return 0
    ways, used = 1, 0
    for c in counts:
        ways *= comb(used + c // length, c // length)
        used += c // length
    return ways


def main():
    counts = [0] * (COLOURS + 1)
    for w in sys.stdin.read().split()[:EDGES]:
        counts[int(w)] += 1
    total = cycles(counts, 1)
    for times, length in (FACE_TURNS, VERTEX_TURNS):
        total += times * cycles(counts, length)
    # a half-turn: colour the two kept edges first, in order
    times, length = HALF_TURNS
    kept = 0
    for a in range(COLOURS + 1):
        for b in range(COLOURS + 1):
            rest = counts[:]
            rest[a] -= 1
            rest[b] -= 1
            if min(rest) >= 0:
                kept += cycles(rest, length)
    total += times * kept
    print(total // ROTATIONS)


main()
