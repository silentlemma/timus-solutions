import sys

SHORTEST = 3  # a route has at least three stops


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    n, m = data[0], data[1]
    adj = [0] * n
    roads = data[2:]
    for i in range(m):
        a, b = roads[2 * i] - 1, roads[2 * i + 1] - 1
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    # paths[mask * n + v]: simple paths from the lowest stop of mask through
    # all of mask, ending at v; a path that can close counts its cycle twice
    paths = [0] * ((1 << n) * n)
    cycles = [0] * (1 << n)
    for s in range(n):
        paths[(1 << s) * n + s] = 1
    for mask in range(1, 1 << n):
        low = mask & -mask
        start = low.bit_length() - 1
        above = ~((low << 1) - 1)  # stops that may still join this path
        base = mask * n
        closing = 0
        free = ~mask & above & ((1 << n) - 1)
        rest = mask
        while rest:
            bit = rest & -rest
            rest ^= bit
            v = bit.bit_length() - 1
            count = paths[base + v]
            if not count:
                continue
            if adj[v] >> start & 1:
                closing += count
            step = adj[v] & free
            while step:
                ubit = step & -step
                step ^= ubit
                paths[(mask | ubit) * n + ubit.bit_length() - 1] += count
        if bin(mask).count("1") >= SHORTEST:
            cycles[mask] = closing // 2

    # the bipartite graph of routes and stops needs as many rows as its
    # largest degree: the longest route or the busiest stop
    longest = max((bin(mask).count("1") for mask in range(1 << n) if cycles[mask]), default=0)
    through = [0] * n
    for mask in range(1 << n):
        if cycles[mask]:
            for v in range(n):
                if mask >> v & 1:
                    through[v] += cycles[mask]
    print(max([longest] + through))


main()
