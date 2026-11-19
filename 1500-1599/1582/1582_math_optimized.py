import os
from sys import stdout

TOTAL = 1000
LIMB_DIGITS = 9


def decimal(token):
    mantissa, separator, exponent = token.lower().partition(b"e")
    mantissa = mantissa.removeprefix(b"+")
    point = mantissa.find(b".")
    scale = len(mantissa) - point - 1 if point >= 0 else 0
    if separator:
        scale -= int(exponent)
    # Normalize padding before constructing large integers or powers of ten.
    digits = mantissa.replace(b".", b"").lstrip(b"0")
    trimmed = digits.rstrip(b"0")
    scale -= len(digits) - len(trimmed)
    value = 0
    for start in range(0, len(trimmed), LIMB_DIGITS):
        chunk = trimmed[start : start + LIMB_DIGITS]
        value = value * 10 ** len(chunk) + int(chunk)
    if scale < 0:
        value *= 10**-scale
        scale = 0
    return value, scale


numerator, denominator = 1, 0
for token in open(0, "rb", buffering=0).read().split():
    value, scale = decimal(token)
    denominator = denominator * value + numerator * 10**scale
    numerator *= value
# Round the exact rational payout half up, without searching over integer payouts.
print((2 * TOTAL * numerator + denominator) // (2 * denominator))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
