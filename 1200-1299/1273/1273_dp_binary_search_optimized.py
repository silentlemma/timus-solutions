from os import _exit as _finish_process
import sys as _finish_sys
from bisect import bisect_left
import sys


def main():
    nums = map(int, sys.stdin.read().split())
    k = next(nums)
    sleepers = sorted((next(nums), next(nums)) for _ in range(k))
    # two sleepers cross when their ends come in opposite orders, so the
    # kept ones form an increasing run of right ends
    tails = []
    for _, right in sleepers:
        index = bisect_left(tails, right)
        if index == len(tails):
            tails.append(right)
        else:
            tails[index] = right
    print(k - len(tails))


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
