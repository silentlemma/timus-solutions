"""One test from a seed and a mode:
1: small n; 2: maximum t with random n up to 10^18;
3: n near squares and products s(s + 1); 4: shuffled final 30000 n;
5: neighbors of x(x + 1) = s - e; 6: neighbors of x^2 = 2s - e + 1;
7: maximum t alternating tiny n and large n inside square intervals.
"""

from math import isqrt
import random
import sys

MOST_T = 30000
MOST_N = 10 ** 18
ROOT = 10 ** 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, 10 ** 6) for _ in range(rng.randint(1, 100))]
    elif mode == 2:
        values = [rng.randint(1, MOST_N) for _ in range(MOST_T)]
    elif mode == 3:
        values = []
        while len(values) < MOST_T:
            s = rng.randint(2, ROOT - 1)
            values.append(s * s + rng.choice((-1, 0, 1, s - 1, s, s + 1, 2 * s)))
    elif mode == 4:
        values = list(range(MOST_N - MOST_T + 1, MOST_N + 1))
        rng.shuffle(values)
    elif mode in (5, 6):
        values = []
        for _ in range(MOST_T // 3):
            s = rng.randint(100, ROOT - 1)
            x = rng.randint(2, isqrt(s) - 1)
            e = s - x * (x + 1) if mode == 5 else 2 * s + 1 - x * x
            values.extend(s * s + e + delta for delta in (-1, 0, 1))
        rng.shuffle(values)
    elif mode == 7:
        values = []
        for _ in range(MOST_T // 2):
            s = rng.randint(ROOT // 2, ROOT - 1)
            values.extend((rng.randint(1, 99), s * s + s // 2))
    else:
        raise ValueError("mode must be between 1 and 7")
    print(len(values))
    print("\n".join(map(str, values)))


main()
