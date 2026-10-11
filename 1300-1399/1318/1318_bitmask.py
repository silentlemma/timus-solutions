import sys
from bisect import bisect_left

WORD = 32
PARTS = 4
SMALL = 32  # pairs of groups with at most this many pairs are checked one by one


def split(nums, lo, hi, bit):
    """First index in nums[lo:hi] with the bit set, when all of them
    agree on the higher bits."""
    return bisect_left(nums, (nums[lo] >> bit | 1) << bit, lo, hi)


def count_reaching(nums, lo, mid, hi, top, limit):
    """Pairs of x from nums[lo:mid] and y from nums[mid:hi] with x ^ y at
    least limit, where every such x ^ y and limit have top as the
    highest bit."""
    found = 0
    stack = [(lo, mid, mid, hi, top - 1)]
    while stack:
        l1, h1, l2, h2, bit = stack.pop()
        if h1 == l1 or h2 == l2:
            continue
        if limit & ((2 << bit) - 1) == 0:
            found += (h1 - l1) * (h2 - l2)  # the rest of limit is zeros
            continue
        if (h1 - l1) * (h2 - l2) <= SMALL:
            found += sum(1 for x in nums[l1:h1] for y in nums[l2:h2] if x ^ y >= limit)
            continue
        m1, m2 = split(nums, l1, h1, bit), split(nums, l2, h2, bit)
        if limit >> bit & 1:
            stack.append((l1, m1, m2, h2, bit - 1))
            stack.append((m1, h1, l2, m2, bit - 1))
        else:
            # pairs that differ in this bit are already above limit
            found += (m1 - l1) * (h2 - m2) + (h1 - m1) * (m2 - l2)
            stack.append((l1, m1, l2, m2, bit - 1))
            stack.append((m1, h1, m2, h2, bit - 1))
    return found


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    nums = []
    for i in range(n):
        value = 0
        for word in data[1 + PARTS * i : 1 + PARTS * (i + 1)]:
            value = value << WORD | int(word)
        nums.append(value)
    nums.sort()
    total = 0
    stack = [(0, n)]
    while stack:
        lo, hi = stack.pop()
        if hi - lo < 2 or nums[lo] == nums[hi - 1]:
            continue
        # every pair across the split has its xor in [2^top, 2^(top + 1))
        top = (nums[lo] ^ nums[hi - 1]).bit_length() - 1
        mid = split(nums, lo, hi, top)
        low = len(str(1 << top)) - 1
        total += low * (mid - lo) * (hi - mid)
        limit = 10 ** (low + 1)
        if limit < 2 << top:
            total += count_reaching(nums, lo, mid, hi, top, limit)
        stack.append((lo, mid))
        stack.append((mid, hi))
    print(2 * total)  # every pair counts in both orders


main()
