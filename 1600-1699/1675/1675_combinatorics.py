import sys

MOD = 10 ** 9 + 7


def main():
    m, n, k, l = (int(w) for w in sys.stdin.read().split())
    top = max(m, n)
    fact = [1] * (top + 1)
    for i in range(1, top + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (top + 1)
    inv[top] = pow(fact[top], MOD - 2, MOD)
    for i in range(top, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def choose(a, b):
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD

    # the other a x b cells must leave no row and no column empty. With j of
    # the b columns forced empty, each of the a rows is any nonzero pattern
    # on the rest; inclusion-exclusion over j, along the shorter side
    a, b = m - k, n - l
    if a > b:
        a, b = b, a
    rest = 0
    for j in range(a + 1):
        term = choose(a, j) * pow(pow(2, a - j, MOD) - 1, b, MOD)
        rest += -term if j % 2 else term
    print(choose(m, k) * choose(n, l) % MOD * (rest % MOD) % MOD)


main()
