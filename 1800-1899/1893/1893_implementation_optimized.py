import os
from sys import stdout

LAST_MEDIUM_ROW = 20


seat = open(0, "rb", buffering=0).read().strip()
row, letter = int(seat[:-1]), seat[-1:]
if row <= 2:
    right_window, aisles = b"D", b"BC"
elif row <= LAST_MEDIUM_ROW:
    right_window, aisles = b"F", b"BCDE"
else:
    right_window, aisles = b"K", b"CDGH"
if letter in (b"A", right_window):
    print("window")
elif letter in aisles:
    print("aisle")
else:
    print("neither")

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
