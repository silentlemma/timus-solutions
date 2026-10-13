"""2000 flies: a seed and a mode. Mode 1 is random points in the whole
cube, mode 2 puts 1500 flies on one line through two far corners among
random others, mode 3 fills a small 13 by 13 by 13 cube where many lines
meet, mode 4 stacks 1000 flies at one point among random others."""

import random
import sys

N = 2000
LIMIT = 10**7


def rand_point(rng):
    return tuple(rng.randint(-LIMIT, LIMIT) for _ in range(3))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        points = [rand_point(rng) for _ in range(N)]
    elif mode == 2:
        # steps of (13332, -13332, 6666) from one corner stay inside the cube
        start, step = (-LIMIT, LIMIT, -LIMIT), (13332, -13332, 6666)
        line = [tuple(s + k * d for s, d in zip(start, step)) for k in range(1500)]
        points = line + [rand_point(rng) for _ in range(N - len(line))]
    elif mode == 3:
        cells = [(x, y, z) for x in range(13) for y in range(13) for z in range(13)]
        points = rng.sample(cells, N)
    else:
        points = [(7, -7, 7)] * (N // 2) + [rand_point(rng) for _ in range(N // 2)]
    rng.shuffle(points)
    print(N)
    print("\n".join("%d %d %d" % p for p in points))


main()
