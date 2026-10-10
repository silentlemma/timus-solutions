import sys


def tokens(stream):
    """The numbers of the input one at a time, so that a million of them
    never sit in memory together."""
    for line in stream:
        yield from line.split()


def main():
    numbers = tokens(sys.stdin.buffer)
    n = int(next(numbers))
    known = {int(next(numbers)) for _ in range(n)}
    m = int(next(numbers))
    # every date the student wrote counts once for each time it is written
    print(sum(1 for _ in range(m) if int(next(numbers)) in known))


main()
