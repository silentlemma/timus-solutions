import sys
from math import gcd


def main():
    p, q, x, y, x1, y1 = map(int, sys.stdin.read().split())
    dx, dy, g = x1 - x, y1 - y, gcd(p, q)
    if g == 0:
        ok = dx == 0 and dy == 0
    elif dx % g or dy % g:
        ok = False
    else:
        # with p/g and q/g coprime, the moves reach every point of the
        # lattice g Z^2, except that when both are odd every move keeps the
        # parity of (dx + dy) / g
        both_odd = (p // g) % 2 and (q // g) % 2
        ok = not both_odd or (dx // g + dy // g) % 2 == 0
    print("YES" if ok else "NO")


main()
