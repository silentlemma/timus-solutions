"""Statements around a hidden deal: a seed, a mode and a size. Mode 1
picks the true statements at random, mode 2 makes most friends tell the
truth about themselves, mode 3 most friends about someone else, and
mode 4 makes many friends claim the same card. The rules of the problem
hold: no two friends name the same person with the same card, and nobody
gives a person the card that person claims."""

import random
import sys

TRIES = 1000


def build(rng, n, mode):
    card = list(range(1, n + 1))
    rng.shuffle(card)
    card = [0] + card  # card[p] is the card friend p holds
    share = {1: 0.5, 2: 0.9, 3: 0.1, 4: 0.3}[mode]
    first = [False] + [rng.random() < share for _ in range(n)]
    crowd = rng.randint(1, n)  # the card many claim in mode 4
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        if first[i]:
            a[i] = card[i]
        else:
            wrong = crowd if mode == 4 and crowd != card[i] else rng.randint(1, n)
            while wrong == card[i]:
                wrong = rng.randint(1, n)
            a[i] = wrong
    claimed, rows = set(), []
    liars = [p for p in range(1, n + 1) if not first[p]]
    rng.shuffle(liars)
    for i in range(1, n + 1):
        if not first[i]:
            # a true claim about someone whose own first statement is false
            options = [p for p in liars if p != i and (p, card[p]) not in claimed]
            if not options:
                return None
            b = options[0]
            c = card[b]
        else:
            for _ in range(TRIES):
                b = rng.randint(1, n)
                c = rng.randint(1, n)
                if b != i and c != card[b] and c != a[b] and (b, c) not in claimed:
                    break
            else:
                return None
        claimed.add((b, c))
        rows.append((a[i], b, c))
    return rows


def main():
    seed, mode, n = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    rows = None
    while rows is None:
        rows = build(rng, n, mode)
    print(n)
    for row in rows:
        print(*row)


main()
