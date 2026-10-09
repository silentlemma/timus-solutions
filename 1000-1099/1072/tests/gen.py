"""A random network: a seed, N, the number of subnets and the shape (0 any
interfaces, 1 a chain of subnets with extra links, 2 two halves that share
no subnet, 3 a bare chain). The computers are numbered at random."""

import random
import sys

ANY, CHAIN, HALVES, LINE = 0, 1, 2, 3
MAX_INTERFACES = 5
FULL = (1 << 32) - 1
SHORTEST_MASK = 8
LONGEST_MASK = 30


def subnet(rng):
    size = rng.randint(SHORTEST_MASK, LONGEST_MASK)
    mask = FULL ^ ((1 << (32 - size)) - 1)
    return rng.getrandbits(32) & mask, mask


def dotted(v):
    return ".".join(str((v >> shift) & 0xFF) for shift in (24, 16, 8, 0))


def main():
    seed, n, count, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    nets = []
    while len(nets) < count:
        net = subnet(rng)
        if net not in nets:
            nets.append(net)
    owned = []
    for i in range(n):
        if shape in (CHAIN, LINE):
            # computer i links subnets i and i + 1, and in a chain maybe one more
            mine = [i % count, (i + 1) % count]
            if shape == CHAIN:
                mine += rng.sample(range(count), rng.randint(0, 1))
        elif shape == HALVES:
            half = range(0, count // 2) if i < n // 2 else range(count // 2, count)
            mine = rng.sample(list(half), rng.randint(1, min(MAX_INTERFACES, len(half))))
        else:
            mine = rng.sample(range(count), rng.randint(1, min(MAX_INTERFACES, count)))
        owned.append(sorted(set(mine))[:MAX_INTERFACES])
    order = list(range(n))
    rng.shuffle(order)
    lines = [str(n)]
    for i in order:
        lines.append(str(len(owned[i])))
        for j in owned[i]:
            net, mask = nets[j]
            host = rng.getrandbits(32) & (FULL ^ mask)
            lines.append(dotted(net | host) + " " + dotted(mask))
    if shape != ANY:
        a, b = order.index(0), order.index(n - 1)
    else:
        a, b = rng.sample(range(n), 2)
    lines.append("%d %d" % (a + 1, b + 1))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
