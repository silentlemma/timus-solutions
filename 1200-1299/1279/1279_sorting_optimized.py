import os
import sys


def main():
    nums = map(int, sys.stdin.read().split())
    n, m, k = next(nums), next(nums), next(nums)
    heights = [next(nums) for _ in range(n * m)]
    # Filling the lowest sections raises stacks below the final minimum h to h.
    # Some stacks at h may get one more container; initially taller ones stay put.
    # The answer is the largest h with sum(max(0, h - height)) <= K.
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
