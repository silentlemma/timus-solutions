import sys


def main():
    read = sys.stdin.buffer.readline
    n, _ = map(int, read().split())
    # every dark region is a rectangle exactly when no 2 x 2 window holds
    # three dark cells; each row is a bit mask, read line by line to stay
    # within 4 MB
    prev = None
    for _ in range(n):
        row = int(read().replace(b" ", b"").strip(), 2)
        if prev is not None:
            a, b, c, d = prev, prev >> 1, row, row >> 1
            # three of four bits: an odd count with at least two set
            if (a ^ b ^ c ^ d) & ((a & b) | (c & d) | ((a | b) & (c | d))):
                print("No")
                return
        prev = row
    print("Yes")


main()
