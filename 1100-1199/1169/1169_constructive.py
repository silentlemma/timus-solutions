SMALLEST_CYCLE = 3


def pairs(s):
    return s * (s - 1) // 2


def main():
    n, k = map(int, input().split())
    # a pair is not critical exactly when both computers lie in the same
    # 2-edge-connected part; such a part has one computer or at least three,
    # so the sizes must split n with pairs(size) adding up to pairs(n) - k
    target = pairs(n) - k
    sizes = [1] + list(range(SMALLEST_CYCLE, n + 1))
    # reach[m] has bit t set when m computers can be split with t inner pairs
    reach = [1] + [0] * n
    for m in range(1, n + 1):
        for s in sizes:
            if s <= m:
                reach[m] |= reach[m - s] << pairs(s)
    if target < 0 or not reach[n] >> target & 1:
        print(-1)
        return
    parts = []
    m, t = n, target
    while m:
        s = next(
            s for s in sizes if s <= m and pairs(s) <= t and reach[m - s] >> (t - pairs(s)) & 1
        )
        parts.append(s)
        m, t = m - s, t - pairs(s)
    # each part is a cycle (or a single computer), and bridges join the first
    # computers of consecutive parts
    edges = []
    first = 1
    for idx, s in enumerate(parts):
        if s > 1:
            edges += [(first + j, first + (j + 1) % s) for j in range(s)]
        if idx:
            edges.append((prev, first))
        prev, first = first, first + s
    print("\n".join("%d %d" % e for e in edges))


main()
