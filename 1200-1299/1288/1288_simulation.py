import sys

SIGNAL = 10**6  # signal values are read in millionths
FACTOR = 10**3  # A has at most three decimals
WALL = 95
LOW = 35


def scaled(token, scale):
    """A non-negative decimal as an exact multiple of 1 / scale."""
    whole, _, frac = token.partition(".")
    digits = len(str(scale)) - 1
    return int(whole or "0") * scale + int((frac + "0" * digits)[:digits] or "0")


def main():
    words = iter(sys.stdin.read().split())

    def number():
        return int(next(words))

    n, d = number(), number()
    s1, e1, l1, s2, e2, l2 = number(), number(), number(), number(), number(), number()
    a = scaled(next(words), FACTOR)
    raw = [scaled(next(words), SIGNAL) for _ in range(n)]
    unit = SIGNAL * FACTOR
    # the front wall: the first value of 95 or more after a value of 35 or less
    surface, low = -1, False
    for i, x in enumerate(raw):
        if low and x >= WALL * SIGNAL:
            surface = i
            break
        low = low or x <= LOW * SIGNAL
    if surface < 0:
        print("No surface.")
        return
    out = ["Surface found at %d." % (surface + 1)]
    # after the wall every value is multiplied by 1 + (m - f) A, here in
    # units of 1 / (SIGNAL * FACTOR)
    value = [
        x * FACTOR if i <= surface else x * (FACTOR + (i - surface) * a) for i, x in enumerate(raw)
    ]
    bottom, low = -1, False
    for i in range(surface + 1, n):
        if low and i - surface >= d and value[i] >= WALL * unit:
            bottom = i
            break
        low = low or value[i] <= LOW * unit
    out.append("No bottom." if bottom < 0 else "Bottom found at %d." % (bottom - surface))
    end = bottom - 1 if bottom >= 0 else n - 1
    for channel, (start, stop, level) in enumerate(((s1, e1, l1), (s2, e2, l2)), 1):
        lo, hi = surface + start, min(surface + stop, end)
        if lo > hi:
            out.append("Channel %d: No search." % channel)
            continue
        best = max(range(lo, hi + 1), key=lambda i: (value[i], -i))
        if value[best] >= level * unit:
            out.append("Channel %d: Object at %d." % (channel, best - surface))
        else:
            out.append("Channel %d: No object." % channel)
    print("\n".join(out))


main()
