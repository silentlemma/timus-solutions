"""Random buses: a seed, K, the largest route number and the shape (0 any
plates, 1 a long chain of exchanges hidden among other buses)."""

import random
import sys

ANY, CHAIN = 0, 1


def main():
    seed, k, top, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    buses = []
    if shape == CHAIN:
        # routes 1, 2, ... each plate showing the next route on its back
        length = k // 2
        start, target = 1, length + 1
        buses = [(i, i + 1) for i in range(1, length + 1)]
    while len(buses) < k:
        buses.append((rng.randint(1, top), rng.randint(1, top)))
    rng.shuffle(buses)
    if shape == CHAIN:
        t, s1, s2 = target, start, start
    else:
        t = rng.randint(1, top)
        s1, s2 = rng.randint(1, top), rng.randint(1, top)
        while t in (s1, s2):
            s1, s2 = rng.randint(1, top), rng.randint(1, top)
    lines = [str(k)] + ["%d %d" % b for b in buses] + ["%d %d %d" % (t, s1, s2)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
