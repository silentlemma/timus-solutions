import math
import sys

EPS = 1e-9  # touching counts as fitting
SIDES = 3


def apex(base, left, right):
    """The third vertex of a triangle on the segment from (0, 0) to (base, 0)
    whose other sides are left (from the origin) and right."""
    x = (base * base + left * left - right * right) / (2 * base)
    return x, math.sqrt(max(0.0, left * left - x * x))


def fits_on(env, card):
    """Can the card lie with its side card[0] on the envelope's side env[0],
    in either of its two mirror images?"""
    m, length = env[0], card[0]
    if length > m + EPS:
        return False
    wx, height = apex(m, env[1], env[2])
    for left, right in ((card[1], card[2]), (card[2], card[1])):
        u, h = apex(length, left, right)
        if h > height + EPS:
            continue
        # the card slides along the side by t in [0, m - length]; its apex
        # (t + u, h) must stay between the envelope's two other sides
        lo = max(0.0, h * wx / height - u)
        hi = min(m - length, m - h * (m - wx) / height - u)
        if lo <= hi + EPS:
            return True
    return False


def main():
    values = [int(v) for v in sys.stdin.read().split()]
    env, card = sorted(values[:SIDES]), sorted(values[SIDES:])
    if env[0] + env[1] == env[2]:
        # a flat envelope holds only a flat card that is no longer
        fits = card[0] + card[1] == card[2] and card[2] <= env[2]
    else:
        # a triangle fits in another one exactly when it fits with one of its
        # sides lying on a side of the other
        fits = any(
            fits_on(env[i:] + env[:i], card[j:] + card[:j])
            for i in range(SIDES)
            for j in range(SIDES)
        )
    print("YES" if fits else "NO")


main()
