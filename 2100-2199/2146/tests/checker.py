"""Check that the printed period is the stored one, that the printed drum
differs from the input in at most k sectors, and that its smallest
circular period is exactly the printed number."""

import sys

ARGS = 4


class Bad(Exception):
    pass


def smallest_period(text):
    n = len(text)
    for d in range(1, n + 1):
        if n % d == 0 and text == text[d:] + text[:d]:
            return d
    return n


def check(source, expected, output):
    data = open(source).read().split()
    n, k, s = int(data[0]), int(data[1]), data[2]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != 2 or not got[0].isdigit():
        raise Bad("expected a period and a drum")
    period, drum = int(got[0]), got[1]
    if period != want:
        raise Bad("period %d, expected %d" % (period, want))
    if len(drum) != n or not all("a" <= c <= "z" for c in drum):
        raise Bad("the drum must have %d lowercase letters" % n)
    changes = sum(a != b for a, b in zip(s, drum))
    if changes > k:
        raise Bad("%d changes, at most %d allowed" % (changes, k))
    if smallest_period(drum) != period:
        raise Bad("the smallest period of the drum is %d" % smallest_period(drum))


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
