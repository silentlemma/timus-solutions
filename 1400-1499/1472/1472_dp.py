import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    boss = [0, 0] + [int(x) for x in data[1 : 2 * n - 1 : 2]]
    price = [0, 0] + [int(x) for x in data[2 : 2 * n : 2]]
    # cut[v]: the cheapest way to separate v from every private below it,
    # or None until v gets a subordinate, so privates stay None (cannot be cut)
    cut = [None] * (n + 1)
    for v in range(n, 1, -1):
        cost = price[v] if cut[v] is None else min(price[v], cut[v])
        p = boss[v]
        cut[p] = cost if cut[p] is None else cut[p] + cost
    sys.stdout.write("%d.00\n" % cut[1])


main()
