import sys


def main():
    k, n, *cars = map(int, sys.stdin.read().split())
    jam = 0
    for count in cars[:n]:
        # the light lets k cars through, but never more than are waiting
        jam = max(0, jam + count - k)
    print(jam)


main()
