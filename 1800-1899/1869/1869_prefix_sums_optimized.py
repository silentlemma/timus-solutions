from struct import Struct
from sys import stdin

SEATS = 36
SLOT_BYTES = 4
SLOT_BITS = 8 * SLOT_BYTES
RADIX = 1 << SLOT_BITS
read = stdin.buffer.readline
size = int(read())
row_format = Struct(f"<{size}I")
east = west = 0
for station in range(size):
    row = int.from_bytes(row_format.pack(*map(int, read().split())), "little")
    offset = station * SLOT_BITS
    mask = (1 << offset) - 1
    left = row & mask
    right = row >> (offset + SLOT_BITS)
    # Division by radix-1 yields suffix sums without carries between fields.
    east += ((right << SLOT_BITS) // (RADIX - 1)) << offset
    # Multiplication by a repunit yields prefixes below this station.
    west += (((left << offset) - left) // (RADIX - 1)) & mask
width = size * SLOT_BYTES
peak = max(
    *row_format.unpack(east.to_bytes(width, "little")),
    *row_format.unpack(west.to_bytes(width, "little")),
)
print((peak + SEATS - 1) // SEATS)
