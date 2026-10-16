import sys

HEADER = 6


def main():
    data = iter(sys.stdin.buffer.read().split())
    n, m, a, b, r, s = (int(next(data)) for _ in range(HEADER))
    # bus i takes the fans after the border P(i-1) up to the border P(i), with
    # P(0) = 0, P(m) = n and a <= P(i) - P(i-1) <= b; a fan in bus f puts
    # P(f) at or above them and P(f-1) below them
    low = [0] * (m + 1)
    high = [n] * (m + 1)
    high[0] = 0
    low[m] = n
    for _ in range(s):
        fan, bus = int(next(data)), int(next(data))
        low[bus] = max(low[bus], fan)
        high[bus - 1] = min(high[bus - 1], fan - 1)
    # the borders reachable from the left end and from the right end each
    # form a range, and a border is possible when it is in both
    lo, hi = low[:], high[:]
    for i in range(1, m + 1):
        lo[i] = max(lo[i], lo[i - 1] + a)
        hi[i] = min(hi[i], hi[i - 1] + b)
    for i in range(m - 1, -1, -1):
        lo[i] = max(lo[i], lo[i + 1] - b)
        hi[i] = min(hi[i], hi[i + 1] - a)
    if any(lo[i] > hi[i] for i in range(m + 1)):
        print("IMPOSSIBLE")
        return
    # fan r rides in bus k when some P(k-1) below r and P(k) at or above r
    # are possible borders a to b apart
    buses = []
    for k in range(1, m + 1):
        x_lo, x_hi = lo[k - 1], min(hi[k - 1], r - 1)
        y_lo, y_hi = max(lo[k], r), hi[k]
        if x_lo <= x_hi and y_lo <= y_hi and y_hi - x_lo >= a and y_lo - x_hi <= b:
            buses.append(k)
    print(len(buses))
    print(" ".join(map(str, buses)))


main()
