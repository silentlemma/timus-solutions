"""Operations from a seed and a mode: mode 1 a few small numbers, 2 the
most operations with random large numbers, 3 the most operations with
multiples of one large number, 4 the most operations on a few equal
numbers, 5 powers of two times small odd numbers, 6 adding the most
numbers and then removing all of them."""

import random
import sys

MOST = 100000
LIMIT = 10 ** 9
SMALL = 12


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    q = rng.randint(1, SMALL) if mode == 1 else MOST
    base = rng.randint(LIMIT // 1000, LIMIT // 100)
    pool = [rng.randint(1, LIMIT) for _ in range(3)]

    def number():
        if mode == 1:
            return rng.randint(1, SMALL)
        if mode == 3:
            return base * rng.randint(1, LIMIT // base)
        if mode == 4:
            return rng.choice(pool)
        if mode == 5:
            return (1 << rng.randint(0, 20)) * rng.choice((1, 3, 5, 7, 9, 11))
        return rng.randint(1, LIMIT)

    held, ops = [], []
    if mode == 6:
        held = [number() for _ in range(q // 2)]
        ops = ["+ %d" % x for x in held]
        rng.shuffle(held)
        ops += ["- %d" % x for x in held]
    while len(ops) < q:
        if held and rng.random() < 0.45:
            i = rng.randrange(len(held))
            held[i], held[-1] = held[-1], held[i]
            ops.append("- %d" % held.pop())
        else:
            held.append(number())
            ops.append("+ %d" % held[-1])
    print(len(ops))
    print("\n".join(ops))


main()
