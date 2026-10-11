import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = list(map(int, data[1 : 2 * n + 1 : 2]))
    ys = list(map(int, data[2 : 2 * n + 2 : 2]))
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    sums = [x + y for x, y in zip(xs, ys)]
    diffs = [x - y for x, y in zip(xs, ys)]
    min_s, max_s, min_d, max_d = min(sums), max(sums), min(diffs), max(diffs)
    # the hull is cut out by eight lines, x, y, x + y and x - y each at
    # their extremes; going counterclockwise from the bottom edge, every
    # corner joins an axis line to a diagonal one
    corners = [
        (min_s - min_y, min_y),
        (max_d + min_y, min_y),
        (max_x, max_x - max_d),
        (max_x, max_s - max_x),
        (max_s - max_y, max_y),
        (min_d + max_y, max_y),
        (min_x, min_x - min_d),
        (min_x, min_s - min_x),
    ]
    hull = []
    for p in corners:
        if not hull or hull[-1] != p:
            hull.append(p)
    while len(hull) > 1 and hull[0] == hull[-1]:
        hull.pop()
    # the sides left all point in different directions, so no corner is in
    # the middle of a straight side
    sys.stdout.write("".join("%d %d\n" % p for p in hull))


main()
