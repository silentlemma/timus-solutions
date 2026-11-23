import os
import sys

BITS = 20  # every number of the message is below 2^20
LOW_BITS = 4
BLOCK = 1 << LOW_BITS


def build_tables():
    size = 1 << BITS
    prime = bytearray([1]) * size
    prime[0] = prime[1] = 0
    divisor = 2
    while divisor * divisor < size:
        if prime[divisor]:
            prime[divisor * divisor :: divisor] = bytes(
                len(range(divisor * divisor, size, divisor))
            )
        divisor += 1
    patterns = {}
    for mask in range(256):
        positions = [2 * bit + 1 for bit in range(8) if mask >> bit & 1]
        pattern = bytes(mask >> bit & 1 for bit in range(8))
        patterns[pattern] = bytes(
            min((offset ^ p for p in positions), default=255) for offset in range(BLOCK)
        )
    odd = bytes(prime[1::2])
    near = bytearray(size)
    occupied = bytearray(size // BLOCK)
    for block, start in enumerate(range(0, len(odd), 8)):
        table = patterns[odd[start : start + 8]]
        near[block * BLOCK : (block + 1) * BLOCK] = table
        occupied[block] = table[0] != 255
    first = [p for p in range(BLOCK) if prime[p]]
    near[:BLOCK] = bytes(min(offset ^ p for p in first) for offset in range(BLOCK))
    occupied[0] = 1
    # has[j][x]: some prime below 2^20 has its top j bits equal to x
    upper = BITS - LOW_BITS
    has = [None] * (upper + 1)
    has[upper] = occupied
    for level in range(upper - 1, -1, -1):
        below = has[level + 1]
        has[level] = bytes(x | y for x, y in zip(below[0::2], below[1::2]))
    return near, has


def key_for(value, near, has):
    direct = near[value]
    if direct != 255:
        return direct
    # The smallest key is the smallest a xor p over primes p below 2^20,
    # since a key below 2^20 reaches the prime 2; choose the bits of p
    # from the top, keeping the bit of a whenever some prime allows it.
    prefix = 0
    upper = BITS - LOW_BITS
    high = value >> LOW_BITS
    for bit in range(upper - 1, -1, -1):
        want = prefix * 2 + (high >> bit & 1)
        prefix = want if has[upper - bit][want] else want ^ 1
    return ((high ^ prefix) << LOW_BITS) | near[prefix * BLOCK + (value & (BLOCK - 1))]


def main():
    near, has = build_tables()
    values = map(int, sys.stdin.buffer.read().split())
    count = next(values)
    sys.stdout.write("\n".join(str(key_for(next(values), near, has)) for _ in range(count)) + "\n")


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
