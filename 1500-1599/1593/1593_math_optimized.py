from math import gcd, isqrt


BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
BATCH = 64
MAX_CYCLE = 1 << 16


def prime(n):
    for p in BASES:
        if n % p == 0:
            return n == p
    odd = n - 1
    twos = (odd & -odd).bit_length() - 1
    odd >>= twos
    for a in BASES:
        value = pow(a, odd, n)
        if value in (1, n - 1):
            continue
        for _ in range(twos - 1):
            value = value * value % n
            if value == n - 1:
                break
        else:
            return False
    return True


def divisor(n):
    c = 1
    while True:
        y, size, factor = 2, 1, 1
        while size <= MAX_CYCLE and factor == 1:
            x = y
            for _ in range(size):
                y = (y * y + c) % n
            for start in range(0, size, BATCH):
                saved, product = y, 1
                for _ in range(min(BATCH, size - start)):
                    y = (y * y + c) % n
                    product = product * abs(x - y) % n
                factor = gcd(product, n)
                if factor != 1:
                    break
            size *= 2
        if factor == n:
            while True:
                saved = (saved * saved + c) % n
                factor = gcd(abs(x - saved), n)
                if factor != 1:
                    break
        if 1 < factor < n:
            return factor
        c += 1


POWER_OF_FOUR = 4
LEGENDRE_MODULUS = 8
LEGENDRE_RESIDUE = 7
TWO_SQUARE_OBSTRUCTION = 3
THREE_SQUARES = 3
FOUR_SQUARES = 4


def collect(n, odd_factors):
    if isqrt(n) ** 2 == n:
        return
    if prime(n):
        if n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION:
            odd_factors.symmetric_difference_update((n,))
        return
    part = divisor(n)
    collect(part, odd_factors)
    collect(n // part, odd_factors)


def solve(n):
    if isqrt(n) ** 2 == n:
        return 1
    while n % POWER_OF_FOUR == 0:
        n //= POWER_OF_FOUR
    if n % LEGENDRE_MODULUS == LEGENDRE_RESIDUE:
        return FOUR_SQUARES
    if n % 2 == 0:
        n //= 2
    if n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION:
        return THREE_SQUARES

    for p in BASES[1:]:
        odd = False
        while n % p == 0:
            n //= p
            odd = not odd
        if odd and p % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION:
            return THREE_SQUARES
    odd_factors = set()
    collect(n, odd_factors)
    return THREE_SQUARES if odd_factors else 2


if __name__ == "__main__":
    print(solve(int(input())))
