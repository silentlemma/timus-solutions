"""Modes:
SEED: two times and small counts, with clean time often near the winner's.
large SEED: distribute 70 or more rejections randomly among all ten problems.
"""

import random
import sys

PROBLEMS = 10
PER_ATTEMPT = 20
LOW, HIGH = 250, 2400


def main():
    if sys.argv[1] == "large":
        rng = random.Random(int(sys.argv[2]))
        t2 = rng.randint(2300, HIGH)
        total = rng.randint(70, (t2 - LOW) // PER_ATTEMPT)
        attempts = [0] * PROBLEMS
        for _ in range(total):
            attempts[rng.randrange(PROBLEMS)] += 1
        clean = t2 - PER_ATTEMPT * total
        t1 = rng.randint(max(LOW, clean - 200), min(t2, clean + 200))
        print(t1, t2)
        print(*attempts)
        return

    rng = random.Random(int(sys.argv[1]))
    t1 = rng.randint(LOW, HIGH)
    attempts = [rng.choice([0, 0, 0, 1, 2, 3]) for _ in range(PROBLEMS)]
    penalty = PER_ATTEMPT * sum(attempts)
    t2 = min(HIGH, max(t1, t1 + penalty + rng.choice([-1, 0, 1, rng.randint(-200, 200)])))
    print(t1, t2)
    print(*attempts)


main()
