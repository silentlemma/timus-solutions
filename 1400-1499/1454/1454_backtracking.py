import sys


def tiles(pieces, width, height):
    # skyline filling: the lowest, then leftmost, stretch of the outline must
    # hold the bottom-left corner of some piece in every tiling
    used = [False] * len(pieces)

    def fill(sky, left):
        if left == 0:
            return True
        k = min(range(len(sky)), key=lambda i: sky[i][2])
        x, span, level = sky[k]
        tried = set()
        for i, (a, b) in enumerate(pieces):
            if used[i]:
                continue
            for w, h in ((a, b), (b, a)):
                if (w, h) in tried or w > span or level + h > height:
                    continue
                tried.add((w, h))
                parts = [(x, w, level + h)] + ([(x + w, span - w, level)] if w < span else [])
                new = []
                for seg in sky[:k] + parts + sky[k + 1 :]:
                    if new and new[-1][2] == seg[2]:
                        new[-1] = (new[-1][0], new[-1][1] + seg[1], seg[2])
                    else:
                        new.append(seg)
                used[i] = True
                if fill(new, left - 1):
                    return True
                used[i] = False
        return False

    return fill([(0, width, 0)], len(pieces))


def main():
    v = [int(x) for x in sys.stdin.read().split()]
    pieces = list(zip(v[0::2], v[1::2]))
    area = sum(w * h for w, h in pieces)
    width = 1
    while width * width <= area:
        if area % width == 0 and tiles(pieces, width, area // width):
            print("YES")
            return
        width += 1
    print("NO")


main()
