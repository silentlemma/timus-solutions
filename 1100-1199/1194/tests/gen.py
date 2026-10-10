"""Generate complete parties, never separating a married couple.

Modes:
  SEED N K WIDEST: shuffle couples and singles, then split groups at random.
  chain N K: peel off one terminal group at each binary split.
  star N K: separate all terminal groups at one crossroads.
"""

import random
import sys


def structured(mode, n, k):
    assert 2 < n <= 20000 and 0 <= 2 * k <= n
    units = [2] * k + [1] * (n - 2 * k)
    print(n, k)
    if mode == "star":
        line = [1, len(units)]
        for number, size in enumerate(units, 2):
            line.extend((number, size))
        print(*line)
        return
    parent, last, remaining = 1, 1, n
    for size in units[:-1]:
        remaining -= size
        print(parent, 2, last + 1, size, last + 2, remaining)
        parent = last + 2
        last += 2


def main():
    if sys.argv[1] in ("chain", "star"):
        mode, n, k = sys.argv[1:]
        structured(mode, int(n), int(k))
        return
    seed, n, k, widest = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    # units: a couple counts 2, a single hobbit 1
    units = [2] * k + [1] * (n - 2 * k)
    rng.shuffle(units)
    lines = ["%d %d" % (n, k)]
    pending = [(1, units)]
    last = 1
    while pending:
        number, group = pending.pop(0)
        if len(group) == 1:
            continue
        parts = rng.randint(2, min(widest, len(group)))
        cuts = sorted(rng.sample(range(1, len(group)), parts - 1))
        pieces = [group[a:b] for a, b in zip([0] + cuts, cuts + [len(group)])]
        line = [number, len(pieces)]
        for piece in pieces:
            last += 1
            line += [last, sum(piece)]
            pending.append((last, piece))
        lines.append(" ".join(map(str, line)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
