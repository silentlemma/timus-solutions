import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    offers = [(data[1 + i], [i + 1]) for i in range(n)]
    pos = n + 2
    for _ in range(data[n + 1]):
        cost, size = data[pos], data[pos + 1]
        offers.append((cost, data[pos + 2 : pos + 2 + size]))
        pos += 2 + size
    wanted = set(data[pos + 1 : pos + 1 + data[pos]])
    # the caps that appear in the fewest offers become the lowest bits,
    # since the lowest missing cap picks which offers are tried
    order = sorted(wanted, key=lambda cap: sum(cap in caps for _, caps in offers))
    bit = {cap: 1 << i for i, cap in enumerate(order)}
    best = {}
    for cost, caps in offers:
        mask = sum(bit[cap] for cap in set(caps) if cap in bit)
        if mask and cost < best.get(mask, cost + 1):
            best[mask] = cost
    # an offer is useless if another one covers as much for no more money
    useful = [
        (cost, mask)
        for mask, cost in best.items()
        if not any(m != mask and m & mask == mask and c <= cost for m, c in best.items())
    ]
    full = (1 << len(order)) - 1
    by_low = [[] for _ in order]
    for cost, mask in useful:
        for i in range(len(order)):
            if mask >> i & 1:
                by_low[i].append((cost, full & ~mask))
    # cheapest[s]: the least money that buys every cap of the set s
    cheapest = [0] * (full + 1)
    for s in range(1, full + 1):
        low = (s & -s).bit_length() - 1
        least = None
        for cost, keep in by_low[low]:
            value = cost + cheapest[s & keep]
            if least is None or value < least:
                least = value
        cheapest[s] = least
    print(cheapest[full])


main()
