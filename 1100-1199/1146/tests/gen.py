"""An N by N array: a seed, N and a mode. Mode 0 takes values from -127 to
127, mode 1 only negative values, mode 2 only positive ones, mode 3 mostly
negative values with a few large positive ones, and the numbers are spread
over lines of random length."""

import random
import sys

TOP = 127
RARE = 0.05


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        nums = [rng.randint(-TOP, -1) for _ in range(n * n)]
    elif mode == 2:
        nums = [rng.randint(1, TOP) for _ in range(n * n)]
    elif mode == 3:
        nums = [TOP if rng.random() < RARE else rng.randint(-TOP, 0) for _ in range(n * n)]
    else:
        nums = [rng.randint(-TOP, TOP) for _ in range(n * n)]
    lines, pos = [], 0
    while pos < len(nums):
        width = rng.randint(1, 2 * n) if mode == 3 else n
        lines.append(" ".join(map(str, nums[pos : pos + width])))
        pos += width
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(lines)))


if __name__ == "__main__":
    main()
