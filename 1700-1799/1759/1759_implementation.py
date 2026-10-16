import sys

DATES = 3
YEAR = 365
LEAP = 4
CENTURY = 100
LEAP_CENTURY = 400
MARCH = 3
MONTHS = 12
# the five months from March to July hold 153 days, and so do August to
# December, which makes the days before a month a simple formula
SPAN_DAYS = 153
SPAN_MONTHS = 5


def day_number(text):
    """Days from a fixed origin, counting years from March so that the
    leap day comes last."""
    d, m, y = (int(v) for v in text.split("."))
    if m < MARCH:
        y -= 1
        m += MONTHS
    leaps = y // LEAP - y // CENTURY + y // LEAP_CENTURY
    return YEAR * y + leaps + (SPAN_DAYS * (m - MARCH) + 2) // SPAN_MONTHS + d


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    best, answer = -1, 0
    for i in range(n):
        born, _, died = words[1 + DATES * i:1 + DATES * (i + 1)]
        life = day_number(died) - day_number(born) + 1
        # the list goes in order of death, so the first record holder died first
        if life > best:
            best, answer = life, i + 1
    print(answer)


main()
