import sys

CENTS = 100
PEAK = 2 * CENTS


def main():
    data = sys.stdin.read().split()
    a, b = (round(float(t) * CENTS) for t in data[:2])
    k = int(data[2])
    # everything is in kopecks: x horns earn a * x - 100 * x^2
    best, best_x, best_y = -1, 0, 0
    y_peak = max(b, 0) // PEAK
    for x in range(k + 1):
        room = k - x
        gain_x = a * x - CENTS * x * x
        # the hoof profit is concave in y, so the best y is next to its peak
        for y in sorted({min(y_peak, room), min(y_peak + 1, room)}):
            total = gain_x + b * y - CENTS * y * y
            if total > best:
                best, best_x, best_y = total, x, y
    print("%d.%02d" % divmod(best, CENTS))
    print(best_x, best_y)


main()
