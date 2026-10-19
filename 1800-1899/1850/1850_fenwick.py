import sys
from bisect import bisect_left, bisect_right


def main():
    numbers = map(int, sys.stdin.buffer.read().split())
    n, s, d = next(numbers), next(numbers), next(numbers)
    planets = sorted((next(numbers), next(numbers)) for _ in range(n))
    dist = [p[0] for p in planets]
    race = [p[1] for p in planets]
    # pieces of planets with gaps of at most d: the tourist moves only
    # inside a piece cut by the range [low, high]
    piece = [0] * n
    first = [0]
    for i in range(1, n):
        if dist[i] - dist[i - 1] > d:
            first.append(i)
        piece[i] = len(first) - 1
    first.append(n)
    pieces = len(first) - 1
    # head[i]: races from the start of i's piece to i; tail[i]: from i to
    # its end; whole[p]: races of piece p
    head, tail, whole = [0] * n, [0] * n, [0] * pieces
    mark = [-1] * (s + 1)
    for p in range(pieces):
        seen = 0
        for i in range(first[p], first[p + 1]):
            if mark[race[i]] != p:
                mark[race[i]] = p
                seen += 1
            head[i] = seen
        whole[p] = seen
        seen = 0
        for i in range(first[p + 1] - 1, first[p] - 1, -1):
            if mark[race[i]] != -2 - p:
                mark[race[i]] = -2 - p
                seen += 1
            tail[i] = seen
    # sparse table of the largest whole piece over ranges of pieces
    table = [whole]
    step = 1
    while 2 * step <= pieces:
        last = table[-1]
        table.append([max(last[i], last[i + step]) for i in range(pieces - 2 * step + 1)])
        step *= 2

    def largest(lo, hi):
        # the largest whole piece among pieces lo..hi - 1
        if lo >= hi:
            return 0
        level = (hi - lo).bit_length() - 1
        return max(table[level][lo], table[level][hi - (1 << level)])

    m = next(numbers)
    answer = [0] * m
    inside = []  # ranges within one piece: (right, left, tourist)
    for t in range(m):
        low, high = next(numbers), next(numbers)
        lo, hi = bisect_left(dist, low), bisect_right(dist, high) - 1
        if lo > hi:
            continue
        if piece[lo] == piece[hi]:
            inside.append((hi, lo, t))
        else:
            answer[t] = max(tail[lo], head[hi], largest(piece[lo] + 1, piece[hi]))
    # distinct races in a range: going right, count each race only at its
    # latest planet, in a Fenwick tree
    inside.sort()
    tree = [0] * (n + 1)
    latest = [-1] * (s + 1)
    j = 0
    for i in range(n):
        if latest[race[i]] >= 0:
            k = latest[race[i]] + 1
            while k <= n:
                tree[k] -= 1
                k += k & -k
        latest[race[i]] = i
        k = i + 1
        while k <= n:
            tree[k] += 1
            k += k & -k
        while j < len(inside) and inside[j][0] == i:
            _, lo, t = inside[j]
            total, k = 0, i + 1
            while k:
                total += tree[k]
                k -= k & -k
            k = lo
            while k:
                total -= tree[k]
                k -= k & -k
            answer[t] = total
            j += 1
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


main()
