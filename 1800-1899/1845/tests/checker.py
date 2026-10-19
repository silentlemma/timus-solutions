"""Checker: the output r must have a smaller absolute value than p, and
the determinant minus r must be divisible by p. The determinant is
computed exactly by Bareiss elimination over the Gaussian integers."""

import sys


class Bad(Exception):
    pass


def determinant(re, im):
    n = len(re)
    sign = 1
    dr, di = 1, 0
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if re[i][k] or im[i][k]), None)
        if pivot is None:
            return 0, 0
        if pivot != k:
            re[k], re[pivot] = re[pivot], re[k]
            im[k], im[pivot] = im[pivot], im[k]
            sign = -sign
        cr, ci = re[k][k], im[k][k]
        norm = dr * dr + di * di
        for i in range(k + 1, n):
            ar, ai = re[i][k], im[i][k]
            for j in range(k + 1, n):
                xr = re[i][j] * cr - im[i][j] * ci - ar * re[k][j] + ai * im[k][j]
                xi = re[i][j] * ci + im[i][j] * cr - ar * im[k][j] - ai * re[k][j]
                re[i][j], left = divmod(xr * dr + xi * di, norm)
                im[i][j], right = divmod(xi * dr - xr * di, norm)
                assert not left and not right, "Bareiss division is not exact"
        dr, di = cr, ci
    return sign * re[n - 1][n - 1], sign * im[n - 1][n - 1]


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n = data[0]
    re = [[data[1 + 2 * (n * i + j)] for j in range(n)] for i in range(n)]
    im = [[data[2 + 2 * (n * i + j)] for j in range(n)] for i in range(n)]
    pr, pi = data[1 + 2 * n * n], data[2 + 2 * n * n]
    got = open(output).read().split()
    if len(got) != 2:
        raise Bad("expected two numbers")
    try:
        rr, ri = int(got[0]), int(got[1])
    except ValueError:
        raise Bad("expected two integers")
    norm = pr * pr + pi * pi
    if rr * rr + ri * ri >= norm:
        raise Bad("the remainder is not smaller than p")
    dr, di = determinant(re, im)
    xr, xi = dr - rr, di - ri
    if (xr * pr + xi * pi) % norm or (xi * pr - xr * pi) % norm:
        raise Bad("the determinant minus the output is not divisible by p")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
