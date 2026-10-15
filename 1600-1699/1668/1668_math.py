import math
import sys
from operator import mul

PRIME = 1000000007  # independence is decided exactly, modulo this prime


def dot(u, v):
    return sum(map(mul, u, v))


def independent(vectors):
    """Indices of a maximal linearly independent subset, found by Gaussian
    elimination modulo PRIME, so no rounding decides the rank."""
    basis = []  # reduced vectors with their pivot positions
    chosen = []
    for k, vec in enumerate(vectors):
        row = [x % PRIME for x in vec]
        for pivot, base in basis:
            f = row[pivot]
            if f:
                row = [(x - f * y) % PRIME for x, y in zip(row, base)]
        pivot = next((i for i, x in enumerate(row) if x), -1)
        if pivot < 0:
            continue
        inv = pow(row[pivot], PRIME - 2, PRIME)
        basis.append((pivot, [x * inv % PRIME for x in row]))
        chosen.append(k)
    return chosen


def qr(columns, size):
    """Q and R of independent columns of the given length: Gram-Schmidt with
    every projection done twice, which keeps Q orthonormal to rounding
    error; Q is also kept transposed so a projection is one pass per row."""
    q, r = [], []
    rows = [[] for _ in range(size)]
    for col in columns:
        v = [float(x) for x in col]
        coef = [0.0] * len(q)
        for _ in range(2):
            if q:
                c = [dot(u, v) for u in q]
                v = [x - dot(c, row) for x, row in zip(v, rows)]
                coef = [a + b for a, b in zip(coef, c)]
        norm = math.sqrt(dot(v, v))
        v = [x / norm for x in v]
        q.append(v)
        r.append(coef + [norm])
        for row, x in zip(rows, v):
            row.append(x)
    return q, r


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    rows = [[int(w) for w in data[2 + i * n:2 + (i + 1) * n]] for i in range(m)]
    b = [int(w) for w in data[2 + m * n:2 + m * n + n]]
    # engine i pushes along rows[i]; the thrust is sum of X_i rows[i]. The
    # shortest best X lies in the span of the columns c_j = (rows[i][j])_i
    cols = [[rows[i][j] for i in range(m)] for j in range(n)]
    basis, _ = qr([cols[j] for j in independent(cols)], m)
    # with X = sum of w_k basis[k], the thrust is K w for K[j][k] = c_j . q_k,
    # and K has full column rank: least squares by QR of K
    k_cols = [[dot(c, u) for c in cols] for u in basis]
    q2, upper = qr(k_cols, n)
    rhs = [dot(u, b) for u in q2]
    size = len(basis)
    w = [0.0] * size
    for i in range(size - 1, -1, -1):
        w[i] = (rhs[i] - sum(upper[k][i] * w[k] for k in range(i + 1, size))) / upper[i][i]
    x = [dot(w, [u[i] for u in basis]) for i in range(m)]
    words = ["%.5f" % v for v in x]
    print(" ".join("0.00000" if s == "-0.00000" else s for s in words))


main()
