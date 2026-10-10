import sys

# the colour of the white sheet
WHITE = 1
# a rectangle is five numbers
FIELDS = 5


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    width, height, n = next(tok), next(tok), next(tok)
    rects = [[next(tok) for _ in range(FIELDS)] for _ in range(n)]
    xs = sorted({0, width} | {x for x1, _, x2, _, _ in rects for x in (x1, x2)})
    ys = sorted({0, height} | {y for _, y1, _, y2, _ in rects for y in (y1, y2)})
    x_at = {x: i for i, x in enumerate(xs)}
    y_at = {y: j for j, y in enumerate(ys)}
    # the rectangles over each strip, from the top one down
    over = [[] for _ in range(len(xs) - 1)]
    for x1, y1, x2, y2, colour in reversed(rects):
        item = (y_at[y1], y_at[y2], colour)
        for i in range(x_at[x1], x_at[x2]):
            over[i].append(item)
    area = {}
    for i in range(len(xs) - 1):
        strip = xs[i + 1] - xs[i]
        # the top rectangles paint the cells of this strip first, and skip[j]
        # leads past painted cells to the next unpainted one
        skip = list(range(len(ys)))
        painted = 0
        for lo, hi, colour in over[i]:
            j = lo
            while skip[j] != j:
                skip[j], j = skip[skip[j]], skip[j]
            got = 0
            while j < hi:
                got += ys[j + 1] - ys[j]
                skip[j] = j + 1
                j += 1
                while skip[j] != j:
                    skip[j], j = skip[skip[j]], skip[j]
            if got:
                area[colour] = area.get(colour, 0) + got * strip
                painted += got
                if painted == height:
                    break
        area[WHITE] = area.get(WHITE, 0) + (height - painted) * strip
    out = ["%d %d" % (c, a) for c, a in sorted(area.items()) if a]
    sys.stdout.write("\n".join(out) + "\n")


main()
