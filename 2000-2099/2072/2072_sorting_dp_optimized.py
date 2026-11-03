import sys

POSITION_BITS = 17
POSITION_MASK = (1 << POSITION_BITS) - 1


def main():
    tokens = (int(word) for line in sys.stdin.buffer for word in line.split())
    n = next(tokens)
    # Positions fit17bits; sorting one integer orders by moisture then position.
    flowers = [(next(tokens) << POSITION_BITS) | i for i in range(n)]
    del tokens
    flowers.sort()
    at_left = at_right = 0
    left = right = 0
    i = 0
    while i < n:
        j = i + 1
        value = flowers[i] >> POSITION_BITS
        while j < n and flowers[j] >> POSITION_BITS == value:
            j += 1
        lo, hi = flowers[i] & POSITION_MASK, flowers[j - 1] & POSITION_MASK
        width = hi - lo
        to_left = min(at_left + abs(left - hi), at_right + abs(right - hi)) + width
        to_right = min(at_left + abs(left - lo), at_right + abs(right - lo)) + width
        at_left, at_right, left, right = to_left, to_right, lo, hi
        i = j
    print(min(at_left, at_right) + n)


main()
