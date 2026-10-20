"""Check a partition into friendship cliques of two or three vertices.

The minimum degree condition guarantees a partition, so NO is never valid.
"""

import sys
from pathlib import Path

MAX_GROUP = 3
ARGUMENT_COUNT = 3


class Bad(Exception):
    pass


def check(source, expected, output):
    data = Path(source).read_text(encoding="utf-8").split()
    n = int(data[0])
    graph = data[1:]
    got = Path(output).read_text(encoding="utf-8").split()
    if not got or got[0] != "YES":
        raise Bad("expected YES and a valid partition")
    if len(got) < 2 or len(got) > 2 * n + 2:
        raise Bad("invalid number of output tokens")
    try:
        values = [int(token) for token in got[1:]]
    except ValueError:
        raise Bad("expected integer group sizes and vertices") from None
    count = values[0]
    if not (n + MAX_GROUP - 1) // MAX_GROUP <= count <= n // 2:
        raise Bad("invalid number of groups")
    seen = [False] * n
    position = 1
    for index in range(count):
        if position == len(values):
            raise Bad("missing group %d" % (index + 1))
        size = values[position]
        position += 1
        if size not in (2, MAX_GROUP):
            raise Bad("group %d must contain two or three vertices" % (index + 1))
        if position + size > len(values):
            raise Bad("incomplete group %d" % (index + 1))
        group = values[position : position + size]
        position += size
        for vertex in group:
            if not 1 <= vertex <= n:
                raise Bad("vertex is outside the valid range")
            if seen[vertex - 1]:
                raise Bad("vertex %d is used more than once" % vertex)
            seen[vertex - 1] = True
        for first in range(size):
            for second in range(first):
                if graph[(group[first] - 1) * n + group[second] - 1] != "1":
                    raise Bad("group %d contains vertices that are not friends" % (index + 1))
    if position != len(values):
        raise Bad("extra tokens after the last group")
    if not all(seen):
        raise Bad("some vertices do not belong to any group")


def main():
    if len(sys.argv) != ARGUMENT_COUNT + 1:
        print("usage: python checker.py INPUT EXPECTED OUTPUT")
        sys.exit(1)
    try:
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
