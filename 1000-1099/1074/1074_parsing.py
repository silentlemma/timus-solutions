import sys

DIGITS = "0123456789"
# exponents beyond this either give zero or an answer longer than allowed
EXP_LIMIT = 1000
FAIL = "Not a floating point number"


def run(s, pos):
    start = pos
    while pos < len(s) and s[pos] in DIGITS:
        pos += 1
    return s[start:pos], pos


def convert(s, n):
    pos = 0
    negative = False
    if pos < len(s) and s[pos] in "+-":
        negative = s[pos] == "-"
        pos += 1
    whole, pos = run(s, pos)
    frac = ""
    if pos < len(s) and s[pos] == ".":
        frac, pos = run(s, pos + 1)
        if not frac:
            return FAIL
    elif not whole:
        return FAIL
    exp = 0
    if pos < len(s) and s[pos] in "eE":
        pos += 1
        sign = 1
        if pos < len(s) and s[pos] in "+-":
            sign = -1 if s[pos] == "-" else 1
            pos += 1
        power, pos = run(s, pos)
        if not power:
            return FAIL
        for c in power:
            exp = min(exp * 10 + int(c), EXP_LIMIT)
        exp *= sign
    if pos != len(s):
        return FAIL
    # the digits of the number with the decimal point after `point` of them
    mantissa = whole + frac
    point = len(whole) + exp

    def digit(i):
        return mantissa[i] if 0 <= i < len(mantissa) else "0"

    if mantissa.strip("0") == "":
        point = 0
    head = "".join(digit(i) for i in range(point)).lstrip("0") or "0"
    tail = "".join(digit(i) for i in range(point, point + n))
    out = head + ("." + tail if n > 0 else "")
    if negative and (head + tail).strip("0"):
        out = "-" + out
    return out


def main():
    lines = sys.stdin.buffer.read().decode("latin-1").split("\n")
    out = []
    for i in range(0, len(lines) - 1, 2):
        s = lines[i].rstrip("\r")
        if s == "#":
            break
        out.append(convert(s, int(lines[i + 1])))
    sys.stdout.write("".join(line + "\n" for line in out))


main()
