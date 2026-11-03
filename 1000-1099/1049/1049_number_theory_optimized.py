from sys import stdin, stdout

BASE = 10
FIRST_ODD_PRIME = 3

exponent = {}
for value in map(int, stdin.read().split()):
    # Remove the complete power of two in one integer operation.
    twos = (value & -value).bit_length() - 1
    if twos:
        exponent[2] = exponent.get(2, 0) + twos
        value >>= twos
    prime = FIRST_ODD_PRIME
    while prime * prime <= value:
        power = 0
        while value % prime == 0:
            power += 1
            value //= prime
        if power:
            exponent[prime] = exponent.get(prime, 0) + power
        prime += 2
    if value > 1:
        exponent[value] = exponent.get(value, 0) + 1
answer = 1
for power in exponent.values():
    answer = answer * (power + 1) % BASE
stdout.write(str(answer))
