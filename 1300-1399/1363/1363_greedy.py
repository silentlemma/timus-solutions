import sys

WHITE = 255
HALF = 127  # the carried error always stays within [-127, 127]


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    out = []
    for i in range(n):
        row = data[2 + i * m : 2 + (i + 1) * m]
        # carry the rounding error along the row, in alternate directions so
        # that a window at either side meets short prefixes in half its rows
        cols = range(m) if i % 2 == 0 else range(m - 1, -1, -1)
        res = [0] * m
        err = 0
        for j in cols:
            err -= int(row[j])
            if err < -HALF:
                err += WHITE
                res[j] = WHITE
        out.append(" ".join(map(str, res)))
    print("\n".join(out))


main()
