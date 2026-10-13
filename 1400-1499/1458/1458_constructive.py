import sys

ROW = bytes.maketrans(b"BW", b"10")  # the soldiers to turn, for an all-W parade


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = [int(line.translate(ROW), 2) for line in data[1 : 1 + n]]
    full = (1 << n) - 1
    # pressing every cell of row a and column b turns only (a, b) when N is
    # even, so (i, j) is pressed when its row, its column and itself add up odd
    columns = 0
    for r in rows:
        columns ^= r
    press = [r ^ columns ^ (full if bin(r).count("1") % 2 else 0) for r in rows]
    total = sum(bin(p).count("1") for p in press)
    if 2 * total > n * n:
        # an all-B parade needs exactly the other cells
        press = [p ^ full for p in press]
        total = n * n - total
    out = [str(total)]
    for i, p in enumerate(press, 1):
        bits = format(p, "0%db" % n)
        j = bits.find("1")
        while j >= 0:
            out.append("%d %d" % (i, j + 1))
            j = bits.find("1", j + 1)
    sys.stdout.write("\n".join(out) + "\n")


main()
