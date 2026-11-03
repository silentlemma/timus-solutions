import sys


def main():
    values = map(int, sys.stdin.buffer)
    n = next(values)
    previous = next(values)
    best, left = -1, 1
    # A chord slope is the mean of its consecutive step slopes.
    for right in range(2, n + 1):
        current = next(values)
        difference = abs(current - previous)
        if difference > best:
            best, left = difference, right - 1
        previous = current
    print(left, left + 1)


main()
