import sys

NEED = 2  # a run needs two generating intervals inside it to be split


def smallest_family(g, width):
    """g[l][r]: the interval of columns l .. r - 1 must be a union of the
    chosen intervals inside it. Turns g into the smallest family of
    intervals that generates every required one: going right, an interval
    that two smaller chosen ones already cover is dropped, and the ones it
    leaned on are moved right so that every interval stays generated."""
    for right in range(1, width + 1):
        while True:
            count = [0] * (width + 1)
            covered = 0  # chosen intervals inside [t, u) ending at u or later
            rest = 0  # those starting before t
            u, t = right, right - 1
            redundant = True
            while u > t:
                covered -= count[u]
                for left in range(u):
                    if g[left][u]:
                        count[left] += 1
                        if left >= t:
                            covered += 1
                        else:
                            rest += 1
                if covered + rest < NEED:
                    redundant = False
                    break
                while covered < NEED:
                    t -= 1
                    covered += count[t]
                    rest -= count[t]
                u -= 1
            if not redundant:
                break
            w = next(left for left in range(u, right) if g[left][right])
            g[w][right] = False
            end = right - 1
            while w > u:
                x = next((left for left in range(u, w) if g[left][end]), -1)
                if x >= 0:
                    g[x][end] = False
                    g[w][end] = True
                    w = x
                end -= 1
    return [(lo, hi) for lo in range(width) for hi in range(lo + 1, width + 1) if g[lo][hi]]


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    rows = data[2 : 2 + n]
    # the black pixels of a column form one run from top to bottom
    top, bottom = [n] * m, [-1] * m
    g = [[False] * (m + 1) for _ in range(m + 1)]
    for row, line in enumerate(rows):
        col = 0
        while col < m:
            if line[col] == "0":
                col += 1
                continue
            left = col
            while col < m and line[col] == "1":
                top[col] = min(top[col], row)
                bottom[col] = max(bottom[col], row)
                col += 1
            g[left][col] = True
    # a chosen interval of columns spans every row where all of them are black
    out = []
    for lo, hi in smallest_family(g, m):
        first = max([0] + top[lo:hi])
        last = min([n - 1] + bottom[lo:hi])
        out.append("%d %d %d %d" % (first + 1, lo + 1, last + 1, hi))
    print(len(out))
    print("\n".join(out))


main()
