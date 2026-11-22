import sys

PREMIUM_LAST = 2
BUSINESS_LAST = 20

seat = sys.stdin.buffer.read().strip()
row, letter = int(seat[:-1]), seat[-1:]
if row <= PREMIUM_LAST:
    right_window, aisles = b"D", b"BC"
elif row <= BUSINESS_LAST:
    right_window, aisles = b"F", b"BCDE"
else:
    right_window, aisles = b"K", b"CDGH"
if letter == b"A" or letter == right_window:
    print("window")
elif letter in aisles:
    print("aisle")
else:
    print("neither")
