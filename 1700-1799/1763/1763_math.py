MOD = 10**9 + 9
# with six sectors the jumps forward and back by three land on the same
# sector, so that table is counted on its own
SIX = 6
SIX_WAYS = 12
# from seven sectors on the counts follow a linear recurrence of order 19,
# found with the Berlekamp-Massey method from counts made by a search over
# the sectors and checked on every table up to 200 sectors
FIRST_SECTORS = 7
STEPS = [int(v) for v in "1 2 -1 1 -2 -1 -2 -3 3 -1 5 2 2 1 -2 0 -3 0 -1".split()]
FIRST = [int(v) for v in """46 144 110 312 290 670 706 1538 1732 3504 4288 8098
    10568 19044 26042 45222 64220 108382 158324""".split()]


def times(p, q):
    """The product of two polynomials modulo the recurrence's
    characteristic polynomial x^k - sum of STEPS[j] x^(k-1-j)."""
    k = len(STEPS)
    full = [0] * (2 * k - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                full[i + j] = (full[i + j] + a * b) % MOD
    for i in range(2 * k - 2, k - 1, -1):
        if full[i]:
            for j, step in enumerate(STEPS):
                full[i - 1 - j] = (full[i - 1 - j] + full[i] * step) % MOD
    return full[:k]


def main():
    n = int(input())
    if n == SIX:
        print(SIX_WAYS)
        return
    k = len(STEPS)
    # x^(n - 7) reduced by the recurrence gives the count as a mix of the
    # first k counts
    power = [1] + [0] * (k - 1)
    base = [0, 1] + [0] * (k - 2)
    e = n - FIRST_SECTORS
    while e:
        if e & 1:
            power = times(power, base)
        base = times(base, base)
        e >>= 1
    print(sum(a * b for a, b in zip(power, FIRST)) % MOD)


main()
