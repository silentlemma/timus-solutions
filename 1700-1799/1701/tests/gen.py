"""One test from a seed and a mode: mode 1 a few employees, consistent
statements with an error at a random place, mode 2 the largest sizes,
all consistent, mode 3 a chain apart from Vasily and a last statement that
puts its lowest member below 0, mode 4 a long chain
built in random order, mode 5 statements about one employee and
contradictions inside a set."""

import random
import sys

MOST_N = 50000
MOST_D = 20000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        # a chain away from Vasily, then a link that puts its lowest member at -1
        n = MOST_N
        value = [0] * n
        lines = []
        for k in range(2, n):
            step = rng.randint(-3, 3)
            value[k] = value[k - 1] + step
            lines.append((k, k - 1, step))
        rng.shuffle(lines)
        low = min(range(1, n), key=lambda k: value[k])
        top = rng.randrange(1, n)
        gap = value[top] - value[low]
        lines.append((top, 0, gap - 1))
        print(n, len(lines))
        for line in lines:
            print(*line)
        return
    n, m = (rng.randint(1, 8), rng.randint(1, 12)) if mode == 1 else (MOST_N, MOST_N)
    # hidden salaries that the statements follow
    salary = [0] * n
    for i in range(1, n):
        if mode == 4:
            salary[i] = max(0, salary[i - 1] + rng.randint(-MOST_D, MOST_D))
        else:
            salary[i] = rng.randint(0, MOST_D)
    lines = []
    for _ in range(m):
        if mode == 4 and n > 1:
            i = rng.randrange(1, n)
            j = i - 1
        else:
            i, j = rng.randrange(n), rng.randrange(n)
        d = salary[i] - salary[j]
        if mode == 5 and rng.random() < 0.3:
            j, d = i, 0
        lines.append((i, j, d))
    if mode in (1, 5) and rng.random() < 0.7:
        k = rng.randrange(m)
        i, j, d = lines[k]
        lines[k] = (i, j, d + 1 if d < MOST_D else d - 1)
    print(n, m)
    for line in lines:
        print(*line)


main()
