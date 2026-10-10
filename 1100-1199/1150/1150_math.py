DIGITS = 10


def main():
    n = int(input())
    count = [0] * DIGITS
    p = 1
    while p <= n:
        # at this position the numbers up to n split into the part above, the
        # digit itself and the part below; every smaller upper part repeats
        # each digit p times here
        high, cur, low = n // (p * DIGITS), n // p % DIGITS, n % p
        for d in range(1, DIGITS):
            count[d] += high * p + (p if d < cur else low + 1 if d == cur else 0)
        # a zero needs a nonzero digit above it, so the upper part 0 is skipped
        if high:
            count[0] += (high - 1) * p + (p if cur else low + 1)
        p *= DIGITS
    print("\n".join(map(str, count)))


main()
