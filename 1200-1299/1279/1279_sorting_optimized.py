import os
import sys


def main():
    nums = map(int, sys.stdin.read().split())
    n, m, k = next(nums), next(nums), next(nums)
    heights = [next(nums) for _ in range(n * m)]
    # filling the lowest sections first raises every section to a level h
    # and some of them one higher, so the answer is the largest h whose
    # missing containers, the sum of h - height below h, fit into K
    heights.sort()
    level = heights[0]
    for count, following in enumerate(heights[1:], 1):
        needed = (following - level) * count
        if needed > k:
            print(level + k // count)
            return
        k -= needed
        level = following
    print(level + k // len(heights))


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
