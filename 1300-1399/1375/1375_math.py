import os
from sys import stdout

ROOT_MODULUS = 4
ROOT_RESIDUE = 3


def square_root(value, prime):
    if prime % ROOT_MODULUS == ROOT_RESIDUE:
        return pow(value, (prime + 1) // ROOT_MODULUS, prime)
    odd, shifts = prime - 1, 0
    while odd % 2 == 0:
        odd //= 2
        shifts += 1
    nonresidue = 2
    while pow(nonresidue, (prime - 1) // 2, prime) != prime - 1:
        nonresidue += 1
    factor = pow(nonresidue, odd, prime)
    remainder = pow(value, odd, prime)
    root = pow(value, (odd + 1) // 2, prime)
    # Tonelli-Shanks lowers the power-of-two order until the remainder is one.
    while remainder != 1:
        index, probe = 1, remainder * remainder % prime
        while probe != 1:
            probe = probe * probe % prime
            index += 1
        change = pow(factor, 1 << (shifts - index - 1), prime)
        root = root * change % prime
        factor = change * change % prime
        remainder = remainder * factor % prime
        shifts = index
    return root


value, prime = map(int, open(0, "rb", buffering=0).read().split())
if prime == 2:
    print(0, value % prime)
else:
    for x in range(prime):
        residue = (value - x * x) % prime
        if residue == 0:
            print(x, 0)
            break
        if pow(residue, (prime - 1) // 2, prime) == 1:
            print(x, square_root(residue, prime))
            break

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
