import sys
from array import array
from math import prod

BLOCK = 256
INDEX_BITS = 14
INDEX_MASK = (1 << INDEX_BITS) - 1
CACHE_SLOTS = 64
CACHE_MASK = CACHE_SLOTS - 1


def main():
    values = map(int, sys.stdin.buffer.read().split())
    queries = array("Q")
    largest = 0
    for n, p in zip(values, values):
        if n == p == 0:
            break
        # n<2^14 and p<2^31: a complete query fits in one45-bit value.
        queries.append((p << INDEX_BITS) | n)
        if n < p:
            largest = max(largest, n)
    del values
    exact = [1]
    value = 1
    for boundary in range(BLOCK, largest + 1, BLOCK):
        # One block product avoids retaining every growing intermediate n!.
        value *= prod(range(boundary - BLOCK + 1, boundary + 1))
        exact.append(value)
    cache_n = [-1] * CACHE_SLOTS
    cache_tail = [1] * CACHE_SLOTS
    output = bytearray()
    for query in queries:
        n, p = query & INDEX_MASK, query >> INDEX_BITS
        if n >= p:
            output.extend(b"0\n")
            continue
        block = n // BLOCK
        slot = n & CACHE_MASK
        # A bounded direct-mapped cache checks the key before reusing its product.
        if cache_n[slot] != n:
            cache_n[slot] = n
            cache_tail[slot] = prod(range(block * BLOCK + 1, n + 1))
        answer = (exact[block] % p) * (cache_tail[slot] % p) % p
        output.extend(str(answer).encode())
        output.extend(b"\n")
    sys.stdout.buffer.write(output)


main()
