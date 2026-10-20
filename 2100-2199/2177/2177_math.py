import sys

MIN_SUM = 3


def longest_chain(first, second):
    if first > second:
        first, second = second, first
    difference = second - first
    if difference == 0:
        return 2
    if difference == 1:
        return second - 1
    if difference == 2:
        if second % 2 == 1:
            return second - 1
        return second // 2
    # A longest chain joins two distinct residue classes modulo the difference.
    return 2 * ((second - MIN_SUM) // difference + 1)


def main():
    first, second = map(int, sys.stdin.buffer.read().split())
    print(longest_chain(first, second))


if __name__ == "__main__":
    main()
