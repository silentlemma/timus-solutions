"""Checker: verify a legal route, its cost, and the minimum possible cost.
The expected route is not used because optimal routes need not be unique.
"""

import math
import re
import sys

MAX_ROUTE = 10_000
MAX_EMPLOYEE = 100_000_000_000_000
ARGUMENT_COUNT = 3
INTEGER = re.compile(r"[+-]?[0-9]+")


class Bad(Exception):
    pass


def optimum(start, target):
    if target <= start:
        return start - target
    if target % start == 0:
        return 0
    for divisor in range(1, math.isqrt(target) + 1):
        if target % divisor:
            continue
        for after in (divisor, target // divisor):
            for before in (after - 1, after + 1):
                if before >= start and before % start == 0:
                    return 1
    # Starts up to five reach a nearest multiple with cost at most two.
    # For six or seven, a factor coprime to six is adjacent to a multiple of six.
    # Otherwise a divisor six, eight, or nine gives a route with cost at most two.
    return 2


def check(source, expected, output):
    with open(source, encoding="utf-8") as stream:
        start, target = map(int, stream.read().split())
    with open(output, encoding="utf-8") as stream:
        words = stream.read().split()
    if len(words) < 2 or not all(INTEGER.fullmatch(word) for word in words):
        raise Bad("expected integer time, route length, and route")
    try:
        values = [int(word) for word in words]
    except ValueError:
        raise Bad("an integer is too long") from None
    reported, count = values[:2]
    if not 1 <= count <= MAX_ROUTE:
        raise Bad("route length is outside the allowed range")
    if len(values) != count + 2:
        raise Bad("route length does not match the number of employees")
    route = values[2:]
    if any(node < 1 or node > MAX_EMPLOYEE for node in route):
        raise Bad("an employee number is outside the allowed range")
    if route[0] != start or route[-1] != target:
        raise Bad("route endpoints do not match the input")
    cost = 0
    for before, after in zip(route, route[1:]):
        if before == after:
            raise Bad("adjacent employees must be different")
        if after < before or after % before:
            cost += abs(after - before)
    if reported != cost:
        raise Bad("reported time does not match the route cost")
    if reported != optimum(start, target):
        raise Bad("route does not have minimum time")


def main():
    try:
        check(*sys.argv[1 : 1 + ARGUMENT_COUNT])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
