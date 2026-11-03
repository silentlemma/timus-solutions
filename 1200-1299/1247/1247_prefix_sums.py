import sys


def main():
    read = sys.stdin.buffer.readline
    size, limit = map(int, read().split())
    prefix = 0
    # Total excess equals limit. A negative prefix makes the suffix too
    # heavy; a prefix above limit already is a forbidden segment.
    for _ in range(size):
        prefix += int(read()) - 1
        if not 0 <= prefix <= limit:
            print("NO")
            return
    print("YES")


main()
