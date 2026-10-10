import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    gap, intervals = data[0], data[2:]
    # at a stop with trams every k minutes the officer, arriving gap
    # minutes after the thief, leaves at best gap - gap % k minutes later,
    # and a gap below k means the thief may still be waiting there
    for k in intervals:
        gap -= gap % k
        if gap == 0:
            print("YES")
            return
    print("NO")


main()
