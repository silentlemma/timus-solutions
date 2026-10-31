import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    black = [0] * (n + 1)
    for i in range(n):
        black[i + 1] = black[i] + int(data[2 + i])

    # each monochromatic run fits in one stable; splitting runs adds no cost.
    runs = 1 + sum(black[i + 1] - black[i] != black[i] - black[i - 1] for i in range(1, n))
    if k >= runs:
        print(0)
        return

    inf = float("inf")
    # one stable has a direct cost; later layers reserve one horse per future stable.
    prev = [black[i] * (i - black[i]) for i in range(n + 1)]
    for stables in range(2, k + 1):
        cur = [inf] * (n + 1)
        # the best last split never moves left as i grows (the black-white
        # cost satisfies the quadrangle inequality), so each half of the
        # range only searches its side of the split found for the middle
        last = n - k + stables
        work = [(stables, last, stables - 1, last - 1)]
        while work:
            lo, hi, opt_lo, opt_hi = work.pop()
            if lo > hi:
                continue
            mid = (lo + hi) // 2
            best, arg = inf, opt_lo
            for j in range(opt_lo, min(mid - 1, opt_hi) + 1):
                # inline the constant-time cost in the innermost loop.
                b = black[mid] - black[j]
                v = prev[j] + b * (mid - j - b)
                if v < best:
                    best, arg = v, j
            cur[mid] = best
            if lo < mid:
                work.append((lo, mid - 1, opt_lo, arg))
            if mid < hi:
                work.append((mid + 1, hi, arg, opt_hi))
        prev = cur
    print(prev[n])


main()
