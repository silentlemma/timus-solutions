import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = [int(v) for v in data[1 : 2 * n + 1 : 2]]
    ys = [int(v) for v in data[2 : 2 * n + 2 : 2]]
    m = int(data[2 * n + 1])
    rest = data[2 * n + 2 :]
    edges = [(xs[i], ys[i], xs[(i + 1) % n], ys[(i + 1) % n]) for i in range(n)]
    out = []
    for j in range(m):
        px, py = int(rest[2 * j]), int(rest[2 * j + 1])
        turns = 0
        on_edge = False
        for ax, ay, bx, by in edges:
            cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
            if cross == 0 and min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by):
                on_edge = True
                break
            # a track crossing the ray to the right of the point: upwards
            # with the point on its left adds a turn, downwards on its right
            # takes one away
            if ay <= py < by:
                if cross > 0:
                    turns += 1
            elif by <= py < ay:
                if cross < 0:
                    turns -= 1
        out.append("EDGE" if on_edge else str(turns))
    sys.stdout.write("\n".join(out) + "\n")


main()
