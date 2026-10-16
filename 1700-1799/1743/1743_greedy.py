import sys

INF = float("inf")


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pieces = []
    for i in range(n):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        pieces.append((min(a, b), max(a, b)))
    # a domino is a range [low, high]; standing upright as (low, high) or
    # flipped as (high, low), two of a kind fit together when nested, and
    # one of each when they overlap; the two kinds are nested chains
    pieces.sort(key=lambda p: (p[0], -p[1]))
    upright, flipped = [], []
    for p in pieces:
        if not upright or p[1] <= upright[-1][1]:
            upright.append(p)
        elif not flipped or p[1] <= flipped[-1][1]:
            flipped.append(p)
        else:
            print("NO")
            return
    # the innermost ranges of the two chains meet in the middle
    if upright and flipped:
        (a, b), (c, d) = upright[-1], flipped[-1]
        if b < c or d < a:
            print("NO")
            return
    out = ["YES"]
    out += ["%d %d" % p for p in upright]
    out += ["%d %d" % (high, low) for low, high in reversed(flipped)]
    print("\n".join(out))


main()
