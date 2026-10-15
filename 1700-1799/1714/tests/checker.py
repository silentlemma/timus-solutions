"""Checker: a word of n letters a and b that needs as many palindromes
as the expected one, counted by the usual dynamic programming."""

import sys


class Bad(Exception):
    pass


def palindromes(s):
    # least number of palindromes that s splits into
    n = len(s)
    best = [0] + [n] * n
    # the starts of the palindromes ending at each position, from every center
    ends = [[] for _ in range(n + 1)]
    for center in range(2 * n - 1):
        lo, hi = center // 2, (center + 1) // 2
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            ends[hi + 1].append(lo)
            lo -= 1
            hi += 1
    for j in range(1, n + 1):
        best[j] = min(best[i] + 1 for i in ends[j])
    return best[n]


def check(source, expected, output):
    n = int(open(source).read())
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if len(got) != 1 or len(got[0]) != n or set(got[0]) - set("ab"):
        raise Bad("expected one word of %d letters a and b" % n)
    need, have = palindromes(want), palindromes(got[0])
    if have != need:
        raise Bad("the word needs %d palindromes, the best needs %d" % (have, need))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
