import sys


def main():
    n, k, m = map(int, sys.stdin.read().split())
    # rooms in turn: every room gets someone, and the split is as even as
    # possible, which leaves the most pairs from different rooms
    room = [i % k for i in range(n)]
    # neighbours in this order always have different rooms
    days = [(i, i + 1) for i in range(0, n - 1, 2)]
    if n % 2:
        days.append((n - 1, 0 if room[n - 1] != room[0] else 1))
    used = {frozenset(d) for d in days}
    for i in range(n):
        for j in range(i + 1, n):
            if len(days) == m:
                break
            if room[i] != room[j] and frozenset((i, j)) not in used:
                days.append((i, j))
    out = [str(r + 1) for r in room]
    out += ["%d %d" % (i + 1, j + 1) for i, j in days[:m]]
    print("\n".join(out))


main()
