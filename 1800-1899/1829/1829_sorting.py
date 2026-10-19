import sys

BITS = 32
FULL = (1 << BITS) - 1


def address(text):
    return int.from_bytes(bytes(map(int, text.split(b"."))), "big")


def pieces(rows):
    # each row covers one aligned block of addresses, and two blocks are
    # nested or apart; sweeping them by start, larger first, with a stack
    # of open blocks cuts the line into pieces routed by the innermost one
    blocks = sorted(((d & m, (d & m) | (FULL ^ m), g) for d, m, g in rows),
                    key=lambda b: (b[0], -b[1]))
    out = []
    stack = []
    pos = 0

    def emit(lo, hi, gate):
        # adjacent pieces with one gateway merge, so equal routing gives
        # equal lists
        if lo > hi:
            return
        if out and out[-1][1] + 1 == lo and out[-1][2] == gate:
            out[-1][1] = hi
        else:
            out.append([lo, hi, gate])

    for lo, hi, gate in blocks + [(FULL + 1, FULL + 1, None)]:
        while stack and stack[-1][1] < lo:
            top = stack.pop()
            emit(pos, top[1], top[2])
            pos = top[1] + 1
        if stack:
            emit(pos, lo - 1, stack[-1][2])
        pos = lo
        stack.append((lo, hi, gate))
    return out


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    tables = []
    for _ in range(2):
        count = int(next(tokens))
        rows = [tuple(address(next(tokens)) for _ in "dmg") for _ in range(count)]
        tables.append(pieces(rows))
    print("YES" if tables[0] == tables[1] else "NO")


main()
