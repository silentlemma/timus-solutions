from sys import stdin, stdout

CHUNK_DIGITS = 1000
RADIX = 10
LOG_NUMERATOR = 30103
LOG_DENOMINATOR = 100000


def emit(value, width):
    if width <= CHUNK_DIGITS:
        stdout.write(str(value).zfill(width))
        return
    half = width // 2
    high, low = divmod(value, RADIX**half)
    emit(high, width - half)
    emit(low, half)


n = int(stdin.read())
value = 2
for index in range(n):
    # This rational upper bound on log10(2) overestimates by at most one digit.
    width = value.bit_length() * LOG_NUMERATOR // LOG_DENOMINATOR + 1
    if value < RADIX ** (width - 1):
        width -= 1
    emit(value, width)
    stdout.write("\n")
    if index + 1 < n:
        value = value * value - value + 1
