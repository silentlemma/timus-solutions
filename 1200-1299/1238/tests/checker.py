"""Checker: the output must be a folded sequence (letters, and X(S) with
an integer X > 1 written without leading zeros) that unfolds to the input
and is as short as the reference answer."""

import sys


class Bad(Exception):
    pass


def unfold(text, pos=0):
    """Unfolds text[pos:] up to a closing bracket or the end."""
    parts = []
    while pos < len(text) and text[pos] != ")":
        c = text[pos]
        if c.isupper():
            parts.append(c)
            pos += 1
        elif c.isdigit():
            end = pos
            while end < len(text) and text[end].isdigit():
                end += 1
            count = text[pos:end]
            if count[0] == "0" or int(count) < 2:
                raise Bad("bad repeat count %s" % count)
            if end >= len(text) or text[end] != "(":
                raise Bad("a count without a bracket")
            inner, pos = unfold(text, end + 1)
            if pos >= len(text) or text[pos] != ")":
                raise Bad("an unclosed bracket")
            if not inner:
                raise Bad("an empty bracket")
            parts.append(inner * int(count))
            pos += 1
        else:
            raise Bad("unexpected character %r" % c)
    return "".join(parts), pos


def main():
    inp, ans, output = sys.argv[1:4]
    source = open(inp).read().split()[0]
    want = len(open(ans).read().split()[0])
    tokens = open(output).read().split()
    if len(tokens) != 1:
        print("expected one word")
        sys.exit(1)
    folded = tokens[0]
    try:
        text, pos = unfold(folded)
        if pos != len(folded):
            raise Bad("an unmatched closing bracket")
    except Bad as e:
        print(e)
        sys.exit(1)
    if text != source:
        print("unfolds to a different sequence")
        sys.exit(1)
    if len(folded) != want:
        print("length %d, the shortest is %d" % (len(folded), want))
        sys.exit(1)


if __name__ == "__main__":
    main()
