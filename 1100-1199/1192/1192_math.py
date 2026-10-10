import math

GRAVITY = 10.0
PI = 3.1415926535  # the value the statement fixes
HALF_TURN = 180.0


def main():
    v, a, k = input().split()
    v, a, k = float(v), float(a), float(k)
    # one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
    # divides v^2 by k, so the flights form a geometric series with ratio 1/k
    flight = v * v * math.sin(2 * a * PI / HALF_TURN) / GRAVITY
    print("%.2f" % (flight * k / (k - 1)))


main()
