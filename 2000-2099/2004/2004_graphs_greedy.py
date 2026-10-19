import sys

ZERO = ord("0")
ONE = ord("1")


def solve(order):
    size = 1 << order
    mask = size - 1
    seen = bytearray(size)
    seen[0] = 1
    result = bytearray(b"0" * order)
    append = result.append
    window = 0
    for _ in range(size - 1):
        window = (window << 1) & mask
        if not seen[window | 1]:
            window |= 1
            append(ONE)
        else:
            append(ZERO)
        seen[window] = 1
    return result


if __name__ == "__main__":
    order = int(sys.stdin.buffer.read())
    sys.stdout.buffer.write(solve(order))
    sys.stdout.buffer.write(b"\n")
