import math

# Lagrange: every number is a sum of four squares, and Legendre: exactly the
# numbers 4^a (8b + 7) need all four
MOST = 4
POWER = 4
MODULUS = 8
REST = 7


def count(n):
    root = math.isqrt(n)
    if root * root == n:
        return 1
    for a in range(1, root + 1):
        b = math.isqrt(n - a * a)
        if b * b == n - a * a:
            return 2
    while n % POWER == 0:
        n //= POWER
    return MOST if n % MODULUS == REST else MOST - 1


print(count(int(input())))
