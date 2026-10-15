import math

SCALE = 1000
HALF_TURN = 180 * SCALE
FULL_TURN = 2 * HALF_TURN
DIGITS = 3


def thousandths(text):
    whole, _, part = text.partition(".")
    return int(whole or 0) * SCALE + int((part + "0" * DIGITS)[:DIGITS])


def main():
    radius_text, angle_text = input().split()
    r = float(radius_text)
    a = thousandths(angle_text)
    # each shore point shows an arc of 2a, so the walk along the shore
    # covers 360 - 2a degrees; chords grow slower than their angles, so
    # it is shortest as full 2a chords and one short chord for the rest
    steps = HALF_TURN // a
    rest = FULL_TURN - steps * 2 * a

    def chord(thousandths_of_degree):
        return 2 * r * math.sin(math.radians(thousandths_of_degree / SCALE) / 2)

    print("%.7f" % (r + (steps - 1) * chord(2 * a) + chord(rest)))


main()
