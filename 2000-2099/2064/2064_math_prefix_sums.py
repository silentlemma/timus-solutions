import sys
from array import array

CAP = 10 ** 6  # the largest moment; taller caterpillars act alike
# small pieces of input and output stay in the young generation of the PyPy GC
CHUNK = 1 << 12
LINES = 1 << 10
ZERO = ord("0")


def tokens():
    # the input holds up to 2 * 10^6 numbers: they are parsed digit by digit from
    # chunks, so no string per number is created and the memory stays small
    stream = sys.stdin.buffer
    value, inside = 0, False
    while True:
        chunk = stream.read(CHUNK)
        if not chunk:
            break
        for b in chunk:
            if b >= ZERO:
                value = value * 10 + b - ZERO
                inside = True
            elif inside:
                yield value
                value, inside = 0, False
    if inside:
        yield value


def main():
    read = tokens()
    n = next(read)
    present = bytearray(CAP + 1)
    for _ in range(n):
        present[min(next(read), CAP)] = 1
    q = next(read)
    x = array("i", [0]) * q
    for i in range(q):
        x[i] = next(read)
    most = max(x)
    limit = 2 * most
    # tent of height t at every odd multiple of t; the envelope of all tents
    # is the answer, and centres beyond 2 * most never matter. Taller tents
    # come later, so plain assignment keeps the maximum
    height = array("i", [0]) * (limit + 1)
    for t in range(1, CAP + 1):
        if not present[t]:
            continue
        if t >= most:
            height[most] = most
            break
        for c in range(t, limit + 1, 2 * t):
            height[c] = t
    # best[x] = max over c of height[c] - |x - c|, by two sweeps
    for i in range(1, limit + 1):
        h = height[i - 1] - 1
        if h > height[i]:
            height[i] = h
    for i in range(limit - 1, -1, -1):
        h = height[i + 1] - 1
        if h > height[i]:
            height[i] = h
    out = sys.stdout
    for start in range(0, q, LINES):
        out.write("\n".join([str(height[v]) for v in x[start:start + LINES]]) + "\n")


main()
