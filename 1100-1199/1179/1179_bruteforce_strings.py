import sys

DIGITS = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SMALLEST = 2
BYTES = 256


def main():
    text = b" " + sys.stdin.buffer.read()
    table = bytearray(BYTES)
    table[DIGITS[0]] = 1
    best_base, best = SMALLEST, -1
    for base in range(SMALLEST, len(DIGITS) + 1):
        table[DIGITS[base - 1]] = 1
        # For this base, 0 means separator and 1 means digit: 01 starts a number.
        count = text.translate(table).count(b"\0\1")
        if count > best:
            best_base, best = base, count
    print(best_base, best)


main()
