import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FIELDS = 3  # a test: a, b and the base k


def whole(x, k):
    out = ""
    while True:
        x, d = divmod(x, k)
        out = DIGITS[d] + out
        if not x:
            return out


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    out, pos = [], 0
    while data[pos] or data[pos + 1]:
        a, b, k = data[pos : pos + FIELDS]
        pos += FIELDS
        text, rest = whole(a // b, k), a % b
        if rest:
            # long division; a remainder seen before starts the period
            seen, digits = {}, []
            while rest and rest not in seen:
                seen[rest] = len(digits)
                rest *= k
                digits.append(DIGITS[rest // b])
                rest %= b
            frac = "".join(digits)
            if rest:
                frac = frac[: seen[rest]] + "(" + frac[seen[rest] :] + ")"
            text += "." + frac
        out.append(text)
    print("\n".join(out))


main()
