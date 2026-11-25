"""Accept any decimal number of at most 10000 digits 1/2 divisible by 2**N."""

import sys

MAX_DIGITS = 10000


def main():
    source, _, output = sys.argv[1:4]
    exponent = int(open(source).read())
    tokens = open(output).read().split()
    if len(tokens) != 1 or not 1 <= len(tokens[0]) <= MAX_DIGITS:
        raise SystemExit("expected one number of at most 10000 digits")
    number = tokens[0]
    if any(digit not in "12" for digit in number):
        raise SystemExit("only digits 1 and 2 are allowed")
    # Stream the residue: converting all 10000 digits would hit Python's int limit.
    divisor = 1 << exponent
    residue = 0
    for digit in number:
        residue = (residue * 10 + int(digit)) % divisor
    if residue:
        raise SystemExit("the number is not divisible by the required power of two")


if __name__ == "__main__":
    main()
