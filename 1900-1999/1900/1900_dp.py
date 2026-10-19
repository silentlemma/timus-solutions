from array import array
import sys

INFINITY = 1_000_000_000


def solve(n, k, weights):
    width = n + 1
    cost = [array("i", [0]) * width for _ in range(width)]
    for left in range(n - 1, 0, -1):
        row, below = cost[left], cost[left + 1]
        prefix = 0
        for right in range(left + 1, n + 1):
            prefix += weights[left - 1][right - left - 1]
            row[right] = below[right] + prefix
    groups = k + 1
    infinity = INFINITY
    previous = [infinity] * width
    for end in range(1, n - groups + 2):
        previous[end] = cost[1][end]
    parents = [None, None]
    for group in range(2, groups + 1):
        current = [infinity] * width
        parent = array("h", [0]) * width

        def fill(left, right, first, last):
            if left > right:
                return
            middle = (left + right) // 2
            best, split = infinity, first
            for cut in range(first, min(last, middle - 1) + 1):
                value = previous[cut] + cost[cut + 1][middle]
                if value < best:
                    best, split = value, cut
            current[middle], parent[middle] = best, split
            fill(left, middle - 1, first, split)
            fill(middle + 1, right, split, last)

        end = n - groups + group
        fill(group, end, group - 1, end - 1)
        previous = current
        parents.append(parent)
    end, cuts = n, []
    for group in range(groups, 1, -1):
        end = parents[group][end]
        cuts.append(end)
    cuts.reverse()
    return cost[1][n] - previous[n], cuts


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = next(tokens), next(tokens)
    weights = [[next(tokens) for _ in range(n - left)] for left in range(1, n)]
    value, cuts = solve(n, k, weights)
    print(value)
    print(*cuts)


if __name__ == "__main__":
    main()
