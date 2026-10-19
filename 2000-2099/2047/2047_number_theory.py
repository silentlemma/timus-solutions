"""Search the unique divisor-count predecessor graph with a segmented sieve."""

from array import array
from math import isqrt
import sys

MAX_TERM = 300
BLOCK_SIZE = 1 << 16
RING_SIZE = MAX_TERM + 1


def primes_up_to(limit):
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b"\0" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def divisor_block(left, right, primes):
    remaining = list(range(left, right + 1))
    counts = [1] * len(remaining)
    for p in primes:
        if p * p > right:
            break
        for offset in range((-left) % p, len(remaining), p):
            value = remaining[offset]
            exponent = 0
            while value % p == 0:
                value //= p
                exponent += 1
            remaining[offset] = value
            counts[offset] *= exponent + 1
    for offset, value in enumerate(remaining):
        if value > 1:
            counts[offset] *= 2
    return counts


def solve(n):
    limit = MAX_TERM * n
    primes = primes_up_to(isqrt(limit))
    history = array("H")
    depth = [0] * RING_SIZE
    for left in range(1, limit + 1, BLOCK_SIZE):
        right = min(limit, left + BLOCK_SIZE - 1)
        counts = divisor_block(left, right, primes)
        for offset, term in enumerate(counts):
            history.append(term)
            total = left + offset
            current = int(total <= MAX_TERM)
            if term <= MAX_TERM and total > term:
                previous = depth[(total - term) % RING_SIZE]
                if previous:
                    current = max(current, previous + 1)
            depth[total % RING_SIZE] = current
            if current >= n:
                answer = []
                for _ in range(n - 1):
                    term = history[total - 1]
                    answer.append(term)
                    total -= term
                answer.append(total)
                answer.reverse()
                return answer
    return None


def main():
    answer = solve(int(sys.stdin.buffer.read()))
    print("Impossible" if answer is None else " ".join(map(str, answer)))


if __name__ == "__main__":
    main()
