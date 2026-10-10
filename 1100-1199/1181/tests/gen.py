"""A colored polygon: a seed, N and a mode. Neighbours always differ and
all three colors appear. Mode 0 colors at random, mode 1 uses one color
exactly once, mode 2 alternates two colors with a few of the third,
mode 3 repeats RGB."""

import random
import sys

COLORS = "RGB"
FEW = 0.05


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    while True:
        if mode == 3:
            cs = [COLORS[i % len(COLORS)] for i in range(n)]
            # when N - 1 is a multiple of 3 the last R would touch the first
            cs[-1] = next(x for x in COLORS if x not in (cs[-2], cs[0]))
        elif mode == 1 or mode == 2:
            a, b, c = rng.sample(COLORS, len(COLORS))
            cs = [a if i % 2 == 0 else b for i in range(n)]
            spots = [1] if mode == 1 else [i for i in range(n) if rng.random() < FEW]
            for i in spots:
                cs[i] = c
            # with N odd the two alternating colors meet at the ends
            if cs[-1] == cs[0]:
                cs[-1] = c
        else:
            cs = [rng.choice(COLORS)]
            for _ in range(n - 1):
                cs.append(rng.choice([x for x in COLORS if x != cs[-1]]))
        if set(cs) == set(COLORS) and all(cs[i] != cs[i - 1] for i in range(n)):
            break
    sys.stdout.write("%d\n%s\n" % (n, "".join(cs)))


if __name__ == "__main__":
    main()
