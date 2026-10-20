import sys

MOD = 1_000_000_007
SIEVE_LIMIT = 100_000
BLOCK_SIZE = 8
PAIR_GAP = BLOCK_SIZE - 1
SECOND_SHIFT = 6
THIRD_SHIFT = 10
FOURTH_SHIFT = 12
INNER_SUM = THIRD_SHIFT + FOURTH_SHIFT


def totient_sums(n):
    limit = min(n, SIEVE_LIMIT)
    small = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if small[prime] == prime:
            for multiple in range(prime, limit + 1, prime):
                small[multiple] -= small[multiple] // prime
    for i in range(1, limit + 1):
        small[i] += small[i - 1]
    count = n // (limit + 1)
    large = [0] * (count + 1)
    # Smaller quotient arguments have already been computed.
    for index in range(count, 0, -1):
        x = n // index
        total = x * (x + 1) // 2
        left = 2
        while left <= x:
            quotient = x // left
            right = x // quotient
            value = small[quotient] if quotient <= limit else large[n // quotient]
            total -= (right - left + 1) * value
            left = right + 1
        large[index] = total
    return limit, small, large


def main():
    n = int(sys.stdin.buffer.read())
    limit, small, large = totient_sums(n)
    modulus = MOD
    factorial = 1
    weighted = previous = total = 0
    left = 1
    while left <= n:
        quotient = n // left
        right = n // quotient
        stop = right + 1 - (right - left + 1) % BLOCK_SIZE
        # Pair eight consecutive factors; differentiate their product to update weighted.
        for i in range(left, stop, BLOCK_SIZE):
            x = i * (i + PAIR_GAP)
            outer = x * (x + SECOND_SHIFT)
            inner = (x + THIRD_SHIFT) * (x + FOURTH_SHIFT)
            product = outer * inner
            derivative = ((2 * x + SECOND_SHIFT) * inner + outer * (2 * x + INNER_SUM)) * (
                2 * i + PAIR_GAP
            )
            weighted = (weighted * product + factorial * derivative) % modulus
            factorial = factorial * product % modulus
        for i in range(stop, right + 1):
            weighted = (weighted * i + factorial) % modulus
            factorial = factorial * i % modulus
        harmonic = weighted * pow(factorial, modulus - 2, modulus) % modulus
        count = small[quotient] if quotient <= limit else large[n // quotient]
        total = (total + (harmonic - previous) * count) % modulus
        previous = harmonic
        left = right + 1
    pairs = n * (n + 1) // 2 % modulus
    print(total * pow(pairs, modulus - 2, modulus) % modulus)


if __name__ == "__main__":
    main()
