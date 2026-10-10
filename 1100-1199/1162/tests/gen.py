"""Exchange points: a seed, N, M and a mode. Rates and commissions have
two decimals. Mode 0 draws rates from 0.01 to 100, mode 1 keeps rates
near 1 with small commissions so that gains are rare and slim, mode 2
makes every exchange lose, mode 3 hides one gaining loop far from S."""

import random
import sys

LOW, HIGH = 1, 10000
FEE = 10000


def money(rng, lo, hi):
    return rng.randint(lo, hi) / 100


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    s = rng.randint(1, n)
    v = money(rng, 0, 100000)
    lines = []
    for k in range(m):
        if mode == 3 and k + 1 < n:
            a, b = k + 1, k + 2
        else:
            a, b = rng.sample(range(1, n + 1), 2) if n > 1 else (1, 1)
        if mode == 1:
            rates = [money(rng, 95, 105), money(rng, 0, 50), money(rng, 95, 105), money(rng, 0, 50)]
        elif mode == 2:
            rates = [
                money(rng, LOW, 100),
                money(rng, 1, FEE),
                money(rng, LOW, 100),
                money(rng, 1, FEE),
            ]
        elif mode == 3:
            gain = k == m - 1
            rates = [
                money(rng, 100 if gain else 90, 101 if gain else 100),
                0.0,
                money(rng, 99, 100),
                0.0,
            ]
        else:
            rates = [
                money(rng, LOW, HIGH),
                money(rng, 0, FEE),
                money(rng, LOW, HIGH),
                money(rng, 0, FEE),
            ]
        lines.append("%d %d %s" % (a, b, " ".join("%.2f" % x for x in rates)))
    sys.stdout.write("%d %d %d %.2f\n%s\n" % (n, m, s, v, "\n".join(lines)))


if __name__ == "__main__":
    main()
