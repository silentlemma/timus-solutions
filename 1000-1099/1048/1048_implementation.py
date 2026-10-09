import sys

ZERO = ord("0")
BASE = 10


def main():
    data = sys.stdin.buffer.read()
    first = data[: data.index(b"\n")].strip()
    n = int(first)
    # all digits in one bytes object: N, then a1 b1 a2 b2 ...; no per-digit
    # objects, which keeps the memory small
    digits = data.translate(None, b" \t\r\n")
    del data
    start = len(first)
    a, b = digits[start : start + 2 * n : 2], digits[start + 1 : start + 2 * n : 2]
    del digits
    out = bytearray(n + 1)
    out[n] = ord("\n")
    carry = 0
    for i in range(n - 1, -1, -1):
        t = a[i] + b[i] - 2 * ZERO + carry
        carry = 1 if t >= BASE else 0
        out[i] = ZERO + t - BASE * carry
    sys.stdout.buffer.write(out)


main()
