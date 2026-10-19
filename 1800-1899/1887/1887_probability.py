import sys

PRIME = 11
DIGITS = 10


def main():
    v = list(map(int, sys.stdin.read().split()))
    n = v[0]
    a, b, c = v[1:n + 1], v[n + 1:2 * n + 1], v[2 * n + 1:]
    # ways[r]: choices of the digits so far whose product is r modulo 11
    ways = [0] * PRIME
    ways[1] = 1
    for i in range(n):
        new = [0] * PRIME
        for x in range(DIGITS):
            factor = (a[i] * x * x + b[i] * x + c[i]) % PRIME
            for r in range(PRIME):
                new[r * factor % PRIME] += ways[r]
        ways = new
    count = [0] * DIGITS
    for r in range(PRIME):
        count[r % DIGITS] += ways[r]
    if min(count) == 0:
        print(-1)
        return
    p = [k / DIGITS ** n for k in count]
    # expected draws from the set of digits seen to all ten: a draw of a
    # missing digit moves on, others repeat; the chance to move on is summed
    # directly so that small probabilities keep their precision
    full = (1 << DIGITS) - 1
    expect = [0.0] * (full + 1)
    for mask in range(full - 1, -1, -1):
        missing = [d for d in range(DIGITS) if not mask >> d & 1]
        move = sum(p[d] for d in missing)
        expect[mask] = (1 + sum(p[d] * expect[mask | 1 << d] for d in missing)) / move
    print("%.10f" % expect[0])


main()
