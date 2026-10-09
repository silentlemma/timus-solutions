"""Two numbers written in columns: a seed, N and the mode. random: random
digits; carry: 0999...9 plus 0...01, one carry through all digits; zeros:
mostly zeros with a few ones; blocks: random carry chains separated by
columns that stop them, with dormant runs of nines between chains.
The first column always sums to at most 8,
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
    elif mode == "blocks":
        a, b = [0], [0]
        while len(a) < n:
            sums = (
                [rng.randrange(9)]
                + [9] * rng.randrange(258)
                + [rng.randrange(10, 19)]
                + [9] * rng.randrange(258)
            )
            for total in sums[: n - len(a)]:
                digit = rng.randrange(max(0, total - 9), min(9, total) + 1)
                a.append(digit)
                b.append(total - digit)
        a[-1] = max(a[-1], 1)
        b[-1] = max(b[-1], 1)
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
