import sys

TARGET = 10000
MIN_VALUE = -32768
MAX_VALUE = 32767


def main():
    source = sys.stdin.buffer
    # the complete statement domain needs one byte per possible first-list value.
    present = bytearray(MAX_VALUE - MIN_VALUE + 1)
    n = int(source.readline())
    for _ in range(n):
        present[int(source.readline()) - MIN_VALUE] = 1
    m = int(source.readline())
    found = False
    for _ in range(m):
        wanted = TARGET - int(source.readline())
        if MIN_VALUE <= wanted <= MAX_VALUE and present[wanted - MIN_VALUE]:
            found = True
    print("YES" if found else "NO")


main()
