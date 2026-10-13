"""Checker: "NO" exactly when the reference says so; otherwise "YES" and a
text of at most 20000 small letters that splits into dictionary words in
at least two different ways."""

import sys

LONGEST = 20000


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    words = set(data[1 : 1 + int(data[0])])
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] != want:
        fail("expected %s" % want)
    if want == "NO":
        if len(got) != 1:
            fail("nothing may follow NO")
        return
    if len(got) != 2:
        fail("expected one text after YES")
    text = got[1]
    if len(text) > LONGEST or not text.isalpha() or not text.islower():
        fail("the text must have at most %d small letters" % LONGEST)
    # ways[i]: the number of splits of text[:i], capped at 2
    ways = [1] + [0] * len(text)
    for i in range(1, len(text) + 1):
        for w in words:
            if len(w) <= i and text.startswith(w, i - len(w)):
                ways[i] = min(2, ways[i] + ways[i - len(w)])
    if ways[-1] < 2:
        fail("the text does not split in two different ways")


main()
