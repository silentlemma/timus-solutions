"""One test from a seed: two penalty times and ten attempt counts, with
the clean time of ZZZ often landing right next to that of QXX."""

import random
import sys

PROBLEMS = 10
PER_ATTEMPT = 20
LOW, HIGH = 250, 2400


def main():
    rng = random.Random(int(sys.argv[1]))
    t1 = rng.randint(LOW, HIGH)
    attempts = [rng.choice([0, 0, 0, 1, 2, 3]) for _ in range(PROBLEMS)]
    penalty = PER_ATTEMPT * sum(attempts)
    t2 = min(HIGH, max(t1, t1 + penalty + rng.choice([-1, 0, 1, rng.randint(-200, 200)])))
    print(t1, t2)
    print(*attempts)


main()
