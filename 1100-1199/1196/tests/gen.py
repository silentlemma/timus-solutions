"""Two lists of years: a seed, N, M and the largest year. The teacher's
list is sorted with repeats, the student's is a mix of the teacher's years
and others."""

import random
import sys


def main():
    seed, n, m, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    known = sorted(rng.randint(1, top) for _ in range(n))
    student = [rng.choice(known) if rng.random() < 0.5 else rng.randint(1, top) for _ in range(m)]
    lines = [str(n)] + [str(y) for y in known] + [str(m)] + [str(y) for y in student]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
