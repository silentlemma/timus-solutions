"""Checker: the same partition of the projects into classes as the
expected answer, in any order of classes and of projects inside a class,
each class ended by 0 and the count of classes first."""

import sys


def classes(text):
    words = text.split()
    if not words:
        return None
    count, pos, out = int(words[0]), 1, []
    for _ in range(count):
        members = []
        while pos < len(words) and words[pos] != "0":
            members.append(int(words[pos]))
            pos += 1
        if pos >= len(words):
            return None
        pos += 1
        out.append(frozenset(members))
    return None if pos != len(words) else set(out)


def main():
    _, expected, output = sys.argv[1:4]
    want, got = classes(open(expected).read()), classes(open(output).read())
    if got is None:
        print("malformed answer")
        sys.exit(1)
    if got != want:
        print("the classes differ from the expected ones")
        sys.exit(1)


if __name__ == "__main__":
    main()
