"""Checker: Impossible exactly when expected; otherwise the expected
number of interpreters, each for two different languages of at most ten
letters, such that every two teams of different languages can talk
through languages that no other team speaks."""

import sys
from collections import deque

LONGEST = 10  # letters in a language, interpreters' ones too


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    words = open(source).read().split()
    n = int(words[0])
    teams = set(words[1 : 1 + n])
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[0] == "Impossible":
        if got != ["Impossible"]:
            fail("expected Impossible")
        return
    if not got or not got[0].isdigit() or int(got[0]) != int(want[0]):
        fail("expected %s interpreters" % want[0])
    if len(got) != 1 + int(want[0]):
        fail("expected %s lines of two languages" % want[0])
    adj = {}
    for pair in got[1:]:
        parts = pair.split("-")
        if (
            len(parts) != 2
            or not all(p.isalpha() and p.islower() and len(p) <= LONGEST for p in parts)
            or parts[0] == parts[1]
        ):
            fail("%s is not two different languages" % pair)
        a, b = parts
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    for start in teams:
        # walk only through languages no team speaks
        seen = {start}
        queue = deque([start])
        while queue:
            lang = queue.popleft()
            if lang != start and lang in teams:
                continue
            for other in adj.get(lang, ()):
                if other not in seen:
                    seen.add(other)
                    queue.append(other)
        if not teams <= seen:
            fail("teams of %s cannot talk to everyone in private" % start)


main()
