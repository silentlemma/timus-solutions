"""Checker: a split point 1 <= i < n and the length of the local root
there, which must be the largest over all points. By the critical
factorization theorem that largest length is the period of the word, so
the length must equal the period and no shorter repetition may fit
around point i; repetitions are compared by polynomial hashes."""

import sys

MOD = (1 << 61) - 1
BASE = 131


class Bad(Exception):
    pass


def check(source, expected, output):
    w = open(source).read().split()[0]
    n = len(w)
    got = open(output).read().split()
    if len(got) != 2 or not all(v.isdigit() for v in got):
        raise Bad("expected two numbers")
    split, length = int(got[0]), int(got[1])
    if not 1 <= split < n:
        raise Bad("split point %d is outside 1..%d" % (split, n - 1))
    border = [0] * n
    k = 0
    for i in range(1, n):
        while k and w[k] != w[i]:
            k = border[k - 1]
        if w[k] == w[i]:
            k += 1
        border[i] = k
    period = n - border[n - 1]
    if length != period:
        raise Bad("the largest local root has length %d, not %d" % (period, length))
    prefix = [0] * (n + 1)
    power = [1] * (n + 1)
    for i, c in enumerate(w):
        prefix[i + 1] = (prefix[i] * BASE + ord(c)) % MOD
        power[i + 1] = power[i] * BASE % MOD

    def piece(lo, hi):
        return (prefix[hi] - prefix[lo] * power[hi - lo]) % MOD

    for r in range(1, period):
        lo, hi = max(0, split - r), min(split, n - r)
        if piece(lo, hi) == piece(lo + r, hi + r):
            raise Bad("a root of length %d fits at point %d" % (r, split))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
