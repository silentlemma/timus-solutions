import sys


def main():
    values = map(int, sys.stdin.buffer.read().split())
    next(values)
    first = next(values)
    before = first
    inside = -first
    finished = inside

    # Track best prefix minima with the flip unstarted, active, or finished.
    # Update the finished state first to preserve the previous active state.
    for value in values:
        if inside > finished:
            finished = inside
        if value < finished:
            finished = value
        if before > inside:
            inside = before
        flipped = -value
        if flipped < inside:
            inside = flipped
        if value < before:
            before = value

    if inside > finished:
        finished = inside
    print(finished)


main()
