"""Rules and a plan: a seed and a mode. The rules follow a hidden order;
mode 1 gives the plan in that order (YES), mode 2 swaps two subjects of
the plan (usually NO), mode 3 uses N = 1000 and M = 100000 with the plan
right, mode 4 the same with one rule turned backwards at the end."""

import random
import sys

SUBJECTS = 1000
RULES = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    big = mode >= 3
    n = SUBJECTS if big else rng.randint(2, 50)
    m = RULES if big else rng.randint(0, 3 * n)
    order = list(range(1, n + 1))
    rng.shuffle(order)
    rules = []
    for _ in range(m):
        i, j = sorted(rng.sample(range(n), 2))
        rules.append((order[i], order[j]))
    plan = order[:]
    if mode == 2:
        i, j = rng.sample(range(n), 2)
        plan[i], plan[j] = plan[j], plan[i]
    if mode == 4:
        a, b = rules[-1]
        rules[-1] = (b, a)
    lines = ["%d %d" % (n, m)] + ["%d %d" % r for r in rules] + [" ".join(map(str, plan))]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
