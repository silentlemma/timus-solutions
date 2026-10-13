import sys


def main():
    k, p = map(int, sys.stdin.read().split())
    # root[v]: some y with y^2 = v (mod p), or -1 when v is not a square
    root = [-1] * p
    for y in range(p):
        v = y * y % p
        if root[v] < 0:
            root[v] = y
    # half the values are squares, so some x soon leaves a square k - x^2
    for x in range(p):
        y = root[(k - x * x) % p]
        if y >= 0:
            print(x, y)
            return
    print("NO SOLUTION")


main()
