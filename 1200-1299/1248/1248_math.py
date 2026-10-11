import sys

DIGITS = 19
HALF = 5
# every input number is a whole multiple of 10^-SHIFT, and every sum has
# more than 19 digits once scaled
SHIFT = 300


def scaled(text):
    """The number times 10^SHIFT, as an exact integer."""
    mantissa, _, exp = text.lower().partition("e")
    whole, _, frac = mantissa.partition(".")
    sign = -1 if whole.startswith("-") else 1
    digits = whole.lstrip("+-") + frac
    return sign * int(digits or "0") * 10 ** (SHIFT + int(exp or "0") - len(frac))


def main():
    words = sys.stdin.read().split()
    total = sum(scaled(w) for w in words[1 : 1 + int(words[0])])
    if total == 0:
        print("0." + "0" * (DIGITS - 1) + "e0")
        return
    sign = "-" if total < 0 else ""
    total = abs(total)
    # keep 19 significant digits, rounding half up on the rest
    extra = len(str(total)) - DIGITS
    kept = (total + HALF * 10 ** (extra - 1)) // 10**extra
    if kept == 10**DIGITS:
        kept //= 10
        extra += 1
    text = str(kept)
    print("%s%s.%se%d" % (sign, text[0], text[1:], extra + DIGITS - 1 - SHIFT))


main()
