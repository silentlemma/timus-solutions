"""One test from a seed and a mode. The results always follow a hidden
order of strength. Mode 1 is 1000 teams with a random share of matches
played, mode 2 has every match played, mode 3 only a few, mode 4 is a
small championship. Each test asks 50000 questions, or fewer if small."""

import random
import sys

LARGEST = 1000
SMALL = 10
QUESTIONS = 50000
FEW = 0.002


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 4 else LARGEST
    played = {1: rng.random(), 2: 1.0, 3: FEW, 4: rng.random()}[mode]
    order = list(range(n))
    rng.shuffle(order)
    rank = [0] * n
    for place, team in enumerate(order):
        rank[team] = place
    rows = []
    for i in range(n):
        row = ["0"] * n
        for j in range(n):
            if rank[i] < rank[j] and rng.random() < played:
                row[j] = "1"
        rows.append("".join(row))
    q = QUESTIONS if n == LARGEST else 2 * n * n
    print(n)
    print("\n".join(rows))
    print(q)
    lines = []
    for _ in range(q):
        a = rng.randint(1, n)
        b = rng.randint(1, n - 1)
        lines.append("%d %d" % (a, b if b < a else b + 1))
    print("\n".join(lines))


main()
