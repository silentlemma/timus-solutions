import sys

FIELDS = 4  # x, y, z and the radius


def main():
    data = list(map(int, sys.stdin.read().split()))
    k = data[0]
    xs, ys, zs, rs = (data[1 + f :: FIELDS][:k] for f in range(FIELDS))
    parent = list(range(k))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for i in range(k):
        x, y, z, r = xs[i], ys[i], zs[i], rs[i]
        # two balls share more than one point when the centres are closer than r1 + r2
        for j in [
            j
            for j in range(i + 1, k)
            if (xs[j] - x) ** 2 + (ys[j] - y) ** 2 + (zs[j] - z) ** 2 < (rs[j] + r) ** 2
        ]:
            parent[find(j)] = find(i)
    groups = {}
    for v in range(k):
        groups.setdefault(find(v), []).append(v)
    # each group lists its planets in order, and groups come by their first planet
    lines = [", ".join(map(str, g)) for g in sorted(groups.values())]
    print("\n".join(lines))


main()
