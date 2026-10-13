import sys


def main():
    n = int(sys.stdin.read())
    # each number of dots v sits on n + 2 ends: on the tiles v-w for every w,
    # and twice on the double v-v; so the dots add up to (n + 2) * (0 + ... + n)
    print((n + 2) * n * (n + 1) // 2)


main()
