"""A chain of movable pulleys: a seed and a mode. Each movable pulley
hangs on one end of the rope over the next one, and the last hangs on a
fixed pulley. Mode 1 puts the free rope on the first axle and the turnip
on the fixed pulley, mode 2 the other way round, mode 3 hangs the turnip
on a chain tied to the ceiling and the free rope on a separate pair of
pulleys, mode 4 the longest chain. Mode 5 reverses that longest chain.
Mode 6 creates a random height-consistent system; optional arguments are
the pulley count (default 32) and connection density in percent (default
100). Mode 7 creates a randomly relabelled path of 32 mixed-type pulleys
with random choices of rope and axle connections."""

import random
import sys

CEILING, TURNIP, FREE = 0, -1, -2
LONGEST = 31


def random_system(rng, n, density):
    kinds = [rng.randint(1, 2) for _ in range(n)]
    if n == 1:
        kinds[0] = 1
    heights = list(range(n))
    rng.shuffle(heights)
    ports = [(i, p) for i in range(n) for p in range(3)]

    def down(port):
        i, p = port
        return kinds[i] == (1 if p < 2 else 2)

    loads = rng.sample([port for port in ports if down(port)], 2)
    blocks = [[kind, CEILING, CEILING, CEILING] for kind in kinds]
    for (i, p), target in zip(loads, (TURNIP, FREE)):
        blocks[i][p + 1] = target
    available = set(ports) - set(loads)
    candidates = [(a, b) for a in ports for b in ports
                  if heights[a[0]] > heights[b[0]] and down(a) and not down(b)]
    rng.shuffle(candidates)
    for a, b in candidates:
        if a in available and b in available and rng.randrange(100) < density:
            blocks[a[0]][a[1] + 1] = b[0] + 1
            blocks[b[0]][b[1] + 1] = a[0] + 1
            available.remove(a)
            available.remove(b)
    return blocks


def random_path(rng):
    n = LONGEST + 1
    blocks = []
    previous = None
    previous_down = None
    for i in range(n):
        kind = rng.randint(1, 2)
        # The incoming connection, or the turnip at the first pulley.
        incoming_down = True if previous is None else not previous_down
        if i == n - 1 and incoming_down:
            kind = 1
        incoming = [p for p in range(3) if (kind == (1 if p < 2 else 2)) == incoming_down]
        entry = rng.choice(incoming)
        exits = [p for p in range(3) if p != entry]
        if i == n - 1:
            exits = [p for p in exits if kind == (1 if p < 2 else 2)]
        leave = rng.choice(exits)
        row = [kind, CEILING, CEILING, CEILING]
        row[entry + 1] = TURNIP if previous is None else i
        if previous is not None:
            blocks[-1][previous + 1] = i + 1
        if i == n - 1:
            row[leave + 1] = FREE
        blocks.append(row)
        previous = leave
        previous_down = kind == (1 if leave < 2 else 2)
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    result = [None] * n
    for old, row in enumerate(blocks):
        result[labels[old] - 1] = [row[0], *[labels[x - 1] if x > 0 else x for x in row[1:]]]
    return result


def extra_mode(seed, mode):
    rng = random.Random(seed)
    if mode == 5:
        blocks = []
        for i in range(1, LONGEST + 1):
            ends = [CEILING, i + 1]
            rng.shuffle(ends)
            blocks.append([2, *ends, TURNIP if i == 1 else i - 1])
        blocks.append([1, LONGEST, FREE, CEILING])
    elif mode == 6:
        n = int(sys.argv[3]) if len(sys.argv) > 3 else LONGEST + 1
        density = int(sys.argv[4]) if len(sys.argv) > 4 else 100
        if not 1 <= n <= LONGEST + 1 or not 0 <= density <= 100:
            raise ValueError('invalid pulley count or density')
        blocks = random_system(rng, n, density)
    else:
        blocks = random_path(rng)
    print(len(blocks))
    for row in blocks:
        print(*row)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (5, 6, 7):
        extra_mode(seed, mode)
        return
    rng = random.Random(seed)
    k = LONGEST if mode == 4 else rng.randint(2, 20)
    first, last = (TURNIP, FREE) if mode == 2 else (FREE, TURNIP)
    if mode == 3:
        k = rng.randint(2, 20)
        first = TURNIP
    blocks = []
    for i in range(1, k + 1):
        load = first if i == 1 else i - 1  # the axle hangs on the previous rope
        ends = [CEILING, i + 1] if i < k or mode != 3 else [CEILING, CEILING]
        rng.shuffle(ends)
        blocks.append([2, *ends, load])
    if mode == 3:
        # a fixed pulley and a movable one on the same rope, with the free load
        blocks.append([1, k + 2, k + 2, CEILING])
        blocks.append([2, k + 1, k + 1, FREE])
    else:
        blocks.append([1, k, last, CEILING])
    print(len(blocks))
    for b in blocks:
        print(*b)


main()
