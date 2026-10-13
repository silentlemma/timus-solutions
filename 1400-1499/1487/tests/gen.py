"""One test from a seed and a mode. The results always follow a hidden
order of strength. Mode 1 is 1000 teams with a random share of matches
played, mode 2 has every match played, mode 3 only a few, mode 4 is a
small championship. Mode 5 has no matches at maximum N and Q; mode 6
has just two wins by team 1000; mode 7 has four disjoint dense three-level
groups; mode 8 is a random transitive three-level championship.
Each test asks 50000 questions, or fewer if small."""

import random
import sys

LARGEST = 1000
SMALL = 10
QUESTIONS = 50000
FEW = 0.002


def structured(seed, mode):
    rng = random.Random(seed)
    n = LARGEST
    rows = [set() for _ in range(n)]
    if mode == 6:
        rows[-1].update((n - 3, n - 2))
    elif mode == 7:
        order = list(range(n))
        rng.shuffle(order)
        for start in range(0, n, 250):
            root = order[start]
            middle = order[start + 1 : start + 75]
            bottom = order[start + 75 : start + 250]
            rows[root].update(middle + bottom)
            for team in middle:
                rows[team].update(bottom)
    elif mode == 8:
        order = list(range(n))
        rng.shuffle(order)
        roots, middle, bottom = order[:25], order[25:225], order[225:]
        for team in middle:
            rows[team].update(other for other in bottom if rng.random() < 0.02)
        for team in roots:
            direct = [other for other in middle if rng.random() < 0.12]
            rows[team].update(direct)
            for other in direct:
                rows[team].update(rows[other])
            rows[team].update(other for other in bottom if rng.random() < 0.002)
    elif mode != 5:
        raise ValueError("unknown mode")
    print(n)
    for row in rows:
        print("".join("1" if j in row else "0" for j in range(n)))
    print(QUESTIONS)
    # Include both directions of pairs near the last matrix row and column.
    border = [1, n - 2, n - 1, n]
    pairs = [(a, b) for a in border for b in border if a != b]
    for _ in range(QUESTIONS - len(pairs)):
        a = rng.randint(1, n)
        b = rng.randint(1, n - 1)
        pairs.append((a, b if b < a else b + 1))
    for a, b in pairs:
        print(a, b)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    if mode >= 5:
        structured(seed, mode)
        return
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
