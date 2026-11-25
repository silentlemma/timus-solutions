"""Reproduce the two prime products embedded in the neighbouring Python solution."""

from math import isqrt, prod
from textwrap import wrap

SMALL_LIMIT = 1000
RATIO_LIMIT = 10**9
HEX_WIDTH = 70


def main():
    limit = isqrt(RATIO_LIMIT)
    prime = bytearray([1]) * (limit + 1)
    prime[:2] = b"\0\0"
    for divisor in range(2, isqrt(limit) + 1):
        if prime[divisor]:
            for composite in range(divisor * divisor, limit + 1, divisor):
                prime[composite] = 0
    for name, low, high in (
        ("SMALL_PRODUCT", 2, SMALL_LIMIT),
        ("LARGE_PRODUCT", SMALL_LIMIT + 1, limit),
    ):
        product = prod(value for value in range(low, high + 1) if prime[value])
        print(f"{name} = int(")
        parts = wrap(format(product, "x"), HEX_WIDTH)
        for index, part in enumerate(parts):
            print(f'    "{part}"' + ("," if index == len(parts) - 1 else ""))
        print("    HEX_BASE,\n)")


if __name__ == "__main__":
    main()
