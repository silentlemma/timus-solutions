import sys


SMALL_REMOVALS = 7


def search(values, kept):
    n = len(values)
    suffix = [0] * (n + 1)
    for index in range(n - 1, -1, -1):
        suffix[index] = suffix[index + 1] | values[index]
    best = 0
    for value in values[:kept]:
        best |= value

    def visit(index, needed, current):
        nonlocal best
        if needed == 0:
            best = max(best, current)
            return
        upper = current | suffix[index]
        if upper <= best:
            return
        # One witness per uncovered bit suffices; fill unused places arbitrarily.
        if needed == n - index or needed >= (suffix[index] & ~current).bit_count():
            best = upper
            return
        visit(index + 1, needed - 1, current | values[index])
        visit(index + 1, needed, current)

    visit(0, kept, 0)
    return best


def solve_dp(values, kept, full):
    count = [kept + 1] * (full + 1)
    count[0] = 0
    upper = 0
    best = 0
    for value in values:
        # Descending updates prevent using an element more than once.
        for mask in range(upper, -1, -1):
            used = count[mask]
            if used < kept:
                merged = mask | value
                if used + 1 < count[merged]:
                    count[merged] = used + 1
                if merged > best:
                    best = merged
        upper |= value
        if best == full:
            break
    return best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, removed = data[:2]
    values = data[2:]
    kept = n - removed
    full = 0
    for value in values:
        full |= value
    if kept >= full.bit_count():
        answer = full
    elif removed <= SMALL_REMOVALS:
        values.sort(reverse=True)
        answer = search(values, kept)
    else:
        values = sorted(set(values), reverse=True)
        answer = solve_dp(values, kept, full)
    print(answer)


if __name__ == "__main__":
    main()
