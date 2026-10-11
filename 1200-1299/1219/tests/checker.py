"""Checker: exactly 1000000 lowercase letters, every letter at most 40000
times, every two consecutive letters at most 2000 times and every three
at most 100 times."""

import string
import sys
from collections import Counter

LENGTH = 1000000
LIMITS = {1: 40000, 2: 2000, 3: 100}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    output = sys.argv[3]
    text = open(output).read().split()
    if len(text) != 1:
        fail("expected a single line of letters")
    s = text[0]
    if len(s) != LENGTH or set(s) - set(string.ascii_lowercase):
        fail("expected %d lowercase letters, got %d characters" % (LENGTH, len(s)))
    for size, limit in LIMITS.items():
        word, count = Counter(s[i : i + size] for i in range(len(s) - size + 1)).most_common(1)[0]
        if count > limit:
            fail("%r occurs %d times, more than %d" % (word, count, limit))


if __name__ == "__main__":
    main()
