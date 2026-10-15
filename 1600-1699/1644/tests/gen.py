"""One test from a seed and a mode: mode 1 consistent records around a
hidden threshold, mode 2 records with one possible lie, mode 3 up to 100
records."""

import random
import sys

LOW, HIGH = 3, 9
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    threshold = rng.randint(LOW, HIGH + 1)  # the least satisfying amount
    n = rng.randint(0, MOST if mode == 3 else 10)
    records = []
    for _ in range(n):
        count = rng.randint(LOW, HIGH)
        records.append([count, "satisfied" if count >= threshold else "hungry"])
    if mode == 2 and records:
        lie = rng.choice(records)
        lie[1] = "hungry" if lie[1] == "satisfied" else "satisfied"
    print(n)
    for count, verdict in records:
        print(count, verdict)


main()
