from math import gcd

EPS = 1e-9  # keeps an exact integer whole; no expectation lies that close below one


def main():
    n = int(input())
    # dp[s][l]: the chance that a random permutation of s elements has only
    # cycles of the lengths seen so far, and that their lcm is l
    dp = [dict() for _ in range(n + 1)]
    dp[0][1] = 1.0
    for k in range(1, n + 1):
        new = [dict(d) for d in dp]
        for s in range(n):
            for lcm, w in dp[s].items():
                joined = lcm * k // gcd(lcm, k)
                weight, m = w, 1
                while s + m * k <= n:
                    weight /= k * m  # m cycles of length k: 1 / (k^m m!)
                    cell = new[s + m * k]
                    cell[joined] = cell.get(joined, 0.0) + weight
                    m += 1
        dp = new
    expected = sum(lcm * w for lcm, w in dp[n].items())
    print(int(expected + EPS))


main()
