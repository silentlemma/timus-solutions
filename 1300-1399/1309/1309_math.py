MOD = 9973
DEG_FIVE = 5
DEG_THREE = 3
COEF_X = 3
COEF_Y = 7


def step(x):
    """g(x, y) = y (x^5 - x + 7) + (x^3 + 3x - x^5), as the pair (a, b) of
    the map y -> a y + b modulo 9973; it depends only on x mod 9973."""
    x5, x3 = pow(x, DEG_FIVE, MOD), pow(x, DEG_THREE, MOD)
    return (x5 - x + COEF_Y) % MOD, (x3 + COEF_X * x - x5) % MOD


def main():
    n = int(input())
    whole, rest = divmod(n, MOD)
    # x = 1 .. 9973 compose into one map, the same for every full period
    big_a, big_b = 1, 0
    for x in range(1, MOD + 1):
        a, b = step(x)
        big_a, big_b = a * big_a % MOD, (a * big_b + b) % MOD
    y = 0
    for _ in range(whole):
        y = (big_a * y + big_b) % MOD
    for x in range(1, rest + 1):
        a, b = step(x)
        y = (a * y + b) % MOD
    print(y)


main()
