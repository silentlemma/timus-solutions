"""One test from a seed and a mode: mode 1 a small random graph, mode 2 a
chain of simple cycles joined by arcs (polynomial growth), mode 3 the
same with one extra arc inside a cycle somewhere, mode 4 a large random
sparse graph, mode 5 a long path with no cycles and a cycle off the
path, mode 6 cycles in parallel branches of different lengths."""

import random
import sys

MOST = 100000


def emit(n, s, t, arcs, rng):
    arcs = list(set(arcs))
    rng.shuffle(arcs)
    names = list(range(1, n + 1))
    rng.shuffle(names)
    print(n, len(arcs), names[s], names[t])
    for a, b in arcs:
        print(names[a], names[b])


def cycle_chain(rng, count, length, extra):
    """count cycles of up to length vertices, each joined to the next."""
    arcs, n, prev = [], 0, None
    first = None
    for c in range(count):
        size = rng.randint(1, length)
        vs = list(range(n, n + size))
        n += size
        for i in range(size):
            arcs.append((vs[i], vs[(i + 1) % size]))
        if prev is not None:
            arcs.append((rng.choice(prev), rng.choice(vs)))
        if first is None:
            first = vs
        prev = vs
    if extra:
        a = rng.randrange(n)
        b = rng.randrange(n)
        arcs.append((a, b))
    return n, first[0], prev[-1], arcs


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, 7)
        arcs = [(a, b) for a in range(n) for b in range(n) if rng.random() < 0.2]
        if not arcs:
            arcs = [(0, 0)]
        emit(n, rng.randrange(n), rng.randrange(n), arcs, rng)
    elif mode in (2, 3):
        count = rng.randint(1, 30)
        n, s, t, arcs = cycle_chain(rng, count, MOST // count // 2, mode == 3)
        emit(n, s, t, arcs[:MOST], rng)
    elif mode == 4:
        n = MOST
        arcs = {(rng.randrange(n), rng.randrange(n)) for _ in range(MOST)}
        emit(n, rng.randrange(n), rng.randrange(n), arcs, rng)
    elif mode == 5:
        n = MOST // 2
        arcs = [(i, i + 1) for i in range(n - 2)] + [(n - 1, n - 1), (5, n - 1)]
        emit(n, 0, n - 2, arcs, rng)
    else:
        # s -> branch_i -> t, branch i a cycle of its own length
        arcs, n = [], 2
        for _ in range(rng.randint(2, 6)):
            size = rng.randint(1, 7)
            vs = list(range(n, n + size))
            n += size
            for i in range(size):
                arcs.append((vs[i], vs[(i + 1) % size]))
            arcs.append((0, vs[0]))
            arcs.append((vs[-1], 1))
        arcs.append((1, 1))
        emit(n, 0, 1, arcs, rng)


main()
