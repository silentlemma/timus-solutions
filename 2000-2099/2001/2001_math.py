import sys


def solve(first, second, empty_first, empty_second):
    return first - empty_first, second - empty_second


def main():
    a1, b1, _, b2, a3, _ = map(int, sys.stdin.buffer.read().split())
    print(*solve(a1, b1, a3, b2))


if __name__ == "__main__":
    main()
