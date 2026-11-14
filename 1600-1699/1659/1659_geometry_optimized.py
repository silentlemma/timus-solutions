import sys

CORNERS = 3
INNER = 0.5
OUTER = -1.5


def main():
    ax, ay, bx, by, cx, cy = map(float, sys.stdin.buffer.read().split())
    gx = (ax + bx + cx) / CORNERS
    gy = (ay + by + cy) / CORNERS
    points = ((ax, ay), (bx, by), (cx, cy))
    write = sys.stdout.write
    for scale in (INNER, OUTER):
        for x, y in points:
            write(f"{gx + scale * (x - gx):.10f} {gy + scale * (y - gy):.10f}\n")


if __name__ == "__main__":
    main()
