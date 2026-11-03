from sys import stdin, stdout

PI = 3.141592653589793
DENOMINATORS = (156, 110, 72, 42, 20, 6)
DECIMAL_SCALE = 1000000
DECIMAL_WIDTH = 6
ROUND_HALF = 0.5
n = int(stdin.read())
if n == 1:
    stdout.write("1")
else:
    x = PI / n
    square, series = x * x, 1.0
    # Horner form through x**13; the next alternating term is <7e-10.
    for denominator in DENOMINATORS:
        series = 1.0 - square * series / denominator
    radius = 1.0 + 1.0 / (x * series)
    scaled = int(radius * DECIMAL_SCALE + ROUND_HALF)
    whole, fraction = divmod(scaled, DECIMAL_SCALE)
    stdout.write(str(whole) + "." + str(fraction).zfill(DECIMAL_WIDTH))
