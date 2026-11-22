from itertools import islice
from os import _exit, read, write

BUFFER_SIZE = 8192


def numbers():
    tail = b""
    while chunk := read(0, BUFFER_SIZE):
        parts = (tail + chunk).split()
        tail = parts.pop() if chunk[-1:] > b" " else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


def intersect(values):
    common = set(islice(values, next(values)))
    second = islice(values, next(values))
    common.intersection_update(second)
    # set intersection may stop once every candidate is found. Consume the
    # remaining second-list values before reading the third length.
    for _ in second:
        pass
    if common:
        common.intersection_update(islice(values, next(values)))
    return common


def main():
    values = numbers()
    common = intersect(values)
    write(1, str(len(common)).encode() + b"\n")
    _exit(0)


main()
