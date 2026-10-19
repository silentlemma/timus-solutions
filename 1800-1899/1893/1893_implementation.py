import sys

PREMIUM_LAST = 2
BUSINESS_LAST = 20

seat = sys.stdin.read().strip()
row, letter = int(seat[:-1]), seat[-1]
if row <= PREMIUM_LAST:
    right_window, aisles = "D", "BC"
elif row <= BUSINESS_LAST:
    right_window, aisles = "F", "BCDE"
else:
    right_window, aisles = "K", "CDGH"
if letter == "A" or letter == right_window:
    print("window")
elif letter in aisles:
    print("aisle")
else:
    print("neither")
