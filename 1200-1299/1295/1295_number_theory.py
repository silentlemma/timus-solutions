MOD = 100
BASES = 4
TEN = 10


def main():
    n = int(input())
    # from the second power on the sum is even but never divisible by 8,
    # so it ends in at most two zeros and its remainder mod 100 decides
    s = sum(pow(b, n, MOD) for b in range(1, BASES + 1)) % MOD
    print(2 if s == 0 else 1 if s % TEN == 0 else 0)


main()
