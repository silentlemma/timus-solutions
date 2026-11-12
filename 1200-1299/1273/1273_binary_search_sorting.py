from bisect import bisect_left
import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    sleepers = sorted((next(data), next(data)) for _ in range(n))
    tails = []
    for _, right in sleepers:
        # Replace the least feasible tail, or extend the increasing subsequence.
        at = bisect_left(tails, right)
        if at == len(tails):
            tails.append(right)
        else:
            tails[at] = right
    print(n - len(tails))


main()
