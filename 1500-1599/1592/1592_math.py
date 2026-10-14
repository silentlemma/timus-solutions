import sys

TWELVE = 12
MINUTE = 60
HOUR = 60 * MINUTE
CYCLE = TWELVE * HOUR  # the dial shows the same after 12 hours


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    times = []
    for word in words[1 : n + 1]:
        h, m, s = (int(x) for x in word.split(":"))
        times.append((h % TWELVE) * HOUR + m * MINUTE + s)  # 12 o'clock is 0
    times.sort()
    total = sum(times)
    # winding clock i forward to t costs t - time_i, plus a full cycle when
    # the clock shows a later time than t; moving t back to the nearest
    # clock time only helps, so only the clock times are tried
    best, best_cost = 0, None
    j = 0  # clocks showing at most t
    for t in times:
        while j < n and times[j] <= t:
            j += 1
        cost = n * t - total + CYCLE * (n - j)
        if best_cost is None or cost < best_cost:
            best, best_cost = t, cost
    h, rest = divmod(best, HOUR)
    print("%d:%02d:%02d" % (h or TWELVE, rest // MINUTE, rest % MINUTE))


main()
