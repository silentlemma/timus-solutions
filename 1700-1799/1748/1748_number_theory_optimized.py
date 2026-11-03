import sys
from bisect import bisect_left, bisect_right

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
MOST = 64


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    queries = data[1 : data[0] + 1]
    limit = max(queries)
    values, counts = [], []

    def grow(index, cap, value, divisors):
        position = bisect_left(values, value)
        if not position or counts[position - 1] < divisors:
            end = position
            # A smaller value with at least this count dominates later entries.
            while end < len(values) and counts[end] <= divisors:
                end += 1
            values[position:end] = [value]
            counts[position:end] = [divisors]
        if index == len(PRIMES):
            return
        prime = PRIMES[index]
        for exponent in range(1, cap + 1):
            if value > limit // prime:
                break
            value *= prime
            grow(index + 1, exponent, value, divisors * (exponent + 1))

    grow(0, MOST, 1, 1)
    output = []
    for query in queries:
        index = bisect_right(values, query) - 1
        output.append(f"{values[index]} {counts[index]}")
    print("\n".join(output))


main()
