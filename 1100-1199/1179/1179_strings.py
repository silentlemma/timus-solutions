import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# anything that is not a digit acts like a digit too large for every base
WALL = len(DIGITS)
SMALLEST = 2
BYTES = 256


def main():
    table = bytearray([WALL]) * BYTES
    for v, ch in enumerate(DIGITS):
        table[ord(ch)] = v
    text = bytes([WALL]) + sys.stdin.buffer.read().translate(table)
    # a number in base k starts at a digit below k whose left neighbour is
    # k or more: a pair (left, right) with right < left starts one in the
    # bases right + 1 .. left, and such a pair is counted as a substring
    count = [0] * (WALL + 2)
    for left in range(1, WALL + 1):
        for right in range(left):
            seen = text.count(bytes([left, right]))
            if seen:
                count[max(right + 1, SMALLEST)] += seen
                count[left + 1] -= seen
    best_k, best, running = SMALLEST, -1, 0
    for k in range(WALL + 1):
        running += count[k]
        if k >= SMALLEST and running > best:
            best_k, best = k, running
    print(best_k, best)


main()
