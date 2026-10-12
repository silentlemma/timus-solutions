import sys

HEADER = 6  # the range, both borders and the count


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    reach, rx, ry, lx, ly, n = data[:HEADER]
    out = []
    for i in range(n):
        x, y = data[HEADER + 2 * i], data[HEADER + 2 * i + 1]
        # inside the sector means left of the right border and right of the
        # left one, borders included; the sector is narrower than a half turn
        right, left = rx * y - ry * x, x * ly - y * lx
        inside = right >= 0 and left >= 0
        # a border's extension behind the gun is out; for a sector of zero
        # width, both borders along one ray, no other test rejects it
        behind = (right == 0 and rx * x + ry * y < 0) or (left == 0 and lx * x + ly * y < 0)
        out.append("YES" if inside and not behind and x * x + y * y <= reach * reach else "NO")
    print("\n".join(out))


main()
