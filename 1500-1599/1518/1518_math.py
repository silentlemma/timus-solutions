import sys

HEADER = 3  # N, X and Y come first


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, x, y = data[0], data[1], data[2]
    keys = data[HEADER : HEADER + n]
    shifts = data[HEADER + n : HEADER + 2 * n]
    # K[i] = sum of K[i - j] * C[n + 1 - j] over j = 1 ... n, so x^n can be
    # replaced by the sum of x^(n - j) over the j with C[n + 1 - j] = 1
    steps = [j for j in range(1, n + 1) if shifts[n - j] == 1]

    def times(p, q):
        """p * q modulo the characteristic polynomial and y."""
        prod = [0] * (2 * n - 1)
        for i, a in enumerate(p):
            if a:
                for j, b in enumerate(q):
                    prod[i + j] += a * b
        for d in range(2 * n - 2, n - 1, -1):
            top = prod[d] % y
            if top:
                for j in steps:
                    prod[d - j] += top
        return [v % y for v in prod[:n]]

    # K[x] is the x - 1 st term counting from K[1], and the coefficients of
    # x^(x - 1) reduced modulo the characteristic polynomial weigh K[1 ... n]
    result = [1] + [0] * (n - 1) if n > 1 else [1]
    base = [0, 1] + [0] * (n - 2) if n > 1 else [shifts[0] % y]
    e = x - 1
    while e:
        if e & 1:
            result = times(result, base)
        base = times(base, base)
        e >>= 1
    print(sum(r * k for r, k in zip(result, keys)) % y)


main()
