import sys

MAX_BASE = 36
BYTE_VALUES = 256
CHUNK_SIZE = 65536
DIGITS = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    table = bytearray(BYTE_VALUES)
    for value, symbol in enumerate(DIGITS):
        table[symbol] = value
    # whitespace maps to zero, so it changes neither the sum nor the maximum
    table = bytes(table)
    total, top = 0, 1
    while True:
        chunk = sys.stdin.buffer.read(CHUNK_SIZE)
        if not chunk:
            break
        digits = chunk.translate(table)
        total += sum(digits)
        top = max(top, max(digits))
    # base is 1 modulo base - 1, so the number is congruent to its digit sum
    for base in range(top + 1, MAX_BASE + 1):
        if total % (base - 1) == 0:
            print(base)
            return
    print("No solution.")


main()
