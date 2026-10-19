"""Checker: n times MM:SS from 00:00 to 59:59, strictly decreasing, each one
showing every lit segment of its reading."""

import re
import sys

DIGITS = [
    "._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
    "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|",
]
COLUMNS = [0, 4, 10, 14]
WIDTH = 3
SECONDS = 60


class Bad(Exception):
    pass


def check(source, expected, output):
    lines = open(source).read().split()
    n = int(lines[0])
    got = open(output).read().split()
    if len(got) != n:
        raise Bad("expected %d times" % n)
    previous = SECONDS * SECONDS
    for r, word in enumerate(got):
        if not re.fullmatch(r"[0-5][0-9]:[0-5][0-9]", word):
            raise Bad("line %d: not a time" % (r + 1))
        value = int(word[:2]) * SECONDS + int(word[3:])
        if value >= previous:
            raise Bad("line %d: not below the previous time" % (r + 1))
        previous = value
        rows = lines[1 + 3 * r:4 + 3 * r]
        digits = [int(c) for c in word if c != ":"]
        for c, d in zip(COLUMNS, digits):
            shown = "".join(row[c:c + WIDTH] for row in rows)
            if any(x != "." and x != y for x, y in zip(shown, DIGITS[d])):
                raise Bad("line %d: %d does not fit the reading" % (r + 1, d))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
