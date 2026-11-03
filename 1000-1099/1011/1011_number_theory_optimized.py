from sys import stdin, stdout

HUNDREDTHS = 100
WHOLE = 100 * HUNDREDTHS


def hundredths(text):
    integer, _, fraction = text.partition(".")
    return int(integer) * HUNDREDTHS + int((fraction + "00")[:2])


p, q = map(hundredths, stdin.read().split())
a, b, c, d = 0, 1, 1, 0
while True:
    numerator, denominator = a + c, b + d
    if WHOLE * numerator <= p * denominator:
        # Every skipped mediant remains at or below the lower endpoint.
        steps = (p * b - WHOLE * a) // (WHOLE * c - p * d)
        a += steps * c
        b += steps * d
    elif WHOLE * numerator >= q * denominator:
        # Equality is excluded at both ends of the open interval.
        steps = (WHOLE * c - q * d) // (q * b - WHOLE * a)
        c += steps * a
        d += steps * b
    else:
        stdout.write(str(denominator))
        break
