"""Two numbers written in columns: a seed, N and the mode. random: random
digits; carry: 0999...9 plus 0...01, one carry through all digits; zeros:
mostly zeros with a few ones. The first column always sums to at most 8,
so the sum has at most N digits, and each number is at least 1."""

import random
import sys


def main():
    seed, n, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    if mode == "carry":
        a = [0] + [9] * (n - 1)
        b = [0] * (n - 1) + [1]
    elif mode == "zeros":
        a = [0] * n
        b = [0] * n
        for _ in range(3):
            a[rng.randrange(1, n)] = 1
            b[rng.randrange(1, n)] = 1
    else:
        a = [rng.randrange(10) for _ in range(n)]
        b = [rng.randrange(10) for _ in range(n)]
        a[0] = rng.randrange(5)
        b[0] = rng.randrange(4)
        a[n - 1] = max(a[n - 1], 1)
        b[n - 1] = max(b[n - 1], 1)
    out = [str(n)] + ["%d %d" % p for p in zip(a, b)]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
