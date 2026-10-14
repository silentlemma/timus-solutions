"""One test from a seed and a mode: up to 1000 queries. Mode 1 adds 400
sorts first and then mixes dense Learn and Eat queries, mode 2 learns the
days of every sort one by one, so that later meals are known, mode 3
mixes everything with few sorts, mode 4 makes Learn consistent with
hidden days until one wrong fact near the end. Mode 5 adds 999 sorts
and asks one maximal-width unknown meal. Mode 6 learns 499 sorts in
reverse order and asks dense meals whose unreduced durations exceed
signed 32-bit arithmetic."""

import random
import sys

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
QUERIES = 1000
TOP = 10**6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    sorts = 0
    days = []
    learned = 0

    def add():
        nonlocal sorts
        sorts += 1
        days.append(rng.randrange(len(DAYS)))
        lines.append("Add")

    def amounts(dense):
        return [rng.randint(0, TOP) if dense or rng.random() < 0.3 else 0 for _ in range(sorts)]

    def learn(a, truthful):
        nonlocal learned
        learned += 1
        s = rng.randrange(len(DAYS))
        e = (s + sum(x * d for x, d in zip(a, days))) % len(DAYS)
        if not truthful:
            e = (e + rng.randint(1, len(DAYS) - 1)) % len(DAYS)
        lines.append("Learn " + " ".join(map(str, a)) + " " + DAYS[s] + " " + DAYS[e])

    def eat(a):
        lines.append("Eat " + " ".join(map(str, a)) + " " + rng.choice(DAYS))

    if mode == 1:
        for _ in range(QUERIES * 2 // 5):
            add()
        while len(lines) < QUERIES:
            learn(amounts(True), True) if rng.random() < 0.5 else eat(amounts(True))
    elif mode == 2:
        for _ in range(QUERIES // 4):
            add()
        for i in range(sorts):
            a = [0] * sorts
            a[i] = rng.randint(1, len(DAYS) - 1)
            learn(a, True)
            eat(amounts(False))
        while len(lines) < QUERIES:
            eat(amounts(True))
    elif mode == 5:
        for _ in range(QUERIES - 1):
            add()
        eat([TOP] * sorts)
    elif mode == 6:
        for _ in range((QUERIES - 2) // 2):
            add()
        days[:] = [6] * sorts
        for i in reversed(range(sorts)):
            a = [0] * sorts
            a[i] = TOP - 2  # 6 modulo 7, so the pivot needs a nontrivial inverse.
            learn(a, True)
        eat([TOP] * sorts)
        eat([rng.randint(TOP - 100, TOP) for _ in range(sorts)])
    else:
        add()
        while len(lines) < QUERIES:
            r = rng.random()
            if r < 0.05 and sorts < len(DAYS):
                add()
            elif r < 0.4:
                truthful = mode == 3 or len(lines) < QUERIES - QUERIES // 10 or rng.random() < 0.9
                learn(amounts(False), truthful)
            else:
                eat(amounts(False))
    print(len(lines))
    print("\n".join(lines))


main()
