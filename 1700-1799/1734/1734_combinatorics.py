MOD = 10 ** 9 + 7
EDGE_KINDS = 3
MIDDLE_KINDS = 4
ONE_COLOUR_KINDS = 2


def main():
    n, k = map(int, input().split())
    squares = n * n // 2
    row = n // 2
    middle = squares - 2 * row
    fact = [1] * (squares + 1)
    for i in range(1, squares + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (squares + 1)
    inv[squares] = pow(fact[squares], MOD - 2, MOD)
    for i in range(squares, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def choose(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD

    # a dark square on the first or last row takes three kinds of piece
    # (the man that would be crowned there is out), any other square four
    total = 0
    for a in range(min(2 * row, k) + 1):
        total += choose(2 * row, a) * pow(EDGE_KINDS, a, MOD) * \
            choose(middle, k - a) * pow(MIDDLE_KINDS, k - a, MOD)
    # positions of one colour: on its last row only the king, elsewhere
    # the man or the king
    one = 0
    for a in range(min(row, k) + 1):
        one += choose(row, a) * choose(middle + row, k - a) * \
            pow(ONE_COLOUR_KINDS, k - a, MOD)
    print((total - 2 * one) % MOD)


main()
