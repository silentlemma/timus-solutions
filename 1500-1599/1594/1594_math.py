MOD = 10**9 + 7


def roots_poly(m):
    """Monic polynomial, lowest coefficient first, whose roots are
    4 cos^2(j pi / (m + 1)) for j = 1 .. ceil(m / 2)."""
    # S_k(x) = U_k(x / 2) grows by S_(k+1) = x S_k - S_(k-1) from S_0 = 1 and
    # S_1 = x, and its roots are 2 cos(j pi / (m + 1)) for j = 1 .. m
    prev, cur = [1], [0, 1]
    for _ in range(m - 1):
        nxt = [0] + cur
        for i, c in enumerate(prev):
            nxt[i] = (nxt[i] - c) % MOD
        prev, cur = cur, nxt
    s = cur
    # the roots come in pairs +-x, plus 0 when m is odd, so an extra factor x
    # when m is odd makes every power even, and x^2 -> y keeps one per pair
    if m % 2 == 1:
        s = [0] + s
    return s[::2]


def det(a):
    """Determinant modulo MOD by Gaussian elimination."""
    size = len(a)
    result = 1
    for col in range(size):
        pivot = next((r for r in range(col, size) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            result = -result
        result = result * a[col][col] % MOD
        inv = pow(a[col][col], MOD - 2, MOD)
        for r in range(col + 1, size):
            f = a[r][col] * inv % MOD
            if f:
                row, top = a[r], a[col]
                for c in range(col, size):
                    row[c] = (row[c] - f * top[c]) % MOD
    return result % MOD


def resultant(p, q):
    """Res(p, q) as the determinant of the Sylvester matrix."""
    d, e = len(p) - 1, len(q) - 1
    size = d + e
    rows = []
    for i in range(e):
        row = [0] * size
        for k, c in enumerate(reversed(p)):
            row[i + k] = c
        rows.append(row)
    for i in range(d):
        row = [0] * size
        for k, c in enumerate(reversed(q)):
            row[i + k] = c
        rows.append(row)
    return det(rows)


def main():
    m, n = (int(x) for x in input().split())
    # Kasteleyn: the number of tilings is the product of a_j + b_k over the
    # roots a_j of roots_poly(m) and b_k of roots_poly(n), which is the
    # resultant of the first with the monic polynomial whose roots are -b_k
    p = roots_poly(m)
    q = roots_poly(n)
    # (-1)^e q(-y) is monic with roots -b_k: coefficient i gets (-1)^(e - i)
    e = len(q) - 1
    flipped = [c if (e - i) % 2 == 0 else -c % MOD for i, c in enumerate(q)]
    print(resultant(p, flipped))


main()
