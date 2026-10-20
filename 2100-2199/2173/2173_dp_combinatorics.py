import sys

MOD = 10 ** 9 + 7


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    wishes = data[2:2 + n]
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (m + 1)
    inv[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    # ways[j]: the sponsors so far fill exactly j problems once; with t
    # mentions placed, (t - j) / 2 problems hold two sponsors and the rest none
    ways = [0] * (m + 1)
    ways[0] = 1
    placed = 0
    for s in wishes:
        following = [0] * (m + 1)
        for j in range(placed % 2, m + 1, 2):
            count = ways[j]
            if not count:
                continue
            empty = m - j - (placed - j) // 2
            # a of the new mentions go to problems with one sponsor, the
            # other s - a to empty problems
            base = count * fact[j] % MOD * fact[empty] % MOD
            for a in range(max(0, s - empty), min(s, j) + 1):
                rest = s - a
                term = base * inv[a] % MOD * inv[j - a] % MOD
                term = term * inv[rest] % MOD * inv[empty - rest] % MOD
                target = j - a + rest
                following[target] = (following[target] + term) % MOD
        ways = following
        placed += s
    print(sum(ways) % MOD)


main()
