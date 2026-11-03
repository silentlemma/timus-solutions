import sys
from itertools import chain

BYTE_BITS = 8
BUFFER_SIZE = 65536
HEADER_FIELDS = 3


def token_blocks():
    read = sys.stdin.buffer.read
    tail = b""
    while True:
        block = read(BUFFER_SIZE)
        if not block:
            break
        fields = (tail + block).split()
        # A chunk may end inside an integer; keep only that unfinished token.
        tail = fields.pop() if block[-1] > ord(" ") else b""
        yield fields
        del fields
    if tail:
        yield [tail]


def main():
    blocks = token_blocks()
    header = []
    for fields in blocks:
        taken = min(HEADER_FIELDS - len(header), len(fields))
        header.extend(map(int, fields[:taken]))
        fields = fields[taken:]
        if len(header) == HEADER_FIELDS:
            break
    else:
        return
    m, n, edges = header
    left, right = min(m, n), max(m, n)
    row_bytes = (right + BYTE_BITS - 1) // BYTE_BITS
    rows = [bytearray(row_bytes) for _ in range(left)]
    pending = None
    for fields in chain([fields], blocks):
        if pending is not None:
            fields.insert(0, pending)
            pending = None
        # Chunk boundaries can split a pair as well as an integer.
        if len(fields) % 2:
            pending = fields.pop()
        values = map(int, fields)
        if m <= n:
            for a, b in zip(values, values):
                b -= 1
                rows[a - 1][b // BYTE_BITS] |= 1 << (b % BYTE_BITS)
        else:
            for a, b in zip(values, values):
                a -= 1
                rows[b - 1][a // BYTE_BITS] |= 1 << (a % BYTE_BITS)
    del fields, blocks
    adjacent = [int.from_bytes(row, "little") for row in rows]
    del rows
    match_l, match_r = [-1] * left, [-1] * right
    parent = [0] * right
    free = (1 << right) - 1
    size = 0
    for root in range(left):
        queue = [root]
        seen = 0
        target = -1
        for v in queue:
            available = adjacent[v] & free
            if available:
                target = (available & -available).bit_length() - 1
                parent[target] = v
                break
            # Only matched right vertices remain. Each is visited once,
            # and its unique matched left vertex extends the BFS tree.
            options = adjacent[v] & ~seen
            seen |= options
            while options:
                bit = options & -options
                u = bit.bit_length() - 1
                parent[u] = v
                queue.append(match_r[u])
                options ^= bit
        if target >= 0:
            free ^= 1 << target
            # Parent links follow the old matching back to the free root.
            while target >= 0:
                v = parent[target]
                old = match_l[v]
                match_l[v], match_r[target] = target, v
                target = old
            size += 1
    print(m + n - size)


main()
