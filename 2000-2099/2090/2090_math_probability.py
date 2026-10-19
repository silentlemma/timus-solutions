import sys

DECIMAL_PLACES = 12
RADIX = 10


def probability(numerator, denominator):
    fraction = 0
    scale = 1
    for _ in range(DECIMAL_PLACES):
        numerator *= RADIX
        fraction = fraction * RADIX + numerator // denominator
        numerator %= denominator
        scale *= RADIX
    if 2 * numerator >= denominator:
        fraction += 1

    whole, fraction = divmod(fraction, scale)
    if fraction == 0:
        return str(whole)
    digits = str(fraction).zfill(DECIMAL_PLACES).rstrip("0")
    return f"{whole}.{digits}"


def main():
    (
        speed,
        _distance,
        _width_engels,
        width_marx,
        green_engels,
        yellow_engels,
        green_marx,
        yellow_marx,
    ) = map(int, sys.stdin.buffer.read().split())

    period = speed * (green_engels + yellow_engels + green_marx + yellow_marx)
    # The other two phases give ties; crossing Marx shifts the winning intervals.
    crosswalk = speed * (green_engels + yellow_marx) - width_marx
    print(probability(crosswalk, period), probability(width_marx, period))


if __name__ == "__main__":
    main()
