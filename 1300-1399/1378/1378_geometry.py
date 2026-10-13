import math
import sys

# from the centre, r1 reaches the farthest point and r2 reaches across it:
# area / (pi r1 r2) is 1 for any oval and 2 / pi for a square, and
# area / (pi r1^2) is 2 / pi for a square, at most 0.41 for a triangle
OVAL = 0.8
SQUARE = 0.5
HALF = 0.5  # a pixel reaches half a pixel beyond its centre


def main():
    words = sys.stdin.read().split()
    w, h = int(words[0]), int(words[1])
    pic = "".join(words[2:])
    ends = []  # a convex figure fills one run of each row
    count = sx = sy = 0
    for y in range(h):
        row = pic[y * w : (y + 1) * w]
        first = row.find("1")
        if first < 0:
            continue
        last = row.rfind("1")
        k = row.count("1")
        ends += [(first, y), (last, y)]
        count += k
        sx += k * (first + last) / 2
        sy += k * y
    cx, cy = sx / count, sy / count
    fx, fy = max(ends, key=lambda p: (p[0] - cx) ** 2 + (p[1] - cy) ** 2)
    r1 = math.hypot(fx - cx, fy - cy)
    ux, uy = (fx - cx) / r1, (fy - cy) / r1
    r2 = max(abs((y - cy) * ux - (x - cx) * uy) for x, y in ends)
    if count / (math.pi * (r1 + HALF) * (r2 + HALF)) > OVAL:
        print("circle")
    elif count / (math.pi * (r1 + HALF) ** 2) > SQUARE:
        print("square")
    else:
        print("triangle")


main()
