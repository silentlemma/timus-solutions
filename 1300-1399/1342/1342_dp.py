import sys

FIELDS = 3  # brooms, the first price and the last price


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    numbers = [int(v) for v in data[2:]]
    factories = [tuple(numbers[i : i + FIELDS]) for i in range(0, FIELDS * n, FIELDS)]
    target = min(m, sum(k for k, _, _ in factories))
    # best[j]: the cheapest way to make exactly j brooms at the factories so far
    best = [0.0] + [float("inf")] * target
    reach = 0
    for k, first, last in factories:
        step = (last - first) / (k - 1) if k > 1 else 0.0
        # cost[x]: x brooms at this factory, the j-th one costing first + step (j - 1)
        cost = [x * first + step * x * (x - 1) / 2 for x in range(k + 1)]
        reach = min(target, reach + k)
        fresh = best[:]
        for j in range(1, reach + 1):
            low = j - min(j, k)
            here = fresh[j]
            for x in range(1, j - low + 1):
                value = best[j - x] + cost[x]
                if value < here:
                    here = value
            fresh[j] = here
        best = fresh
    out = []
    if target < m:
        out.append("Maximum possible amount: %d" % target)
    out.append("Minimum possible cost: %.2f" % best[target])
    print("\n".join(out))


main()
