import sys
from math import gcd


def parse(line):
    """A fraction "-7 3/4", "-7/11" or "11" as a numerator and denominator."""
    line = line.strip()
    sign = -1 if line.startswith("-") else 1
    whole, num, den = 0, 0, 1
    for token in line.lstrip("-").split():
        if "/" in token:
            num, den = (int(x) for x in token.split("/"))
        else:
            whole = int(token)
    return sign * (whole * den + num), den


def show(num, den):
    if den < 0:
        num, den = -num, -den
    g = gcd(num, den)
    num, den = num // g, den // g
    sign = "-" if num < 0 else ""
    whole, rest = divmod(abs(num), den)
    if not rest:
        return "%s%d" % (sign, whole)
    if not whole:
        return "%s%d/%d" % (sign, rest, den)
    return "%s%d %d/%d" % (sign, whole, rest, den)


def main():
    lines = sys.stdin.read().split("\n")
    an, ad = parse(lines[0])
    op = lines[1].strip()
    bn, bd = parse(lines[2])
    if op == "+":
        result = an * bd + bn * ad, ad * bd
    elif op == "-":
        result = an * bd - bn * ad, ad * bd
    elif op == "*":
        result = an * bn, ad * bd
    else:
        result = an * bd, ad * bn
    print(show(*result))


main()
