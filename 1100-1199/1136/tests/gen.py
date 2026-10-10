"""The odd-session order of a parliament seated in the given entry order:
a seed, N and a mode. Mode 0 enters random distinct numbers, mode 1 enters
them increasing (one long right wing), mode 2 decreasing, mode 3 takes the
smallest and largest left in turn (a zigzag), mode 4 the medians first (a
balanced tree)."""

import random
import sys

LIMIT = 65535


def balanced(nums):
    out, stack = [], [(0, len(nums))]
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            mid = (lo + hi) // 2
            out.append(nums[mid])
            stack += [(lo, mid), (mid + 1, hi)]
    return out


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    nums = sorted(rng.sample(range(1, LIMIT + 1), n))
    if mode == 0:
        rng.shuffle(nums)
    elif mode == 2:
        nums.reverse()
    elif mode == 3:
        nums = [nums[k // 2] if k % 2 == 0 else nums[-1 - k // 2] for k in range(n)]
    elif mode == 4:
        nums = balanced(nums)
    left, right = {}, {}
    for v in nums[1:]:
        u = nums[0]
        while True:
            side = left if v < u else right
            if u not in side:
                side[u] = v
                break
            u = side[u]
    # left wing, right wing, chairman
    order, stack = [], [nums[0]]
    while stack:
        u = stack.pop()
        order.append(u)
        for child in (left.get(u), right.get(u)):
            if child is not None:
                stack.append(child)
    order.reverse()
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(map(str, order))))


if __name__ == "__main__":
    main()
