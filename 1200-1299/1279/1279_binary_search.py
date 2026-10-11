import sys


def main():
    nums = map(int, sys.stdin.read().split())
    n, m, k = next(nums), next(nums), next(nums)
    heights = [next(nums) for _ in range(n * m)]
    # filling the lowest sections first raises every section to a level h
    # and some of them one higher, so the answer is the largest h whose
    # missing containers, the sum of h - height below h, fit into K
    lo, hi = min(heights), min(heights) + k
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if sum(mid - x for x in heights if x < mid) <= k:
            lo = mid
        else:
            hi = mid - 1
    print(lo)


main()
