import sys
from fractions import Fraction

DAY = 24 * 60 * 60
MINUTE = 60
ELEMENTS = "AEFW"
# a line about an element: its code, the strong moment and power, the weak ones
FIELDS = 5


def seconds(text):
    h, m, s = map(int, text.split(":"))
    return (h * MINUTE + m) * MINUTE + s


def clock(t):
    return "%02d:%02d:%02d" % (t // (MINUTE * MINUTE), t // MINUTE % MINUTE, t % MINUTE)


def main():
    tok = sys.stdin.read().split()
    moments = {}
    for k in range(len(ELEMENTS)):
        code, strong, top, weak, low = tok[FIELDS * k : FIELDS * (k + 1)]
        moments[code] = (seconds(strong), int(top), seconds(weak), int(low))
    light, dark = tok[FIELDS * len(ELEMENTS)], tok[FIELDS * len(ELEMENTS) + 1]
    side = {e: light.count(e) - dark.count(e) for e in ELEMENTS}

    def power(e, t):
        # the power falls linearly from the strong moment to the weak one and
        # rises back over the rest of the day
        strong, top, weak, low = moments[e]
        fall, since = (weak - strong) % DAY, (t - strong) % DAY
        if since <= fall:
            return top + Fraction((low - top) * since, fall)
        return low + Fraction((top - low) * (since - fall), DAY - fall)

    def advantage(t):
        return sum(side[e] * power(e, t) for e in ELEMENTS if side[e])

    # the advantage is linear between the moments, so its largest value over
    # the day is at a moment or at either end of the day
    times = sorted(
        {0, DAY - 1} | {m[0] for m in moments.values()} | {m[2] for m in moments.values()}
    )
    best = max(times, key=lambda t: (advantage(t), -t))
    if advantage(best) <= 0:
        print("We can't win!")
    else:
        print(clock(best))
        print("%.2f" % advantage(best))


main()
