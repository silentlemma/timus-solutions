import heapq
import sys

ROOT2 = 2**0.5
EXTRA = ROOT2 - 1


def main():
    words = iter(sys.stdin.read().split())
    n, m, k = int(next(words)), int(next(words)), int(next(words))
    v = float(next(words))
    rows = [next(words) for _ in range(m)]
    nums = map(int, words)
    # cells numbered over a grid with a border of buildings, so no move
    # needs a bounds check
    w = n + 2
    free = bytearray((m + 2) * w)
    for r, row in enumerate(rows):
        for c, ch in enumerate(row[:n]):
            if ch == ".":
                free[(r + 1) * w + c + 1] = 1
    # a step along a side costs 1, along a diagonal sqrt 2, and a diagonal
    # may pass a building's corner
    moves = [(1, 1.0), (-1, 1.0), (w, 1.0), (-w, 1.0)]
    moves += [(w + 1, ROOT2), (w - 1, ROOT2), (-w + 1, ROOT2), (-w - 1, ROOT2)]
    inf = float("inf")
    row = [c // w for c in range(len(free))]
    col = [c % w for c in range(len(free))]

    def walk(start, target):
        """Shortest walk by A* with the octile distance as the estimate,
        which never exceeds the true length; None if unreachable."""
        ty, tx = row[target], col[target]

        def guess(c):
            dy, dx = abs(row[c] - ty), abs(col[c] - tx)
            return dx + EXTRA * dy if dx > dy else dy + EXTRA * dx

        dist = [inf] * len(free)
        dist[start] = 0.0
        heap = [(guess(start), start)]
        pop, push = heapq.heappop, heapq.heappush
        while heap:
            f, c = pop(heap)
            d = dist[c]
            if c == target:
                return d
            if f > d + guess(c):
                continue
            for step, cost in moves:
                nc = c + step
                if free[nc]:
                    nd = d + cost
                    if nd < dist[nc]:
                        dist[nc] = nd
                        push(heap, (nd + guess(nc), nc))
        return None

    x, y = next(nums), next(nums)
    at = y * w + x
    free[at] = 1  # John stands there, whatever the map shows
    # parts of the town joined by moves, so an unreachable bomb costs nothing
    part = [0] * len(free)
    count = 0
    for c in range(len(free)):
        if free[c] and not part[c]:
            count += 1
            part[c] = count
            stack = [c]
            while stack:
                a = stack.pop()
                for step, _ in moves:
                    b = a + step
                    if free[b] and not part[b]:
                        part[b] = count
                        stack.append(b)
    total = 0.0
    known = {}
    for i in range(k):
        x, y = next(nums), next(nums)
        target = y * w + x
        # an unreachable bomb is skipped and John stays where he is
        if part[target] != part[at]:
            continue
        if (at, target) not in known:
            known[at, target] = known[target, at] = walk(at, target)
        total += known[at, target]
        at = target
    print("%.2f" % (total / v))


main()
