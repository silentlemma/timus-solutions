import sys

PERCENT = 100
OUTPUT_SCALE = 100000000


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, limit = data[0], data[1]
    own = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent, own[i] = data[2 * i - 2], data[2 * i - 1]
        children[parent].append(i)
    order = [1]
    for v in order:
        order.extend(children[v])
    order.reverse()

    def ready_by(num, den):
        # x = 100 num/den: a noble with c vassals waits for ceil(num c/den)
        # of them, so the wait is that order statistic of their ready days
        ready = [0] * (n + 1)
        for v in order:
            c = len(children[v])
            need = (num * c + den - 1) // den
            wait = 0
            if need:
                wait = sorted(ready[w] for w in children[v])[need - 1]
            ready[v] = wait + own[v]
        return ready[1] <= limit

    # the answer is a largest fraction m/c over the vassal counts c
    counts = sorted({len(ch) for ch in children if ch})
    fractions = sorted({(m / c, m, c) for c in counts for m in range(c + 1)})
    if not fractions:
        fractions = [(1.0, 1, 1)]
    lo, hi = 0, len(fractions) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ready_by(fractions[mid][1], fractions[mid][2]):
            lo = mid
        else:
            hi = mid - 1
    _, m, c = fractions[lo]
    answer = (PERCENT * m * OUTPUT_SCALE + c // 2) // c
    print(f"{answer // OUTPUT_SCALE}.{answer % OUTPUT_SCALE:08d}")


main()
