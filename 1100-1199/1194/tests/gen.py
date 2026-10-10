"""A night out: a seed, N, K and the most groups a split makes. The K
couples and the single hobbits are shuffled, and groups split at random,
never parting a couple, until every group is a single hobbit or a
couple; the splits are written in the order they happen."""

import random
import sys


def main():
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
