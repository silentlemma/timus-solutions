import sys

MOD = 10 ** 9 + 7


def main():
    level = int(sys.stdin.read())
    # the numbers form a perfect binary tree walked by tree distance; each
    # edge counts the nodes below it times the nodes above it, which sums to
    # 2^l ((l - 1)(2^l + 1) - 2 (2^l - 2))
    power = pow(2, level, MOD)
    print(power * ((level - 1) * (power + 1) - 2 * (power - 2)) % MOD)


main()
