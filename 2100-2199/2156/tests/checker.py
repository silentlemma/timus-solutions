"""Check that the answer is YES and that the two printed sets are
non-empty, split all conversations and have equal total interest."""

import sys

ARGS = 4


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n = data[0]
    a = data[1:n + 1]
    talk = [abs(a[i] - a[(i + 1) % n]) for i in range(n)]
    if open(expected).read().split()[0] != "YES":
        raise Bad("the stored answer is not YES")
    words = open(output).read().split()
    if not words or words[0] != "YES":
        raise Bad("expected YES")
    try:
        numbers = list(map(int, words[1:]))
    except ValueError:
        raise Bad("expected integers")
    parts = []
    pos = 0
    for _ in range(2):
        if pos >= len(numbers):
            raise Bad("a set is missing")
        size = numbers[pos]
        part = numbers[pos + 1:pos + 1 + size]
        if size < 1 or len(part) != size:
            raise Bad("each set must be non-empty and complete")
        parts.append(part)
        pos += 1 + size
    if pos != len(numbers):
        raise Bad("extra output")
    together = parts[0] + parts[1]
    if sorted(together) != list(range(1, n + 1)):
        raise Bad("the sets must split the conversations 1..n")
    first = sum(talk[i - 1] for i in parts[0])
    second = sum(talk[i - 1] for i in parts[1])
    if first != second:
        raise Bad("sums %d and %d differ" % (first, second))


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
