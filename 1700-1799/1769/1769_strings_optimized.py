import sys

BASE = 10
DIGITS = 6
ZERO = ord("0")


def main():
    text = sys.stdin.buffer.readline().strip()
    first = 1
    # All shorter positive numbers are present before the next length is tried.
    for length in range(1, DIGITS + 1):
        count = (BASE - 1) * first
        seen = bytearray(count)
        value, modulus = 0, first * BASE
        for i, digit in enumerate(text):
            value = (value * BASE + digit - ZERO) % modulus
            if i + 1 >= length and value >= first:
                seen[value - first] = 1
        missing = seen.find(0)
        if missing != -1:
            print(first + missing)
            return
        first *= BASE


main()
