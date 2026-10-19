import sys

EDGE = 10 ** 9


def main():
    v = list(map(int, sys.stdin.read().split()))
    n, k = v[0], v[1]
    rest = iter(v[2:])
    candles = sorted(zip(rest, rest))
    # take the first k candles from the left, ties broken from below: all
    # columns left of candle k, and its own column up to it; the cut from
    # it to (x - 1, EDGE) leaves the rest of its column outside
    x, y = candles[k - 1]
    polygon = [(-EDGE, -EDGE), (x, -EDGE), (x, y)]
    if x - 1 > -EDGE:
        polygon.append((x - 1, EDGE))
    polygon.append((-EDGE, EDGE))
    print(len(polygon))
    print("\n".join("%d %d" % p for p in polygon))


main()
