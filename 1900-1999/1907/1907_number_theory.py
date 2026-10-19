import sys

FIRST_ODD_PRIME = 3


def count_sizes(first, limit):
    odd_part = first
    while odd_part % 2 == 0:
        odd_part //= 2
    primes = []
    divisor = FIRST_ODD_PRIME
    while divisor * divisor <= odd_part:
        if odd_part % divisor == 0:
            primes.append(divisor)
            while odd_part % divisor == 0:
                odd_part //= divisor
        divisor += 2
    if odd_part > 1:
        primes.append(odd_part)
    odd_only = first % 2 == 0

    def coprime_count(bound, index):
        if bound == 0:
            return 0
        if index == len(primes):
            return (bound + 1) // 2 if odd_only else bound
        return coprime_count(bound, index + 1) - coprime_count(
            bound // primes[index], index + 1
        )

    bad = coprime_count(limit if odd_only else limit // 2, 0)
    return limit - bad


def main():
    first, limit = map(int, sys.stdin.buffer.read().split())
    print(count_sizes(first, limit))


if __name__ == "__main__":
    main()
