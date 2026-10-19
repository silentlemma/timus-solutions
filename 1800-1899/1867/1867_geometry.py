import sys
from math import isqrt


def place(d, n, p, a, b, flip):
    # atom 0 at the origin, atom p at (a, b); every other atom follows from
    # its distances to these two up to a reflection in the line through
    # them, and the first atom off that line picks the side by flip
    big = a * a + b * b
    signs = (-1, 1) if flip else (1, -1)
    xs, ys = [0] * n, [0] * n
    for i in range(1, n):
        twice = d[0][i] - d[p][i] + big  # twice the dot product with (a, b)
        if twice % 2:
            return None
        dot = twice // 2
        square = big * d[0][i] - dot * dot  # the cross product, squared
        if square < 0 or isqrt(square) ** 2 != square:
            return None
        cross = isqrt(square)
        row = d[i]
        for sign in signs:
            nx, ny = a * dot + b * sign * cross, b * dot - a * sign * cross
            if nx % big or ny % big:
                continue
            x, y = nx // big, ny // big
            if all((x - xs[j]) ** 2 + (y - ys[j]) ** 2 == row[j] for j in range(i)):
                break
        else:
            return None
        xs[i], ys[i] = x, y
    return xs, ys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    p = next((i for i in range(1, n) if d[0][i]), 0)
    if p == 0:
        # everything sits at the origin
        fine = all(v == 0 for row in d for v in row)
        print("\n".join(["0 0"] * n) if fine else "Impossible")
        return
    big = d[0][p]
    # the symmetries of the grid bring atom p to (a, b) with 0 <= a <= b
    for a in range(isqrt(big // 2) + 1):
        b = isqrt(big - a * a)
        if a * a + b * b != big:
            continue
        for flip in (False, True):
            found = place(d, n, p, a, b, flip)
            if found:
                print("\n".join("%d %d" % pair for pair in zip(*found)))
                return
    print("Impossible")


main()
