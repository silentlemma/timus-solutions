import sys
from decimal import Decimal, localcontext

MOD = 998_244_353
MAX_N = 100_000
MAX_VALUE = 100_000_000
SLOT_DIGITS = len(str(MAX_N * MAX_VALUE * (MOD - 1)))


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, days = data[:2]
    values = data[2:]
    inverses = [0] * n
    inverses[1] = 1
    kernel = [1] * n
    # Repeated prefix sums have coefficients C(days + i - 1, i).
    for i in range(1, n):
        if i > 1:
            inverses[i] = MOD - (MOD // i) * inverses[MOD % i] % MOD
        kernel[i] = kernel[i - 1] * (days + i - 1) % MOD * inverses[i] % MOD

    # Each exact convolution coefficient fits in one decimal slot without carries.
    pattern = f"%0{SLOT_DIGITS}d"
    left = Decimal("".join(pattern % value for value in reversed(values)))
    right = Decimal("".join(pattern % value for value in reversed(kernel)))
    with localcontext() as context:
        context.prec = 2 * n * SLOT_DIGITS
        context.Emax = context.prec
        product = str(left * right)
    digits = product[-n * SLOT_DIGITS :].zfill(n * SLOT_DIGITS)
    answer = [
        str(int(digits[i : i + SLOT_DIGITS]) % MOD)
        for i in range((n - 1) * SLOT_DIGITS, -1, -SLOT_DIGITS)
    ]
    print(" ".join(answer))


if __name__ == "__main__":
    main()
