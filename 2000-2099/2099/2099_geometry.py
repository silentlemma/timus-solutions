import sys

DIM = 3


def sub(u, v):
    return [a - b for a, b in zip(u, v)]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def main():
    v = list(map(int, sys.stdin.read().split()))
    a, b, c, d = (v[i:i + DIM] for i in range(0, len(v), DIM))
    ab, cd, ac = sub(b, a), sub(d, c), sub(c, a)
    # the turn is a right angle, the two lines meet, the turning point
    # P = A + t AB with t = (AC . AB) / |AB|^2 is not before B, and C is not
    # before P on the second line, (C - P) . CD = AC . CD >= 0
    ok = (dot(ab, cd) == 0 and dot(ac, cross(ab, cd)) == 0
          and dot(ac, ab) >= dot(ab, ab) and dot(ac, cd) >= 0)
    print("Valid" if ok else "Invalid")


main()
