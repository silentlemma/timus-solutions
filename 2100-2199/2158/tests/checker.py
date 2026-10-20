"""Check the multiset and both progressions; compare impossibility with the stored answer."""

import sys
from collections import Counter


class Bad(Exception):
    pass


def is_arithmetic(values):
    if len(values) <= 2:
        return True
    difference = values[1] - values[0]
    return all(values[i] - values[i - 1] == difference for i in range(2, len(values)))


def is_geometric(values):
    if len(values) == 1:
        return True
    if 0 in values:
        return all(value == 0 for value in values)
    first, second = values[:2]
    return all(values[i] * first == values[i - 1] * second for i in range(2, len(values)))


def check(source, expected, output):
    with open(source, encoding="utf-8") as stream:
        data = list(map(int, stream.read().split()))
    size = data[0]
    with open(expected, encoding="utf-8") as stream:
        answer = stream.read().split()
    with open(output, encoding="utf-8") as stream:
        tokens = stream.read().split()
    if tokens == ["-1"]:
        if answer != ["-1"]:
            raise Bad("a partition exists")
        return
    try:
        values = list(map(int, tokens))
    except ValueError:
        raise Bad("expected integer tokens") from None
    if len(values) != size + 1:
        raise Bad("expected a length and all input values")
    count = values[0]
    if not 1 <= count < size:
        raise Bad("both progressions must be nonempty")
    if Counter(values[1:]) != Counter(data[1:]):
        raise Bad("the values do not match the input multiset")
    arithmetic = values[1 : count + 1]
    geometric = values[count + 1 :]
    if not is_arithmetic(arithmetic):
        raise Bad("the first progression is not arithmetic")
    if not is_geometric(geometric):
        raise Bad("the second progression is not geometric with a nonzero ratio")


def main():
    try:
        check(*sys.argv[1:])
    except (Bad, OSError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
