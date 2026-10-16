import sys


def main():
    n = int(sys.stdin.read())
    if n == 2:
        touches = [1, 1]
    else:
        # sweep 2..n-1 and back: the first pass catches one parity of the
        # start, the second pass the other
        touches = list(range(2, n)) + list(range(n - 1, 1, -1))
    print(len(touches))
    print(*touches)


main()
