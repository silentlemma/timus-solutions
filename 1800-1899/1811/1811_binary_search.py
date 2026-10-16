import sys

FIELDS = 3  # x, y and the price of a route


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    cheapest = {}
    numbers = iter(map(int, data[2:2 + FIELDS * k]))
    for x, y, c in zip(numbers, numbers, numbers):
        key = (x - 1) * n + y - 1
        if c < cheapest.get(key, c + 1):
            cheapest[key] = c
    # the edges sorted by cost; the first m of them are those of cost up to
    # the m-th cost
    edges = sorted((c, key // n, key % n) for key, c in cheapest.items())
    reach = [0] * n  # reach[x]: the targets x pays for, as a bit mask
    size = [0] * n
    into = [[] for _ in range(n)]  # into[y]: (edge index, operator)
    for i, (c, x, y) in enumerate(edges):
        into[y].append((i, x))
    # the target with the fewest ways in comes first when picking a witness
    rare = sorted(range(n), key=lambda y: len(into[y]))
    full = (1 << n) - 1
    half = (n + 1) // 2

    def feasible(m):
        for a in range(n):
            # one operator of a covering pair pays for at least half
            if size[a] < half:
                continue
            missing = full ^ reach[a]
            if not missing:
                return True
            t = next(y for y in rare if missing >> y & 1)
            for i, b in into[t]:
                if i < m and reach[b] & missing == missing:
                    return True
        return False

    def move(frm, to):
        # take the edges between the two prefixes in or out
        step = 1 if to > frm else -1
        for i in range(frm, to) if step == 1 else range(frm - 1, to - 1, -1):
            _, x, y = edges[i]
            reach[x] ^= 1 << y
            size[x] += step

    now = 0
    lo, hi = 1, len(edges)
    move(now, hi)
    now = hi
    if not edges or not feasible(hi):
        print("No solution")
        return
    while lo < hi:
        mid = (lo + hi) // 2
        move(now, mid)
        now = mid
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(edges[lo - 1][0])


main()
