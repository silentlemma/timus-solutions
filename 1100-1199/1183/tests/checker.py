"""Checker: the printed line must be a regular bracket sequence, contain
the given brackets as a subsequence and be as short as the stored
answer."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def regular(s):
    stack = []
    for c in s:
        if c in "([":
            stack.append(c)
        elif not stack or stack.pop() + c not in ("()", "[]"):
            return False
    return not stack


def main():
    inp, ans, output = sys.argv[1:4]
    given = open(inp).read().strip()
    best = open(ans).read().strip()
    got = open(output).read().strip()
    if any(c not in "()[]" for c in got):
        fail("not brackets")
    if not regular(got):
        fail("not a regular sequence")
    it = iter(got)
    if not all(c in it for c in given):
        fail("the given brackets are not a subsequence")
    if len(got) != len(best):
        fail("length %d instead of %d" % (len(got), len(best)))


if __name__ == "__main__":
    main()
