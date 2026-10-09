import sys


def main():
    d, e, f, dp, ep, h = map(int, sys.stdin.read().split())
    # pier p - 1 written in F bits is the path to it, a left turn being 1 and
    # the first turn the highest bit; a stone k hours from the sea is that
    # path without its last k turns
    a, depth_a = (ep - 1) >> e, f - e
    b, depth_b = (dp - 1) >> d, f - d
    hours = 0
    while depth_a > depth_b:
        a, depth_a, hours = a >> 1, depth_a - 1, hours + 1
    while depth_b > depth_a:
        b, depth_b, hours = b >> 1, depth_b - 1, hours + 1
    while a != b:
        a, b, hours = a >> 1, b >> 1, hours + 2
    print("YES" if hours <= h else "NO")


main()
