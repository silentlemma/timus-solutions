import heapq
import sys
from bisect import bisect_left, insort

# the local search stops after this many improvements
ROUNDS = 20000
# an exact split of two generals may use at most this many bits of tables
SPLIT_BITS = 4000000
WORD = 64


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, limit = next(tok), next(tok), next(tok)
    value = [next(tok) for _ in range(n)]
    # largest boxes first, each to the general with the least gold so far
    order = sorted(range(n), key=lambda i: -value[i])
    sums = [0] * m
    boxes = [[] for _ in range(m)]
    poorest = [(0, g) for g in range(m)]
    for i in order:
        s, g = heapq.heappop(poorest)
        boxes[g].append((value[i], i))
        sums[g] = s + value[i]
        heapq.heappush(poorest, (sums[g], g))
    for group in boxes:
        group.sort()

    def exchange(hi, lo):
        # the move or swap of boxes from hi to lo that leaves the smallest gap
        # between the two, if it is smaller than now
        d = sums[hi] - sums[lo]
        if d <= 1:
            return False
        best, best_a, best_b = d, -1, -1
        a, b = boxes[hi], boxes[lo]
        half = d // 2
        candidates = []
        if len(a) > 1:
            k = bisect_left(a, (half, -1))
            candidates += [(a[ia][0], ia, -1) for ia in (k - 1, k) if 0 <= ia < len(a)]
        for ia in range(len(a)):
            if ia > 0 and a[ia][0] == a[ia - 1][0]:
                continue
            k = bisect_left(b, (a[ia][0] - half, -1))
            candidates += [(a[ia][0] - b[ib][0], ia, ib) for ib in (k - 1, k) if 0 <= ib < len(b)]
        for t, ia, ib in candidates:
            if 0 < t < d and abs(d - 2 * t) < best:
                best, best_a, best_b = abs(d - 2 * t), ia, ib
        if best_a < 0:
            return False
        x = a.pop(best_a)
        sums[hi] -= x[0]
        sums[lo] += x[0]
        if best_b >= 0:
            y = b.pop(best_b)
            insort(a, y)
            sums[hi] += y[0]
            sums[lo] -= y[0]
        insort(b, x)
        return True

    def split(hi, lo):
        # the most even split of the boxes of hi and lo found by subset sums,
        # kept when it narrows their gap and leaves each general a box
        items = boxes[hi] + boxes[lo]
        total = sums[hi] + sums[lo]
        words = total // WORD + 1
        if (len(items) + 1) * words * WORD > SPLIT_BITS:
            return False
        reach = [1]
        for v, _ in items:
            reach.append(reach[-1] | reach[-1] << v)
        t = total // 2
        while t > 0 and not reach[-1] >> t & 1:
            t -= 1
        if t == 0 or total - 2 * t >= sums[hi] - sums[lo]:
            return False
        small, big, rest = [], [], t
        for k in range(len(items) - 1, -1, -1):
            if not reach[k] >> rest & 1:
                small.append(items[k])
                rest -= items[k][0]
            else:
                big.append(items[k])
        if not small or not big:
            return False
        boxes[hi], boxes[lo] = sorted(big), sorted(small)
        sums[hi], sums[lo] = total - t, t
        return True

    # then even out the richest and the poorest general against the others
    for _ in range(ROUNDS):
        hi = sums.index(max(sums))
        lo = sums.index(min(sums))
        if sums[hi] - sums[lo] <= limit:
            break
        if exchange(hi, lo):
            continue
        up = sorted(range(m), key=lambda g: sums[g])
        down = sorted(range(m), key=lambda g: -sums[g])
        moved = any(g != hi and exchange(hi, g) for g in up)
        moved = moved or any(g != lo and exchange(g, lo) for g in down)
        moved = moved or split(hi, lo)
        moved = moved or any(g != hi and split(hi, g) for g in up)
        moved = moved or any(g != lo and split(g, lo) for g in down)
        if not moved:
            break
    out = [str(max(sums) - min(sums))]
    for group in boxes:
        out.append(" ".join(str(i + 1) for i in sorted(i for _, i in group)))
    sys.stdout.write("\n".join(out) + "\n")


main()
