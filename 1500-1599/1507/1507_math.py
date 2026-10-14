import sys


def multiply(x, y):
    """The boolean product of two matrices kept as row bitmasks."""
    out = []
    for row in x:
        acc, j = 0, 0
        while row:
            if row & 1:
                acc |= y[j]
            row >>= 1
            j += 1
        out.append(acc)
    return out


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # only whether an entry is zero matters: all entries are non-negative
    a = [sum(1 << j for j in range(n) if data[1 + i * n + j] != "0") for i in range(n)]
    low, high = n * (n - 1), n * (n + 1)
    # A^low by repeated squaring
    cur, base, e = [1 << i for i in range(n)], a, low
    while e:
        if e & 1:
            cur = multiply(cur, base)
        base = multiply(base, base)
        e >>= 1
    seen = [0] * n
    for _ in range(low, high + 1):
        seen = [s | c for s, c in zip(seen, cur)]
        cur = multiply(cur, a)
    print("Yes" if all(s == (1 << n) - 1 for s in seen) else "No")


main()
