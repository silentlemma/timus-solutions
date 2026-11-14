MODULUS = 9973
PERIOD_SCALE = 5219
PERIOD_SHIFT = 2283
LINEAR_TERM = 3
SCALE_OFFSET = 7


def solve(n):
    periods, rest = divmod(n, MODULUS)
    scale, shift = PERIOD_SCALE, PERIOD_SHIFT
    value = 0
    # Compose the same affine map for every complete period.
    while periods:
        if periods & 1:
            value = (scale * value + shift) % MODULUS
        shift = (scale + 1) * shift % MODULUS
        scale = scale * scale % MODULUS
        periods >>= 1
    for x in range(1, rest + 1):
        square = x * x % MODULUS
        cube = square * x % MODULUS
        fifth = cube * square % MODULUS
        value = ((fifth - x + SCALE_OFFSET) * value + cube + LINEAR_TERM * x - fifth) % MODULUS
    return value


if __name__ == "__main__":
    print(solve(int(input())))
