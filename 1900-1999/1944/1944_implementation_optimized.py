MAX_COORD = 100
SPAN = 2 * MAX_COORD + 1

reader = open(0, "rb", closefd=False)
points = []
left = right = lower = upper = 0
for _ in range(int(reader.readline())):
    x, y = map(int, reader.readline().split())
    left = min(left, x)
    right = max(right, x)
    lower = min(lower, y)
    upper = max(upper, y)
    points.append((y + MAX_COORD) * SPAN + x + MAX_COORD)
points.sort()

width = right - left + 1
vertical = bytearray(b"." * width)
vertical[-left] = ord("|")
horizontal = bytearray(b"-" * width)
horizontal[-left] = ord("+")
writer = open(1, "wb", closefd=False)
position = len(points) - 1
for y in range(upper, lower - 1, -1):
    row = bytearray(horizontal if y == 0 else vertical)
    # Nonnegative packed coordinates sort by row, then by column.
    while position >= 0 and points[position] // SPAN == y + MAX_COORD:
        x = points[position] % SPAN - MAX_COORD
        row[x - left] = ord("*")
        position -= 1
    writer.write(row)
    writer.write(b"\n")
writer.flush()
