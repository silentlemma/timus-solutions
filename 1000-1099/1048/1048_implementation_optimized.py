import sys

ZERO = ord("0")
BASE = 10


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    out = bytearray(n + 1)
    out[n] = ord("\n")
    # Keep only column sums, not the input and two separate operand arrays.
    for i in range(n):
        a, b = read().split()
        out[i] = a[0] + b[0] - 2 * ZERO
    carry = 0
    for i in range(n - 1, -1, -1):
        value = out[i] + carry
        carry = value // BASE
        out[i] = ZERO + value % BASE
    sys.stdout.buffer.write(out)


main()
