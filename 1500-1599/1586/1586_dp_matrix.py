import sys
from math import isqrt

MOD = 1000000009
LOW = 100
HIGH = 1000
PAIRS = 100
WINDOW = 3


def multiply(left, right):
    columns = list(zip(*right))
    return [[sum(a * b for a, b in zip(row, col)) % MOD for col in columns] for row in left]


def main():
    n = int(sys.stdin.read())
    primes = [p for p in range(LOW, HIGH) if all(p % d for d in range(2, isqrt(p) + 1))]
    if n == WINDOW:
        print(len(primes))
        return
    ways = [0] * PAIRS
    for p in primes:
        ways[p % PAIRS] += 1
    first = [0] * PAIRS
    for p in primes:
        first[p % PAIRS] += ways[p // 10]
    # after four digits, both suffix digits end a prime and must be coprime to ten.
    # derive these digits from the primes rather than storing a transition table.
    endings = {p % 10 for p in primes}
    states = sorted(a * 10 + b for a in endings for b in endings)
    index = {value: i for i, value in enumerate(states)}
    transition = [[0] * len(states) for _ in states]
    for p in primes:
        source, target = p // 10, p % PAIRS
        if source in index and target in index:
            transition[index[source]][index[target]] += 1
    result = [[first[state] for state in states]]
    exponent = n - WINDOW - 1
    # n <= 10000 needs at most fourteen squarings; all arithmetic is exact modulo mod.
    while exponent:
        if exponent % 2:
            result = multiply(result, transition)
        exponent //= 2
        if exponent:
            transition = multiply(transition, transition)
    print(sum(result[0]) % MOD)


main()
