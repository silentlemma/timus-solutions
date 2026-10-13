import sys


def chain(xs, ys, order):
    """Positions on one monotone chain, keeping points that lie on its edges."""
    stack = []
    for i in order:
        x, y = xs[i], ys[i]
        while len(stack) > 1:
            a, b = stack[-2], stack[-1]
            if (xs[b] - xs[a]) * (y - ys[a]) - (ys[b] - ys[a]) * (x - xs[a]) >= 0:
                break
            stack.pop()
        stack.append(i)
    return stack


def flat(xs, ys):
    ax, ay, dx, dy = xs[0], ys[0], xs[-1] - xs[0], ys[-1] - ys[0]
    return all(dx * (y - ay) == dy * (x - ax) for x, y in zip(xs, ys))


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    vals = iter(map(int, data[1 : 1 + 2 * n]))
    points = sorted(zip(vals, vals))
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    layers = 0
    # peel hulls with their whole border while the rest still has area
    while len(xs) > 2 and not flat(xs, ys):
        layers += 1
        size = len(xs)
        border = set(chain(xs, ys, range(size)))
        border.update(chain(xs, ys, range(size - 1, -1, -1)))
        keep = [i for i in range(size) if i not in border]
        xs = [xs[i] for i in keep]
        ys = [ys[i] for i in keep]
    print(layers)


main()
