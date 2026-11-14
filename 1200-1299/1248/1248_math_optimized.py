import sys


DIGITS = 19
# The smallest exponent is -100, with at most 18 fractional digits.
SHIFT = 118
DECIMAL = 10


def sum_terms(lines, count):
    total = 0
    for _ in range(count):
        mantissa, _, exponent = next(lines).strip().lower().partition(b"e")
        whole, _, fraction = mantissa.partition(b".")
        scale = SHIFT + int(exponent or b"0") - len(fraction)
        total += int(whole + fraction) * DECIMAL**scale
    return total


def format_sum(total):
    if total == 0:
        return "0.000000000000000000e0"
    sign = "-" if total < 0 else ""
    digits = str(abs(total))
    exponent = len(digits) - 1 - SHIFT
    kept = digits[:DIGITS].ljust(DIGITS, "0")
    if digits[DIGITS : DIGITS + 1] >= "5":
        kept = str(int(kept) + 1)
        if len(kept) > DIGITS:
            kept = kept[:DIGITS]
            exponent += 1
    return f"{sign}{kept[0]}.{kept[1:]}e{exponent}"


def main():
    lines = sys.stdin.buffer
    print(format_sum(sum_terms(lines, int(next(lines)))))


if __name__ == "__main__":
    main()
