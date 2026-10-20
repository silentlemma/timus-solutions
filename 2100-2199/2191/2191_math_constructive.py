import sys

DIGITS = 18
POWER = 10**DIGITS


def number(numerator, denominator):
    """Print a nonnegative fraction with at most DIGITS decimals, truncated."""
    scaled = numerator * POWER // denominator
    whole, fraction = divmod(scaled, POWER)
    if not fraction:
        return str(whole)
    return f"{whole}.{fraction:0{DIGITS}d}".rstrip("0")


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    xs = data[1 : 2 * n + 1 : 2]
    ys = data[2 : 2 * n + 2 : 2]
    output = []

    def term(numerator, denominator, root, constant=False):
        # Writes c |x - root| with c = numerator / denominator as one term.
        if numerator < 0:
            sign, numerator = "-", -numerator
        else:
            sign = "+" if output else ""
        if constant:
            output.append(f"{sign}|0x+{number(numerator, denominator)}|")
            return
        shift = numerator * root
        inside = "-" if shift >= 0 else "+"
        coefficient = number(numerator, denominator)
        output.append(f"{sign}|{coefficient}x{inside}{number(abs(shift), denominator)}|")

    # A kink at x_i where the slope turns from s to t is (t - s) / 2 |x - x_i|.
    for i in range(1, n - 1):
        left_dx, left_dy = xs[i] - xs[i - 1], ys[i] - ys[i - 1]
        right_dx, right_dy = xs[i + 1] - xs[i], ys[i + 1] - ys[i]
        term(right_dy * left_dx - left_dy * right_dx, 2 * left_dx * right_dx, xs[i])

    first_dx, first_dy = xs[1] - xs[0], ys[1] - ys[0]
    last_dx, last_dy = xs[-1] - xs[-2], ys[-1] - ys[-2]
    # On [x_1, x_N] the kinks add (t - s) / 2 times x - x_i; the term at x_1
    # restores the first slope and a constant fixes the value at x_1.
    term(first_dy * last_dx + last_dy * first_dx, 2 * first_dx * last_dx, xs[0])
    span = xs[-2] - xs[0]
    term(
        2 * ys[0] * last_dx - last_dy * span + (ys[-2] - ys[0]) * last_dx,
        2 * last_dx,
        0,
        True,
    )
    sys.stdout.write("".join(output) + "\n")


main()
