import sys


def main():
    n = int(sys.stdin.read())
    # derangements: d(1) = 0 and d(k) = k d(k - 1) + (-1)^k
    count = 0
    for k in range(2, n + 1):
        count = k * count + (1 if k % 2 == 0 else -1)
    print(count)


main()
