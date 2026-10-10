"""Checker: the channels must be laid one after another as a walk that
starts and ends at A, and they must be exactly the missing channels, each
once."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n, a = int(data[0]), int(data[1])
    missing = set()
    for i in range(n):
        for j in range(n):
            if i != j and data[2 + i * n + j] == "0":
                missing.add((i + 1, j + 1))
    try:
        nums = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(nums) % 2:
        fail("an odd number of values")
    walk = [(nums[k], nums[k + 1]) for k in range(0, len(nums), 2)]
    if len(walk) != len(missing) or set(walk) != missing:
        fail("not exactly the missing channels, each once")
    at = a
    for u, v in walk:
        if u != at:
            fail("channel %d %d does not start where the layer is" % (u, v))
        at = v
    if at != a:
        fail("the layer does not come back to A")


if __name__ == "__main__":
    main()
