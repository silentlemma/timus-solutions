import sys

PACK_BITS = 18
PACK_BYTES = 9
GROUP_SIZE = 4
SMALL_MATCHES = 2048
MASK_COUNT = 16
BYTE_BITS = 8
LAST_GROUP_BIT = GROUP_SIZE - 1
COEFFICIENT_BYTES = (PACK_BITS + BYTE_BITS - 1) // BYTE_BITS


def match_starts(a, b):
    n, m = len(a), len(b)
    if m > n:
        return []
    # Testing uniform high symbols avoids KMP overhead on the dense worst case.
    high = bytes(v >> 1 for v in b)
    text = bytes(v >> 1 for v in a)
    if high.count(high[:1]) == m and text.count(high[:1]) == n:
        return range(n - m + 1)
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j and high[j] != high[i]:
            j = prefix[j - 1]
        if high[j] == high[i]:
            j += 1
        prefix[i] = j
    starts = []
    j = 0
    for i, value in enumerate(text):
        while j and high[j] != value:
            j = prefix[j - 1]
        if high[j] == value:
            j += 1
        if j == m:
            starts.append(i - m + 1)
            j = prefix[j - 1]
    return starts


TABLE18 = tuple(
    sum(((mask >> j) & 1) << (PACK_BITS * j) for j in range(GROUP_SIZE)).to_bytes(
        PACK_BYTES, "little"
    )
    for mask in range(MASK_COUNT)
)


def pack18(bits):
    n = len(bits)
    bits += bytes((-n) % GROUP_SIZE)
    table = TABLE18
    data = b"".join(
        table[
            bits[i]
            | bits[i + 1] << 1
            | bits[i + 2] << 2
            | bits[i + LAST_GROUP_BIT] << LAST_GROUP_BIT
        ]
        for i in range(0, n, GROUP_SIZE)
    )
    return int.from_bytes(data, "little")


def solve(a, b):
    n, m = len(a), len(b)
    starts = match_starts(a, b)
    if not starts:
        return None
    low = bytes(v & 1 for v in a)
    pattern = bytes(v & 1 for v in b)
    if len(starts) <= SMALL_MATCHES:
        trans = bytes.maketrans(b"\0\1", b"01")
        x = int(low.translate(trans)[::-1], 2)
        y = int(pattern.translate(trans)[::-1], 2)
        mask = (1 << m) - 1
        best, answer = m + 1, -1
        for start in starts:
            changes = (((x >> start) ^ y) & mask).bit_count()
            if changes < best:
                best, answer = changes, start
                if not best:
                    break
        return best, answer + 1
    x, y = pack18(low), pack18(pattern[::-1])
    product = x * y
    width = PACK_BITS
    product = product.to_bytes((width * (n + m - 1) + BYTE_BITS - 1) // BYTE_BITS, "little")
    coefficient_mask = (1 << width) - 1
    ones = sum(low[:m]) + sum(pattern)
    start_index = 0
    best, answer = m + 1, -1
    for start in range(n - m + 1):
        if start == starts[start_index]:
            bit_offset = width * (start + m - 1)
            offset, shift = divmod(bit_offset, BYTE_BITS)
            count = (
                int.from_bytes(product[offset : offset + COEFFICIENT_BYTES], "little") >> shift
            ) & coefficient_mask
            changes = ones - 2 * count
            if changes < best:
                best, answer = changes, start
                if not best:
                    break
            start_index += 1
            if start_index == len(starts):
                break
        if start < n - m:
            ones += low[start + m] - low[start]
    return best, answer + 1


def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    values = bytes(int(token, 2) for token in tokens[2:])
    del tokens
    result = solve(values[:n], values[n:])
    if result is None:
        print("No")
    else:
        print("Yes")
        print(*result)


if __name__ == "__main__":
    main()
