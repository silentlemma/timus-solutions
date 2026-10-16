import sys


def arrange(n, h, lefts, d, start):
    """The strips in order, signed when turned over, if their left ends can
    be start, start + d, ..., start + (n - 1) d; None otherwise."""
    place = [0] * n
    flexible = []
    for k, x in enumerate(lefts):
        spots = []
        for value, sign in ((x, 1), (h - d - x, -1)):
            if d:
                step, rest = divmod(value - start, d)
                if rest == 0 and 0 <= step < n and all(s != step for s, _ in spots):
                    spots.append((step, sign))
            elif value == start and not spots:
                spots.append((k, sign))
        if not spots:
            return None
        if len(spots) == 1:
            step, sign = spots[0]
            if place[step]:
                return None
            place[step] = sign * (k + 1)
        else:
            flexible.append((k, spots))
    # a strip that fits two places pairs place i with place K - i, so only
    # strips of the same pair compete once the strips with one choice are in
    for k, spots in flexible:
        free = [(s, sign) for s, sign in spots if not place[s]]
        if not free:
            return None
        step, sign = free[0]
        place[step] = sign * (k + 1)
    return place


def main():
    data = sys.stdin.buffer.read().split()
    h, n = int(data[0]), int(data[1])
    ends = [int(v) for v in data[2:2 + 2 * n]]
    lefts, rights = ends[0::2], ends[1::2]
    # turning a strip over keeps its slope, so all slopes must be equal; the
    # left end x of a strip turns into h - d - x
    d = rights[0] - lefts[0]
    if any(r - l != d for l, r in zip(lefts, rights)):
        print(0)
        return
    ends = lefts + [h - d - x for x in lefts]
    if d == 0:
        starts = [lefts[0], h - lefts[0]]
    else:
        first, last = (min(ends), max(ends)) if d > 0 else (max(ends), min(ends))
        # the strip with the extreme end either starts the line or, turned,
        # ends it
        starts = [first, last - (n - 1) * d]
    for start in starts:
        place = arrange(n, h, lefts, d, start)
        if place:
            print(" ".join(map(str, place)))
            return
    print(0)


main()
