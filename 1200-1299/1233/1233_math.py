import sys


def solve(k, m):
    digits = str(k)
    # numbers not longer than k that come no later than k: for each length,
    # those from 10^(l-1) up to the first l digits of k; any N >= k has them
    before = sum(int(digits[:size]) - 10 ** (size - 1) + 1 for size in range(1, len(digits) + 1))
    if m < before:
        return 0
    # each further number before k is longer than k: of length l it lies in
    # [10^(l-1), k * 10^(l-len(k))), and N is the (m - before)-th of them
    need, low, top = m - before, 10 ** len(digits), k * 10
    if need == 0:
        return k
    while top > low:
        if top - low >= need:
            return low + need - 1
        need -= top - low
        low, top = low * 10, top * 10
    # k is a power of ten, and no longer number comes before it
    return 0


def main():
    k, m = map(int, sys.stdin.read().split())
    print(solve(k, m))


main()
