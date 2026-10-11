"""A village: a seed, N, a mode and a number of victims. People are put in
a random order and each gets up to two parents among those before it, so
there are no cycles. Mode 1 gives parents at random; mode 2 makes one long
line of descent; mode 3 gives nobody parents."""

import random
import sys


def main():
    seed, n, mode, victims = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    order = list(range(1, n + 1))
    rng.shuffle(order)
    links = []
    for k in range(1, n):
        child = order[k]
        if mode == 1:
            for parent in rng.sample(order[:k], min(k, rng.randint(0, 2))):
                links.append((child, parent))
        elif mode == 2:
            links.append((child, order[k - 1]))
    rng.shuffle(links)
    lines = [str(n)] + ["%d %d" % link for link in links] + ["BLOOD"]
    lines += [str(v) for v in rng.sample(range(1, n + 1), victims)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
