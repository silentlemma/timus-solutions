"""Checker: Yes exactly when expected; otherwise No and a line of pieces,
each a nonempty prefix of the first word, that together spell the
second word."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    word, last = open(source).read().split()[:2]
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or got[0] != want[0]:
        raise Bad("expected %s, got %s" % (want[0], got[0] if got else "nothing"))
    if got[0] == "Yes":
        if len(got) != 1:
            raise Bad("extra output after Yes")
        return
    pieces = got[1:]
    for piece in pieces:
        if not word.startswith(piece):
            raise Bad("%s... is not a prefix of the word" % piece[:20])
    if "".join(pieces) != last:
        raise Bad("the pieces do not spell the last word")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
