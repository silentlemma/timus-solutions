import sys

MOD = 10**9 + 9
LOW = 100  # the three-digit numbers
HIGH = 1000
PAIRS = 100  # the last two digits
WINDOW = 3  # neighbouring digits that form a prime


def main():
    n = int(sys.stdin.read())
    primes = [p for p in range(LOW, HIGH) if all(p % d for d in range(2, p) if d * d <= p)]
    # ways[t]: numbers of the length so far that end in the two digits t and
    # whose every three neighbouring digits form a three-digit prime
    ways = [0] * PAIRS
    for p in primes:
        ways[p % PAIRS] += 1
    for _ in range(n - WINDOW):
        nxt = [0] * PAIRS
        for p in primes:
            # a prime abc extends a number ending in ab to one ending in bc
            nxt[p % PAIRS] = (nxt[p % PAIRS] + ways[p // 10]) % MOD
        ways = nxt
    print(sum(ways) % MOD)


main()
