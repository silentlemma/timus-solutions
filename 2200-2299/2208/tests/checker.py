"""Check every reported pair after applying the preceding point updates."""

import math
import sys


class Bad(Exception):
    pass


def read_lines(path):
    with open(path, encoding="utf-8") as stream:
        return stream.read().splitlines()


def check(source, expected, output):
    with open(source, encoding="utf-8") as stream:
        data = iter(map(int, stream.read().split()))
    size, count = next(data), next(data)
    values = [0] + [next(data) for _ in range(size)]
    answers = read_lines(expected)
    actual = read_lines(output)
    query = 0
    for _ in range(count):
        kind, left, right = next(data), next(data), next(data)
        if kind == 2:
            values[left] = right
            continue
        query += 1
        if query > len(actual):
            raise Bad("query %d: missing answer" % query)
        if query > len(answers):
            raise Bad("expected output has too few answers")
        words = actual[query - 1].split()
        if words == ["-1"]:
            if answers[query - 1].split() != ["-1"]:
                raise Bad("query %d: a valid pair exists" % query)
            continue
        if len(words) != 2:
            raise Bad("query %d: expected -1 or two positions" % query)
        try:
            first, second = map(int, words)
        except ValueError as error:
            raise Bad("query %d: positions must be integers" % query) from error
        if not left <= first <= right or not left <= second <= right:
            raise Bad("query %d: a position is outside the interval" % query)
        if first == second:
            raise Bad("query %d: positions must be different" % query)
        if math.gcd(values[first], values[second]) == 1:
            raise Bad("query %d: the selected values are coprime" % query)
    if len(actual) != query:
        raise Bad("expected %d answer lines, found %d" % (query, len(actual)))
    if len(answers) != query:
        raise Bad("expected output has the wrong number of answers")


def main():
    try:
        check(*sys.argv[1:])
    except (Bad, OSError, ValueError, StopIteration) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
