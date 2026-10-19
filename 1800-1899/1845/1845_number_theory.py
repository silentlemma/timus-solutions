import sys


def remainder(xr, xi, pr, pi):
    # x - p q with q = x / p rounded in both parts: the norm of what is left
    # is at most half the norm of p
    norm = pr * pr + pi * pi
    nr, ni = xr * pr + xi * pi, xi * pr - xr * pi  # x times the conjugate of p
    qr, qi = (2 * nr + norm) // (2 * norm), (2 * ni + norm) // (2 * norm)
    return xr - (pr * qr - pi * qi), xi - (pr * qi + pi * qr)


def determinant(re, im):
    # Bareiss elimination over the Gaussian integers: every division by the
    # previous pivot is exact, so all entries stay integer
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
        rk, ik = re[k], im[k]
        cr, ci = rk[k], ik[k]
        norm = dr * dr + di * di
        for i in range(k + 1, n):
            ri, ii = re[i], im[i]
            ar, ai = ri[k], ii[k]
            for j in range(k + 1, n):
                xr = ri[j] * cr - ii[j] * ci - ar * rk[j] + ai * ik[j]
                xi = ri[j] * ci + ii[j] * cr - ar * ik[j] - ai * rk[j]
                ri[j] = (xr * dr + xi * di) // norm
                ii[j] = (xi * dr - xr * di) // norm
        dr, di = cr, ci
    return sign * re[n - 1][n - 1], sign * im[n - 1][n - 1]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:1 + 2 * n * n]
    re = [values[2 * n * i:2 * n * (i + 1):2] for i in range(n)]
    im = [values[2 * n * i + 1:2 * n * (i + 1):2] for i in range(n)]
    pr, pi = data[1 + 2 * n * n], data[2 + 2 * n * n]
    print(*remainder(*determinant(re, im), pr, pi))


main()
