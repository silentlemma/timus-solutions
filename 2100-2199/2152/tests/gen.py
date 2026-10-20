"""Generate uniquely optimal package data: python gen.py MODE SEED.

Modes: 1 small mixed, 2 medium mixed, 3 maximal weight edits, 4 maximal partial
budget, 5 maximal unchanged, 6 maximal total, 7 fractional price edits,
8 small threshold boundaries, and 9 maximal distinct gains. Every selected edit is uniquely best,
and the selection ends at a strict gain boundary.
"""

import random
import sys

MAX_N = 200000
MAX_VALUE = 10**9
PERCENT = 100
MAX_DIGIT = 9
SMALL_N = 30
MEDIUM_MIN = 200
MEDIUM_N = 3000
SMALL_VALUE = 1000
SMALL_RATE = 20
WIDE_PLACE = 10**8
DISTINCT_THRESHOLD = 500000000
PRICE_N = 200
BOUNDARY_N = 20
BOUNDARY_DELTA = 3
MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_ALL = 3
MODE_PARTIAL = 4
MODE_UNCHANGED = 5
MODE_OVERFLOW = 6
MODE_PRICE = 7
MODE_BOUNDARY = 8
MODE_DISTINCT = 9


def options(value, threshold, rate):
    original = max(0, value - threshold) * rate
    best = 0
    ways = 0
    place = 1
    digits = value
    while digits:
        old_digit = digits % 10
        for new_digit in range(10):
            if new_digit == old_digit:
                continue
            new_value = value + (new_digit - old_digit) * place
            gain = max(0, new_value - threshold) * rate - original
            if gain > best:
                best, ways = gain, 1
            elif gain == best:
                ways += 1
        place *= 10
        digits //= 10
    return best, ways


def unique_budget(rows, limits, rng):
    mxw, mxp, a, b = limits
    gains = []
    for weight, price in rows:
        weight_gain, weight_ways = options(weight, mxw, a * PERCENT)
        price_gain, price_ways = options(price, mxp, b)
        gain = max(weight_gain, price_gain)
        ways = 0
        if weight_gain == gain:
            ways += weight_ways
        if price_gain == gain:
            ways += price_ways
        gains.append((gain, ways))
    gains.sort(reverse=True)
    budgets = [0]
    for index, (gain, ways) in enumerate(gains):
        if gain == 0 or ways != 1:
            break
        if index + 1 == len(gains) or gains[index + 1][0] < gain:
            budgets.append(index + 1)
    if len(budgets) > 1 and rng.randrange(SMALL_RATE) != 0:
        return rng.choice(budgets[1:])
    return 0


def random_value(rng, limit):
    width = rng.randrange(1, len(str(limit)) + 1)
    return rng.randint(1, min(limit, 10**width))


def mixed(rng, medium, boundary):
    if medium:
        n = rng.randint(MEDIUM_MIN, MEDIUM_N)
        value_limit = MAX_VALUE
    else:
        n = rng.randint(1, SMALL_N)
        value_limit = rng.choice((SMALL_VALUE, MAX_VALUE))
    mxw = random_value(rng, value_limit)
    mxp = random_value(rng, value_limit)
    a = rng.randint(1, SMALL_RATE)
    b = rng.randint(1, PERCENT)
    rows = []
    if boundary:
        n = rng.randint(1, BOUNDARY_N)
        for _ in range(n):
            weight = max(1, min(MAX_VALUE, mxw + rng.randint(-BOUNDARY_DELTA, BOUNDARY_DELTA)))
            price = max(1, min(MAX_VALUE, mxp + rng.randint(-BOUNDARY_DELTA, BOUNDARY_DELTA)))
            rows.append((weight, price))
    else:
        for _ in range(n):
            rows.append((random_value(rng, value_limit), random_value(rng, value_limit)))
    limits = (mxw, mxp, a, b)
    return rows, unique_budget(rows, limits, rng), limits


def maximal(rng, mode):
    if mode == MODE_UNCHANGED:
        limits = (MAX_VALUE, MAX_VALUE, MAX_VALUE, PERCENT)
        rows = [(rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)) for _ in range(MAX_N)]
        return rows, 0, limits
    if mode == MODE_OVERFLOW:
        rows = [(MAX_VALUE, MAX_VALUE)] * MAX_N
        return rows, MAX_N, (1, 1, MAX_VALUE, PERCENT)
    limits = (1, rng.randint(1, MAX_VALUE), MAX_VALUE, rng.randint(1, PERCENT))
    rows = []
    for index in range(MAX_N):
        if mode == MODE_PARTIAL and index < MAX_N // 2:
            weight = MAX_VALUE
        else:
            weight = rng.randint(WIDE_PLACE, MAX_DIGIT * WIDE_PLACE - 1)
        rows.append((weight, rng.randint(1, MAX_VALUE)))
    rng.shuffle(rows)
    budget = MAX_N // 2 if mode == MODE_PARTIAL else MAX_N
    return rows, budget, limits


def price_only(rng):
    n = rng.randint(1, PRICE_N)
    limits = (MAX_VALUE, 1, rng.randint(1, MAX_VALUE), rng.randint(1, PERCENT - 1))
    rows = [(MAX_DIGIT, random_value(rng, MAX_VALUE)) for _ in range(n)]
    return rows, unique_budget(rows, limits, rng), limits


def distinct_gains(rng):
    limits = (
        DISTINCT_THRESHOLD,
        rng.randint(1, MAX_VALUE),
        MAX_VALUE,
        rng.randint(1, PERCENT),
    )
    rows = [
        (rng.randint(WIDE_PLACE, DISTINCT_THRESHOLD - 1), rng.randint(1, MAX_VALUE))
        for _ in range(MAX_N)
    ]
    tails = sorted((weight % WIDE_PLACE for weight, _ in rows), reverse=True)
    budget = MAX_N // 2
    while budget < MAX_N and tails[budget - 1] == tails[budget]:
        budget += 1
    return rows, budget, limits


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode in (MODE_SMALL, MODE_MEDIUM, MODE_BOUNDARY):
        rows, budget, limits = mixed(rng, mode == MODE_MEDIUM, mode == MODE_BOUNDARY)
    elif mode in (MODE_ALL, MODE_PARTIAL, MODE_UNCHANGED, MODE_OVERFLOW):
        rows, budget, limits = maximal(rng, mode)
    elif mode == MODE_PRICE:
        rows, budget, limits = price_only(rng)
    elif mode == MODE_DISTINCT:
        rows, budget, limits = distinct_gains(rng)
    else:
        raise SystemExit("unknown mode")
    lines = ["%d %d" % (len(rows), budget), "%d %d %d %d" % limits]
    lines.extend("%d %d" % row for row in rows)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
