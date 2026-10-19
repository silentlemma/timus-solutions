"""Two routing tables from a seed and a mode. Mode 1 a few rows in a
small corner of the address space, mode 2 the most rows there, mode 3
the most rows spread everywhere. Mode 4 has exactly 65536 rows: two
shuffled /17 partitions with random gateways and unmasked host bits.
Mode 5 has 65535 rows in a complete prefix tree through /15, whose
leaves all route to zero, against one equivalent default route.
In modes 1-3, the second table is the first one
rewritten with some blocks split into halves of the same gateway and
then, for odd seeds, changed in one row, so both answers come up."""

import random
import sys

LIMIT = 65536
BITS = 32
FULL = (1 << BITS) - 1
SMALL = 6


def text(value):
    return ".".join(str(value >> s & 255) for s in (24, 16, 8, 0))


def mask(length):
    return FULL ^ ((1 << (BITS - length)) - 1)


def maximal(seed, mode):
    rng = random.Random(seed)
    if mode == 4:
        route_mask = mask(17)
        gates = [0, FULL] + [rng.randint(0, FULL) for _ in range(LIMIT // 2 - 2)]
        tables = []
        for _ in range(2):
            rows = [(index << 15 | rng.getrandbits(15), route_mask, gate)
                    for index, gate in enumerate(gates)]
            rng.shuffle(rows)
            tables.append(rows)
    else:
        rows = []
        for length in range(16):
            route_mask = mask(length)
            for prefix in range(1 << length):
                network = prefix << (BITS - length)
                network |= rng.getrandbits(BITS - length)
                gate = 0 if length == 15 else rng.randint(0, FULL)
                rows.append((network, route_mask, gate))
        rng.shuffle(rows)
        tables = [rows, [(FULL, 0, 0)]]
    for rows in tables:
        print(len(rows))
        for row in rows:
            print(*(text(value) for value in row))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    if mode in (4, 5):
        maximal(seed, mode)
        return
    rng = random.Random(seed)
    gates = [rng.randint(0, FULL) for _ in range(rng.randint(1, 4))]
    base = rng.randint(0, FULL) & mask(16)
    count = rng.randint(1, SMALL) if mode == 1 else LIMIT // 4
    first = {}
    while len(first) < count:
        if mode == 3:
            length, address = rng.randint(0, BITS), rng.randint(0, FULL)
        elif mode == 2:
            length, address = rng.randint(16, BITS), base | rng.randint(0, 65535)
        else:
            length, address = rng.randint(20, BITS), base | rng.randint(0, 4095)
        first[(address & mask(length), length)] = rng.choice(gates)
    second = dict(first)
    for key in list(second):
        prefix, length = key
        if key in second and length < BITS and rng.random() < 0.3:
            # split the block into its halves, keeping more specific rows
            gate = second.pop(key)
            half = 1 << (BITS - length - 1)
            for child in ((prefix, length + 1), (prefix | half, length + 1)):
                second.setdefault(child, gate)
    if seed % 2 and second:
        key = rng.choice(list(second))
        second[key] = rng.randint(0, FULL)
    for table in (first, second):
        rows = list(table.items())
        rng.shuffle(rows)
        print(len(rows))
        for (prefix, length), gate in rows:
            # bits outside the mask are allowed in the written address
            noise = rng.randint(0, FULL) & ~mask(length) if rng.random() < 0.3 else 0
            print(text(prefix | noise), text(mask(length)), text(gate))


main()
