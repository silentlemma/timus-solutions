import sys


def main():
    n = int(sys.stdin.read())
    out = []
    for k in range(n):
        # kids take the first free horse at or after a random one: linear
        # probing on a circle of n slots with k taken. By Knuth's analysis
        # the wait is (Q - 1)/2 with Q = sum (j + 1) k!/(k - j)! / n^j
        q, term = 0.0, 1.0
        for j in range(k + 1):
            q += (j + 1) * term
            term *= (k - j) / n
        out.append("%.9f" % ((q - 1) / 2))
    print("\n".join(out))


main()
