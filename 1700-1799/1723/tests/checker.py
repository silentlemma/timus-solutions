"""Checker: a nonempty substring of the universal spell that occurs in it,
overlaps included, as many times as the expected answer does."""

import sys


class Bad(Exception):
    pass


def occurrences(text, word):
    return sum(text.startswith(word, i) for i in range(len(text)))


def check(source, expected, output):
    text = open(source).read().split()[0]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if len(got) != 1:
        raise Bad("expected one word")
    word = got[0]
    if word not in text:
        raise Bad("%s is not a substring of the spell" % word)
    count, best = occurrences(text, word), occurrences(text, want)
    if count != best:
        raise Bad("%s occurs %d times, the best spell %d" % (word, count, best))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
