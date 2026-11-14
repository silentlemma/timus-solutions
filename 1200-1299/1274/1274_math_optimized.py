import sys


def parse(line):
    fields = line.split()
    fraction, slash, denominator = fields[-1].partition(b"/")
    if not slash:
        return int(fraction), 1
    den = int(denominator)
    num = int(fraction)
    if len(fields) == 1:
        return num, den
    whole = int(fields[0])
    return whole * den + (-num if fields[0].startswith(b"-") else num), den


def main():
    read = sys.stdin.buffer.readline
    an, ad = parse(read())
    operator = read().strip()
    bn, bd = parse(read())
    den = ad * bd
    if operator == b"+":
        num = an * bd + bn * ad
    elif operator == b"-":
        num = an * bd - bn * ad
    elif operator == b"*":
        num = an * bn
    else:
        num, den = an * bd, ad * bn
    if den < 0:
        num, den = -num, -den
    sign = "-" if num < 0 else ""
    whole, remainder = divmod(abs(num), den)
    if remainder:
        # Reduce only the remainder. The whole part is already final.
        a, b = den, remainder
        while b:
            a, b = b, a % b
        prefix = f"{whole} " if whole else ""
        print(f"{sign}{prefix}{remainder // a}/{den // a}")
    else:
        print(f"{sign}{whole}")


main()
