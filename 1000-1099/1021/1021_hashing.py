import sys

TARGET = 10000


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n1 = data[0]
    first = data[1 : 1 + n1]
    second = data[2 + n1 : 2 + n1 + data[1 + n1]]
    # a pair exists exactly when some TARGET - b of the second list is in the first
    wanted = {TARGET - b for b in second}
    print("YES" if wanted.intersection(first) else "NO")


main()
