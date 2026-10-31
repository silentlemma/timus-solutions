import sys
from array import array
from operator import mul

# readlines returns whole lines of about this many bytes per batch.
INPUT_BATCH_BYTES = 65536


def pair_sum(values):
    # the sum of |a_i - a_j| over all pairs: in sorted order the i-th value is at
    # least the i values before it and at most the n - 1 - i after it, so it
    # enters the sum with weight 2i - (n - 1)
    weights = range(1 - len(values), len(values), 2)
    return sum(map(mul, sorted(values), weights))


def main():
    source = sys.stdin.buffer
    n = int(source.readline())
    # coordinates <= 10^6 fit signed 32-bit elements.
    xs, ys = array("i"), array("i")
    while True:
        lines = source.readlines(INPUT_BATCH_BYTES)
        if not lines:
            break
        # whole lines keep each coordinate pair together at batch boundaries.
        values = list(map(int, b"".join(lines).split()))
        xs.extend(values[::2])
        ys.extend(values[1::2])
    del values
    # walking along the streets, a visit covers |dx| + |dy|
    print((pair_sum(xs) + pair_sum(ys)) // (n * (n - 1) // 2))


main()
