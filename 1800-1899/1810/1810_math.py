import sys
from collections import Counter

MOD = 3
SHIFT = 32


def add(a, b):
    """Sum of two vectors over GF(3), each kept as two bit masks: the
    coordinates equal to 1 and the coordinates equal to 2."""
    a1, a2 = a
    b1, b2 = b
    t = (a1 | b2) ^ (a2 | b1)
    return (a2 | b2) ^ t, (a1 | b1) ^ t


def main():
    data = list(map(int, sys.stdin.read().split()))
    k, n = data[0], data[1]
    rows = [data[2 + i * (n + 1):2 + (i + 1) * (n + 1)] for i in range(k)]
    target = [row[n] for row in rows]
    # vectors w that are orthogonal to the column of every variable span the
    # null space of the transposed matrix, and y is Ax for some x exactly when
    # every such w is orthogonal to y
    m = [[rows[i][j] for i in range(k)] for j in range(n)]
    pivots = []
    for c in range(k):
        r = len(pivots)
        sel = next((i for i in range(r, n) if m[i][c]), None)
        if sel is None:
            continue
        m[r], m[sel] = m[sel], m[r]
        if m[r][c] == 2:
            m[r] = [v * 2 % MOD for v in m[r]]
        for i in range(n):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [(v - f * w) % MOD for v, w in zip(m[i], m[r])]
        pivots.append(c)
    rank = len(pivots)
    basis = []
    for free in range(k):
        if free not in pivots:
            w = [0] * k
            w[free] = 1
            for i, c in enumerate(pivots):
                w[c] = -m[i][free] % MOD
            basis.append(w)
    # what y_i = v adds to the syndrome (w . y) over all w of the basis
    contribution = []
    for i in range(k):
        ones = sum(1 << j for j, w in enumerate(basis) if w[i] == 1)
        twos = sum(1 << j for j, w in enumerate(basis) if w[i] == 2)
        contribution.append({1: (ones, twos), 2: (twos, ones)})

    def syndromes(coords):
        sums = [(0, 0)]
        for i in coords:
            options = [v for v in range(MOD) if v != target[i]]
            sums = [s if v == 0 else add(s, contribution[i][v]) for s in sums for v in options]
        return sums

    # every y_i has two allowed values: meet in the middle on syndromes
    half = k // 2
    left = Counter(one << SHIFT | two for one, two in syndromes(range(half)))
    total = sum(left[two << SHIFT | one] for one, two in syndromes(range(half, k)))
    print(total * MOD ** (n - rank))


main()
