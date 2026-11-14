MAX_LENGTH = 10000


def pivot(length, path):
    # Work with the gaps around the entries. Each split leaves one gap on either side.
    start, gaps = 0, length + 1
    for right in path:
        left = gaps // 2
        if right:
            start += left
            gaps -= left
        else:
            gaps = left
    return start + gaps // 2 - 1


def lengths(target, steps, maximum=MAX_LENGTH):
    runs = []
    path = []

    def first_at_least(lo, hi, value):
        while lo < hi:
            mid = (lo + hi) // 2
            if pivot(mid, path) < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def visit(lo, hi, depth):
        if lo >= hi:
            return
        # Along this fixed path the pivot moves only right as length grows.
        first = first_at_least(lo, hi, target)
        after = first_at_least(first, hi, target + 1)
        if depth == steps:
            if first < after:
                if runs and runs[-1][1] + 1 == first:
                    runs[-1] = runs[-1][0], after - 1
                else:
                    runs.append((first, after - 1))
            return
        path.append(True)
        visit(lo, first, depth + 1)
        path[-1] = False
        visit(after, hi, depth + 1)
        path.pop()

    visit(target + 1, maximum + 1, 1)
    return runs


def main():
    target, steps = map(int, open(0).read().split())
    runs = lengths(target, steps)
    print(len(runs))
    for start, end in runs:
        print(start, end)


if __name__ == "__main__":
    main()
