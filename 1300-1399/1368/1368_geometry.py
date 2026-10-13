import math
import sys

ENDS = (1, 2)  # the first and last rows of a best shape are this narrow
SCALE = 8  # no k cells have fewer than sqrt(SCALE k - SHIFT) + 2 neighbours
SHIFT = 4


def widths_for(k):
    """Row widths of a region of k cells with the smallest fence.

    With row ends moving by at most one cell per row the fence is two cells
    per row plus the first and the last row; no fence is smaller than
    sqrt(8 k - 4) + 2, so try fences of growing size from there."""
    fence = math.isqrt(SCALE * k - SHIFT - 1) + 1 + 2
    while True:
        for first in ENDS:
            for last in ENDS:
                rows, odd = divmod(fence - first - last, 2)
                if odd or rows < 1:
                    continue
                full = [min(first + 2 * i, last + 2 * (rows - 1 - i)) for i in range(rows)]
                if rows == 1:
                    full = [first] if first == last else []
                if not full or sum(full) < k:
                    continue
                # cap the widest rows at the smallest level that holds k cells
                low = max(full[0], full[-1])
                lo, hi = low, max(full)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if sum(min(w, mid) for w in full) < k:
                        lo = mid + 1
                    else:
                        hi = mid
                cap = lo
                widths = [min(w, cap) for w in full]
                extra = sum(widths) - k
                inner = [i for i in range(1, rows - 1) if widths[i] == cap]
                if cap > low and extra <= len(inner):
                    for i in inner[:extra]:
                        widths[i] -= 1
                    return widths
                if extra == 0:
                    return widths
        fence += 1


def main():
    k = int(sys.stdin.read())
    widths = widths_for(k)
    # place the rows from y = 0 up, the first one starting at x = 0; the ends
    # move by at most one cell, the left one first when the row narrows
    left, right = [0], [widths[0] - 1]
    for w in widths[1:]:
        grow = w - (right[-1] - left[-1] + 1)
        dl = -1 if grow == 2 else (1 if grow < 0 else 0)
        left.append(left[-1] + dl)
        right.append(left[-1] + w - 1)
    top = len(widths) - 1
    fence = [(x, -1) for x in range(left[0], right[0] + 1)]
    fence += [(right[y] + 1, y) for y in range(top + 1)]
    fence += [(x, top + 1) for x in range(right[top], left[top] - 1, -1)]
    fence += [(left[y] - 1, y) for y in range(top, -1, -1)]
    print(len(fence))
    print("\n".join("%d %d" % c for c in fence))


main()
