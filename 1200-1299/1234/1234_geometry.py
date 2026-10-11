import sys

TENTHS = 10
BRICK_SIDES = 3


def fits(p, q, a, b):
    # whether a p x q rectangle (p >= q) fits into an a x b one (a >= b); a
    # turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
    # by Carver's criterion, multiplied out here to stay in integers
    if q > b:
        return False
    if p <= a:
        return True
    s, d = (p + q) ** 2, (p - q) ** 2
    return (a + b) ** 2 * d + (a - b) ** 2 * s >= 2 * s * d


def main():
    v = [round(float(x) * TENTHS) for x in sys.stdin.read().split()]
    brick, hole = sorted(v[:BRICK_SIDES]), sorted(v[BRICK_SIDES:])
    # the face of the two shorter sides is the easiest to put through
    print("YES" if fits(brick[1], brick[0], hole[1], hole[0]) else "NO")


main()
