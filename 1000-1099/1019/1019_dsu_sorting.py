import sys
from bisect import bisect_left

END = 10**9
TOKENS_PER_REPAINT = 3


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    paints = []
    for i in range(n):
        a, b, c = data[1 + TOKENS_PER_REPAINT * i : 1 + TOKENS_PER_REPAINT * (i + 1)]
        paints.append((int(a), int(b), c))
    xs = sorted({0, END} | {a for a, _, _ in paints} | {b for _, b, _ in paints})
    pieces = len(xs) - 1
    piece = ["w"] * pieces
    # the colour of a piece is set by the last repainting covering it: go
    # backwards and paint only pieces that are still free, skipping the rest
    next_free = list(range(pieces + 1))

    def find(i):
        root = i
        while next_free[root] != root:
            root = next_free[root]
        while next_free[i] != root:
            next_free[i], i = root, next_free[i]
        return root

    for a, b, c in reversed(paints):
        p, stop = find(bisect_left(xs, a)), bisect_left(xs, b)
        while p < stop:
            piece[p] = c
            next_free[p] = p + 1
            p = find(p + 1)

    # the longest run of white pieces; a strict comparison keeps the leftmost
    best, i = (0, 0), 0
    while i < pieces:
        j = i
        while j < pieces and piece[j] == piece[i]:
            j += 1
        if piece[i] == "w" and xs[j] - xs[i] > best[1] - best[0]:
            best = (xs[i], xs[j])
        i = j
    print(*best)


main()
