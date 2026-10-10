import sys

# among three vectors no longer than L, some sum or difference of two of them
# is no longer than L, so they can be merged into one
KEEP = 3


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n, length = next(tok), next(tok)
    # nodes 0..n-1 are the input vectors, later nodes are merged pairs
    x, y = [], []
    parent, rel = [], []

    def add(vx, vy):
        x.append(vx)
        y.append(vy)
        parent.append(-1)
        rel.append(1)
        return len(x) - 1

    def join(a, b, s):
        node = add(x[a] + s * x[b], y[a] + s * y[b])
        parent[a] = parent[b] = node
        rel[b] = s
        return node

    for _ in range(n):
        add(next(tok), next(tok))
    active = []
    for i in range(n):
        active.append(i)
        if len(active) < KEEP:
            continue
        choice = next(
            (p, q, s)
            for p in range(KEEP)
            for q in range(p + 1, KEEP)
            for s in (-1, 1)
            if (x[active[p]] + s * x[active[q]]) ** 2 + (y[active[p]] + s * y[active[q]]) ** 2
            <= length * length
        )
        p, q, s = choice
        rest = [active[r] for r in range(KEEP) if r not in (p, q)]
        active = rest + [join(active[p], active[q], s)]
    # two vectors no longer than L: a sign making their dot product
    # non-positive keeps the sum within sqrt(2) L
    if len(active) == 2:
        a, b = active
        join(a, b, -1 if x[a] * x[b] + y[a] * y[b] > 0 else 1)
    sign = [1] * len(x)
    for k in range(len(x) - 1, -1, -1):
        if parent[k] >= 0:
            sign[k] = sign[parent[k]] * rel[k]
    print("YES")
    print("".join("+" if sign[i] > 0 else "-" for i in range(n)))


main()
