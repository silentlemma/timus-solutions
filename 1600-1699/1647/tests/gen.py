"""One triangle from a seed and mode: 1 small random coordinates,
2 random coordinates up to 2000, 3 long and thin, 4 nearly equilateral,
5 nearly right with a dot product of exactly plus or minus one.
"""

import random
import sys

LIMIT = 2000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    span = 10 if mode == 1 else LIMIT
    while True:
        if mode == 4:
            pts = [(x + rng.randint(-20, 20), y + rng.randint(-20, 20))
                   for x, y in [(-1000, -577), (1000, -577), (0, 1155)]]
            rng.shuffle(pts)
        elif mode == 5:
            leg = rng.randint(1000, 1900)
            offset = rng.choice([-1, 1])
            pts = [(0, 0), (leg, 1), (-1, leg + offset)]
            for _ in range(rng.randrange(4)):
                pts = [(-y, x) for x, y in pts]
            rng.shuffle(pts)
        elif mode == 3:
            pts = [(-LIMIT, rng.randint(-2, 2)), (LIMIT, rng.randint(-2, 2)),
                   (rng.randint(-LIMIT, LIMIT), rng.randint(-3, 3))]
        else:
            pts = [(rng.randint(-span, span), rng.randint(-span, span)) for _ in range(3)]
        (x1, y1), (x2, y2), (x3, y3) = pts
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            break
    print(*[v for p in pts for v in p])


main()
