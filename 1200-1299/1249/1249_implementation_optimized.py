import sys


def main():
    read = sys.stdin.buffer.readline
    n, _ = map(int, read().split())
    previous = 0
    for _ in range(n):
        current = int(read().translate(None, b" \t\r\n"), 2)
        both, single = previous & current, previous ^ current
        # Three dark cells mean a vertically full column next to a column
        # with exactly one dark cell. Bit shifts check both orders at once.
        if (both & (single >> 1)) | (single & (both >> 1)):
            print("No")
            return
        previous = current
    print("Yes")


main()
