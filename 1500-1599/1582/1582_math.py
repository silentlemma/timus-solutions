import sys

TOTAL = 1000
MAX_ODD = 100
OUTCOMES = 3


def decimal(token):
    parts = token.lower().split('e')
    mantissa = parts[0]
    exponent = int(parts[1]) if len(parts) == 2 else 0
    point = mantissa.find('.')
    scale = len(mantissa) - point - 1 if point >= 0 else 0
    scale -= exponent
    value = int(mantissa.replace('.', ''))
    if scale < 0:
        value *= 10 ** -scale
        scale = 0
    return value, scale


def main():
    sys.set_int_max_str_digits(0)
    odds = [decimal(v) for v in sys.stdin.read().split()]
    numerator = 1
    denominator = 0
    for value, scale in odds:
        denominator = denominator * value + numerator * 10 ** scale
        numerator *= value
    numerator *= TOTAL
    # betting in proportion to 1 / k on every outcome pays the same whatever
    # happens, and any other split pays less on some outcome
    low, high = 0, TOTAL * MAX_ODD // OUTCOMES + 1
    while low + 1 < high:
        middle = (low + high) // 2
        if 2 * numerator >= (2 * middle - 1) * denominator:
            low = middle
        else:
            high = middle
    print(low)


main()
