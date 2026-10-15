import sys


def pair_sum(values):
    # the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
    # is larger than the i values before it
    total = before = 0
    for i, v in enumerate(sorted(values)):
        total += v * i - before
        before += v
    return total


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = list(map(int, data[1:2 * n + 1:2]))
    ys = list(map(int, data[2:2 * n + 1:2]))
    # walking along the streets, a visit covers |dx| + |dy|
    print((pair_sum(xs) + pair_sum(ys)) // (n * (n - 1) // 2))


main()
