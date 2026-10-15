"""Checker: IMPOSSIBLE exactly when expected; otherwise an expression in
the grammar, without spaces, at most 100000 characters, with the numbers
1..N in increasing order, whose value is the permutation."""

import sys

LONGEST = 100000
NONE = "IMPOSSIBLE"


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n = int(data[0])
    perm = [int(w) for w in data[1:1 + n]]
    want = open(expected).read().strip()
    text = open(output).read().strip()
    if want == NONE or text == NONE:
        if want != text:
            raise Bad("expected %r, got %r" % (want[:30], text[:30]))
        return
    if len(text) > LONGEST:
        raise Bad("the expression is longer than %d" % LONGEST)
    pos = 0
    numbers = []

    def peek():
        return text[pos] if pos < len(text) else ""

    def expression():
        nonlocal pos
        parts = [sequence()]
        while peek() == "*":
            pos += 1
            parts.append(sequence())
        return ("star", parts)

    def sequence():
        nonlocal pos
        if peek() != "(":
            raise Bad("a sequence must start with ( at %d" % pos)
        pos += 1
        items = [element()]
        while peek() == ",":
            pos += 1
            items.append(element())
        if peek() != ")":
            raise Bad("expected ) at %d" % pos)
        pos += 1
        return ("seq", items)

    def element():
        nonlocal pos
        if peek() == "(":
            return expression()
        start = pos
        while peek().isdigit():
            pos += 1
        if start == pos or text[start] == "0":
            raise Bad("expected a number at %d" % start)
        value = int(text[start:pos])
        numbers.append(value)
        return ("num", value)

    tree = expression()
    if pos != len(text):
        raise Bad("unexpected text at %d" % pos)
    if numbers != list(range(1, n + 1)):
        raise Bad("the numbers are not 1..%d in increasing order" % n)
    # the value: a star of parts lists them from the last to the first
    got = []
    todo = [tree]
    while todo:
        kind, body = todo.pop()
        if kind == "num":
            got.append(body)
        elif kind == "seq":
            todo.extend(reversed(body))
        else:
            todo.extend(body)
    if got != perm:
        raise Bad("the expression gives another permutation")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


# the parser recurses a few levels per nesting level, up to about 10^5
sys.setrecursionlimit(1000000)
main()
