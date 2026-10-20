import sys

BITS = 20  # every number of the message is below 2^20


def main():
    size = 1 << BITS
    prime = bytearray([1]) * size
    prime[0] = prime[1] = 0
    i = 2
    while i * i < size:
        if prime[i]:
            prime[i * i::i] = bytes(len(range(i * i, size, i)))
        i += 1
    # has[j][x]: some prime below 2^20 has its top j bits equal to x
    has = [None] * (BITS + 1)
    has[BITS] = prime
    for level in range(BITS - 1, -1, -1):
        below = has[level + 1]
        has[level] = bytes(x | y for x, y in zip(below[0::2], below[1::2]))
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for a in map(int, data[1:t + 1]):
        # The smallest key is the smallest a xor p over primes p below 2^20,
        # since a key below 2^20 reaches the prime 2; choose the bits of p
        # from the top, keeping the bit of a whenever some prime allows it.
        prefix = 0
        for bit in range(BITS - 1, -1, -1):
            want = prefix * 2 + (a >> bit & 1)
            prefix = want if has[BITS - bit][want] else want ^ 1
        out.append(a ^ prefix)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
