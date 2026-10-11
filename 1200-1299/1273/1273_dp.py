import sys


def main():
    nums = map(int, sys.stdin.read().split())
    k = next(nums)
    sleepers = sorted((next(nums), next(nums)) for _ in range(k))
    # two sleepers cross when their ends come in opposite orders, so the
    # kept ones form an increasing run of right ends
    longest = [1] * k
    for i in range(k):
        for j in range(i):
            if sleepers[j][1] < sleepers[i][1]:
                longest[i] = max(longest[i], longest[j] + 1)
    print(k - max(longest, default=0))


main()
