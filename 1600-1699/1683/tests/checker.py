"""Checker: as many folds as the expected answer (the least possible),
each measuring between 1 cm and half of the current strip, ending with a
strip of 1 cm."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not words:
        raise Bad("empty output")
    count = int(words[0])
    if count != want:
        raise Bad("%d folds instead of %d" % (count, want))
    if len(words) != count + 1:
        raise Bad("%d fold lengths for %d folds" % (len(words) - 1, count))
    length = n
    for word in words[1:]:
        x = int(word)
        if not 1 <= x <= length - x:
            raise Bad("cannot fold %d cm of a strip of %d cm" % (x, length))
        length -= x
    if length != 1:
        raise Bad("the strip ends %d cm long" % length)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
