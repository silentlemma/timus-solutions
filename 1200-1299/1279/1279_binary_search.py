import sys


def main():
    nums = map(int, sys.stdin.read().split())
    n, m, k = next(nums), next(nums), next(nums)
    heights = [next(nums) for _ in range(n * m)]
    # Filling the lowest sections raises stacks below the final minimum h to h.
    # Some stacks at h may get one more container; initially taller ones stay put.
    # The answer is the largest h with sum(max(0, h - height)) <= K.
    lo, hi = min(heights), min(heights) + k
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if sum(mid - x for x in heights if x < mid) <= k:
            lo = mid
        else:
            hi = mid - 1
    print(lo)


main()
