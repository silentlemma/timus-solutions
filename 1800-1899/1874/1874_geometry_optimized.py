from sys import stdin, stdout

AREA_SCALE = 4
ROOT_POWER = 0.5
DECIMAL_SCALE = 1000000
DECIMAL_WIDTH = 6
ROUND_HALF = 0.5
a, b = map(int, stdin.read().split())
area = (a * a + b * b + 2 * 2**ROOT_POWER * a * b) / AREA_SCALE
# The scaled value is below2**47; rounding adds at most half a micro-unit.
scaled = int(area * DECIMAL_SCALE + ROUND_HALF)
whole, fraction = divmod(scaled, DECIMAL_SCALE)
stdout.write(str(whole) + "." + str(fraction).zfill(DECIMAL_WIDTH))
