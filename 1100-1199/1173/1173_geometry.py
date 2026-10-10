import sys
from functools import cmp_to_key

# coordinates have at most three decimals, so in thousandths they are exact
# integers and every turn below is decided without rounding
SCALE = 1000


def exact(token):
    return round(float(token) * SCALE)


def main():
    data = iter(sys.stdin.read().split())
    hx, hy = exact(next(data)), exact(next(data))
    n = int(next(data))
    friends = []
    for _ in range(n):
        x, y, ident = next(data), next(data), next(data)
        friends.append((exact(x) - hx, exact(y) - hy, int(ident)))

    def half(p):
        return 0 if p[1] > 0 or (p[1] == 0 and p[0] > 0) else 1

    def by_angle(p, q):
        if half(p) != half(q):
            return half(p) - half(q)
        return -1 if p[0] * q[1] - p[1] * q[0] > 0 else 1

    friends.sort(key=cmp_to_key(by_angle))
    # consecutive friends by angle, joined in turn, never cross; the house
    # closes the loop across one angular gap, which must be the one wider
    # than half a turn if there is one
    start = 0
    for i in range(n):
        p, q = friends[i - 1], friends[i]
        if p[0] * q[1] - p[1] * q[0] < 0:
            start = i
    order = friends[start:] + friends[:start]
    print("\n".join(["0"] + [str(p[2]) for p in order] + ["0"]))


main()
