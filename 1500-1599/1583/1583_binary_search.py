import math
import sys

AREA = 100  # the cross-section of the bar, 10 by 10 cm
LENGTH = 100
PIECE = 500  # grams, at one gram per cubic centimetre
MICRONS = 10000  # in a centimetre
STEPS = 100
CAP = 3  # a cap of height h has volume pi h^2 (3 r - h) / 3
HALF = 0.5


def main():
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    holes = []
    for _ in range(n):
        next(words)  # x
        y = float(next(words))
        next(words)  # z
        holes.append((y, float(next(words))))

    def cheese(at):
        """The weight of the bar from its start to the mark at (in cm): the
        full volume minus the part of every hole below the mark, a spherical
        cap of height h with volume pi h^2 (3 r - h) / 3."""
        weight = AREA * at
        for centre, r in holes:
            h = min(max(at - (centre - r), 0.0), 2 * r)
            weight -= math.pi * h * h * (CAP * r - h) / CAP
        return weight

    cuts, start = [], 0
    while cheese(LENGTH) - cheese(start / MICRONS) >= PIECE:
        # the mark where the next piece reaches 500 grams, then rounded to the
        # micrometre grid; the next piece starts at the cut actually made
        base = cheese(start / MICRONS)
        lo, hi = start / MICRONS, float(LENGTH)
        for _ in range(STEPS):
            mid = (lo + hi) / 2
            if cheese(mid) - base < PIECE:
                lo = mid
            else:
                hi = mid
        start = math.floor(hi * MICRONS + HALF)
        if start >= LENGTH * MICRONS:
            break
        cuts.append(start)
    print(len(cuts))
    for c in cuts:
        print(c)


main()
