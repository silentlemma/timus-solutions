"""Two lists of years. Modes:

SEED N M TOP: sorted random teacher years with repeats; student years mix
teacher years and independent random years, all between 1 and TOP.
last N: N distinct teacher years ending at 10^9, and one query for 10^9.
all-hit N M: teacher years 1 through N, and M queries in descending cycles.
"""

import random
import sys


def main():
    mode = sys.argv[1]
    if mode in ("last", "all-hit"):
        n = int(sys.argv[2])
        m = 1 if mode == "last" else int(sys.argv[3])
        if not (1 <= n <= 15000 and 1 <= m <= 1000000):
            raise ValueError("list sizes outside the task limits")
        top = 10**9
        known = range(top - n + 1, top + 1) if mode == "last" else range(1, n + 1)
        student = [top] if mode == "last" else (n - i % n for i in range(m))
        lines = [str(n)] + [str(y) for y in known] + [str(m)]
        lines.extend(str(y) for y in student)
        sys.stdout.write("\n".join(lines) + "\n")
        return

    seed, n, m, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    known = sorted(rng.randint(1, top) for _ in range(n))
    student = [rng.choice(known) if rng.random() < 0.5 else rng.randint(1, top) for _ in range(m)]
    lines = [str(n)] + [str(y) for y in known] + [str(m)] + [str(y) for y in student]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
