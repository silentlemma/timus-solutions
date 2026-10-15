import sys

LIMIT = 10 ** 9
MOST = 1500
# A missing range stays below any real sum even after adding all positive weights.
NEG = -2 * MOST * LIMIT


def best_range(sums, counts):
    # Only prefixes leaving at least two teams are eligible as left ends.
    prefix, inside = [0], [0]
    for s, c in zip(sums, counts):
        prefix.append(prefix[-1] + s)
        inside.append(inside[-1] + c)
    best, where = NEG, (0, 0)
    low, low_at, t = NEG, 0, 0
    for r in range(1, len(prefix)):
        while t < r and inside[t] <= inside[r] - 2:
            if low == NEG or prefix[t] < low:
                low, low_at = prefix[t], t
            t += 1
        if low != NEG and prefix[r] - low > best:
            best, where = prefix[r] - low, (low_at, r - 1)
    return where


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    teams = sorted(zip(data, data, data))
    ages, starts = [], []
    positions, weights = [], []
    fs = sorted({f for _, f, _ in teams})
    f_at = {f: i for i, f in enumerate(fs)}
    for i, (a, f, s) in enumerate(teams):
        if not ages or a != ages[-1]:
            ages.append(a)
            starts.append(i)
        positions.append(f_at[f])
        weights.append(s)
    starts.append(n)
    del teams, data, f_at
    size = 1
    while size < len(fs):
        size *= 2
    width = 2 * size
    # Prefixes and suffixes must contain a team. A crossing range then
    # contains at least two; only leaves need to distinguish one from two.
    answer, answer_ages = NEG, (0, 0)
    for left in range(len(ages)):
        total = [0] * width
        prefix = [NEG] * width
        suffix = [NEG] * width
        best = [NEG] * width
        for right in range(left, len(ages)):
            for i in range(starts[right], starts[right + 1]):
                v = size + positions[i]
                t = total[v] + weights[i]
                if prefix[v] != NEG:
                    best[v] = t
                total[v] = prefix[v] = suffix[v] = t
                v >>= 1
                while v:
                    a = 2 * v
                    b = a + 1
                    ta, tb = total[a], total[b]
                    total[v] = ta + tb
                    pa, pb = prefix[a], prefix[b]
                    sa, sb = suffix[a], suffix[b]
                    x = ta + pb
                    prefix[v] = pa if pa > x else x
                    x = tb + sa
                    suffix[v] = sb if sb > x else x
                    top = sa + pb
                    if best[a] > top:
                        top = best[a]
                    if best[b] > top:
                        top = best[b]
                    best[v] = top
                    v >>= 1
            if best[1] > answer:
                answer, answer_ages = best[1], (left, right)
    left, right = answer_ages
    sums, counts = [0] * len(fs), [0] * len(fs)
    for i in range(starts[left], starts[right + 1]):
        fi = positions[i]
        sums[fi] += weights[i]
        counts[fi] += 1
    lo, hi = best_range(sums, counts)
    sys.stdout.write(f"{ages[left]} {ages[right]}\n{fs[lo]} {fs[hi]}\n")


main()
