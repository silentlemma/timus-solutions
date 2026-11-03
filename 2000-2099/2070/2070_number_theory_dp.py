from math import isqrt

FOURTH_ROOT_LIMIT = 1000
FIRST_HIGHER_EXPONENT = 4


def prime_count(n):
    if n < 2:
        return 0
    root = isqrt(n)
    small = [max(0, value - 1) for value in range(root + 1)]
    large = [0] + [n // i - 1 for i in range(1, root + 1)]
    for prime in range(2, root + 1):
        if small[prime] == small[prime - 1]:
            continue
        before = small[prime - 1]
        square = prime * prime
        # g(v) counts survivors after smaller primes. Remove the multiples
        # of this prime whose remaining factor is at least prime.
        for i in range(1, min(root, n // square) + 1):
            reduced = n // i // prime
            count = small[reduced] if reduced <= root else large[n // reduced]
            large[i] -= count - before
        # Descending values preserve the previous-prime layer in both arrays.
        for value in range(root, square - 1, -1):
            small[value] -= small[value // prime] - before
    return large[1]


def solve(left, right):
    bad = prime_count(isqrt(right)) - prime_count(isqrt(left - 1))
    composite = bytearray(FOURTH_ROOT_LIMIT + 1)
    composite[0] = composite[1] = 1
    for prime in range(2, isqrt(FOURTH_ROOT_LIMIT) + 1):
        if not composite[prime]:
            for multiple in range(prime * prime, FOURTH_ROOT_LIMIT + 1, prime):
                composite[multiple] = 1
    # k+1 prime and k>=2 implies even k. Squares are counted above.
    # every remaining base has p^4<=R, hence p<=1000 under the limits.
    for prime in range(2, FOURTH_ROOT_LIMIT + 1):
        if composite[prime]:
            continue
        square = prime * prime
        power, exponent = square * square, FIRST_HIGHER_EXPONENT
        if power > right:
            break
        while power <= right:
            if power >= left and not composite[exponent + 1]:
                bad += 1
            power *= square
            exponent += 2
    return right - left + 1 - bad


def main():
    left, right = map(int, input().split())
    print(solve(left, right))


main()
