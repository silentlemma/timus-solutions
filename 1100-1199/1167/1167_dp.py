import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    black = [0] * (n + 1)
    for i in range(n):
        black[i + 1] = black[i] + int(data[2 + i])

    def cost(j, i):
        # horses j..i-1 in one stable: black times white
        b = black[i] - black[j]
        return b * (i - j - b)

    inf = float("inf")
    prev = [0] + [inf] * n
    for stables in range(1, k + 1):
        cur = [inf] * (n + 1)
        # the best last split never moves left as i grows (the black-white
        # cost satisfies the quadrangle inequality), so each half of the
        # range only searches its side of the split found for the middle
        work = [(stables, n, stables - 1, n - 1)]
        while work:
            lo, hi, opt_lo, opt_hi = work.pop()
            if lo > hi:
                continue
            mid = (lo + hi) // 2
            best, arg = inf, opt_lo
            for j in range(opt_lo, min(mid - 1, opt_hi) + 1):
                v = prev[j] + cost(j, mid)
                if v < best:
                    best, arg = v, j
            cur[mid] = best
            work.append((lo, mid - 1, opt_lo, arg))
            work.append((mid + 1, hi, arg, opt_hi))
        prev = cur
    print(prev[n])


main()
