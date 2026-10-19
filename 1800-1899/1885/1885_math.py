def main():
    h, t, v, x = map(int, input().split())
    # the least time climbs at x as long as possible and at full speed in
    # the remaining seconds; the most climbs just faster than x, or during
    # all t seconds when that is too slow to reach h
    least = max(0, h - t * x) / (v - x)
    most = min(t, h / x)
    print("%.6f %.6f" % (least, most))


main()
