"""Check the digit edits, their exact optimal fee, and the reported real total."""

from decimal import Decimal, DecimalException, InvalidOperation, localcontext
import sys

PERCENT = 100
MAX_DIGIT = 9
DECIMAL_PRECISION = 80
ERROR_SCALE = 10**9
HEADER_SIZE = 6


class Bad(Exception):
    pass


def fee(value, threshold, rate):
    return max(0, value - threshold) * rate


def best_gain(value, threshold, rate):
    old_fee = fee(value, threshold, rate)
    best = 0
    place = 1
    digits = value
    while digits:
        digit = digits % 10
        candidate = value + (MAX_DIGIT - digit) * place
        best = max(best, fee(candidate, threshold, rate) - old_fee)
        place *= 10
        digits //= 10
    return best


def changed_digits(old, new):
    if new < 0:
        raise Bad("negative package data")
    before = str(old)
    after = str(new)
    if len(after) > len(before):
        raise Bad("a digit was added")
    after = after.zfill(len(before))
    return sum(left != right for left, right in zip(before, after))


def check(source, expected, output):
    del expected
    with open(source, encoding="utf-8") as stream:
        data = list(map(int, stream.read().split()))
    n, k, mxw, mxp, a, b = data[:HEADER_SIZE]
    with open(output, encoding="utf-8") as stream:
        got = stream.read().split()
    if len(got) != 1 + 2 * n:
        raise Bad("expected one total and one pair per package")
    try:
        reported = Decimal(got[0])
    except InvalidOperation as error:
        raise Bad("the total is not a real number") from error
    if not reported.is_finite():
        raise Bad("the total must be finite")
    if not all(token.isascii() and token.isdigit() for token in got[1:]):
        raise Bad("package data must be nonnegative integers")

    rate = a * PERCENT
    original_total = 0
    actual_total = 0
    changed = 0
    gains = []
    for index in range(n):
        offset = HEADER_SIZE + 2 * index
        weight, price = data[offset : offset + 2]
        offset = 1 + 2 * index
        new_weight, new_price = map(int, got[offset : offset + 2])
        changes = changed_digits(weight, new_weight) + changed_digits(price, new_price)
        if changes > 1:
            raise Bad("package %d has more than one changed digit" % (index + 1))
        changed += changes
        if changed > k:
            raise Bad("too many packages were changed")
        original_total += fee(weight, mxw, rate) + fee(price, mxp, b)
        actual_total += fee(new_weight, mxw, rate) + fee(new_price, mxp, b)
        gains.append(max(best_gain(weight, mxw, rate), best_gain(price, mxp, b)))

    gains.sort(reverse=True)
    optimal_total = original_total + sum(gains[:k])
    if actual_total != optimal_total:
        raise Bad("the package data do not attain the maximal fee")
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        answer = Decimal(optimal_total) / PERCENT
        tolerance = max(Decimal(1), abs(answer)) / ERROR_SCALE
        if abs(reported - answer) > tolerance:
            raise Bad("the reported total disagrees with the package data")


def main():
    try:
        check(*sys.argv[1:])
    except (Bad, ValueError, OSError, DecimalException) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
