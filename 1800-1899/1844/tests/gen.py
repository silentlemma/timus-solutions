"""Tests from a seed and a mode: mode 1 ten short plans over a few mages,
2 ten of the longest plans over many mages, 3 ten of the longest plans
over a few mages, so that the offices often share one, 4 ten long plans
that take mages in nested order, both in the same order or in opposite
orders, 5 ten of the longest plans where every mage is held briefly."""

import random
import sys

TESTS = 10
MOST = 1000
FEW = 4


def plan(rng, length, mages, hold):
    # length steps that call and release mages; every call is released
    held, free, ops = [], list(range(1, mages + 1)), []

    def move(source, target):
        # a random mage from source to target, by swapping it to the end
        i = rng.randrange(len(source))
        source[i], source[-1] = source[-1], source[i]
        target.append(source.pop())
        return target[-1]

    while len(ops) < length:
        left = length - len(ops)
        if free and left > len(held) and (not held or rng.random() < hold):
            ops.append("+ %d" % move(free, held))
        else:
            ops.append("- %d" % move(held, free))
    return ops


def nested(rng, length, mages, flip):
    order = rng.sample(range(1, mages + 1), length // 2)
    calls = ["+ %d" % a for a in order]
    first = calls + ["- %d" % a for a in reversed(order)]
    if flip:
        order.reverse()
    second = ["+ %d" % a for a in order] + ["- %d" % a for a in reversed(order)]
    return first, second


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(TESTS)
    for _ in range(TESTS):
        if mode == 4:
            length = 2 * rng.randint(1, MOST // 2)
            mages = MOST
            sandro, zagamius = nested(rng, length, mages, rng.random() < 0.5)
        else:
            short = mode == 1
            mages = rng.randint(1, FEW) if mode in (1, 3) else MOST
            n = 2 * rng.randint(1, FEW if short else MOST // 2)
            m = 2 * rng.randint(1, FEW if short else MOST // 2)
            if mode != 1:
                n = m = MOST
            hold = 0.1 if mode == 5 else 0.6
            sandro, zagamius = plan(rng, n, mages, hold), plan(rng, m, mages, hold)
        print(len(sandro), len(zagamius), mages)
        print("\n".join(sandro + zagamius))


main()
