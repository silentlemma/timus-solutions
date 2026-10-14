import sys


def main():
    words = iter(sys.stdin.read().split())
    total = int(next(words)) + 2
    xs, ys = [], []
    for _ in range(total):
        xs.append(int(next(words)))
        ys.append(int(next(words)))
    # always run to the farthest point not visited yet: the point before had
    # this one as its farthest, so it was at least as far as the next one,
    # which makes every turn acute
    path = [1]
    cx, cy = xs.pop(0), ys.pop(0)
    ids = list(range(2, total + 1))
    while ids:
        dist = [(x - cx) ** 2 + (y - cy) ** 2 for x, y in zip(xs, ys)]
        far = dist.index(max(dist))
        cx, cy = xs[far], ys[far]
        path.append(ids[far])
        # the last point takes the place of the visited one
        xs[far], ys[far], ids[far] = xs[-1], ys[-1], ids[-1]
        xs.pop()
        ys.pop()
        ids.pop()
    print("YES")
    print(" ".join(map(str, path)))


main()
