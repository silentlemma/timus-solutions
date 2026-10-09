import sys
from operator import mul

# linear independence is tested modulo a large prime: exact, and a set that is
# independent modulo the prime is independent over the rationals
P = 2147483647


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m, n = data[0], data[1]
    flat = data[2 : 2 + m * n]
    vec = [[x % P for x in flat[i * n : (i + 1) * n]] for i in range(m)]
    cost = data[2 + m * n : 2 + m * n + m]
    # the greedy algorithm of a matroid: the cheapest vectors first, and among
    # equal prices the smaller numbers first, which gives the smallest list too
    order = sorted(range(m), key=lambda i: (cost[i], i))
    # a fully reduced basis: row r has 1 in its pivot and 0 in all other pivots,
    # so the remainder of v in a free coordinate k is v[k] - sum(v[pivot] * row[k])
    pivots = []
    rows = []
    free = list(range(n))
    column = {k: [] for k in free}
    chosen = []
    for i in order:
        if len(chosen) == n:
            break
        v = vec[i]
        coeffs = [v[p] for p in pivots]
        rest = {k: (v[k] - sum(map(mul, coeffs, column[k]))) % P for k in free}
        piv = next((k for k in free if rest[k]), -1)
        if piv < 0:
            continue
        inv = pow(rest[piv], P - 2, P)
        new = [0] * n
        for k in free:
            new[k] = rest[k] * inv % P
        # clear the new pivot from the other rows
        for row in rows:
            f = row[piv]
            if f:
                for k in free:
                    row[k] = (row[k] - f * new[k]) % P
        pivots.append(piv)
        rows.append(new)
        free.remove(piv)
        column = {k: [row[k] for row in rows] for k in free}
        chosen.append(i)
    if len(chosen) < n:
        print(0)
        return
    out = [sum(cost[i] for i in chosen)] + [i + 1 for i in sorted(chosen)]
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
