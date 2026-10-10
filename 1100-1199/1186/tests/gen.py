"""A chemistry test: a seed, the number of right sides and the depth of
brackets. The left side is a random formula; each right side is either
the same totals written element by element in random order (so it is
equal), a random formula, or the expanded form with one count changed.
Formulas stay within 100 characters and every total within 10000."""

import random
import sys
from collections import Counter

ELEMENTS = ["H", "He", "C", "O", "N", "Si", "Ge", "Na", "Cl", "U"]
LONGEST = 100
MOST = 10000


def multiplier(rng):
    r = rng.random()
    if r < 0.6:
        return 1
    return rng.choice([2, 3, 5, 10, 12, 20, 99, 100])


def sequence(rng, depth):
    # a random sequence and how often each element occurs in it
    out, acc = "", Counter()
    for _ in range(rng.randint(1, 3)):
        if depth and rng.random() < 0.3:
            body, counts = sequence(rng, depth - 1)
            body = "(" + body + ")"
        else:
            name = rng.choice(ELEMENTS)
            body, counts = name, Counter({name: 1})
        k = multiplier(rng)
        out += body + (str(k) if k > 1 else "")
        acc += Counter({e: c * k for e, c in counts.items()})
    return out, acc


def formula(rng, depth):
    terms, total = [], Counter()
    for _ in range(rng.randint(1, 3)):
        body, counts = sequence(rng, depth)
        k = multiplier(rng)
        terms.append((str(k) if k > 1 else "") + body)
        total += Counter({e: c * k for e, c in counts.items()})
    return "+".join(terms), total


def expanded(rng, total):
    names = list(total)
    rng.shuffle(names)
    return "+".join((str(total[e]) if total[e] > 1 else "") + e for e in names)


def fits(text, total):
    return len(text) <= LONGEST and all(c <= MOST for c in total.values())


def main():
    seed, n, depth = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    while True:
        left, total = formula(rng, depth)
        if fits(left, total) and fits(expanded(rng, total), total):
            break
    lines = [left, str(n)]
    while len(lines) < n + 2:
        kind = rng.randrange(3)
        if kind == 0:
            right, counts = expanded(rng, total), total
        elif kind == 1:
            right, counts = formula(rng, depth)
        else:
            counts = Counter(total)
            counts[rng.choice(list(counts))] += rng.choice([-1, 1])
            counts = +counts
            if not counts:
                continue
            right = expanded(rng, counts)
        if fits(right, counts):
            lines.append(right)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
