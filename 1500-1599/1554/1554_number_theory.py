import sys

MOD = 2007


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    f = [0] + [x % MOD for x in data[1 : n + 1]]
    # (F * G)(n) sums F(n / d) G(d) over the divisors d of n and is 0 for n > 1,
    # so G(n) = -G(1) * (the sum over the proper divisors), with G(1) = 1 / F(1),
    # and a sieve adds G(d) times F to every multiple of d once G(d) is known
    first = pow(f[1], -1, MOD)
    g = [0] * (n + 1)
    acc = [0] * (n + 1)
    for d in range(1, n + 1):
        g[d] = first if d == 1 else -first * acc[d] % MOD
        for k in range(2, n // d + 1):
            acc[d * k] += f[k] * g[d]
    print(" ".join(map(str, g[1:])))


main()
