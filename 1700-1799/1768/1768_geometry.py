import cmath
import sys

# a wrong set must move by 1e-5 to become right, so one turn misses by more
# than 1e-5 / n, while right sets given to 1e-10 miss by far less
EPS = 1e-8


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = [complex(float(data[1 + 2 * i]), float(data[2 + 2 * i])) for i in range(n)]
    centre = sum(pts) / n
    z = [p - centre for p in pts]
    # the vertices of a regular polygon in order turn into each other by a
    # rotation of 2 pi / n about the centre, one way or the other
    ok = False
    if abs(z[0]) > EPS:
        for way in (1, -1):
            turn = cmath.exp(way * 2j * cmath.pi / n)
            if all(abs(z[(i + 1) % n] - turn * z[i]) <= EPS for i in range(n)):
                ok = True
    print("YES" if ok else "NO")


main()
