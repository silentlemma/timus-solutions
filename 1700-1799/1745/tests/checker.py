"""Checker: a correct bracket sequence made of distinct words, as long as
the expected one, with the length and word count stated right."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    pieces = words[1:n + 1]
    best = int(open(expected).read().split()[0])
    lines = open(output).read().split("\n")
    head = lines[0].split()
    if len(head) != 2 or not all(w.isdigit() for w in head):
        raise Bad("expected the length and the word count")
    length, k = map(int, head)
    used = lines[1].split() if len(lines) > 1 else []
    if len(used) != k or not all(w.isdigit() for w in used):
        raise Bad("expected %d word numbers" % k)
    used = [int(w) for w in used]
    if len(set(used)) != k or not all(1 <= i <= n for i in used):
        raise Bad("the words are not distinct numbers from 1 to n")
    text = "".join(pieces[i - 1] for i in used)
    depth = 0
    for c in text:
        depth += 1 if c == "(" else -1
        if depth < 0:
            raise Bad("a prefix closes more than it opens")
    if depth:
        raise Bad("the sequence does not close all brackets")
    if len(text) != length:
        raise Bad("the stated length %d is not %d" % (length, len(text)))
    if length != best:
        raise Bad("length %d, the longest is %d" % (length, best))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
