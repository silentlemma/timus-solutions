"""Random negotiation pairs covering everyone: a seed, M, N, K and a mode.
Mode 0 draws random pairs, mode 1 builds staircases, where member i of A
talks to members i and i + 1 of B and a greedy matching goes wrong, mode 2
draws pairs only inside a few dense blocks, mode 3 sends most members of
A to a few hubs of B so that the matching stays small."""

import random
import sys

BLOCKS = 5
HUBS = 10


def main():
    seed, m, n, k, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    pairs = []
    # everyone needs a pair first
    for a in range(1, m + 1):
        pairs.append((a, rng.randint(1, n)))
    for b in range(1, n + 1):
        pairs.append((rng.randint(1, m), b))
    while len(pairs) < k:
        if mode == 1:
            a = rng.randint(1, m)
            b = min(n, a * n // m + rng.randint(0, 1))
            pairs.append((a, max(1, b)))
        elif mode == 2:
            parts = min(BLOCKS, m, n)
            block = rng.randrange(parts)
            a = rng.randint(block * m // parts, (block + 1) * m // parts - 1) + 1
            b = rng.randint(block * n // parts, (block + 1) * n // parts - 1) + 1
            pairs.append((a, b))
        elif mode == 3:
            pairs.append((rng.randint(1, m), rng.randint(1, min(n, HUBS))))
        else:
            pairs.append((rng.randint(1, m), rng.randint(1, n)))
    rng.shuffle(pairs)
    lines = ["%d %d %d" % (m, n, len(pairs))] + ["%d %d" % p for p in pairs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
