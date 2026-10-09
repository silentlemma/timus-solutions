MAX_N = 10000


def steps(n, target):
    """The number of comparisons after which the search over n elements
    reaches index target, when every other element sends it towards it."""
    p, q, count = 0, n - 1, 0
    while p <= q:
        count += 1
        i = (p + q) // 2
        if i == target:
            return count
        if target < i:
            q = i - 1
        else:
            p = i + 1
    return 0


def main():
    target, length = map(int, input().split())
    # any array whose elements before the target are smaller and after it are
    # larger leads the search there, so only n decides the number of steps
    runs = []
    for n in range(target + 1, MAX_N + 1):
        if steps(n, target) != length:
            continue
        if runs and runs[-1][1] == n - 1:
            runs[-1][1] = n
        else:
            runs.append([n, n])
    print("\n".join([str(len(runs))] + ["%d %d" % (a, b) for a, b in runs]))


main()
