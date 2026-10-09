"""A consistent random sequence: a seed, N, the largest step between
neighbours (in hundredths) and the limit of |a_i| (in hundredths). The
values a_i have two decimals and a_{i+1} + a_{i-1} is chosen even (in
hundredths), so every c_i has two decimals too."""

import random
import sys


def fmt(h):
    sign = "-" if h < 0 else ""
    return "%s%d.%02d" % (sign, abs(h) // 100, abs(h) % 100)


def main():
    seed, n, step, limit = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    a = [rng.randint(-limit, limit), rng.randint(-limit, limit)]
    while len(a) < n + 2:
        lo, hi = max(-limit, a[-1] - step), min(limit, a[-1] + step)
        v = rng.randint(lo, hi)
        if (v + a[-2]) % 2:
            v += 1 if v < hi else -1
        a.append(v)
    c = [(a[i + 1] + a[i - 1]) // 2 - a[i] for i in range(1, n + 1)]
    lines = [str(n), fmt(a[0]), fmt(a[n + 1])] + [fmt(x) for x in c]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
