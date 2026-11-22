INF = 10000
PINS = 10
MAX_BONUS_MULTIPLIER = 3


def score(totals):
    l0, l1, l2, l3 = 0, INF, INF, INF
    h0, h1, h2, h3 = 0, -INF, -INF, -INF
    for total in totals[:-1]:
        if total < PINS:
            low = min(l0, l1, l2 + total, l3 + total) + total
            high = max(h0, h1 + total, h2 + total, h3 + 2 * total) + total
            l0, l1, l2, l3 = low, INF, INF, INF
            h0, h1, h2, h3 = high, -INF, -INF, -INF
        else:
            low1 = min(l0, l1, l2 + PINS, l3 + PINS) + PINS
            high1 = max(
                h0 + PINS, h1 + 2 * PINS - 1, h2 + 2 * PINS, h3 + MAX_BONUS_MULTIPLIER * PINS - 1
            )
            low2, low3 = min(l0, l1 + PINS) + PINS, min(l2, l3 + PINS) + 2 * PINS
            high2, high3 = max(h0, h1 + PINS) + PINS, max(h2, h3 + PINS) + 2 * PINS
            l0, l1, l2, l3 = INF, low1, low2, low3
            h0, h1, h2, h3 = -INF, high1, high2, high3
    last = totals[-1]
    if last < PINS:
        low = min(l0, l1, l2 + last, l3 + last)
        high = max(h0, h1 + last, h2 + last, h3 + 2 * last)
    elif last <= 2 * PINS:
        low = min(l0, l1, l2 + PINS, l3 + PINS)
        high = max(h0, h1 + PINS, h2 + last, h3 + last + PINS)
    else:
        low = min(l0, l1 + PINS, l2 + 2 * PINS, l3 + MAX_BONUS_MULTIPLIER * PINS)
        high = max(h0, h1 + PINS, h2 + 2 * PINS, h3 + MAX_BONUS_MULTIPLIER * PINS)
    return low + last, high + last


totals = list(map(int, open(0, "rb", buffering=0).read().split()))
low, high = score(totals)
open(1, "wb", buffering=0).write((str(low) + " " + str(high) + "\n").encode())
