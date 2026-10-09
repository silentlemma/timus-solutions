import sys

JURY = 255
# influence, side, x and y of every plot
FIELDS = 4


def main():
    tok = list(map(int, sys.stdin.read().split()))
    size, park, m, *rest = tok
    plots = [rest[i : i + FIELDS] for i in range(0, FIELDS * m, FIELDS)]
    top = size - park + 1
    # sliding the park left only drops plots until its left side reaches a
    # plot's right side or the border, so only those positions are tried
    xs = sorted({1} | {x + s for _, s, x, _ in plots if x + s <= top})
    ys = sorted({1} | {y + s for _, s, _, y in plots if y + s <= top})
    best = JURY
    for px in xs:
        strip = [(y, y + s, w) for w, s, x, y in plots if px < x + s and x < px + park]
        for py in ys:
            worst = 1
            for lo, hi, w in strip:
                if py < hi and lo < py + park and w > worst:
                    worst = w
            best = min(best, worst)
    print("IMPOSSIBLE" if best == JURY else best)


main()
